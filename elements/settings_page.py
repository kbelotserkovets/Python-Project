from elements.base import *
from locators.settings_page_locators import SettingsPageLocators


class SettingsPage(Page):
    def __init__(self, driver):
        self.locator = SettingsPageLocators
        super().__init__(driver)

    def fill_user_form(self, new_first_name, new_last_name, new_age):
        first_name = self.find_element(*SettingsPageLocators.FIRST_NAME)
        last_name = self.find_element(*SettingsPageLocators.LAST_NAME)
        age = self.find_element(*SettingsPageLocators.AGE)

        first_name.clear()
        first_name.send_keys(new_first_name)

        last_name.clear()
        last_name.send_keys(new_last_name)

        age.clear()
        age.send_keys(new_age)

    def select_male_gender(self):
        self.find_element(*SettingsPageLocators.GENDER_MALE).click()

    def select_female_gender(self):
        self.find_element(*SettingsPageLocators.GENDER_FEMALE).click()

    def click_save_changes_button(self):
        self.find_element(*SettingsPageLocators.SAVE_CHANGES).click()

    def check_settings_changes(self):
        first_name = self.find_element(*SettingsPageLocators.FIRST_NAME)
        last_name = self.find_element(*SettingsPageLocators.LAST_NAME)
        age = self.find_element(*SettingsPageLocators.AGE)
