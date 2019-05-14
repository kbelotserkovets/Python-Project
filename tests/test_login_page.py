import os
import unittest
from elements.dashboard_page import *


class LoginPageTest(unittest.TestCase, LoginPage):

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(current_dir, 'chromedriver')
        self.driver = webdriver.Chrome(chromedriver_path)
        self.page = Page(driver=self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_with_valid_data(self):
        expected_url = 'https://staging.onestopwellness.ai/dashboard'
        self.user_login_with_valid_data()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DashboardPageLocators.HEADER))
        self.assertEqual(self.driver.current_url, expected_url, 'URL should be "https://staging.onestopwellness.ai/dashboard"')

    def test_login_with_in_valid_data(self):
        self.user_login_with_in_valid_data()
        expected_error_message = 'Invalid email or password, please try again'
        actual_error_message = self.find_element(*LoginPageLocators.ERROR_MESSAGE).text
        self.assertEqual(actual_error_message, expected_error_message, 'Error text should be: "Invalid email or password, please try again"')

    def test_login_with_empty_fields(self):
        self.user_login_with_empty_data()
        expected_error_text = 'The field is required.'
        actual_email_error_text = self.find_element(*LoginPageLocators.ERROR_EMPTY_EMAIL_FIELD).text
        actual_password_error_text = self.find_element(*LoginPageLocators.ERROR_EMPTY_PASSWORD_FIELD).text
        self.assertEqual(expected_error_text, actual_email_error_text, 'Empty email field should contain the text: {}'.format(expected_error_text))
        self.assertEqual(expected_error_text, actual_password_error_text, 'Empty password field should contain the text: {}'.format(expected_error_text))
