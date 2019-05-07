from selenium.webdriver.common.action_chains import ActionChains


class Page(object):

    def __init__(self, driver, base_url='https://staging.onestopwellness.ai/'):
        self.base_url = base_url
        self.driver = driver
        driver.maximize_window()
        driver.implicitly_wait(5)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title


class LoginPage(Page):
    def __init__(self, driver):
        self.driver = driver

