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

    
    def validaddambulanceccall(self,patientname,vehicleno,date,chargecate,chargename,standardcharge,note,payment):
        try:
            self.click(HomePage.ambulanceBtn)
            self.click(AmbulancePage.addambulance)
            self.click(AddAmbulanceCall.selectPatient)
            self.send_keys(AddAmbulanceCall.selectPatientBox,patientname)
            self.click(AddAmbulanceCall.selectPatientList)
            self.select_by_visible_text(AddAmbulanceCall.vehicleno,vehicleno)
            self.select_date(AddAmbulanceCall.date,date)
            self.click(AddAmbulanceCall.chargecate)
            self.send_keys(AddAmbulanceCall.chargecatebox,chargecate)
            self.click(AddAmbulanceCall.chargecatelist)
            self.click(AddAmbulanceCall.chargename)
            self.wait_for_visibility(AddAmbulanceCall.chargenameul)
            self.send_keys(AddAmbulanceCall.chargenamebox,chargename)
            self.click(AddAmbulanceCall.chargenameList)
            self.wait_for_value_to_be_present(AddAmbulanceCall.standardcharge,standardcharge)
            self.send_keys(AddAmbulanceCall.note,note)
            self.wait_for_value_to_be_present(AddAmbulanceCall.payment,payment)
            self.click(AddAmbulanceCall.savebtn)
            self.log.info("Added New add ambulance call record")
        except Exception as e:
            self.driver.save_screenshot("Screenshots/addambulancecall.png")
    

    def invalidaddambulanceccall(self):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.addambulance)
        self.click(AddAmbulanceCall.selectPatient)
        self.send_keys(AddAmbulanceCall.selectPatientBox,get_value("config.ini","ambulance details","patientname"))
        self.click(AddAmbulanceCall.selectPatientList)
        self.select_by_visible_text(AddAmbulanceCall.vehicleno,get_value("config.ini","ambulance details","vehicleno"))
        self.select_date(AddAmbulanceCall.date,("config.ini","ambulance details","date"))
        self.click(AddAmbulanceCall.chargecate)
        self.send_keys(AddAmbulanceCall.chargecatebox,get_value("config.ini","ambulance details","chargecate"))
        self.click(AddAmbulanceCall.chargecatelist)
        self.send_keys(AddAmbulanceCall.note,get_value("config.ini","ambulance details","note"))
        self.click(AddAmbulanceCall.savebtn)
        self.log.info("added ambulance call with not filling required field")
    
    def invalidemptyfieldaddambulance(self):
        self.click(HomePage.ambulanceBtn)
        self.click(AmbulancePage.addambulance)
        self.click(AddAmbulanceCall.savebtn)
        self.log.info("added ambulance call with empty field")
    
    def assertvalidaddambulancecall(self):
        self.log.info("Asserted new add ambulance call record")
        return get_value("config.ini","ambulance details","addsuccessmess") in self.get_text(AmbulancePage.successmes)
    
    def assertinvalidaddambulancecall(self):
        self.log.info("Asserted invalid add ambulance call record")
        return get_value("config.ini","ambulance details","invalidmess") in self.get_text(AddAmbulanceCall.invalidmes)
    
    def assertemptyfieldaddambulancecall(self):
        self.log.info("Asserted empty field add ambulance call record")
        print(self.get_text(AddAmbulanceCall.emptyfieldinvalid))
        return get_value("config.ini","ambulance details","emptyinvalidmess") in self.get_text(AddAmbulanceCall.invalidmes)
