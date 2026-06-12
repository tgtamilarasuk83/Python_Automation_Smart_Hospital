from actions.base_action import BaseAction
from pages.DonorManagementPage import DonorManagementPage


class DonorManagementAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    def clickBloodBankMenu(self):
        self.click(DonorManagementPage.blood_bank_menu)

    def clickDonorDetails(self):
        self.click(DonorManagementPage.donor_details)

    def clickAddBloodDonor(self):
        self.click(DonorManagementPage.add_blood_donor)

    def enterDonorName(self, donor_name):
        self.send_keys(DonorManagementPage.donor_name, donor_name)

    def enterDateOfBirth(self, dob):
        self.send_keys(DonorManagementPage.date_of_birth, dob)

    def enterBloodGroup(self, blood_group):
        self.send_keys(DonorManagementPage.blood_group, blood_group)

    def enterGender(self, gender):
        self.send_keys(DonorManagementPage.gender, gender)

    def enterFatherName(self, father_name):
        self.send_keys(DonorManagementPage.father_name, father_name)

    def enterContactNumber(self, contact_number):
        self.send_keys(DonorManagementPage.contact_number, contact_number)

    def enterAddress(self, address):
        self.send_keys(DonorManagementPage.address, address)

    def clickSaveButton(self):
        self.click(DonorManagementPage.save_button)

    def addDonor(self,
                 donor_name,
                 dob,
                 blood_group,
                 gender,
                 father_name,
                 contact_number,
                 address):

        self.clickAddBloodDonor()

        self.enterDonorName(donor_name)
        self.enterDateOfBirth(dob)
        self.enterBloodGroup(blood_group)
        self.enterGender(gender)
        self.enterFatherName(father_name)
        self.enterContactNumber(contact_number)
        self.enterAddress(address)

        self.clickSaveButton()

    def searchDonor(self, donor_name):
        self.send_keys(DonorManagementPage.search_donor, donor_name)

    def getSearchResult(self):
        return self.get_text(DonorManagementPage.search_result)
    def getValidationMessage(self):
        return self.get_text(DonorManagementPage.validation_messages)
    def verifyDonorName(self, donor_name):
        result = self.get_text(DonorManagementPage.search_result)
        return donor_name in result