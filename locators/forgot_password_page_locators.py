from selene.support import by


class ForgotPassPageLocators(object):

    EMAIL              =  by.name('email')
    FORGOT_PASSWORD    =  '[class*="forgot_pass"]'
    NEXT               =  '[class*="btn_issue_details"]'
    SIGN_IN            =  '[class*="sign_in"]'
    EMAIL_TITLE        =  '[class*="email_title__"]'
    SMALL_EMAIL_TITLE  =  '[class*="email_title_item"]'
    ERROR_MESSAGE      =  '[class*="error_message"]'
    ERROR_EMPTY_EMAIL  =  '[class*="custom_error"] > [class*="error_message"]'