# Page Locators
# Page Actions
# Webdriver - Init
# Custom Function
# No Assertion here ( They are not test Cases )
# Page Class

from selenium.webdriver.common.by import By

class LoginPage():

    # WebDriver -Init
    def __init__(self, driver):
        self.driver = driver

        # Page Locators
        username = (By.XPATH, "//input[@id='login-username']")
        password = (By.XPATH, "//input[@id='login-password']")
        submit_button = (By.XPATH, "//button[@id='js-login-btn']")
        error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")

    # Forgot Pass, start a free trial ....

    # Page Actions
    # Return a WebElement --> username
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    # Page Actions
    def login_to_vwo(self, user, pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()
        # get username and keys - email
        # get password and send keys - password
        # click the submit button and navigate to dashboard Page
