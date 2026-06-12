from actions.AddAmbulanceCallAction import AddAmmbulanceCallAction
from actions.LoginAction import LoginAction
import pytest


@pytest.mark.usefixtures("setup")
def test_validSearchAmbulanceCall(setup):
    driver = setup
    logact = LoginAction(driver)
    addact = AddAmmbulanceCallAction(driver)
    logact.validLogin()
    addact.validaddambulanceccall()
    assert addact.assertvalidaddambulancecall()
    print("Test Passed")

def test_invalidSearchAmbulanceCall(setup):
    driver = setup
    logact = LoginAction(driver)
    addact = AddAmmbulanceCallAction(driver)
    logact.validLogin()
    addact.invalidaddambulanceccall()
    assert addact.assertinvalidaddambulancecall()
    print("Test Passed")


