from selenium.webdriver.support import expected_conditions as EC
from actions.base_action import BaseAction
from pages.PharmacyBillPage import PharmacyBillPage
from utilities.logger import log_generator

logger = log_generator()
PHARMACY_BILL_URL = "https://demo.smart-hospital.in/admin/pharmacy/bill"

class PharmacyBillpageAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    def clickPharmacy(self):
        self.click(PharmacyBillPage.pharmacyMenu)
        logger.info("Clicked Pharmacy menu")

    def clickMedicinesButton(self):
        self.click(PharmacyBillPage.medicinesBtn)
        logger.info("Clicked Medicines button")

    def clickPatientsearchbar(self):
        self.click(PharmacyBillPage.searchInputbar)

    def searchName(self, patient):
        elem = self.driver.find_element(*PharmacyBillPage.searchInputbar)
        elem.clear()
        elem.send_keys(patient)
        logger.info(f"Searched for patient: {patient}")

    def isPatientPresent(self, patient_name):
        rows = self.driver.find_elements(*PharmacyBillPage.searchnamerow)
        for row in rows:
            if patient_name.lower() in row.text.strip().lower():
                return True
        return False

    def isNoDataMessageDisplayed(self):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(PharmacyBillPage.noDataMessage))
            return "No data available in table" in elem.text
        except Exception:
            return False

    def isOnPharmacyBillPage(self):
        return self.driver.current_url == PHARMACY_BILL_URL