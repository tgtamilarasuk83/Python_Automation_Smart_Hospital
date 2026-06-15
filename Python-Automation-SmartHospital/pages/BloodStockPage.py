from selenium.webdriver.common.by import By

class BloodStockPage:
    blood_bankstatus = (By.XPATH, "//h3[contains(text(),'Blood Bank Status')]")
    blood_bagtable = (By.XPATH, "(//table)[1]")
    component_table = (By.XPATH, "(//table)[2]")
    add_icon = (By.XPATH, "(//button[contains(@class,'btn-primary')])[1]")
    popup = (By.XPATH, "//h4[contains(text(),'Blood Donor Details')]")
    blood_donor = (By.XPATH, "//span[@id='select2-blood_donor_id-container']")
    search_box = (By.XPATH, "//input[@class='select2-search__field']")
    donate_date = (By.XPATH, "//input[@name='donate_date']")
    bag_field = (By.XPATH, "//input[@name='bag_no']")
    charge_category = (By.XPATH, "//span[@id='select2-charge_category-container']")
    charge_name = (By.XPATH, "//span[@id='select2-code-container']")
    calculate_button = (By.XPATH, "//button[normalize-space()='Calculate']")
    save_button = (By.XPATH, "(//button[text()=' Save']/self::button)[1]")
    validationMessage = (By.XPATH, "//div[contains(@class,'toast-message')]")
    issue_date = (By.XPATH, "//label[contains(text(),'Issue Date')]")

    @staticmethod
    def dynamic_option(option):
        return (By.XPATH, f"//li[contains(@class,'select2-results__option') and contains(normalize-space(),'{option}')]")

    @staticmethod
    def added_bag_number(bag):
        return (By.XPATH, f"(//table//td[normalize-space()='{bag}'])[1]")

    @staticmethod
    def issue_button(bag):
        return (By.XPATH, f"//td[normalize-space()='{bag}']/parent::tr//button[contains(text(),'Issue')]")
    
    @staticmethod
    def blood_group_option(blood_group):
        return (By.XPATH, f"//li[normalize-space()='{blood_group}']")