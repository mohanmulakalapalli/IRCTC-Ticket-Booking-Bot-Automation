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
from pages.test_data import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD

# Setup logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "sanity_run.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_report_email(recipient_email, subject, html_body, attachments):
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
    except Exception as e:
        error_msg = f"❌ Failed to send email: {e}"
        logging.error(error_msg)
        print(error_msg)

def build_html_report(log_file_path):
    """Create a rich HTML body for the email."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = ""
    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as f:
            log_content = f.read().replace('\n', '<br>')

    html = f"""
    <html>
    <body style="font-family: Arial; line-height: 1.6;">
        <h2>🚆 IRCTC Tatkal Booking - Automation Report</h2>
        <p><b>Date & Time:</b> {timestamp}</p>
        <p><b>Status:</b> ✅ Booking Completed Successfully</p>
        <hr>
        <h3>📜 Log Summary</h3>
        <div style="background:#f4f4f4;padding:10px;border:1px solid #ccc;">
            {log_content}
        </div>
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
        bot = IRCTCTatkalBot()
        bot.run()
        logging.info("Tatkal booking completed.")

        # Create report file
        os.makedirs("report", exist_ok=True)
        report_path = "report/booking_report.txt"
        with open(report_path, "w") as f:
            f.write("Tatkal Booking Report\n")
            f.write("Status: Booking Completed\n")
            f.write("Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        # Collect screenshots
        screenshots_dir = "report/screenshots"
        screenshots = [os.path.join(screenshots_dir, f) for f in os.listdir(screenshots_dir) if os.path.isfile(os.path.join(screenshots_dir, f))]

        # Generate email HTML content
        html_body = build_html_report(log_file)

        # Send the email
        send_report_email(
            recipient_email=EMAIL_RECEIVER,
            subject="✅ Tatkal Automation Booking Report",
            html_body=html_body,
            attachments=[report_path, log_file] + screenshots
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
