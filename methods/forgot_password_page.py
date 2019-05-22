from selene.support.jquery_style_selectors import s
from locators.forgot_password_page_locators import ForgotPassPageLocators


class ForgotPasswordPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = ForgotPassPageLocators

    def click_forgot_password_button(self):
        s(ForgotPassPageLocators.FORGOT_PASSWORD).click()

    def click_sign_in_button(self):
        s(ForgotPassPageLocators.SIGN_IN).click()

    def click_next_button(self):
        s(ForgotPassPageLocators.NEXT).click()

    def send_forgot_password_request(self, email):
        self.click_forgot_password_button()
        s(ForgotPassPageLocators.EMAIL).send_keys(email)
        self.click_next_button()



