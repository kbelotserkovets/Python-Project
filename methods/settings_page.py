from selene.support.conditions import have
from selene.support.jquery_style_selectors import s
from locators.settings_page_locators import SettingsPageLocators
from locators.dashboard_page_locators import DashboardPageLocators


class SettingsPage(object):
    def __init__(self, driver):
        self.driver = driver

    def open_user_settings(self):
        s(DashboardPageLocators.USER_AVATAR).click()
        s(DashboardPageLocators.SETTINGS).click()

    def fill_user_form(self, new_first_name, new_last_name, new_age):
        s(SettingsPageLocators.FIRST_NAME).set(new_first_name)
        s(SettingsPageLocators.LAST_NAME).set(new_last_name)
        s(SettingsPageLocators.AGE).set(new_age)

    def select_male_gender(self):
        s(SettingsPageLocators.GENDER_MALE).click()

    def select_female_gender(self):
        s(SettingsPageLocators.GENDER_FEMALE).click()

    def click_save_changes_button(self):
        s(SettingsPageLocators.SAVE_CHANGES).click()

    def check_settings_changes(self, expected_first_name, expected_last_name, expected_age):
        s(SettingsPageLocators.FIRST_NAME).should(have.value(expected_first_name))
        s(SettingsPageLocators.LAST_NAME).should(have.value(expected_last_name))
        s(SettingsPageLocators.AGE).should(have.value(expected_age))
