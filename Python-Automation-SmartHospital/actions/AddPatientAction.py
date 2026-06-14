import time
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from actions.base_action import BaseAction
from pages.AddPatientPage import AddPatientPage
from utilities.logger import log_generator

log = log_generator()


class AddPatientAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.short_wait = WebDriverWait(self.driver, 3)

    def navigate_to_add_patient(self):
        self.click(AddPatientPage.patient_menu)
        self.click(AddPatientPage.add_patient)
        log.info("Navigated to Add Patient page")

    def enter_patient_name(self, name):
        self.send_keys(AddPatientPage.patient_name, name)

    def enter_guardian_name(self, guardian):
        self.send_keys(AddPatientPage.guardian_name, guardian)

    def select_gender(self, gender):
        self.select_by_visible_text(AddPatientPage.gender, gender)

    def enter_dob(self, dob):
        """
        Uses JavaScript to set Age/Year/Day directly — avoids ID mismatch issues.
        Triggers 'input' and 'change' events so the form registers the values.
        """
        age   = str(date.today().year - dob.year)
        year  = str(dob.year)
        month = dob.strftime("%B")   # full name e.g. "February"
        day   = str(dob.day)

        # Set Age via JS
        self.driver.execute_script("""
            var inputs = document.querySelectorAll('input');
            for(var i=0; i<inputs.length; i++){
                if(inputs[i].placeholder=='Age' || inputs[i].name=='age' || inputs[i].id=='age'){
                    inputs[i].value = arguments[0];
                    inputs[i].dispatchEvent(new Event('input'));
                    inputs[i].dispatchEvent(new Event('change'));
                    break;
                }
            }
        """, age)
        time.sleep(0.3)

        # Set Year via JS
        self.driver.execute_script("""
            var inputs = document.querySelectorAll('input');
            for(var i=0; i<inputs.length; i++){
                if(inputs[i].placeholder=='Year' || inputs[i].name=='year' || inputs[i].id=='year'){
                    inputs[i].value = arguments[0];
                    inputs[i].dispatchEvent(new Event('input'));
                    inputs[i].dispatchEvent(new Event('change'));
                    break;
                }
            }
        """, year)
        time.sleep(0.3)

        # Set Month via select dropdown
        try:
            self.select_by_visible_text(AddPatientPage.dob_month, month)
        except Exception:
            self.driver.execute_script("""
                var selects = document.querySelectorAll('select');
                for(var i=0; i<selects.length; i++){
                    if(selects[i].name=='month' || selects[i].id=='month'){
                        for(var j=0; j<selects[i].options.length; j++){
                            if(selects[i].options[j].text == arguments[0]){
                                selects[i].selectedIndex = j;
                                selects[i].dispatchEvent(new Event('change'));
                                break;
                            }
                        }
                        break;
                    }
                }
            """, month)
        time.sleep(0.3)

        # Set Day via JS
        self.driver.execute_script("""
            var inputs = document.querySelectorAll('input');
            for(var i=0; i<inputs.length; i++){
                if(inputs[i].placeholder=='Day' || inputs[i].name=='day' || inputs[i].id=='day'){
                    inputs[i].value = arguments[0];
                    inputs[i].dispatchEvent(new Event('input'));
                    inputs[i].dispatchEvent(new Event('change'));
                    break;
                }
            }
        """, day)
        time.sleep(0.3)
        log.info(f"Filled DOB: age={age} | {day}/{month}/{year}")

    def enter_phone(self, phone):
        self.send_keys(AddPatientPage.phone, str(phone))

    def enter_email(self, email):
        self.send_keys(AddPatientPage.email, email)

    def select_blood_group(self, blood_group):
        self.select_by_visible_text(AddPatientPage.blood_group, blood_group)

    def enter_address(self, address):
        self.send_keys(AddPatientPage.address, address)

    def click_save(self):
        self.jsclick(AddPatientPage.save_button)

    def get_toast_message(self):
        try:
            msg = self.short_wait.until(
                EC.visibility_of_element_located(
                    AddPatientPage.toast_message)).text
            log.info(f"Toast message: {msg}")
            return msg
        except Exception:
            log.error("Toast message not found within 3 seconds")
            return ""

    def is_patient_in_table(self, name):
        locator = (By.XPATH,
                   f"//table//tbody//td[contains(normalize-space(.), '{name}')]")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            log.info(f"PASS — '{name}' found in Patient List table")
            return True
        except Exception:
            log.error(f"FAIL — '{name}' NOT found in Patient List table")
            return False

    def add_patient(self, name, guardian, gender, dob,
                    phone, email, blood_group, address):
        self.enter_patient_name(name)
        self.enter_guardian_name(guardian)
        self.select_gender(gender)
        self.enter_dob(dob)
        self.enter_phone(phone)
        self.enter_email(email)
        self.select_blood_group(blood_group)
        self.enter_address(address)
        self.click_save()
        log.info(f"Add Patient form submitted for: {name}")
    def is_phone_error_displayed(self):
       
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    AddPatientPage.phone_error))
            log.info("Phone error message displayed")
            return True
        except Exception:
            log.error("Phone error message NOT displayed")
            return False
    def is_email_error_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    AddPatientPage.email_error))
            log.info("Email error message displayed")
            return True
        except Exception:
            log.error("Email error message NOT displayed")
            return False
