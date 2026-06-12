from selenium.webdriver.common.by import By
class AmbulancePage:

    def __init__(self,driver):
        self.driver = driver

    searchInput = (By.CSS_SELECTOR,"input[type='search']")
    tableValue = (By.XPATH,"//table[@id='DataTables_Table_0']/tbody/tr[1]/td[5]")
    tableValue2 = (By.XPATH,"//table[@id='DataTables_Table_0']/tbody/tr[1]/td[1]/child::div")
    ambulanceList = (By.XPATH,"/html/body/div[1]/div/section/div/div/div/div[1]/div/a[2]")
    successmes = (By.XPATH,"//*[@id='toast-container']/div/div")
    addambulance = (By.LINK_TEXT,"Add Ambulance Call")
    

