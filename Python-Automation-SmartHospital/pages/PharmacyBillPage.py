from selenium.webdriver.common.by import By

class PharmacyBillPage:
    pharmacyMenu           = (By.XPATH, "//a[@href='https://demo.smart-hospital.in/admin/pharmacy/bill']")
    pharmacyBillPageHeader = (By.XPATH, "//h3[@class='box-title titlefix']")
    searchInputbar         = (By.XPATH, "//input[@type='search']")
    searchnamerow          = (By.XPATH, "//tbody/tr/td[4]")
    noDataMessage          = (By.XPATH, "//td[@class='dataTables_empty']")
    medicinesBtn           = (By.XPATH, "//a[contains(text(),'Medicines')]")