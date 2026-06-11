from actions.LoginAction import LoginAction
from actions.DonorManagementAction import DonorManagementAction
from utilities.excel_reader import get_data
import pytest


class TestDonorManagement:

    def test_add_donor(self, setup):

        login = LoginAction(setup)
        login.validLogin()

        donor = DonorManagementAction(setup)

        donor.clickBloodBankMenu()
        donor.clickDonorDetails()

        donor.addDonor(
            "Raja",
            "12/05/1998",
            "B+",
            "Male",
            "Ramesh",
            "9876543210",
            "Chennai"
        )

    def test_all_fields_empty(self, setup):

        login = LoginAction(setup)
        login.validLogin()

        donor = DonorManagementAction(setup)

        donor.clickBloodBankMenu()
        donor.clickDonorDetails()

        donor.clickAddBloodDonor()
        donor.clickSaveButton()

        validation_message = donor.getValidationMessage()

        assert "Donor Name field is required" in validation_message
        assert "Date Of Birth field is required" in validation_message
        assert "Blood Group field is required" in validation_message
        assert "Gender field is required" in validation_message

    @pytest.mark.parametrize(
    "donor_name",
    get_data("SearchDonor.xlsx", "Sheet1")
)
    def test_search_donor(self, setup, donor_name):

        login = LoginAction(setup)
        login.validLogin()

        donor = DonorManagementAction(setup)

        donor.clickBloodBankMenu()
        donor.clickDonorDetails()

        donor.searchDonor(donor_name[0])

        assert donor.verifyDonorName(donor_name[0])