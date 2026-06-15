from selenium.webdriver.common.by import By
from utilities.config_reader import get_value
class AddAmbulanceCall:

    def __init__(self,driver):
        self.driver = driver
    
    selectPatient = (By.XPATH,"//*[@id='myModal']/div/div/div/div/div[1]/div/span[1]/span[1]/span")
    selectPatientBox = (By.CLASS_NAME,"select2-search__field")
    selectPatientList = (By.XPATH,f"//li[contains(text(),'{get_value('config.ini','ambulance details','patientname')}')]")
    vehicleno = (By.ID,"vehicle_no")
    date = (By.NAME,"date")
    standardcharge = (By.ID,"standard_charge")
    payment = (By.ID,"payment_amount")
    chargecate = (By.XPATH,"//*[@id='formcall']/div[1]/div/div/div[1]/div[4]/div/div/span/span[1]/span")
    chargecateselect = (By.NAME,"charge_category_id")
    chargecatebox = (By.CLASS_NAME,"select2-search__field")
    chargecatelist = (By.XPATH,f"//li[contains(text(),'{get_value('config.ini','ambulance details','chargecate')}')]")
    chargename = (By.ID,"select2-code-container")
    chargenamebox = (By.CLASS_NAME,"select2-search__field")
    chargenameselect = (By.XPATH,"//*[@id='code']")
    chargenameul = (By.ID,"select2-code-results")
    chargenameList = (By.XPATH,f"//li[contains(text(),'{get_value('config.ini','ambulance details','chargename')}')]")
    note = (By.ID,"note")
    savebtn = (By.ID,"formcallbtn")
    invalidmes = (By.XPATH,"//*[@id='toast-container']/div/div/p[2]")
    