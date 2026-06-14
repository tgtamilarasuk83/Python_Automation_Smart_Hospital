from selenium.webdriver.common.by import By

class BloodIssuePage:

    blood_bank_menu = (By.XPATH, "//span[normalize-space()='Blood Bank']")
    blood_issue_details = (By.XPATH, "//a[normalize-space()='Blood Issue Details']")
    issue_blood_button = (By.XPATH, "//button[contains(text(),'Issue Blood')]")
    patient_dropdown = (By.XPATH, "(//span[contains(@class,'select2-selection--single')])[1]")
    issue_date = (By.XPATH, "//input[@name='date_of_issue']")
    doctor_dropdown = (By.XPATH, "(//span[contains(@class,'select2-selection--single')])[2]")
    blood_group = (By.XPATH, "//span[contains(@id,'blood_group')]")
    reference_name = (By.XPATH, "//input[@id='reference']")
    blood_bag_dropdown = (By.XPATH, "(//span[@role='combobox']/following::span[text()='Select'])[1]")
    charge_category_dropdown = (By.XPATH, "(//span[contains(@class,'select2-selection--single')])[5]")
    charge_name_dropdown = (By.XPATH, "(//span[@class='select2-selection__rendered'])[6]")
    payment_amount = (By.XPATH, "//input[@id='payment_amount']")
    save_button = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
    success_message = (By.XPATH, "//div[contains(@class,'toast-message')]")
    search_box = (By.XPATH, "//input[@class='select2-search__field']")
    first_option = (By.XPATH, "//li[text()='Select']/following-sibling::li[1]")
    first_row = (By.XPATH,"(//table/tbody/tr)[1]")
    delete_button = (By.XPATH,"(//i[@class='fa fa-trash'])[1]")
    delete_message = (By.XPATH,"//div[contains(text(),'Record Deleted Successfully')]")
    validation_message = (By.XPATH,"//div[@class='toast toast-error']")
    
    @staticmethod
    def dynamic_option(option):
        return (By.XPATH,f"//li[contains(@class,'select2-results__option') and contains(text(),'{option}')]")
    
    new_patient = (By.XPATH,"//span[contains(text(),'New Patient')]")
    name = (By.XPATH,"//label[text()='Name']/following-sibling::input")
    age_year = (By.CSS_SELECTOR,"input[placeholder='Year']")
    age_month = (By.CSS_SELECTOR,"input[placeholder='Month']")
    age_day = (By.CSS_SELECTOR,"input[placeholder='Day']")
    patient_save = (By.XPATH,"(//button[normalize-space()='Save'])[3]")
    add_patient_popup = (By.XPATH,"//h4[contains(text(),'Add Patient')]")
    success_message = (By.XPATH,"//div[contains(@class,'toast-message')]")