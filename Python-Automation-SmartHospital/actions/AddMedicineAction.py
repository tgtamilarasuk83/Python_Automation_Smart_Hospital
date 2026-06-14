from selenium.webdriver.support import expected_conditions as EC
from actions.base_action import BaseAction
from pages.AddMedicinePage import AddMedicinePage
from utilities.logger import log_generator


class AddMedicineAction(BaseAction):
    logger = log_generator()

    def __init__(self, driver):
        super().__init__(driver)
        self.page = AddMedicinePage()

    def click_add_medicine_button(self):
        self.logger.info("Clicking Add Medicine button")
        self.click(self.page.add_medicine_button)

    def enter_medicine_details(
        self,
        medicine_name,
        medicine_category,
        medicine_company,
        medicine_composition,
        medicine_group,
        unit,
        min_level,
        reorder_level,
        tax,
        box_packing,
        vat,
        rack_number,
        note,
    ):
        self.logger.info(f"Entering medicine details for: {medicine_name}")
        self.clear(self.page.medicine_name_field)
        self.send_keys(self.page.medicine_name_field, medicine_name)

        self.clear(self.page.composition_field)
        self.send_keys(self.page.composition_field, medicine_composition)

        self.clear(self.page.min_level_field)
        self.send_keys(self.page.min_level_field, min_level)

        self.clear(self.page.reorder_level_field)
        self.send_keys(self.page.reorder_level_field, reorder_level)

        self.clear(self.page.tax_field)
        self.send_keys(self.page.tax_field, tax)

        self.clear(self.page.box_packing_field)
        self.send_keys(self.page.box_packing_field, box_packing)

        self.clear(self.page.vat_field)
        self.send_keys(self.page.vat_field, vat)

        self.clear(self.page.rack_number_field)
        self.send_keys(self.page.rack_number_field, rack_number)

        self.clear(self.page.note_field)
        self.send_keys(self.page.note_field, note)

        # Dropdowns
        self.select_by_visible_text(self.page.category_dropdown, medicine_category)
        self.select_by_visible_text(self.page.company_dropdown, medicine_company)
        self.select_by_visible_text(self.page.group_dropdown, medicine_group)
        self.select_by_visible_text(self.page.unit_dropdown, unit)

    def click_save_button(self):
        self.logger.info("Clicking Save button")
        self.click(self.page.save_button)

    def verify_medicine_added(self):
        self.logger.info("Verifying medicine modal is visible")
        return self.is_displayed(self.page.medicine_tab)