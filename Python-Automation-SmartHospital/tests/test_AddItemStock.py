from actions.AddItemStockAction import AddItemStockAction
from actions.LoginAction import LoginAction

def test_invetoryPage(setup):
    driver = setup
    add_stock = AddItemStockAction(driver)
    login_action = LoginAction(driver)
    login_action.validLogin()
    add_stock.clickInventory()
    stock = AddItemStockAction(driver)
    assert stock.assetinventory()
    

    
    
def test_add_item_stock(setup):
    driver = setup
    add_stock = AddItemStockAction(driver)
    # login first
    login_action = LoginAction(driver)
    login_action.validLogin()
    add_stock.clickInventory()
    add_stock.clickAddItemStock()
    add_stock.AddItemStock(itemcategory="Syringe Packs",item="Syringe",supplier="VK Supplier",store="SK Pharma",quantity="100",purchaseprice="500",description="Adding new stock for Syringe")
    data1 = [
    "Syringe",
    "Syringe Packs",
    "VK Supplier",
    "SK Pharma",
    "Adding new stock for Syringe",
    "100",]
    
    data = add_stock.get_row_data()
    print(data)

    assert data1 == data
    
def test_add_item_stockMissinddata(setup):
    driver = setup
    add_stock = AddItemStockAction(driver)
    # login first
    login_action = LoginAction(driver)
    login_action.validLogin()
    add_stock.clickInventory()
    add_stock.clickAddItemStock()
    add_stock.AddItemStock(itemcategory="Syringe Packs",item="Syringe",supplier="VK Supplier",store="SK Pharma",quantity="",purchaseprice="",description="")

    assert add_stock.ToeMessage()
    
def test_deleteStockitem(setup):
    driver =setup
    add_stock = AddItemStockAction(driver)
    # login first
    login_action = LoginAction(driver)
    login_action.validLogin()
    add_stock.clickInventory()
    add_stock.deleteStockitem()
    