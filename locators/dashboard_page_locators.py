from selenium.webdriver.common.by import By


class DashboardPageLocators(object):

    USER_AVATAR        = (By.CSS_SELECTOR, 'div[class*="right_column_menu"] > div[class*="user_information"] > div[class*="user_profile"] > div[class*="user_photo"]')
    SETTINGS           = (By.CSS_SELECTOR, '[class*="right_column_menu"] [class*="profile_menu"] > [class*="menu_items_container"] > [class*="menu_items"] > li > [href="/settings"]')
    PROFILE_MENU       = (By.CSS_SELECTOR, 'div[class*="right_column_menu"] > div[class*="user_information"] > div[class*="user_profile"] > div[class*="profile_menu"] > div[class*="menu_items_container"]')
    HEADER             = (By.CSS_SELECTOR, '[class*="__nav_bar_header"]')
    NOTIFICATION_BELL  = (By.CSS_SELECTOR, 'div[class*="header"] div[class*="notification_icon"]')
    DAILY_PROGRESS     = (By.CSS_SELECTOR, '[class*="daily_progress_container"]')