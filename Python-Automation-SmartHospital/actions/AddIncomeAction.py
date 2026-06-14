import time
from selenium.webdriver.support import expected_conditions as EC
from actions.base_action import BaseAction
from pages.AddIncomPage import AddIncomePage
from utilities.logger import log_generator

log = log_generator()


class AddIncomeAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_add_income(self):
        finance = self.driver.find_element(*AddIncomePage.finance_menu)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finance)
        finance.click()
        time.sleep(1)
        self.click(AddIncomePage.income_link)
        time.sleep(1)
        self.click(AddIncomePage.add_income_btn)
        log.info("Navigated to Add Income page")

    def fill_income_form(self, income_head, name, invoice_number, date, amount, description):
        self.select_by_visible_text(AddIncomePage.income_head, income_head)
        self.send_keys(AddIncomePage.name,           name)
        self.send_keys(AddIncomePage.invoice_number, invoice_number)
        self.send_keys(AddIncomePage.date,           date)
        self.send_keys(AddIncomePage.amount,         str(amount))
        self.send_keys(AddIncomePage.description,    description)
        log.info(f"Filled income form: {income_head} | {name} | amount={amount}")

    def fill_mandatory_fields(self, income_head, name, invoice_number, date, amount):
        self.select_by_visible_text(AddIncomePage.income_head, income_head)
        self.send_keys(AddIncomePage.name,           name)
        self.send_keys(AddIncomePage.invoice_number, invoice_number)
        self.send_keys(AddIncomePage.date,           date)
        self.send_keys(AddIncomePage.amount,         str(amount))
        log.info(f"Filled mandatory fields for: {name}")

    def submit_form(self):
        self.click(AddIncomePage.submit_btn)
        time.sleep(1)
        log.info("Clicked Submit button")

    def assert_first_row_name(self, name):
        """After submit page lands on Income List — assert first row name matches"""
        try:
            first_name = self.wait.until(
                EC.visibility_of_element_located(AddIncomePage.first_row_name)).text
            log.info(f"First row name in table: '{first_name}'")
            result = name.lower() in first_name.lower()
            if result:
                log.info(f"PASS — '{name}' found in first row")
            else:
                log.error(f"FAIL — '{name}' NOT in first row, found '{first_name}'")
            return result
        except Exception as e:
            log.error(f"First row assertion failed: {e}")
            return False

    def assert_first_row_invoice(self, invoice_number):
        """After submit page lands on Income List — assert first row invoice matches"""
        try:
            first_invoice = self.wait.until(
                EC.visibility_of_element_located(AddIncomePage.first_row_invoice)).text
            log.info(f"First row invoice in table: '{first_invoice}'")
            result = invoice_number in first_invoice
            if result:
                log.info(f"PASS — '{invoice_number}' found in first row")
            else:
                log.error(f"FAIL — '{invoice_number}' NOT in first row, found '{first_invoice}'")
            return result
        except Exception as e:
            log.error(f"First row invoice assertion failed: {e}")
            return False

    def assert_validation_error(self):
        msg = self.get_text(AddIncomePage.toast_message)
        log.info(f"Validation message: {msg}")
        return "field is required" in msg

    def is_income_in_table(self, name):
        locator = AddIncomePage.income_name_in_table(name)
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            log.info(f"Income record '{name}' FOUND in table")
            return True
        except Exception:
            log.error(f"Income record '{name}' NOT FOUND in table")
            return False