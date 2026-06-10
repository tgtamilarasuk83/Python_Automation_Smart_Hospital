from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from actions.base_action import base_action

class LoginAction(base_action):

    def __init__(self,driver):
        super().__init__(self,driver)

    def validLogin(self):
        self.click(LoginPage.superAdmin)
        self.click(LoginPage.signinBtn)

    def assertHome(self):
        return "Smart Hospital & Research Center" in self.get_text(HomePage.pageHeading)
    
    