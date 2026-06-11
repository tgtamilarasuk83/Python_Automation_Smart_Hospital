from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from actions.base_action import BaseAction
from utilities.logger import log_generator
from utilities.config_reader import get_value

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
        return get_value("config.ini","login details","validassertmess") in self.get_text(HomePage.pageHeading)
    
    
    def assertEmptyField(self):
        self.log.info("Asserted empty field log in")
        return get_value("config.ini","login details","emptyfielderrmessage") in self.get_text(LoginPage.emptyMessage)
    
    def assertinvalidusername(self):
        self.log.info("Asserted invalid username log in")
        return get_value("config.ini","login details","invalidmessage") in self.get_text(LoginPage.invalidUsername)
    
    def assertinvalidpassword(self):
        self.log.info("Asserted invalid password log in")
        return get_value("config.ini","login details","invalidmessage") in self.get_text(LoginPage.invalidUsername)
    