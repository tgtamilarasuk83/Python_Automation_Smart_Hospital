from actions.AmbulanceListAction import AmbulanceListAction
from actions.LoginAction import LoginAction
import pytest
from utilities.excel_reader import get_data

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("vehicleno,vehiclemodel,yearmade,drivername,drivercontact,vehicletype",get_data("AddAmbulanceData.xlsx","Validdata"))
def test_addambulance(setup,vehicleno,vehiclemodel,yearmade,drivername,drivercontact,vehicletype):
    driver = setup
    logact = LoginAction(driver)
    addact = AmbulanceListAction(driver)
    logact.validLogin()
    addact.validaddambulance(vehicleno,vehiclemodel,yearmade,drivername,drivercontact,vehicletype)
    assert addact.assertvalidaddambulance()
    print("Test Passed")

@pytest.mark.parametrize("vehicleno,yearmade,drivername,drivercontact,vehicletype",get_data("AddAmbulanceData.xlsx","Invaliddata"))
def test_invalidaddambulance(setup,vehicleno,yearmade,drivername,drivercontact,vehicletype):
    driver = setup
    logact = LoginAction(driver)
    addact = AmbulanceListAction(driver)
    logact.validLogin()
    addact.invalidaddambulance(vehicleno,yearmade,drivername,drivercontact,vehicletype)
    assert addact.assertinvalidaddambulance()
    print("Test Passed")

def test_deletedetails(setup):
    driver = setup
    logact = LoginAction(driver)
    addact = AmbulanceListAction(driver)
    logact.validLogin()
    addact.deletedetail()
    assert addact.assertdeletedetail()
    print("Test Passed")

