import pytest
from actions.LoginAction import LoginAction
from actions.BloodIssueAction import BloodIssueAction
from actions.BloodStockAction import BloodStockAction
from utilities.excel_reader import get_data
from utilities.csv_reader import get_data as get_csv_data

class TestBloodStock:

    @pytest.mark.parametrize("blood_group", get_data("BloodStock.xlsx", "BloodGroup"))
    def test_verify_blood_stock_details(self, setup, blood_group):
        login = LoginAction(setup)
        blood_issue = BloodIssueAction(setup)
        blood_stock = BloodStockAction(setup)
        login.validLogin()
        blood_issue.clickBloodBankMenu()
        assert blood_stock.is_blood_stock_status_page_displayed()
        blood_stock.select_blood_group(blood_group[0])
        assert blood_stock.is_blood_bag_details_displayed()
        assert blood_stock.is_blood_component_details_displayed()

    @pytest.mark.parametrize("blood_donor,donate_date,bag,charge_category,charge_name", get_data("BloodStock.xlsx", "AddDonor"))
    def test_add_blood_donor(self, setup, blood_donor, donate_date, bag, charge_category, charge_name):
        login = LoginAction(setup)
        blood_issue = BloodIssueAction(setup)
        blood_stock = BloodStockAction(setup)
        login.validLogin()
        blood_issue.clickBloodBankMenu()
        blood_stock.clickAddIcon()
        assert blood_stock.isBloodDonorPopupDisplayed()
        blood_stock.selectBloodDonor(blood_donor)
        blood_stock.enterDonateDate(donate_date)
        blood_stock.enterBag(str(bag))
        blood_stock.selectChargeCategory(charge_category)
        blood_stock.selectChargeName(charge_name)
        blood_stock.clickCalculateButton()
        blood_stock.clickSaveButton()
        assert blood_stock.isBagNumberDisplayed(str(bag))

    @pytest.mark.parametrize("bag", get_csv_data("IssueBag.csv"))
    def test_blood_issue_navigation(self, setup, bag):
        login = LoginAction(setup)
        blood_issue = BloodIssueAction(setup)
        blood_stock = BloodStockAction(setup)
        login.validLogin()
        blood_issue.clickBloodBankMenu()
        blood_stock.clickIssueButton(bag[0])
        assert blood_stock.isBloodIssuePageDisplayed()
        
    def test_donor_mandatory_fields_validation(self,setup):
        login = LoginAction(setup)
        blood_issue = BloodIssueAction(setup)
        blood_stock = BloodStockAction(setup)
        login.validLogin()
        blood_issue.clickBloodBankMenu()
        blood_stock.clickAddIcon()
        assert blood_stock.isBloodDonorPopupDisplayed()
        blood_stock.clickSaveButton()
        actual_message = blood_stock.getValidationMessage()
        assert "Blood Donor field is required" in actual_message