from pages.complainPage import ComplaintPage
from utilities.excel_reader import get_data
import os


class ComplaintAction:

    def __init__(self, driver):
        self.driver = driver

    def submit_complaint(self):

        print("Current Working Directory:", os.getcwd())
        print("Excel Exists:", os.path.exists("./data_files/TamilarasuK_ComplaintdataSheet.xlsx"))

        test_data = get_data(
            "TamilarasuK_ComplaintdataSheet.xlsx",
            "Sheet1"
        )

        for row in test_data:

            name = row[0]
            email = row[1]
            contact = row[2]
            description = row[3]

            self.driver.find_element(*ComplaintPage.complaintBtn).click()

            self.driver.find_element(*ComplaintPage.name).clear()
            self.driver.find_element(*ComplaintPage.name).send_keys(name)

            self.driver.find_element(*ComplaintPage.email).clear()
            self.driver.find_element(*ComplaintPage.email).send_keys(email)

            self.driver.find_element(*ComplaintPage.contact).clear()
            self.driver.find_element(*ComplaintPage.contact).send_keys(contact)

            self.driver.find_element(*ComplaintPage.description).clear()
            self.driver.find_element(*ComplaintPage.description).send_keys(description)

            self.driver.find_element(*ComplaintPage.submit).click()

    def submit_without_filling_form(self):
        self.driver.find_element(*ComplaintPage.complaintBtn).click()
        self.driver.find_element(*ComplaintPage.submit).click()

    def submit_without_name(self,email,contact,description):
        self.driver.find_element(*ComplaintPage.complaintBtn).click()
        self.driver.find_element(*ComplaintPage.email).send_keys(email)
        self.driver.find_element(*ComplaintPage.contact).send_keys(contact)
        self.driver.find_element(*ComplaintPage.description).send_keys(description)
        self.driver.find_element(*ComplaintPage.submit).click()

    def submit_without_email(self,name,contact,description):
        self.driver.find_element(*ComplaintPage.complaintBtn).click()
        self.driver.find_element(*ComplaintPage.name).send_keys(name)
        self.driver.find_element(*ComplaintPage.contact).send_keys(contact)
        self.driver.find_element(*ComplaintPage.description).send_keys(description)
        self.driver.find_element(*ComplaintPage.submit).click()

    def submit_without_contact(self,name,email,description):
        self.driver.find_element(*ComplaintPage.complaintBtn).click()
        self.driver.find_element(*ComplaintPage.name).send_keys(name)
        self.driver.find_element(*ComplaintPage.email).send_keys(email)
        self.driver.find_element(*ComplaintPage.description).send_keys(description)
        self.driver.find_element(*ComplaintPage.submit).click()

    def submit_without_description(self,name,email,contact):
        self.driver.find_element(*ComplaintPage.complaintBtn).click()
        self.driver.find_element(*ComplaintPage.name).send_keys(name)
        self.driver.find_element(*ComplaintPage.email).send_keys(email)
        self.driver.find_element(*ComplaintPage.contact).send_keys(contact)
        self.driver.find_element(*ComplaintPage.submit).click()