from selenium.webdriver.common.by import By

class AmbulanceListPage:

    def __init__(self,driver):
        super().__init__(driver)

    addAmbulance = (By.XPATH,"//a[contains(text(),'Add Ambulance')]")
    vehicleno = (By.NAME,"vehicle_no")
    vehiclemodel = (By.NAME,"vehicle_model")
    yearmade = (By.CSS_SELECTOR,"input[name='manufacture_year']")
    drivername = (By.CSS_SELECTOR,"input[name='driver_name']")
    drivercontact = (By.CSS_SELECTOR,"input[name='driver_contact']")
    vehicletype = (By.XPATH,"//select[@name='vehicle_type']")
    message = (By.XPATH,"//*[@id='toast-container']/div/div")
    savebtn = (By.ID,"formaddbtn")
    tablerow1 = (By.XPATH,"//table[@id='DataTables_Table_0']/tbody/tr[1]")
    delbtn = (By.XPATH,"//*[@id='DataTables_Table_0']/tbody/tr[1]/td[2]/div/a/i")
