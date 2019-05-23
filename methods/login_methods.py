import os
from selene.support.jquery_style_selectors import s
from locators.login_page import LoginPageLocators


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def enter_email_password(self, email, password):
        s(LoginPageLocators.EMAIL).set_value(email)
        s(LoginPageLocators.PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        s(LoginPageLocators.SIGN_IN).click()

    def user_login_with_valid_user(self):
        self.enter_email_password(os.environ.get("username"), os.environ.get("password"))
        self.click_sign_in_button()

    def user_login_with_in_valid_user(self):
        self.enter_email_password("test@test.su", "qwerty123")
        self.click_sign_in_button()

    def user_login_with_empty_data(self):
        self.enter_email_password("", "")
        self.click_sign_in_button()
