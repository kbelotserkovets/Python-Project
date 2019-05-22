import unittest
from selene import browser, driver
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from locators.forgot_password_page import ForgotPassPageLocators

from methods import forgot_password_page


class ForgotPasswordPageTestCase(unittest.TestCase):

    def setUp(self):
        browser.open_url("https://staging.onestopwellness.ai")

    def test_forgot_password_with_valid_email(self):
        page = forgot_password_page.ForgotPasswordPage(driver)
        page.send_forgot_password_request("ksenia.kim.88@mail.ru")
        s(ForgotPassPageLocators.EMAIL_TITLE).should(have.exact_text("CHECK YOUR EMAIL"))
        s(ForgotPassPageLocators.SMALL_EMAIL_TITLE).should(have.exact_text("Please check your inbox, an email is on the way"))

    def test_forgot_password_with_in_valid_email(self):
        page = forgot_password_page.ForgotPasswordPage(driver)
        page.send_forgot_password_request("test@test.ru")
        s(ForgotPassPageLocators.ERROR_MESSAGE).should(have.exact_text("User not found"))

    def test_forgot_password_with_empty_fields(self):
        page = forgot_password_page.ForgotPasswordPage(driver)
        page.send_forgot_password_request("")
        s(ForgotPassPageLocators.ERROR_EMPTY_EMAIL).should(have.exact_text("The field is required."))

    def test_sign_in_button_on_forgot_password_form(self):
        page = forgot_password_page.ForgotPasswordPage(driver)
        page.click_forgot_password_button()
        page.click_sign_in_button()
        browser.should(have.url(exact_value="https://staging.onestopwellness.ai/signin"))

    def tearDown(self):
        browser.close()

if __name__ == '__main__':
    unittest.main()
