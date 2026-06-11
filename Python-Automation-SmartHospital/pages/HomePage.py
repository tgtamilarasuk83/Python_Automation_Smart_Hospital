from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self,driver):
        self.driver = driver
    
    pageHeading = (By.XPATH,"//header[@id='alert']/nav/div[1]/child::span")
    ambulanceBtn = (By.XPATH,"//section[@id='sibe-box']/ul[2]/child::li[11]/a")
    
    