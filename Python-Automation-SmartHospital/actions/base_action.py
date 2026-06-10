from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()