from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from elements.login_page import *
from locators.dashboard_page_locators import DashboardPageLocators


class DashboardPage(LoginPage):

    def __init__(self, driver):
        self.locator = DashboardPageLocators
        super().__init__(driver)

    def open_user_settings(self):
        self.user_login()
        self.find_element(*DashboardPageLocators.USER_AVATAR).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*DashboardPageLocators.PROFILE_MENU))
        self.find_element(*DashboardPageLocators.SETTINGS).click()
