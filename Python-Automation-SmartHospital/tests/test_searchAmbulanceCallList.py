from actions.SearchAmbulanceCallListAction import SearchAmbulanceCallListAction
from actions.LoginAction import LoginAction
import pytest


@pytest.mark.usefixtures("setup")
def test_validSearchAmbulanceCall(setup):
    driver = setup
    logact = LoginAction(driver)
    searchact = SearchAmbulanceCallListAction(driver)
    logact.validLogin()
    searchact.searchvalidambulancecall()
    assert searchact.assertingvalidsearch()
    print("Test Passed")

@pytest.mark.parametrize("ambulanceNumber",["UP14 #$ 1234","@!21 CD 4587"])
def test_invalidSearchAmbulanceCall(setup,ambulanceNumber):
    driver = setup
    logact = LoginAction(driver)
    searchact = SearchAmbulanceCallListAction(driver)
    logact.validLogin()
    searchact.searchinvalidambulancecall(ambulanceNumber)
    assert searchact.assertinginvalidsearch()
    print("Test Passed")
