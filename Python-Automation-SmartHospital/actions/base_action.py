from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
    
    
    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    def wait_for_text_to_be_present(self,locator,text):
        return self.wait.until(EC.text_to_be_present_in_element(locator,text))

    def move_to_element(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )
    def select_by_visible_text(self, locator, text):
        element = self.driver.find_element(*locator)
        Select(element).select_by_visible_text(text)
    
    
    
    def wait_for_visible(self, locator, timeout=20):
     return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

    def wait_for_clickable1(self, locator, timeout=20):
     return WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    def wait_for_text_to_be_present(self,locator,text):
        return self.wait.until(EC.text_to_be_present_in_element(locator,text))

