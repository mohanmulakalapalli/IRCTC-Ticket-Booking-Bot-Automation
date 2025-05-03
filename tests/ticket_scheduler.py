import schedule
import time
from main import IRCTCTatkalBot

def run_automation():
    """Run the main automation script."""
    print("Starting Tatkal booking automation...")
    bot = None
    try:
        bot = IRCTCTatkalBot()
        bot.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if bot and bot.driver:
            bot.driver.quit()  # Ensure the browser is closed

# Schedule to run every minute
schedule.every(1).minute.do(run_automation)

# Schedule for 10 AM daily
# schedule.every().day.at("10:00").do(run_automation)


while True:
    schedule.run_pending()
    time.sleep(1)  # Check every second for pending tasks