# URL Constants

# Credentials:
username = "testuser"
password = "testpass"
# passenger_name = "Ravi"
# passenger_age = "28"

import os
from pathlib import Path

# Dynamic URL paths
URL_Login = "file:///D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/login.html"
URL_Search = "file:///D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/search.html"
URL_Booking = "D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/booking.html"
URL_Payment = "D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/payment.html"


# Credentials (use environment variables for production)
username = os.getenv("TEST_USERNAME", "testuser")
password = os.getenv("TEST_PASSWORD", "testpass")

EMAIL_SENDER = os.getenv("EMAIL_SENDER", "pavankumaryerra9@gmail.com")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "mohanmulakalapalli@gmail.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "bunny8688873902paru")

# Telegram credentials
BOT_TOKEN = "8190881950:AAFKtHfHrXgxBDOtFLJcAaapG0-OpTANesQ"
CHAT_ID = "1080852678"
