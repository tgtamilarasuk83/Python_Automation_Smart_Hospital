from selenium.webdriver.common.by import By


class ContactUsPage:

    # Contact Us Button
    contact_us_btn = (By.XPATH, "//a[normalize-space()='Contact Us']")

    # Form Fields
    name = (By.XPATH, "//input[@id='name']")
    email = (By.XPATH, "//input[@id='email']")
    subject = (By.XPATH, "//input[@id='subject']")
    description = (By.XPATH, "//textarea[@id='description']")

    # Submit Button
    submit = (By.XPATH, "//input[@name='submit']")

    # Success Message
    success_message = (By.XPATH, "//div[@class='alert alert-success' and normalize-space()='We will contact you soon.']")