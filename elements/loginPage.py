from elements.base import *
from locators.loginPage import LoginPageLocators


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def enter_email_password(self, email, password):
        self.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self.find_element(*LoginPageLocators.SIGN_IN).click()

    def click_forgot_password_button(self):
        self.find_element(*LoginPageLocators.SIGN_IN).click()

    def user_login(self):
        self.enter_email_password()
        self.click_sign_in_button()
