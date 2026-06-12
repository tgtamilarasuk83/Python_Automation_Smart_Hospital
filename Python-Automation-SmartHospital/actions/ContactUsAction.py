from actions.base_action import BaseAction
from pages.ContactUsPage import ContactUsPage


class ContactUsAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    def submit_form(self, name, email, subject, description):
        self.click(ContactUsPage.contact_us_btn)
        self.send_keys(ContactUsPage.name, name)
        self.send_keys(ContactUsPage.email, email)
        self.send_keys(ContactUsPage.subject, subject)
        self.send_keys(ContactUsPage.description, description)
        self.click(ContactUsPage.submit)
    def is_success_message_displayed(self):
       return self.is_displayed(ContactUsPage.success_message)
    def is_Error_message_displayed(self):
       return self.is_displayed(ContactUsPage.Error_message)