from selenium.webdriver.support import expected_conditions as EC
from actions.base_action import BaseAction
from pages.SearchPatientPage import SearchPatientPage
from utilities.logger import log_generator
log = log_generator()
class SearchPatientAction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
    def navigate_to_patient_list(self):
        self.click(SearchPatientPage.patient_menu)
        log.info("Navigated to Patient List page")
    def search_patient(self, name):
        search_elem = self.wait.until(
            EC.visibility_of_element_located(SearchPatientPage.search_box))
        search_elem.clear()
        search_elem.send_keys(name)
        log.info(f"Entered search text: {name}")
    
        
    def is_search_result_displayed(self, name):
        locator = SearchPatientPage.search_result_name(name)
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            log.info(f"Search result FOUND for: '{name}'")
            return True
        except Exception:
            log.error(f"Search result NOT FOUND for: '{name}'")
            return False

    def is_no_data_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(SearchPatientPage.records_zero))
            log.info("'No data available in table' message displayed — invalid search confirmed")
            return True
        except Exception:
            log.error("'No data available in table' message NOT displayed")
            return False
    