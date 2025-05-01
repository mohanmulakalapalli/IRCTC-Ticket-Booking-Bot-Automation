from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.captcha_input = (By.ID, "captcha-input")
        self.captcha_text = (By.ID, "captcha")
        self.refresh_button = (By.CLASS_NAME, "refresh-button")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def generate_captcha(self):
        """Click the refresh button to generate a new CAPTCHA."""
        self.driver.find_element(*self.refresh_button).click()

    def get_captcha_text(self):
        """Retrieve the CAPTCHA text displayed on the page."""
        return self.driver.find_element(*self.captcha_text).text

    def login(self, username, password, captcha):
        """Perform the login action."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.captcha_input).send_keys(captcha)
        self.driver.find_element(*self.login_button).click()

    def accept_alert(self):
        """Accept a JavaScript alert if present."""
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            print("No alert present to accept.")

    def dismiss_alert(self):
        """Dismiss a JavaScript alert if present."""
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except NoAlertPresentException:
            print("No alert present to dismiss.")