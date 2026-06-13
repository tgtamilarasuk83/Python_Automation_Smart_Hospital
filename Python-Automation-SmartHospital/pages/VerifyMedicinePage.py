from selenium.webdriver.common.by import By

class VerifyMedicinePage:
    medicinebutton      = (By.XPATH, "//div[@class='box-tools pull-right']/a")
    medicinesearchbar   = (By.XPATH, "//input[@placeholder='Search...']")
    medicinenotfoundtxt = (By.XPATH, "//td[@class='dataTables_empty']/child::div[contains(text(),'No data available in table')]")

    @staticmethod
    def medicinecheckbox(medicine):
        return (By.XPATH, f"//tr[td[normalize-space()='{medicine}']]//input[@type='checkbox']")

    @staticmethod
    def medicinetext(searchedmedicine):
        return (By.XPATH, f"//tr[td[contains(normalize-space(),'{searchedmedicine}')]]/td[2]")