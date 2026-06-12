from pages.AddItemStockPage import AddNewStockPage
from actions.base_action import BaseAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddItemStockAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    # ---------------- UI ACTIONS ---------------- #

    def clickInventory(self):
        self.move_to_element(AddNewStockPage.InventoryPage)
        self.click(AddNewStockPage.InventoryPage)

    def clickAddItemStock(self):
        self.wait_for_clickable(AddNewStockPage.ADD_NEW_STOCK)
        self.click(AddNewStockPage.ADD_NEW_STOCK)

    def AddItemStock(self, itemcategory, item, supplier, store,
                     quantity, purchaseprice, description):

        self.wait_for_visible(AddNewStockPage.ITEM_CATEGORY)
        self.select_by_visible_text(AddNewStockPage.ITEM_CATEGORY, itemcategory)

        self.wait_for_visible(AddNewStockPage.ITEM)
        self.select_by_visible_text(AddNewStockPage.ITEM, item)

        self.wait_for_visible(AddNewStockPage.SUPPLIER)
        self.select_by_visible_text(AddNewStockPage.SUPPLIER, supplier)

        self.wait_for_visible(AddNewStockPage.STORE)
        self.select_by_visible_text(AddNewStockPage.STORE, store)

        self.send_keys(AddNewStockPage.QUANTITY, quantity)
        self.send_keys(AddNewStockPage.PURCHASE_PRICE, purchaseprice)
        self.send_keys(AddNewStockPage.DESCRIPTION, description)

        self.click(AddNewStockPage.SAVE_BUTTON)
       

    # ---------------- TABLE DATA ---------------- #

    def get_row_data(self):
        self.driver.refresh()
        row_data = []

        for i in range(1, 8):
            if i == 5:
                continue

            xpath = f'//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[{i}]'
            element = self.driver.find_element("xpath", xpath)
            row_data.append(element.text)

        print(row_data)
        return row_data
    
    def assetinventory(self):
        inventory = self.wait_for_clickable(AddNewStockPage.ADD_NEW_STOCK)
        return inventory.is_displayed()
    def ToeMessage(self):
        toemessage = self.wait_for_visibility(AddNewStockPage.TOAST_MESSAGE)
        return toemessage.is_displayed()
    
    def deleteStockitem(self):
     self.jsclicking(AddNewStockPage.Deletebutton)

     alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

     assert alert is not None

     print(alert.text)
     alert.accept()
     
    
        