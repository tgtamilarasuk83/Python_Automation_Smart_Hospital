import pytest
from actions.LoginAction import LoginAction
from actions.SearchPatientAction import SearchPatientAction
from utilities.logger import log_generator

log = log_generator()
valid_search_data = [
    "Olivier Thomas",
    ]
@pytest.mark.parametrize("name", valid_search_data)
def test_search_valid_patient(setup, name):

    driver = setup

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

