from selenium.webdriver.common.by import By

class DonorManagementPage:

    blood_bankmenu = (By.XPATH, "//span[normalize-space()='Blood Bank']")
    donor_details = (By.XPATH, "//a[contains(normalize-space(),'Donor Details')]")
    add_blooddonor = (By.XPATH, "//a[contains(@onclick,'myModal')]")
    add_donorpopup = (By.XPATH, "//h4[text()='Add Donor Details']")
    donor_name = (By.XPATH, "(//input[@name='donor_name'])[1]")
    date_of_birth = (By.XPATH, "(//input[@name='date_of_birth'])[1]")
    blood_group = (By.XPATH, "(//select[@name='blood_group'])[1]")
    gender = (By.XPATH, "(//select[@name='gender'])[1]")
    father_name = (By.NAME, "father_name")
    contact_number = (By.NAME, "contact_no")
    address = (By.NAME, "address")
    save_button = (By.XPATH, "//button[@id='formaddbtn']")
    validation_messages = (By.XPATH,"//div[contains(@class,'toast-message')]")
    search_donor = (By.XPATH,"//div[@class='dataTables_filter']/descendant::input")
    search_result = (By.XPATH,"(//table//tbody)[1]")
 