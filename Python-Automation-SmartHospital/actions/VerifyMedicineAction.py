from utilities.logger import log_generator
from actions.base_action import BaseAction
from utilities.config_reader import get_value
from pages.VerifyMedicinePage import VerifyMedicinePage


class VerifyMedicineAction(BaseAction):
    logger = log_generator()

    def __init__(self, driver):
        super().__init__(driver)

    def assertmedicinepage(self):
        self.logger.info("Verifying moved to the medicine stock page")
        expected_url = get_value("config.ini", "medicine details", "medicinepageurl")
        return expected_url in self.driver.current_url

    def searchvalidmedicine(self):
        medicine = get_value("config.ini", "medicine details", "validmedicine")
        self.logger.info(f"Searching for valid medicine: {medicine}")
        self.send_keys(VerifyMedicinePage.medicinesearchbar, medicine)

    def searchinvalidmedicine(self):
        medicine = get_value("config.ini", "medicine details", "invalidmedicine")
        self.logger.info(f"Searching for invalid medicine: {medicine}")
        self.send_keys(VerifyMedicinePage.medicinesearchbar, medicine)

    def medicinestatus(self, status_type):
        if status_type == "present":
            medicine = get_value("config.ini", "medicine details", "validmedicine")
            expected_status = get_value(
                "config.ini", "medicine details", "presentStatus"
            )
            self.logger.info(f"Checking present status for medicine: {medicine}")
            try:
                text = self.get_text(VerifyMedicinePage.medicinetext(medicine))
                self.logger.info(f"Medicine '{medicine}' is present in the table")
                return expected_status.lower() in text.lower()
            except:
                self.logger.warning(f"Medicine '{medicine}' not found in table")
                return False

        elif status_type == "absent":
            medicine = get_value("config.ini", "medicine details", "invalidmedicine")
            expected_status = get_value(
                "config.ini", "medicine details", "absentStatus"
            )
            self.logger.info(f"Checking absent status for medicine: {medicine}")
            try:
                text = self.get_text(VerifyMedicinePage.medicinenotfoundtxt)
                self.logger.info(f"Medicine '{medicine}' is absent in the table")
                return expected_status.lower() in text.lower()
            except:
                self.logger.warning("Could not verify absent status")
                return False

    def deletemedicine(self):
        medicine = get_value("config.ini", "medicine details", "deletablemedicine")
        self.logger.info(f"Deleting medicine: {medicine}")
        self.send_keys(VerifyMedicinePage.medicinesearchbar, medicine)
        self.click(VerifyMedicinePage.medicinecheckbox(medicine))
        self.logger.info(f"Checkbox clicked for medicine: {medicine}")
        self.click(VerifyMedicinePage.deletebutton)
        self.logger.info("Delete button clicked")
        self.handle_alert()
        self.logger.info("Alert handled")
        try:
            self.get_text(
                VerifyMedicinePage.medicinenotfoundtxt
            ) 
            self.logger.info(
                f"Medicine '{medicine}' deleted successfully - no longer in table"
            )
            return True
        except:
            self.logger.warning("Medicine still appears in table after delete")
            return False

    def deletenotfoundmedicine(self):
        medicine = get_value("config.ini", "medicine details", "nondeletablemedicine")
        self.logger.info(f"Searching for non-existent medicine: {medicine}")
        self.clear(VerifyMedicinePage.medicinesearchbar)
        self.send_keys(VerifyMedicinePage.medicinesearchbar, medicine)
        try:
            text=self.get_text(VerifyMedicinePage.medicinenotfoundtxt)
            print(text)
            self.logger.info(f"Medicine '{medicine}' not found in table as expected")
            return True
        except:
            self.logger.warning(f"Medicine '{medicine}' unexpectedly found in table")
            return False
