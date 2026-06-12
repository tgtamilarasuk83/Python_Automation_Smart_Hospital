from selenium.webdriver.common.by import By


class AddNewStockPage:

    # BUTTONS
    InventoryPage = (By.XPATH, "//span[contains(text(),'Inventory')]")
    ADD_NEW_STOCK = (By.XPATH, "//a[@class='btn btn-primary btn-sm additemstock']")

    # DROPDOWN
    ITEM_CATEGORY = (By.XPATH, "//select[@id='item_category_id']")
    ITEM = (By.XPATH, "//select[@id='item_id']")
    STORE = (By.XPATH, "//select[@id='store_id']")
    SUPPLIER = (By.XPATH, "//select[@id='supplier_id']")

    # INPUT FIELDS
    QUANTITY = (By.XPATH, "//input[@id='quantity']")
    PURCHASE_PRICE = (By.XPATH, "//input[@id='purchase_price']")
    DESCRIPTION = (By.XPATH, "//textarea[@id='description']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and @id='form1btn']")

    # TOAST / ALERT
    TOAST_MESSAGE = (By.XPATH, "//div[contains(@class,'toast-message')]")
    # delete_item
    Deleteitem = (By.XPATH,'//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[1]')
    Deletebutton =(By.XPATH,"//tbody/tr[3]/td[1]/div[2]/a[2]/i[1]")
    
