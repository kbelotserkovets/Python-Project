from selenium.webdriver.common.by import By


class ForgotPassPage(object):

    EMAIL              = (By.NAME, 'email')
    NEXT               = (By.CSS_SELECTOR, '[class*="btn_issue_details"]')
    SIGN_IN            = (By.CSS_SELECTOR, '[class*="sign_in"]')
    EMAIL_TITLE        = (By.CSS_SELECTOR, '[class*="email_title__"]')
    SMALL_EMAIL_TITLE  = (By.CSS_SELECTOR, '[class*="email_title_item"]')
    ERROR_MESSAGE      = (By.CSS_SELECTOR, '[class*="error_message"]')
    ERROR_EMPTY_EMAIL  = (By.CSS_SELECTOR, '[class*="custom_error"]')