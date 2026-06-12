import os
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from actions.base_action import BaseAction
from pages.PharmacyBillPage import PharmacyBillPage
from utilities.logger import log_generator

logger = log_generator()

PHARMACY_BILL_URL = "https://demo.smart-hospital.in/admin/pharmacy/bill"
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")


class PharmacyBillpageAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    def clickPharmacy(self):
        self.click(PharmacyBillPage.pharmacyMenu)
        logger.info("Clicked Pharmacy menu")

    def clickPatientsearchbar(self):
        self.click(PharmacyBillPage.searchInputbar)

    def searchName(self, patient):
        logger.info(f"Searching patient name: {patient}")
        self.wait.until(
            EC.visibility_of_element_located(PharmacyBillPage.searchInputbar)
        )
        elem = self.driver.find_element(*PharmacyBillPage.searchInputbar)
        elem.click()
        elem.clear()
        elem.send_keys(patient)
        try:
            self.wait.until(
                EC.presence_of_element_located(PharmacyBillPage.searchnamerow)
            )
        except Exception:
            pass

    def isPatientPresent(self, patient_name):
        for attempt in range(3):
            try:
                self.wait.until(
                    EC.presence_of_all_elements_located(PharmacyBillPage.searchnamerow)
                )
                rows = self.driver.find_elements(*PharmacyBillPage.searchnamerow)
                for row in rows:
                    actual = row.text.strip()
                    if patient_name.lower() in actual.lower():
                        return True
                return False
            except StaleElementReferenceException:
                self.wait.until(
                    EC.presence_of_all_elements_located(PharmacyBillPage.searchnamerow)
                )
        return False

    def pageisDisplayed(self):
        self.wait.until(
            EC.visibility_of_element_located(PharmacyBillPage.pharmacyBillPageHeader)
        )
        elem = self.driver.find_element(*PharmacyBillPage.pharmacyBillPageHeader)
        return elem.is_displayed()

    def isNoDataMessageDisplayed(self):
        try:
            elem = self.wait.until(
                EC.visibility_of_element_located(PharmacyBillPage.noDataMessage)
            )
            return "No data available in table" in elem.text
        except Exception:
            logger.error("No Data message not displayed")
            return False

    def clickCSVButton(self):
        self.clickPharmacy()
        self.wait.until(
            EC.visibility_of_element_located(PharmacyBillPage.pharmacyBillPageHeader)
        )
        logger.info(f"Current URL before CSV click: {self.driver.current_url}")
        csv_elem = self.wait.until(
            EC.element_to_be_clickable(PharmacyBillPage.csvButton)
        )
        logger.info(
            f"CSV button found: {csv_elem.is_displayed()}, enabled: {csv_elem.is_enabled()}"
        )
        self.driver.execute_script("arguments[0].click();", csv_elem)
        logger.info("Clicked CSV export button")

    def isCSVFileDownloaded(self, timeout=30):
        logger.info(f"Checking downloads folder: {DOWNLOADS_FOLDER}")
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: any(
                    file.endswith(".csv") or file.endswith(".crdownload")
                    for file in os.listdir(DOWNLOADS_FOLDER)
                )
            )
            WebDriverWait(self.driver, timeout).until(
                lambda driver: any(
                    file.endswith(".csv") for file in os.listdir(DOWNLOADS_FOLDER)
                )
                and not any(
                    file.endswith(".crdownload")
                    for file in os.listdir(DOWNLOADS_FOLDER)
                )
            )
            csv_file = next(
                f for f in os.listdir(DOWNLOADS_FOLDER) if f.endswith(".csv")
            )
            logger.info(f"CSV file downloaded: {csv_file}")
            return True
        except Exception:
            logger.warning(f"No CSV file found after {timeout} seconds")
            return False

    def clearDownloadsFolder(self):
        files = os.listdir(DOWNLOADS_FOLDER)
        for file in files:
            if file.endswith(".csv"):
                os.remove(os.path.join(DOWNLOADS_FOLDER, file))
                logger.info(f"Deleted old CSV: {file}")
    def clickMedicinesButton(self):
        self.click(PharmacyBillPage.medicinesBtn)
        logger.info("Clicked Medicines button")