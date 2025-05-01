import schedule
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from main import IRCTCTatkalBot
from pages.test_data import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD


def send_report_email(recipient_email, subject, body, attachments):
    """Send an email with the report and screenshots."""
    sender_email = EMAIL_SENDER  # Replace with your email
    sender_password = EMAIL_PASSWORD  # Replace with your email password

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    for file_path in attachments:
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(file_path)}',
            )
            msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def run_automation():
    """Run the main automation script and send a report email."""
    print("Starting Tatkal booking automation...")
    bot = None
    try:
        bot = IRCTCTatkalBot()
        bot.run()

        # Generate a report file
        report_path = "report/booking_report.txt"
        os.makedirs("report", exist_ok=True)  # Ensure the report directory exists
        with open(report_path, "w") as report_file:
            report_file.write("Tatkal Booking Report\n")
            report_file.write("Booking completed successfully.\n")
            report_file.write("Screenshots are attached.\n")

        # Collect all screenshots
        screenshots_dir = "report/screenshots"
        screenshots = [os.path.join(screenshots_dir, file) for file in os.listdir(screenshots_dir)]

        # Send the email
        send_report_email(
            recipient_email=EMAIL_RECEIVER,  # Replace with passenger's email
            subject="Tatkal Booking Report",
            body="Please find attached the booking report and screenshots.",
            attachments=[report_path] + screenshots
        )

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bot and bot.driver:
            bot.driver.quit()  # Ensure the browser is closed


# Schedule to run every minute
schedule.every(1).minute.do(run_automation)

while True:
    schedule.run_pending()
    time.sleep(1)  # Check every second for pending tasks