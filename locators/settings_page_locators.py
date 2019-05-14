from selenium.webdriver.common.by import By


class SettingsPageLocators(object):

    FIRST_NAME       = (By.NAME, 'firstName')
    LAST_NAME        = (By.NAME, 'lastName')
    AGE              = (By.NAME, 'age')
    GENDER_MALE      = (By.CSS_SELECTOR, '[value="Male"]')
    GENDER_FEMALE    = (By.CSS_SELECTOR, '[value="Female"]')
    SAVE_CHANGES     = (By.CSS_SELECTOR, '[class*="button_save_changes"]')
