import pytest
from actions.LoginAction import LoginAction
from actions.AddIncomeAction import AddIncomeAction
from utilities.config_reader import get_value
from utilities.logger import log_generator

log = log_generator()


# ── Scenario 1: Add income with all valid details ─────────────────────────
def test_add_income_valid(setup):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    name    = get_value("config.ini", "income details", "name")
    invoice = get_value("config.ini", "income details", "invoice_number")

    add_income = AddIncomeAction(driver)
    add_income.navigate_to_add_income()
    add_income.fill_income_form(
        get_value("config.ini", "income details", "income_head"),
        name, invoice,
        get_value("config.ini", "income details", "date"),
        get_value("config.ini", "income details", "amount"),
        get_value("config.ini", "income details", "description")
    )
    add_income.submit_form()

    assert add_income.assert_first_row_name(name), \
        f"FAIL - '{name}' not found in first row"
    assert add_income.assert_first_row_invoice(invoice), \
        f"FAIL - '{invoice}' not found in first row"
    log.info("PASS - Scenario 1: Income added and verified in first row")


# ── Scenario 2: Mandatory fields only ────────────────────────────────────
def test_add_income_mandatory_fields_only(setup):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    name    = get_value("config.ini", "income details", "mandatory_name")
    invoice = get_value("config.ini", "income details", "mandatory_invoice")

    add_income = AddIncomeAction(driver)
    add_income.navigate_to_add_income()
    add_income.fill_mandatory_fields(
        get_value("config.ini", "income details", "mandatory_income_head"),
        name, invoice,
        get_value("config.ini", "income details", "mandatory_date"),
        get_value("config.ini", "income details", "mandatory_amount")
    )
    add_income.submit_form()

    assert add_income.assert_first_row_name(name), \
        f"FAIL - '{name}' not found in first row"
    assert add_income.assert_first_row_invoice(invoice), \
        f"FAIL - '{invoice}' not found in first row"
    log.info("PASS - Scenario 2: Mandatory fields income verified in first row")


# ── Scenario 3: Empty form — validation error ─────────────────────────────
def test_add_income_empty_form(setup):

    driver = setup

    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed"
    log.info("Login successful")

    add_income = AddIncomeAction(driver)
    add_income.navigate_to_add_income()
    add_income.submit_form()

    assert add_income.assert_validation_error(), \
        "FAIL - Validation error not shown for empty form"
    log.info("PASS - Scenario 3: Validation error shown for empty form")