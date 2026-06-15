import pytest
from actions.LoginAction import LoginAction
from actions.PharmacyBillpageAction import PharmacyBillpageAction


def test_pharmacy_bill_page_displayed(setup):
    driver = setup
    loginact = LoginAction(driver)
    pharact = PharmacyBillpageAction(driver)

    loginact.validLogin()
    pharact.clickPharmacy()

    assert pharact.isOnPharmacyBillPage()
    print("Successfully moved to the Pharmacy Bill page")


@pytest.mark.parametrize("patient_name, result", [
    ("Ashok",         "present"),
    ("praveen raj",   "not found"),
    ("victor xavier", "not found"), ])
def test_search_patient(setup, patient_name, result):
    driver = setup
    loginact = LoginAction(driver)
    pharact = PharmacyBillpageAction(driver)

    loginact.validLogin()
    pharact.clickPharmacy()
    pharact.clickPatientsearchbar()
    pharact.searchName(patient_name)

    if result.lower() == "present":
        found = pharact.isPatientPresent(patient_name)
        assert found is not None
        print("Patient is present")

    elif result.lower() == "not found":
        no_data = pharact.isNoDataMessageDisplayed()
        assert no_data
        print("Patient not found")