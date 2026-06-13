from selenium.webdriver.common.by import By


class AddIncomePage:

    finance_menu     = (By.XPATH, "//span[normalize-space()='Finance']")
    income_link      = (By.XPATH, "//a[normalize-space()='Income']")
    add_income_btn   = (By.XPATH, "//a[@class='btn btn-primary btn-sm addincome']")
    income_head      = (By.XPATH, "//select[@id='inc_head_id']")
    name             = (By.XPATH, "//input[@id='name']")
    invoice_number   = (By.XPATH, "//input[@id='invoice_no']")
    date             = (By.XPATH, "//input[@id='date']")
    amount           = (By.XPATH, "//input[@id='amount']")
    description      = (By.XPATH, "//textarea[@id='description']")
    submit_btn       = (By.XPATH, "//button[@id='add_incomebtn']")
    toast_message    = (By.XPATH, "//div[contains(@class,'toast-message')]")

    # ── First row assertion — newest record always appears at top ─────────
    first_row_name    = (By.XPATH, "//table//tbody/tr[1]/td[1]")
    first_row_invoice = (By.XPATH, "//table//tbody/tr[1]/td[2]")

    @staticmethod
    def income_name_in_table(name):
        return (By.XPATH,
                f"//table//tbody//td[contains(normalize-space(.), '{name}')]")