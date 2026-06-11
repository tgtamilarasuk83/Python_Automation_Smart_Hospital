from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
    
    superAdmin = (By.XPATH,"//div[@class='form-bottom']/div/child::a[contains(text(),'Super Admin')]")
    signinBtn = (By.XPATH,"//button[@type='submit']")
    emptyMessage = (By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div[2]/form/div[1]/span/p")
    invalidUsername = (By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[1]")
    usernameField = (By.XPATH,"//input[@id='email']")
    passwordField = (By.XPATH,"//input[@id='password']")