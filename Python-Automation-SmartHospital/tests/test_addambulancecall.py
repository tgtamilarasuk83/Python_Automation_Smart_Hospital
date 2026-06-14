from actions.AddAmbulanceCallAction import AddAmmbulanceCallAction
from actions.LoginAction import LoginAction
import pytest
from utilities.csv_reader import get_data


@pytest.mark.parametrize("patientname,vehicleno,date,chargecate,chargename,standardcharge,note,payment",get_data("AddAmbulanceCallValid.csv"))
@pytest.mark.usefixtures("setup")
def test_validaddAmbulanceCall(setup,patientname,vehicleno,date,chargecate,chargename,standardcharge,note,payment):
    driver = setup
    logact = LoginAction(driver)
    addact = AddAmmbulanceCallAction(driver)
    logact.validLogin()
    addact.validaddambulanceccall(patientname,vehicleno,date,chargecate,chargename,standardcharge,note,payment)
    assert addact.assertvalidaddambulancecall()
    print("Test Passed")

def test_invalidaddAmbulanceCall(setup):
    driver = setup
    logact = LoginAction(driver)
    addact = AddAmmbulanceCallAction(driver)
    logact.validLogin()
    addact.invalidaddambulanceccall()
    assert addact.assertinvalidaddambulancecall()
    print("Test Passed")

def test_emptyaddAmbulanceCall(setup):
    driver = setup
    logact = LoginAction(driver)
    addact = AddAmmbulanceCallAction(driver)
    logact.validLogin()
    addact.invalidemptyfieldaddambulance()
    assert addact.assertemptyfieldaddambulancecall()
    print("Test Passed") 


