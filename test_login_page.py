import os
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.base import Page
from locators import dashboardPage, forgotPasswordPage, loginPage, settingsPage


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(current_dir, 'chromedriver')
        self.driver = webdriver.Chrome(chromedriver_path)
        self.page = Page(driver=self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_with_valid_data(self):
        self.user_sign_in("ksenia.kim.88@mail.ru", "testtest")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="__nav_bar_header"]')))
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/dashboard',
                         'URL should be "https://staging.onestopwellness.ai/dashboard"')

    def test_error_message_in_login_with_invalid_data(self):
        self.user_sign_in("ksenia.kim.88@mail.ru", "qwerty")
        error_message = self.driver.find_element_by_css_selector('[class*="error__"]').text
        self.assertEqual(error_message, 'Invalid email or password, please try again',
                         'Error text should be: "Invalid email or password, please try again"')

    def test_user_login_with_empty_field(self):
        self.user_sign_in("", "")
        custom_login_error = self.driver.find_element(*LoginPage.ERROR_EMPTY_EMAIL_FIELD)
        custom_password_error = self.driver.find_element(*LoginPage.ERROR_EMPTY_PASSWORD_FIELD)
        self.assertTrue(custom_login_error.is_displayed(), "The color of email field's border should be RED")
        self.assertTrue(custom_password_error.is_displayed(), "The color of password field's border should be RED")

    def test_change_user_name(self):
        driver = self.driver
        self.user_sign_in("ksenia.kim.88@mail.ru", "testtest")

        self.open_user_settings()

        first_name = driver.find_element(*SettingsPage.FIRST_NAME)
        last_name = driver.find_element(*SettingsPage.LAST_NAME)
        age = driver.find_element(*SettingsPage.AGE)
        gender_female = driver.find_element(*SettingsPage.GENDER_FEMALE)

        first_name.clear()
        first_name.send_keys("Kseniya")

        last_name.clear()
        last_name.send_keys("Kims")

        age.clear()
        age.send_keys("30")

        gender_female.click()

        driver.find_element(*SettingsPage.SAVE_CHANGES).click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))

        self.open_user_settings()

        first_name = driver.find_element(*SettingsPage.FIRST_NAME)
        last_name = driver.find_element(*SettingsPage.LAST_NAME)
        age = driver.find_element(*SettingsPage.AGE)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName")))

        self.assertEqual(first_name.get_attribute("value"), "Ksenia")
        self.assertEqual(last_name.get_attribute("value"), "Kims")
        self.assertEqual(age.get_attribute("value"), "30")

    def test_forgot_password(self):
        driver = self.driver
        self.forgot_password('ksenia.kim.88@mail.ru')
        email_title = driver.find_element(*ForgotPassPage.EMAIL_TITLE).text
        small_email_title = driver.find_element(*ForgotPassPage.SMALL_EMAIL_TITLE).text
        self.assertEqual(email_title, 'CHECK YOUR EMAIL', 'Title should contain text: "CHECK YOUR EMAIL"')
        self.assertEqual(small_email_title, 'Please check your inbox, an email is on the way',
                         'Under "CHECK YOUR EMAIL" title, user should observe text: "Please check your inbox, an email is on the way"')
        driver.find_element(*ForgotPassPage.NEXT).click()
        self.assertEqual(driver.current_url, 'https://staging.onestopwellness.ai/signin',
                         'After send request for reset password, user should observe "Sign In" page')

    def test_forgot_password_for_not_existing_email(self):
        self.forgot_password('test@test.com')
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class*="error_message"]')))
        error_message = self.driver.find_element(*ForgotPassPage.ERROR_MESSAGE).text
        self.assertEqual(error_message, 'User not found')

    def test_forgot_password_empty_field(self):
        self.forgot_password("")
        custom_error = self.driver.find_element(*ForgotPassPage.ERROR_EMPTY_EMAIL)
        self.assertTrue(custom_error.is_displayed())

    def test_sign_in_button_on_forgot_password_form(self):
        self.forgot_password("")
        self.driver.find_element(*ForgotPassPage.SIGN_IN).click()
        self.assertEqual(self.driver.current_url, 'https://staging.onestopwellness.ai/signin',
                         'After send request for reset password, user should observe "Sign In" page')


if __name__ == '__main__':
    unittest.main()
