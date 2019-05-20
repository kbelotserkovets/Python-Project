from selene.support import by


class LoginPageLocators(object):

    EMAIL                       = by.name('email')
    PASSWORD                    = by.name('password')
    SIGN_IN                     = '[class*="sign_in_button"]'
    ERROR_MESSAGE               = '[class*="error__"]'
    ERROR_EMPTY_EMAIL_FIELD     = '[class*="login_form"] > [class*="custom_error"] > [class*="error_message"]'
    ERROR_EMPTY_PASSWORD_FIELD  = '[class*="password_field"] > [class*="custom_error"] > [class*="error_message"]'