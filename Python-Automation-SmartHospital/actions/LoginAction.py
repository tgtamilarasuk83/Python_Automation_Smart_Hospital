from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from actions.base_action import BaseAction
import pytest


class LoginAction(BaseAction):

    def __init__(self,driver):
        super().__init__(driver)

    def validLogin(self):
        self.click(LoginPage.superAdmin)
        self.click(LoginPage.signinBtn)
    
    def emptyfieldLogin(self):
        self.click(LoginPage.signinBtn)

    def invalidusername(self,username):
        self.click(LoginPage.superAdmin)
        self.send_keys(LoginPage.usernameField,username)
        self.click(LoginPage.signinBtn)
    
    def invalidpassword(self,password):
        self.click(LoginPage.superAdmin)
        self.send_keys(LoginPage.passwordField,password)
        self.click(LoginPage.signinBtn)
    
    def assertHome(self):
        return "Smart Hospital & Research Center" in self.get_text(HomePage.pageHeading)
    
    def assertEmptyField(self):
        return "Username field is required" in self.get_text(LoginPage.emptyMessage)
    
    def assertinvalidusername(self):
        return "Invalid Username or Password" in self.get_text(LoginPage.invalidUsername)
    
    def assertinvalidpassword(self):
        return "Invalid Username or Password" in self.get_text(LoginPage.invalidUsername)
    