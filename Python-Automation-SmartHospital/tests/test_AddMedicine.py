import pytest
from actions.LoginAction import LoginAction
from actions.AddMedicineAction import AddMedicineAction
from actions.VerifyMedicineAction import VerifyMedicineAction
from actions.PharmacyBillpageAction import PharmacyBillpageAction
from utilities.csv_reader import get_data


class TestAddMedicine:
    @pytest.mark.parametrize(
        "medicineName, medicineCategory, medicineCompany, medicineComposition, "
        "medicineGroup, unit, minLevel, reorderLevel, tax, boxPacking, vat, rackNumber, note",
        get_data("AddMedicine.csv"),
    )
    def test_add_new_medicine(
        self,
        setup,
        medicineName,
        medicineCategory,
        medicineCompany,
        medicineComposition,
        medicineGroup,
        unit,
        minLevel,
        reorderLevel,
        tax,
        boxPacking,
        vat,
        rackNumber,
        note,
    ):
        driver = setup
        logact       = LoginAction(driver)
        verifymed    = VerifyMedicineAction(driver)
        pharmacybill = PharmacyBillpageAction(driver)
        addmedicine  = AddMedicineAction(driver)

        logact.validLogin()
        pharmacybill.clickPharmacy()
        pharmacybill.clickMedicinesButton()
        verifymed.assertmedicinepage()
        addmedicine.click_add_medicine_button()
        addmedicine.enter_medicine_details(
            medicineName, medicineCategory, medicineCompany, medicineComposition,
            medicineGroup, unit, minLevel, reorderLevel, tax, boxPacking, vat, rackNumber, note,
        )
        addmedicine.click_save_button()
        addmedicine.verify_medicine_added()