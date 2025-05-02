import os
import time
import logging
import requests
from datetime import datetime
from main import IRCTCTatkalBot

# Telegram credentials
BOT_TOKEN = "8190881950:AAFKtHfHrXgxBDOtFLJcAaapG0-OpTANesQ"
CHAT_ID = "1080852678"

# Setup logging
os.makedirs("logs", exist_ok=True)
log_file = "logs/sanity_run.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_telegram_message(text, file_path=None):
    """Send a message and optionally a file to Telegram chat."""
    msg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    doc_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

    # Send the message
    response = requests.post(msg_url, data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    })
    if response.ok:
        print("✅ Telegram message sent.")
    else:
        print(f"❌ Message failed: {response.text}")

    # Send file if provided
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            res = requests.post(doc_url, data={"chat_id": CHAT_ID}, files={"document": f})
            if res.ok:
                print(f"✅ File sent: {file_path}")
            else:
                print(f"❌ Failed to send file: {file_path}, error: {res.text}")

def run_automation():
    """Run TatkalBot and send report/logs to Telegram."""
    logging.info("🚆 Automation started")
    bot = None
    try:
        bot = IRCTCTatkalBot()
        bot.run()

        # Prepare report
        os.makedirs("report", exist_ok=True)
        report_path = "report/booking_report.txt"
        with open(report_path, "w") as f:
            f.write("Tatkal Booking Report\n")
            f.write("Status: Booking Completed\n")
            f.write("Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        message = (
            "📤 <b>Tatkal Booking Completed</b>\n"
            "🕒 <i>{}</i>\n"
            "✅ Booking flow executed successfully.\n"
            "📎 Attached: Booking Report + Logs".format(datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
        )

        # Send summary + report + log file
        send_telegram_message(message, file_path=report_path)
        send_telegram_message("📝 Automation Log File:", file_path=log_file)

        # Attach screenshots if present
        screenshots_dir = "report/screenshots"
        if os.path.exists(screenshots_dir):
            for file in os.listdir(screenshots_dir):
                full_path = os.path.join(screenshots_dir, file)
                send_telegram_message(f"📸 Screenshot: {file}", file_path=full_path)

    except Exception as e:
        error_msg = f"❌ Booking failed: {e}"
        logging.error(error_msg)
        send_telegram_message(f"<b>{error_msg}</b>")
    finally:
        if bot and bot.driver:
            bot.driver.quit()
        logging.info("✅ Automation ended")

# Run once for test (no schedule)
if __name__ == "__main__":
    run_automation()
