from pages.AmbulancePage import AmbulancePage
from pages.HomePage import HomePage
from actions.base_action import BaseAction
from utilities.config_reader import get_value
from utilities.logger import log_generator

class SearchAmbulanceCallListAction(BaseAction):

    log = log_generator()

    def __init__(self,driver):
        super().__init__(driver)

    def searchvalidambulancecall(self):
        self.click(HomePage.ambulanceBtn)
        self.send_keys(AmbulancePage.searchInput,get_value("config.ini","ambulance details","ambulanceNumber"))
        self.wait_for_text_to_be_present(AmbulancePage.tableValue,get_value("config.ini","ambulance details","ambulanceNumber"))
        self.log.info("Search Valid Ambulance Call List")

    def searchinvalidambulancecall(self,ambulanceNumber):
        self.click(HomePage.ambulanceBtn)
        self.send_keys(AmbulancePage.searchInput,ambulanceNumber)
        self.log.info("Searched using invalid ambulance call list")

    
    def assertingvalidsearch(self):
        self.log.info("Asserted valid search of ambulance call list")
        return get_value("config.ini","ambulance details","ambulanceNumber") in self.get_text(AmbulancePage.tableValue)

    
    def assertinginvalidsearch(self):
        self.log.info("Asserted invalid search of ambulance call list")
        return get_value("config.ini","ambulance details","invalidambulancesearchmessage") in self.get_text(AmbulancePage.tableValue2)

        

