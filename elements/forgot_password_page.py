from elements.base import *
from locators.forgot_password_page_locators import ForgotPassPageLocators


class ForgotPasswordPage(Page):
    def __init__(self, driver):
        self.locator = ForgotPassPageLocators
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(*ForgotPassPageLocators.EMAIL).send_keys(email)

    def click_sign_in_button(self):
        self.find_element(*ForgotPassPageLocators.SIGN_IN).click()

    def click_next_button(self):
        self.find_element(*ForgotPassPageLocators.NEXT).click()

    def send_forgot_password_request(self):
        pass

