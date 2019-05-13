from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from elements.loginPage import *
from locators.dashboardPage import DashboardPage


class DashboardPage(LoginPage):

    def __init__(self, driver):
        self.locator = DashboardPage
        super().__init__(driver)

    def open_user_settings(self):
        self.user_login()
        self.find_element(*DashboardPage.USER_AVATAR).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((DashboardPage.PROFILE_MENU)))
        self.find_element(*DashboardPage.SETTINGS).click()
