from selenium.webdriver.common.by import By

class ComplaintPage:

    complaintBtn = By.XPATH, "//a[normalize-space()='Complain']"
    name = By.ID, "name"
    email = By.ID, "email"
    contact = By.ID, "contact"
    description = By.ID, "description"
    submit = By.CSS_SELECTOR, "input[type='submit'][name='submit']"
    successMsg = By.XPATH, "//*[contains(@class,'alert-success')]"
    errorMsg = By.XPATH, (
        "//*[contains(@class,'alert-danger') "
        "or contains(@class,'invalid-feedback') "
        "or contains(@class,'text-danger')]"
    )