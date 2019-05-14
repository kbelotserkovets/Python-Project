from selenium.webdriver.common.by import By


class LoginPageLocators(object):

    EMAIL                       = (By.NAME, 'email')
    PASSWORD                    = (By.NAME, 'password')
    SIGN_IN                     = (By.CSS_SELECTOR, '[class*="sign_in_button"]')
    ERROR_MESSAGE               = (By.CSS_SELECTOR, '[class*="error__"]')
    FORGOT_PASSWORD             = (By.CSS_SELECTOR, '[class*="forgot_pass"]')
    ERROR_EMPTY_EMAIL_FIELD     = (By.CSS_SELECTOR, '[class*="login_form"] > [class*="custom_error"] > [class*="error_message"]')
    ERROR_EMPTY_PASSWORD_FIELD  = (By.CSS_SELECTOR, '[class*="password_field"] > [class*="custom_error"] > [class*="error_message"]')