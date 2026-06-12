from selenium.webdriver.common.by import By
class SearchPatientPage:
    def __init__(self, driver):
        self.driver = driver
    patient_menu      = (By.XPATH, "//i[@class='fa fa-user']//following-sibling::span")
    records_zero      = (By.XPATH, "//div[contains(normalize-space(),'Records: 0 to 0 of 0')]")
    search_box        = (By.XPATH, "//label//child::input[@type='search']")
    def search_result_name(name):
        return (By.XPATH,
                f"//table//tbody//tr[not(contains(@style,'display: none'))]//td[contains(normalize-space(.), '{name}')]")
