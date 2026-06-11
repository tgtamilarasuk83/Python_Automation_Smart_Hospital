from actions.ContactUsAction import ContactUsAction
import pytest
from selenium import webdriver   

@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://demo.smart-hospital.in/")

    yield driver

    driver.quit()


def test_contact_us(setup):

    driver = setup

    contact = ContactUsAction(driver)

    contact.submit_form(
        "Tamil",
        "tamilarasu@test.com",
        "Automation Issue",
        "This is a test message from automation script"
    )

    assert contact.is_success_message_displayed()