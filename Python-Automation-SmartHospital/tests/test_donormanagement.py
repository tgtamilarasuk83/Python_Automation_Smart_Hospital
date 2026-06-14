import pytest
from actions.LoginAction import LoginAction
from actions.DonorManagementAction import DonorManagementAction
from pages.DonorManagementPage import DonorManagementPage
from utilities.excel_reader import get_data as get_excel_data
from utilities.csv_reader import get_data as get_csv_data


class TestDonorManagement:

    @pytest.mark.parametrize("donor_name,dob,blood_group,gender,father_name,contact_number,address",get_csv_data("AddDonor.csv"))
    def test_add_donor(self,setup,donor_name,dob,blood_group,gender,father_name,contact_number,address):
        login = LoginAction(setup)
        login.validLogin()
        donor = DonorManagementAction(setup)
        donor.clickBloodBankMenu()
        donor.clickDonorDetails()
        donor.addDonor(donor_name,dob,blood_group,gender,father_name,contact_number,address)
        assert donor.is_displayed(DonorManagementPage.donor_name)

    @pytest.mark.parametrize("donor_name,dob,blood_group,gender",get_excel_data("DonorManagement.xlsx", "DonorMandatoryField")) 
    def test_add_donor_mandatory_fields(self,setup,donor_name,dob,blood_group,gender):
        login = LoginAction(setup)
        login.validLogin()
        donor = DonorManagementAction(setup)
        donor.clickBloodBankMenu()
        donor.clickDonorDetails()
        donor.clickAddBloodDonor()
        donor.enterDonorName(donor_name)
        donor.enterDateOfBirth(dob)
        donor.enterBloodGroup(blood_group)
        donor.enterGender(gender)
        donor.clickSaveButton()
        assert donor.is_displayed(DonorManagementPage.donor_name)

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
       
    @pytest.mark.parametrize("donor_name",get_excel_data("DonorManagement.xlsx", "SearchDonor"))
    def test_search_donor(self, setup, donor_name):
        login = LoginAction(setup)
        login.validLogin()
        donor = DonorManagementAction(setup)
        donor.clickBloodBankMenu()
        donor.clickDonorDetails()
        donor.searchDonor(donor_name[0])
        assert donor.verifyDonorName(donor_name[0])
 