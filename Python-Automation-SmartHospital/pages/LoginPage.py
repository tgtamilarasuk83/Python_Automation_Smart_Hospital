from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
    
    superAdmin = (By.XPATH,"//div[@class='form-bottom']/div/child::a[contains(text(),'Super Admin')]")
    signinBtn = (By.XPATH,"//button[@type='submit']")