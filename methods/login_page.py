from selene.support.jquery_style_selectors import s
from locators.login_page_locators import LoginPageLocators


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators
        # super().__init__(driver)

    def enter_email_password(self, email, password):
        s(LoginPageLocators.EMAIL).set_value(email)
        s(LoginPageLocators.PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        s(LoginPageLocators.SIGN_IN).click()
    #
    # def click_forgot_password_button(self):
    #     s(LoginPageLocators.FORGOT_PASSWORD).click()

    def user_login_with_valid_user(self):
        self.enter_email_password("ksenia.kim.88@mail.ru", "testtest")
        self.click_sign_in_button()

    def user_login_with_in_valid_user(self):
        self.enter_email_password("ksenia.kim.88@mail.ru", "123")
        self.click_sign_in_button()

    def user_login_with_empty_data(self):
        self.enter_email_password("", "")
        self.click_sign_in_button()