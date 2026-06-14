import re
import pytest
import allure
from actions.LoginAction import LoginAction
from actions.AddPatientAction import AddPatientAction
from utilities.excel_reader import get_data
from utilities.logger import log_generator

log = log_generator()

patient_data = get_data("AddPatientdetails.xlsx", "Sheet1")
invalid_phone_data = get_data("AddPatientdetails.xlsx", "Sheet2")
invalid_email_data = get_data("AddPatientdetails.xlsx", "Sheet3")
# ── Regex for pre-check ───────────────────────────────────────────────────
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\d+$'



# ── Scenario 1: Add patient with valid data ───────────────────────────────
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


# ── Scenario 3: Invalid phone — 8 columns only, no expected_error ─────────
@allure.feature("Add Patient")
@pytest.mark.parametrize(
    "name,guardian,gender,dob,phone,email,blood_group,address",
    invalid_phone_data
)
def test_add_patient_invalid_phone(setup, name, guardian, gender, dob,
                                   phone, email, blood_group, address):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    # Regex pre-check — confirm phone has letters
    assert not re.match(PHONE_REGEX, str(phone)), \
        f"Test data error — '{phone}' contains only numbers"
    log.info(f"Confirmed '{phone}' is invalid phone — proceeding")

    patient = AddPatientAction(driver)
    patient.navigate_to_add_patient()
    patient.add_patient(
        name, guardian, gender,
        dob, phone, email, blood_group, address
    )

    assert patient.is_phone_error_displayed(), \
        f"FAIL - Phone error not shown for '{phone}'"

    log.info(f"PASS - Scenario 3: Phone error shown for '{phone}'")


# ── Scenario 4: Invalid email — 8 columns only, no expected_error ─────────
@allure.feature("Add Patient")
@pytest.mark.parametrize(
    "name,guardian,gender,dob,phone,email,blood_group,address",
    invalid_email_data
)
def test_add_patient_invalid_email(setup, name, guardian, gender, dob,
                                   phone, email, blood_group, address):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    # Regex pre-check — confirm email is invalid
    assert not re.match(EMAIL_REGEX, str(email)), \
        f"Test data error — '{email}' is a valid email"
    log.info(f"Confirmed '{email}' is invalid email via regex — proceeding")

    patient = AddPatientAction(driver)
    patient.navigate_to_add_patient()
    patient.add_patient(
        name, guardian, gender,
        dob, phone, email, blood_group, address
    )

    assert patient.is_email_error_displayed(), \
        f"FAIL - Email error not shown for '{email}'"

    log.info(f"PASS - Scenario 4: Email error shown for '{email}'")