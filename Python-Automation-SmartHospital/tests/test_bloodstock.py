import pytest
from actions.LoginAction import LoginAction
from actions.BloodIssueAction import BloodIssueAction
from actions.BloodStockAction import BloodStockAction

from utilities.excel_reader import get_data
from utilities.csv_reader import get_data as get_csv_data


class TestBloodStock:

    @pytest.mark.parametrize(
        "blood_group",
        get_data("BloodStock.xlsx", "BloodGroup")
    )
    def test_verify_blood_stock_details(
        self,
        setup,
        blood_group
    ):
        login = LoginAction(setup)
        blood_issue = BloodIssueAction(setup)
        blood_stock = BloodStockAction(setup)

        login.validLogin()

        blood_issue.clickBloodBankMenu()

        assert blood_stock.is_blood_stock_status_page_displayed()

        blood_stock.select_blood_group(blood_group[0])

        assert blood_stock.is_blood_bag_details_displayed()

        assert blood_stock.is_blood_component_details_displayed()
