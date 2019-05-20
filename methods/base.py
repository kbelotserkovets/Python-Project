# from selenium.webdriver.common.action_chains import ActionChains
# from selene import *
#
#
# class Page(object):
#
#     def __init__(self, driver, base_url='https://staging.onestopwellness.ai/'):
#         self.base_url = base_url
#         self.driver = driver
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#
#     def hover_element(self, *locator):
#         element = self.find_element(*locator)
#         hover = ActionChains(self.driver).move_to_element(element)
#         hover.perform()
#
#     def find_element(self, *locator):
#         return self.driver.find_element(*locator)
#
#     def get_title(self):
#         return self.driver.title
#
#     def get_url(self):
#         return self.driver.current_url
#
#     def page_has_loaded(self):
#         page_state = self.driver.execute_script('return document.readyState;')
#         print(page_state)
#         return page_state == 'complete'
