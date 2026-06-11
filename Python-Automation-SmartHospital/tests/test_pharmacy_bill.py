import pytest
from actions.LoginAction import LoginAction
from actions.PharmacyBillpageAction import PharmacyBillpageAction

pharmacypage_URL = "https://demo.smart-hospital.in/admin/pharmacy/bill"


@pytest.mark.usefixtures("setup")
class TestPharmacyBillPage:

    @pytest.mark.billpage
    def test_pharmacy_bill_page_displayed(self, setup):
        LoginAction(setup).validLogin()
        pa = PharmacyBillpageAction(setup)
        pa.clickPharmacy()
        assert pa.pageisDisplayed(), "Pharmacy Bill page not displayed"
        print("Successfully moved to the Pharmacy Bill page")

    @pytest.mark.searchname
    @pytest.mark.parametrize(
        "patient_name, result",
        [
            ("Ashok", "present"),
            ("praveen raj", "not found"),
            ("victor xavier", "not found"),
        ],
    )
    def test_search_patient(self, setup, patient_name, result):
        LoginAction(setup).validLogin()
        pa = PharmacyBillpageAction(setup)

        pa.clickPharmacy()
        actual_url = setup.current_url
        assert (
            actual_url == pharmacypage_URL
        ), f"Not on pharmacy bill page. URL: {actual_url}"
        print("The user is on the Pharmacy Bill page")

        pa.clickPatientsearchbar()
        pa.searchName(patient_name)

        searched = setup.find_element(
            *__import__(
                "pages.PharmacyBillPage", fromlist=["PharmacyBillPage"]
            ).PharmacyBillPage.searchInputbar
        ).get_attribute("value")

        if result.lower() == "present":
            found = pa.isPatientPresent(searched)
            assert found is not None, f"Patient '{patient_name}' not found in table"
            print("Patient is present")
        elif result.lower() == "not found":
            no_data = pa.isNoDataMessageDisplayed()
            assert no_data, f"Expected 'No data available' for '{patient_name}'"
            print("Patient not found — no data message shown")

    @pytest.mark.exportbill
    def test_export_bill_csv(self, setup):
        LoginAction(setup).validLogin()
        pa = PharmacyBillpageAction(setup)
        pa.clearDownloadsFolder()
        pa.clickCSVButton()
        assert pa.isCSVFileDownloaded(), "CSV file was not downloaded successfully"
