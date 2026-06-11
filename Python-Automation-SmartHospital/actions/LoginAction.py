from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from actions.base_action import BaseAction
from utilities.logger import log_generator

class LoginAction(BaseAction):

    log = log_generator()

    def __init__(self,driver):
        super().__init__(driver)

    def validLogin(self):
        self.click(LoginPage.superAdmin)
        self.click(LoginPage.signinBtn)
        self.log.info("Logged in as Super Admin")
    
    def emptyfieldLogin(self):
        self.click(LoginPage.signinBtn)
        self.log.info("Logged in using empty field")

    def invalidusername(self,username):
        self.click(LoginPage.superAdmin)
        self.send_keys(LoginPage.usernameField,username)
        self.click(LoginPage.signinBtn)
        self.log.info("Logged in using invalid username")
    
    def invalidpassword(self,password):
        self.click(LoginPage.superAdmin)
        self.send_keys(LoginPage.passwordField,password)
        self.click(LoginPage.signinBtn)
        self.log.info("Logged in using invalid password")
    
    def assertHome(self):
        self.log.info("Asserted super admin log in")
        return "Smart Hospital & Research Center" in self.get_text(HomePage.pageHeading)
    
    
    def assertEmptyField(self):
        self.log.info("Asserted empty field log in")
        return "Username field is required" in self.get_text(LoginPage.emptyMessage)
    
    def assertinvalidusername(self):
        self.log.info("Asserted invalid username log in")
        return "Invalid Username or Password" in self.get_text(LoginPage.invalidUsername)
    
    def assertinvalidpassword(self):
        self.log.info("Asserted invalid password log in")
        return "Invalid Username or Password" in self.get_text(LoginPage.invalidUsername)
    