from actions.base_action import BaseAction
from pages.AddAmbulanceCallPage import AddAmbulanceCall
from pages.AmbulancePage import AmbulancePage
from pages.HomePage import HomePage
from utilities.config_reader import get_value
from utilities.logger import log_generator
import time

class AddAmmbulanceCallAction(BaseAction):

    log = log_generator()

    def __init__(self,driver):
        super().__init__(driver)
    
    def validaddambulanceccall(self):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.addambulance)
        self.click(AddAmbulanceCall.selectPatient)
        self.send_keys(AddAmbulanceCall.selectPatientBox,get_value("config.ini","ambulance details","patientname"))
        self.click(AddAmbulanceCall.selectPatientList)
        self.select_by_visible_text(AddAmbulanceCall.vehicleno,"BS4 - MP20CD2105")
        self.select_date(AddAmbulanceCall.date, "06/12/2026 12:54 PM")
        self.click(AddAmbulanceCall.chargecate)
        self.send_keys(AddAmbulanceCall.chargecatebox,get_value("config.ini","ambulance details","chargecate"))
        self.click(AddAmbulanceCall.chargecatelist)
        self.click(AddAmbulanceCall.chargename)
        self.wait_for_visibility(AddAmbulanceCall.chargenameul)
        self.send_keys(AddAmbulanceCall.chargenamebox,"Private")
        self.click(AddAmbulanceCall.chargenameList)
        self.wait_for_value_to_be_present(AddAmbulanceCall.standardcharge,"150.00")
        self.send_keys(AddAmbulanceCall.note,"This is sample data for test")
        self.wait_for_value_to_be_present(AddAmbulanceCall.payment,"172.50")
        self.click(AddAmbulanceCall.savebtn)
        self.log.info("Added New add ambulance call record")
    

    def invalidaddambulanceccall(self):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.addambulance)
        self.click(AddAmbulanceCall.selectPatient)
        self.send_keys(AddAmbulanceCall.selectPatientBox,get_value("config.ini","ambulance details","patientname"))
        self.click(AddAmbulanceCall.selectPatientList)
        self.select_by_visible_text(AddAmbulanceCall.vehicleno,"BS4 - MP20CD2105")
        self.select_date(AddAmbulanceCall.date, "06/12/2026 12:54 PM")
        self.click(AddAmbulanceCall.chargecate)
        self.send_keys(AddAmbulanceCall.chargecatebox,get_value("config.ini","ambulance details","chargecate"))
        self.click(AddAmbulanceCall.chargecatelist)
        self.send_keys(AddAmbulanceCall.note,"This is sample data for test")
        self.click(AddAmbulanceCall.savebtn)
        self.log.info("added ambulance call with not filling required field")
    
    def assertvalidaddambulancecall(self):
        self.log.info("Asserted new add ambulance call record")
        return get_value("config.ini","ambulance details","addsuccessmess") in self.get_text(AmbulancePage.successmes)
    
    def assertinvalidaddambulancecall(self):
        self.log.info("Asserted invalid add ambulance call record")
        return get_value("config.ini","ambulance details","invalidmess") in self.get_text(AddAmbulanceCall.invalidmes)
