import pytest
from actions.LoginAction import LoginAction
from actions.PharmacyBillpageAction import PharmacyBillpageAction
from actions.PurchaseMedicineAction import PurchaseMedicineAction
from utilities.excel_reader import get_data

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("supplierName,medicineCategory,medicineName,batchNo,expiryMonth,mrp,batchAmount,salePrice,packingQty,quantity,purchasePrice,tax,paymentMode,paymentNote",get_data("PurchaseMedicine.xlsx","Purchase"))
def test_valid_purchase_medicine(setup,supplierName,medicineCategory,medicineName,batchNo,expiryMonth,mrp,batchAmount,salePrice,packingQty,quantity,purchasePrice,tax,paymentMode,paymentNote):
        driver = setup
        loginact = LoginAction(driver)
        pharmacyact = PharmacyBillpageAction(driver)
        purchaseact = PurchaseMedicineAction(driver)

        loginact.validLogin()
        pharmacyact.clickPharmacy()
        pharmacyact.clickMedicinesButton()

        purchaseact.clickPurchaseMedicineButton()
        purchaseact.clickAddPurchaseButton()

        purchaseact.enterPurchaseDetailsFromExcel(supplierName,medicineCategory,medicineName,batchNo,expiryMonth,mrp,batchAmount,salePrice,packingQty,quantity,purchasePrice,tax,paymentMode,paymentNote)
        purchaseact.clickSaveButton()

        assert purchaseact.isPurchaseSuccessful(), "Purchase was not successful"
        print("Test Passed")
        
@pytest.mark.InvalidPurchase
def test_invalid_purchase_medicine(setup):
    driver = setup
    loginact = LoginAction(driver)
    pharmacyact = PharmacyBillpageAction(driver)
    purchaseact = PurchaseMedicineAction(driver)

    loginact.validLogin()
    pharmacyact.clickPharmacy()
    pharmacyact.clickMedicinesButton()

    purchaseact.clickPurchaseMedicineButton()
    purchaseact.clickAddPurchaseButton()

    purchaseact.clickSaveButton()

    assert purchaseact.isValidationMessageDisplayed(), "Validation message not displayed"
    print("Test Passed")