from selene.support import by


class SettingsPageLocators(object):

    FIRST_NAME       =  by.name('firstName')
    LAST_NAME        =  by.name('lastName')
    AGE              =  by.name('age')
    GENDER_MALE      =  '[value="Male"]'
    GENDER_FEMALE    =  '[value="Female"]'
    SAVE_CHANGES     =  '[class*="button_save_changes"]'
