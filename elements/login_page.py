from elements.base import *
from locators.login_page_locators import LoginPageLocators
from selenium import webdriver


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

    def user_login_with_valid_data(self):
        self.enter_email_password("ksenia.kim.88@mail.ru", "testtest")
        self.click_sign_in_button()

    def user_login_with_in_valid_data(self):
        self.enter_email_password("ksenia.kim.88@mail.ru", "123")
        self.click_sign_in_button()

    def user_login_with_empty_data(self):
        self.enter_email_password("", "")
        self.click_sign_in_button()

    def check_current_url(self):
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/dashboard',
                         'URL should be "https://staging.onestopwellness.ai/dashboard"')
