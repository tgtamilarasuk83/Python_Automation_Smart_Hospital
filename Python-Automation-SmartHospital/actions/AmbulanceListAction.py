from pages.AmbulanceListPage import AmbulanceListPage
from actions.base_action import BaseAction
from pages.AmbulancePage import AmbulancePage
from utilities.config_reader import get_value
from utilities.logger import log_generator
from pages.HomePage import HomePage

class AmbulanceListAction(BaseAction):

    log = log_generator()

    def __init__(self,driver):
        super().__init__(driver)

    def validaddambulance(self,vehicleno,vehiclemodel,yearmade,drivername,drivercontact,vehicletype):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.ambulanceList)
        self.click(AmbulanceListPage.addAmbulance)
        self.send_keys(AmbulanceListPage.vehicleno,vehicleno)
        self.send_keys(AmbulanceListPage.vehiclemodel,vehiclemodel)
        self.send_keys(AmbulanceListPage.yearmade,yearmade)
        self.send_keys(AmbulanceListPage.drivername,drivername)
        self.send_keys(AmbulanceListPage.drivercontact,drivercontact)
        self.select_by_visible_text(AmbulanceListPage.vehicletype,vehicletype)
        self.click(AmbulanceListPage.savebtn)
        self.log.info("Added Ambulance")
    
    def invalidaddambulance(self,vehicleno,yearmade,drivername,drivercontact,vehicletype):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.ambulanceList)
        self.click(AmbulanceListPage.addAmbulance)
        self.send_keys(AmbulanceListPage.vehicleno,vehicleno)
        self.send_keys(AmbulanceListPage.yearmade,yearmade)
        self.send_keys(AmbulanceListPage.drivername,drivername)
        self.send_keys(AmbulanceListPage.drivercontact,drivercontact)
        self.select_by_visible_text(AmbulanceListPage.vehicletype,vehicletype)
        self.click(AmbulanceListPage.savebtn)
        self.log.info("added Invalid add ambulance")
    
    def deletedetail(self):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.ambulanceList)
        self.hover(AmbulanceListPage.tablerow1)
        self.click(AmbulanceListPage.delbtn)
        self.log.info("Deleted the Details")
    
    def assertvalidaddambulance(self):
        self.log.info("Asserted add ambulance")
        return get_value("config.ini","ambulance details","addambulancevalidmessage") in self.get_text(AmbulanceListPage.message)
    
    def assertinvalidaddambulance(self):
        self.log.info("Asserted invalid add ambulance")
        return get_value("config.ini","ambulance details","addambulanceinvalidmessage") in self.get_text(AmbulanceListPage.message)
    
    def assertdeletedetail(self):
        return self.handle_alert()
