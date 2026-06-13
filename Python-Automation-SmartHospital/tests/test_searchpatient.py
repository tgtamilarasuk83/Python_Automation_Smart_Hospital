import pytest
from actions.LoginAction import LoginAction
from actions.SearchPatientAction import SearchPatientAction
from utilities.logger import log_generator
log = log_generator()
valid_search_data = [
    "John Marshall",
    ]
invalid_search_data = [
    "ghdckdcd",
]
@pytest.mark.parametrize("name", valid_search_data)
def test_search_valid_patient(setup, name):

    driver = setup
    # Step 1 - Login
    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed - home page not reached"
    log.info("Login successful")

    search = SearchPatientAction(driver)
    search.navigate_to_patient_list()

    search.search_patient(name)

    assert search.is_search_result_displayed(name), \
        f"FAIL - '{name}' not found in search results"

    log.info(f"PASS - '{name}' found in search results")
@pytest.mark.parametrize("name", invalid_search_data)
def test_search_invalid_patient(setup, name):

    driver = setup

    # Step 1 - Login
    login = LoginAction(driver)
    login.validLogin()
    assert login.assertHome(), "Login failed - home page not reached"
    log.info("Login successful")

    # Step 2 - Go to Patient List
    search = SearchPatientAction(driver)
    search.navigate_to_patient_list()

    # Step 3 - Search invalid name
    search.search_patient(name)

    # Step 4 - Assert "No data available in table" is shown
    assert search.is_no_data_displayed(), \
        f"FAIL - 'No data available' message not shown for invalid name '{name}'"

    log.info(f"PASS - 'No data available' correctly shown for invalid name '{name}'")

