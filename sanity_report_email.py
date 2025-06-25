import schedule
import time
import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from main import IRCTCTatkalBot
from configurations.test_data import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD
import humanize
import io
import contextlib

# Setup logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "sanity_run.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_report_email(recipient_email, subject, html_body, attachments, skipped_files=None):
    """Send a professional HTML email with logs and attachments."""
    sender_email = EMAIL_SENDER
    sender_password = EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(html_body, 'html'))

    for file_path in attachments:
        if os.path.exists(file_path):
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(file_path)}',
                )
                msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info("Email sent successfully.")
            print("✅ Email sent successfully to", recipient_email)
            if skipped_files:
                print("⚠️ Some files were skipped due to size limits:", skipped_files)
    except Exception as e:
        error_msg = f"❌ Failed to send email: {e}"
        logging.error(error_msg)
        print(error_msg)

def parse_details_from_output(output):
    passenger_details = {}
    ticket_info = {}
    lines = output.splitlines()
    section = None
    for line in lines:
        if "Passenger Details:" in line:
            section = "passenger"
            continue
        if "Ticket Information:" in line:
            section = "ticket"
            continue
        if section and ":" in line:
            key, value = line.split(":", 1)
            if section == "passenger":
                passenger_details[key.strip()] = value.strip()
            elif section == "ticket":
                ticket_info[key.strip()] = value.strip()
        if section and not line.strip():
            section = None
    return passenger_details, ticket_info

def build_html_report(timestamp, passenger_details, ticket_info):
    passenger_html = ""
    if passenger_details:
        passenger_html = (
            "<h3>Passenger Details:</h3>"
            "<div style='background:#f4f4f4;padding:10px;border:1px solid #ccc;'>"
            + "<br>".join(f"{k}: {v}" for k, v in passenger_details.items())
            + "</div>"
        )
    ticket_html = ""
    if ticket_info:
        ticket_html = (
            "<h3>Ticket Information:</h3>"
            "<div style='background:#f4f4f4;padding:10px;border:1px solid #ccc;'>"
            + "<br>".join(f"{k}: {v}" for k, v in ticket_info.items())
            + "</div>"
        )
    html = f"""
    <html>
    <body style="font-family: Arial; line-height: 1.6;">
        <h2>🚆 IRCTC Tatkal Booking - Automation Report</h2>
        <p><b>Status:</b> ✅ Booking Completed Successfully</p>
        <p><b>Time:</b> {timestamp}</p>
        <hr>
        {passenger_html}
        <br>
        {ticket_html}
        <hr>
        <p>📎 Attached: Booking report, Screenshots, Logs</p>
        <p style="color:gray;font-size:small;">This is an automated message from TatkalBot QA System.</p>
    </body>
    </html>
    """
    return html

def run_automation():
    """Run the bot and send a professional email with report."""
    logging.info("==== Automation Execution Started ====")
    bot = None
    try:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            bot = IRCTCTatkalBot()
            bot.run()
        output = buf.getvalue()
        passenger_details, ticket_info = parse_details_from_output(output)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info("Tatkal booking completed.")

        # Create report file and passenger details and ticket info
        os.makedirs("report", exist_ok=True)
        report_path = "report/booking_report.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("🚆 IRCTC Tatkal Booking - Automation Report\n\n")
            f.write("Status: ✅ Booking Completed Successfully\n")
            f.write(f"Time: {timestamp}\n\n")
            f.write("Passenger Details:\n")
            for k, v in passenger_details.items():
                f.write(f"{k}: {v}\n")
            f.write("\nTicket Information:\n")
            for k, v in ticket_info.items():
                f.write(f"{k}: {v}\n")

        # Collect screenshots
        screenshots_dir = "report/screenshots/main"
        screenshots = []
        if os.path.exists(screenshots_dir):
            screenshots = [os.path.join(screenshots_dir, f) for f in os.listdir(screenshots_dir) if os.path.isfile(os.path.join(screenshots_dir, f))]

        # Gmail max size is 25MB, but use 20MB for safety
        MAX_EMAIL_SIZE = 20 * 1024 * 1024
        attachments = [report_path, log_file] + screenshots
        total_size = 0
        final_attachments = []
        skipped_files = []

        for file_path in attachments:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                if total_size + file_size <= MAX_EMAIL_SIZE:
                    final_attachments.append(file_path)
                    total_size += file_size
                else:
                    skipped_files.append(f"{os.path.basename(file_path)} ({humanize.naturalsize(file_size)})")

        # Generate email HTML content
        html_body = build_html_report(timestamp, passenger_details, ticket_info)

        # Send the email
        send_report_email(
            recipient_email=EMAIL_RECEIVER,
            subject="✅ Tatkal Automation Booking Report",
            html_body=html_body,
            attachments=final_attachments,
            skipped_files=skipped_files if skipped_files else None
        )
    except Exception as e:
        logging.error(f"Automation failed: {e}")
    finally:
        if bot and bot.driver:
            bot.driver.quit()
        logging.info("==== Automation Execution Finished ====")

# Schedule every 1 minute (adjust for production)
schedule.every(1).minute.do(run_automation)

while True:
    schedule.run_pending()
    time.sleep(1)
