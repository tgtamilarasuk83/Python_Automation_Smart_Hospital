import pytest
import allure
from actions.LoginAction import LoginAction
from actions.AddPatientAction import AddPatientAction
from utilities.excel_reader import get_data
from utilities.logger import log_generator

log = log_generator()

patient_data = get_data("AddPatientdetails.xlsx", "Sheet1")


# ── Scenario 1: Add patient with valid data ───────────────────────────────
@allure.feature("Add Patient")
@pytest.mark.parametrize(
    "name,guardian,gender,dob,phone,email,blood_group,address",
    patient_data
)
def test_add_patient_valid(setup, name, guardian, gender, dob,
                           phone, email, blood_group, address):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    patient = AddPatientAction(driver)
    patient.navigate_to_add_patient()
    patient.add_patient(
        name, guardian, gender,
        dob, phone, email, blood_group, address
    )

    # Primary assert — catch toast before it disappears (3 sec short wait)
    toast = patient.get_toast_message()

    if "record saved successfully" in toast.lower():
        log.info(f"PASS — Toast: '{toast}'")

    else:
        # Fallback — page lands on Patient List, find name in table
        log.info(f"Toast missed or failed — asserting '{name}' in table")
        assert patient.is_patient_in_table(name), \
            f"FAIL - '{name}' not found in Patient List table after add"

    log.info(f"PASS - Scenario 1: Patient '{name}' added successfully")


# ── Scenario 2: Submit empty form — assert validation error ───────────────
@allure.feature("Add Patient")
def test_add_patient_empty_form(setup):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    patient = AddPatientAction(driver)
    patient.navigate_to_add_patient()
    patient.click_save()
    log.info("Clicked Save without filling any fields")

    toast = patient.get_toast_message()
    assert "field is required" in toast.lower(), \
        f"FAIL - Expected validation error, got: '{toast}'"

    log.info(f"PASS - Scenario 2: Validation error shown: '{toast}'")