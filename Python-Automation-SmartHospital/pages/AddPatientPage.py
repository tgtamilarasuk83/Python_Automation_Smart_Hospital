from selenium.webdriver.common.by import By


class AddPatientPage:

    # ── Navigation ────────────────────────────────────────────────────────
    patient_menu    = (By.XPATH, "//span[normalize-space()='Patient']")
    add_patient     = (By.XPATH, "//div[@class='box-header ptbnull']//a[1]")

    # ── Form Fields ───────────────────────────────────────────────────────
    patient_name    = (By.XPATH, "//input[@id='name']")
    guardian_name   = (By.XPATH, "//div[@class='col-lg-6 col-md-6 col-sm-6']//input[@name='guardian_name']")
    gender          = (By.XPATH, "//select[@id='addformgender']")
    dob_age         = (By.XPATH, "//input[@id='age']")
    dob_year        = (By.XPATH, "//input[@id='year']")
    dob_month       = (By.XPATH, "//select[@id='month']")
    dob_day         = (By.XPATH, "//input[@id='day']")
    phone           = (By.XPATH, "//input[@id='number']")
    email           = (By.XPATH, "//input[@id='addformemail']")
    blood_group     = (By.XPATH, "//div[@class='col-sm-3']//select[@name='blood_group']")
    address         = (By.XPATH, "//div[@class='col-lg-12 col-md-12 col-sm-12']//input[@name='address']")
    save_button     = (By.XPATH, "//button[@id='formaddpabtn']")

    # ── Toast Message — success and error both use same locator ───────────
    toast_message   = (By.XPATH, "//div[@class='toast-message']")

    # ── Patient List — first row name for table assertion ─────────────────
    first_row_name  = (By.XPATH, "//table//tbody/tr[1]/td[1]")