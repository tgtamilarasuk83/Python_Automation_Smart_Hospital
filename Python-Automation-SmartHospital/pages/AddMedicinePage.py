from selenium.webdriver.common.by import By


class AddMedicinePage:
    medicine_tab = (By.CLASS_NAME, "modal-content")
    
    add_medicine_button = (By.XPATH, "//a[@class='btn btn-primary btn-sm addmedicine']")
    save_button = (By.ID, "formaddbtn")

    medicine_name_field = (By.ID, "medicine_name")
    composition_field = (By.NAME, "medicine_composition")
    min_level_field = (By.XPATH, "//form[@id='formadd']//input[@name='min_level']")
    reorder_level_field = (By.XPATH, "//form[@id='formadd']//input[@name='reorder_level']")
    tax_field = (By.NAME, "vat")
    box_packing_field = (By.XPATH, "//form[@id='formadd']//input[@name='unit_packing']")
    vat_field = (By.XPATH, "//form[@id='formadd']//input[@name='vat_ac']")
    rack_number_field = (By.XPATH, "//form[@id='formadd']//input[@name='rack_number']")
    note_field = (By.NAME, "note")

    category_dropdown = (By.NAME, "medicine_category_id")
    company_dropdown = (By.NAME, "medicine_company")
    group_dropdown = (By.NAME, "medicine_group")
    unit_dropdown = (By.NAME, "unit")