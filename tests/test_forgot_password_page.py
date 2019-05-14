import os
import unittest
from elements.forgot_password_page import *


class ForgotPasswordPageTest(unittest.TestCase, LoginPage):

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(current_dir, 'chromedriver')
        self.driver = webdriver.Chrome(chromedriver_path)
        self.page = Page(driver=self.driver)

    def tearDown(self):
        self.driver.close()
