from actions.base_action import BaseAction
from pages.BloodStockPage import BloodStockPage
from selenium.webdriver.common.keys import Keys



class BloodStockAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)

    def is_blood_stock_status_page_displayed(self):
        return self.is_displayed(
            BloodStockPage.blood_bank_status
        )

    def select_blood_group(self, blood_group):
        self.click(
            BloodStockPage.blood_group_option(blood_group)
        )

    def is_blood_bag_details_displayed(self):
        return self.is_displayed(
            BloodStockPage.blood_bag_table
        )

    def is_blood_component_details_displayed(self):
        return self.is_displayed(
            BloodStockPage.component_table
        )
    def clickAddIcon(self):
        self.click(BloodStockPage.add_icon)

    def isBloodDonorPopupDisplayed(self):
        return self.is_displayed(BloodStockPage.popup)

    def selectBloodDonor(self, donor):

        self.click(BloodStockPage.blood_donor)

        self.send_keys(BloodStockPage.search_box, donor)

        self.click(BloodStockPage.dynamic_option(donor))

    def enterDonateDate(self, donate_date):

        self.clear(BloodStockPage.donate_date)

        self.send_keys(BloodStockPage.donate_date, donate_date)

        self.driver.find_element(
            *BloodStockPage.donate_date
        ).send_keys(Keys.TAB)

    def enterBag(self, bag):
        self.send_keys(BloodStockPage.bag_field, bag)

    def selectChargeCategory(self, category):

        self.click(BloodStockPage.charge_category)

        self.send_keys(BloodStockPage.search_box, category)

        self.click(BloodStockPage.dynamic_option(category))

    def selectChargeName(self, charge_name):

        self.click(BloodStockPage.charge_name)

        self.send_keys(BloodStockPage.search_box, charge_name)

        self.click(BloodStockPage.dynamic_option(charge_name))

    def clickCalculateButton(self):
        self.click(BloodStockPage.calculate_button)

    def clickSaveButton(self):
        self.click(BloodStockPage.save_button)

    def isBagNumberDisplayed(self, bag):
        return self.is_displayed(
            BloodStockPage.added_bag_number(bag)
        )
    def clickIssueButton(self, bag):
        self.click(BloodStockPage.issue_button(bag))

    def isBloodIssuePageDisplayed(self):
        return self.is_displayed(BloodStockPage.issue_date)
    