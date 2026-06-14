from selenium.webdriver.common.by import By


class AddIncomePage:

    finance_menu     = (By.XPATH, "//span[normalize-space()='Finance']")
    income_link      = (By.XPATH, "//a[normalize-space()='Income']")
    add_income_btn   = (By.XPATH, "//div[@class='col-md-12']//descendant::a[@data-toggle='modal']")
    income_head      = (By.XPATH, "//select[@id='inc_head_id']")
    name             = (By.XPATH, "//label[@for='exampleInputEmail1']//following::input[@id='name']")
    invoice_number   = (By.XPATH, "//label[@for='exampleInputEmail1']//following-sibling::input[@id='invoice_no']")
    date             = (By.XPATH, "//input[@id='date']")
    amount           = (By.XPATH, "//div[@class='form-group']/child::input[@id='amount']")
    description      = (By.XPATH, "//textarea[@id='description']")
    submit_btn       = (By.XPATH, "//button[@id='add_incomebtn']")
    toast_message    = (By.XPATH, "//div[contains(@class,'toast-message')]")
    first_row_name    = (By.XPATH, "//table//tbody/tr[1]/td[1]")
    first_row_invoice = (By.XPATH, "//table//tbody/tr[1]/td[2]")

    @staticmethod
    def income_name_in_table(name):
        return (By.XPATH,
                f"//table//tbody//td[contains(normalize-space(.), '{name}')]")