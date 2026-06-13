from selenium.webdriver.common.by import By
class PurchaseMedicinePage:
    def __init__(self,driver):
        super().__init__(driver)
    purchaseMedicineButton = (By.XPATH, "//a[normalize-space()='Purchase']")
    addPurchaseButton = (By.XPATH, "//a[contains(@class,'addpurchase')]")
    supplierDropdown = (By.XPATH, "(//span[contains(@class,'select2-selection--single')])[1]")
    supplierSearchBox = (By.XPATH, "//span[contains(@class,'select2-container--open')]//input[@type='search']")
    medicineCategoryDropdown = (By.NAME, "medicine_category_id[]")
    medicineDropdown = (By.NAME, "medicine_name[]")
    batchNoField = (By.ID, "batchno")
    expiryMonthField = (By.ID, "expiry")
    mrpField = (By.ID, "mrp")
    batchAmountField = (By.ID, "batch_amount")
    salePriceField = (By.ID, "sale_price")
    packingQtyField = (By.ID, "packing_qty")
    quantityField = (By.ID, "quantity0")
    purchasePriceField = (By.ID, "purchase_price0")
    taxField = (By.ID, "purchase_tax0")
    paymentModeDropdown = (By.NAME, "payment_mode")
    paymentNoteField = (By.NAME, "payment_note")
    saveButton = (By.XPATH, "//button[contains(text(),'Save')]")
    addPurchaseButtoncheck = (By.XPATH, "//a[contains(@class,'addpurchase')]")
    @staticmethod
    def supplierOption(supplier):
        return (By.XPATH, f"//li[contains(@class,'select2-results__option') and normalize-space()='{supplier}']")
    validationMessage = (By.CSS_SELECTOR, "div.toast-error")