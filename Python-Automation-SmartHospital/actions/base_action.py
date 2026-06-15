from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


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
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_text_to_be_present(self, locator, text):
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_for_value_to_be_present(self, locator, text):
        return self.wait.until(
            EC.text_to_be_present_in_element_value(locator, text)
        )

    def select_by_visible_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        select = Select(element)
        select.select_by_visible_text(text)

    def hover(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        ActionChains(self.driver).move_to_element(element).perform()

    def handle_alert(self):
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            return True
        except:
            return False

    def clear(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator)
        ).clear()

    def select_date(self, element, date):
        ele = self.driver.find_element(*element)
        self.driver.execute_script(
            "arguments[0].value=arguments[1];",
            ele,
            date
        )

    def jsclick(self, locator):
        ele = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            ele
        )

    def move_to_element(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

    def wait_for_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_url(self):
        return self.driver.current_url