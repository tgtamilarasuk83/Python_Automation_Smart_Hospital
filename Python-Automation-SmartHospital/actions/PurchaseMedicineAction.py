from actions.base_action import BaseAction
from pages.PurchaseMedicinePage import PurchaseMedicinePage
from utilities.excel_reader import get_data
from utilities.logger import log_generator

logger = log_generator()


class PurchaseMedicineAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    def clickPurchaseMedicineButton(self):
        self.click(PurchaseMedicinePage.purchaseMedicineButton)
        logger.info("Clicked Purchase Medicine button")

    def clickAddPurchaseButton(self):
        self.click(PurchaseMedicinePage.addPurchaseButton)
        logger.info("Clicked Add Purchase button")

    def clickSaveButton(self):
        self.click(PurchaseMedicinePage.saveButton)
        logger.info("Clicked Save button")

    def enterPurchaseDetailsFromExcel(self, supplierName, medicineCategory, medicineName, batchNo, expiryMonth, mrp, batchAmount, salePrice, packingQty, quantity, purchasePrice, tax, paymentMode, paymentNote):
        self.click(PurchaseMedicinePage.supplierDropdown)
        self.send_keys(PurchaseMedicinePage.supplierSearchBox, supplierName)
        self.click(PurchaseMedicinePage.supplierOption(supplierName))
        self.select_by_visible_text(PurchaseMedicinePage.medicineCategoryDropdown, medicineCategory)
        self.select_by_visible_text(PurchaseMedicinePage.medicineDropdown, medicineName)
        self.send_keys(PurchaseMedicinePage.batchNoField, batchNo)
        self.send_keys(PurchaseMedicinePage.expiryMonthField, str(expiryMonth))
        self.send_keys(PurchaseMedicinePage.mrpField, str(mrp))
        self.send_keys(PurchaseMedicinePage.batchAmountField, str(batchAmount))
        self.send_keys(PurchaseMedicinePage.salePriceField, str(salePrice))
        self.send_keys(PurchaseMedicinePage.packingQtyField, str(packingQty))
        self.send_keys(PurchaseMedicinePage.quantityField, str(quantity))
        self.send_keys(PurchaseMedicinePage.purchasePriceField, str(purchasePrice))
        self.send_keys(PurchaseMedicinePage.taxField, str(tax))
        self.select_by_visible_text(PurchaseMedicinePage.paymentModeDropdown, paymentMode)
        self.send_keys(PurchaseMedicinePage.paymentNoteField, paymentNote)
        logger.info(f"Entered all purchase details for supplier: {supplierName}")

    def isPurchaseSuccessful(self):
        return self.is_displayed(PurchaseMedicinePage.addPurchaseButtoncheck)
    def isValidationMessageDisplayed(self):
        return self.is_displayed(PurchaseMedicinePage.validationMessage)
    