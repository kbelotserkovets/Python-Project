from elements.base import *
from locators.forgotPasswordPage import ForgotPassPage


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = ForgotPassPage
        super().__init__(driver)

    def enter_email_password(self, email):
        self.find_element(*ForgotPassPage.EMAIL).send_keys(email)

    def click_sign_in_button(self):
        self.find_element(*ForgotPassPage.SIGN_IN).click()

    def click_next_button(self):
        self.find_element(*ForgotPassPage.NEXT).click()
