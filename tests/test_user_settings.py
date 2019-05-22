import unittest
from selene import browser, driver
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s
from locators.dashboard_page_locators import DashboardPageLocators

from methods import settings_page
from methods import login_page


class UserSettingsPageTestCase(unittest.TestCase):

    def setUp(self):
        browser.open_url("https://staging.onestopwellness.ai")

    def test_change_user_name_and_surname(self):
        login = login_page.LoginPage(driver)
        login.user_login_with_valid_user()
        page = settings_page.SettingsPage(driver)
        page.open_user_settings()
        page.fill_user_form("Ksu", "Kim", "30")
        page.click_save_changes_button()
        browser.wait_for(s(DashboardPageLocators.DAILY_PROGRESS), be.visible)
        page.open_user_settings()
        page.check_settings_changes("Ksu", "Kim", "30")

    def tearDown(self):
        browser.close()


if __name__ == '__main__':
    unittest.main()