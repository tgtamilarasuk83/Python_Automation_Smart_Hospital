from selenium.webdriver.common.by import By


class AddPatientPage:

    patient_menu    = (By.XPATH, "//span[normalize-space()='Patient']")
    add_patient     = (By.XPATH, "//div[@class='box-tools pull-right']//descendant::a[@data-toggle='modal']")
    patient_name    = (By.XPATH, "//small[@class='req']//following::input[@id='name']")
    guardian_name   = (By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6']//input[@name='guardian_name']")
    gender          = (By.XPATH, "//select[@id='addformgender']")
    dob_age         = (By.XPATH, "//input[@id='age']")
    dob_year        = (By.XPATH, "//input[@id='year']")
    dob_month       = (By.XPATH, "//select[@id='month']")
    dob_day         = (By.XPATH, "//input[@id='day']")
    phone           = (By.XPATH, "//div//child::input[@id='number']")
    email           = (By.XPATH, "//input[@id='addformemail']")
    blood_group     = (By.XPATH, "//div[@class='col-sm-3']//select[@name='blood_group']")
    address         = (By.XPATH, "//div[@class='col-lg-12 col-md-12 col-sm-12']//input[@name='address']")
    save_button     = (By.XPATH, "//button[@id='formaddpabtn']")
    toast_message   = (By.XPATH, "//div[@class='toast-message']")
    phone_error      = (By.XPATH, "//p[normalize-space()='Phone field must contain only numbers']")
    email_error      = (By.XPATH, "//p[normalize-space()='Email field must contain a valid email address']")
    first_row_name  = (By.XPATH, "//table//tbody/tr[1]/td[1]")