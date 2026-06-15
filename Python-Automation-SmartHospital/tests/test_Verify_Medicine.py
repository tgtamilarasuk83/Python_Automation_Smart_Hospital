import pytest
from actions.LoginAction import LoginAction
from actions.VerifyMedicineAction import VerifyMedicineAction
from actions.PharmacyBillpageAction import PharmacyBillpageAction

@pytest.mark.bala
def test_valid_medicine_search(setup):
    driver = setup
    logact       = LoginAction(driver)
    verifymed    = VerifyMedicineAction(driver)
    pharmacybill = PharmacyBillpageAction(driver)

    logact.validLogin()
    pharmacybill.clickPharmacy()
    pharmacybill.clickMedicinesButton()
    verifymed.assertmedicinepage()
    verifymed.searchvalidmedicine()
    verifymed.medicinestatus("present")
    
@pytest.mark.bala
def test_invalid_medicine_search(setup):
    driver = setup
    logact       = LoginAction(driver)
    verifymed    = VerifyMedicineAction(driver)
    pharmacybill = PharmacyBillpageAction(driver)

    logact.validLogin()
    pharmacybill.clickPharmacy()
    pharmacybill.clickMedicinesButton()
    verifymed.assertmedicinepage()
    verifymed.searchinvalidmedicine()
    verifymed.medicinestatus("absent")

@pytest.mark.bala  
def test_delete_medicine(setup):
    driver = setup
    logact       = LoginAction(driver)
    verifymed    = VerifyMedicineAction(driver)
    pharmacybill = PharmacyBillpageAction(driver)
    logact.validLogin()
    pharmacybill.clickPharmacy()
    pharmacybill.clickMedicinesButton()
    verifymed.assertmedicinepage()
    verifymed.deletemedicine()
    verifymed.deletenotfoundmedicine()
        
