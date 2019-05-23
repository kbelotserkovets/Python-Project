import unittest
from selene import browser, driver
from selene.support.conditions import have, be
from selene.support.jquery_style_selectors import s

from locators.dashboard_page import DashboardPageLocators
from locators.login_page import LoginPageLocators

from methods import login_methods


class LoginPageTestCase(unittest.TestCase):

    def setUp(self):
        browser.open_url("https://staging.onestopwellness.ai")

    def test_login_with_valid_data(self):
        page = login_methods.LoginPage(driver)
        page.user_login_with_valid_user()
        browser.wait_for(s(DashboardPageLocators.HEADER), be.visible)
        browser.should(have.url("https://staging.onestopwellness.ai/dashboard"))

    def test_login_with_in_valid_data(self):
        page = login_methods.LoginPage(driver)
        page.user_login_with_in_valid_user()
        actual_error_message = s(LoginPageLocators.ERROR_MESSAGE)
        actual_error_message.should(have.exact_text('Invalid email or password, please try again'))

    def test_login_with_empty_fields(self):
        page = login_methods.LoginPage(driver)
        page.user_login_with_empty_data()

        actual_email_error_text = s(LoginPageLocators.ERROR_EMPTY_EMAIL_FIELD)
        actual_password_error_text = s(LoginPageLocators.ERROR_EMPTY_PASSWORD_FIELD)

        actual_email_error_text.should(have.exact_text("The field is required."))
        actual_password_error_text.should(have.exact_text("The field is required."))

    def tearDown(self):
        browser.close()


if __name__ == '__main__':
    unittest.main()
