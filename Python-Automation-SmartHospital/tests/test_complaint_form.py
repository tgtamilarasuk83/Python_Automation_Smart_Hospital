from actions.ComplainAction import ComplaintAction
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


def test_complaint_form(setup):
    driver = setup
    complaint = ComplaintAction(driver)
    complaint.submit_complaint()


def test_submit_without_filling_form(setup):
    driver = setup
    complaint = ComplaintAction(driver)
    complaint.submit_without_filling_form()


def test_submit_without_name(setup):
    driver = setup
    complaint = ComplaintAction(driver)
    complaint.submit_without_name(
        "tamil@gmail.com",
        "9876543210",
        "Missing Name Test"
    )


def test_submit_without_email(setup):
    driver = setup
    complaint = ComplaintAction(driver)
    complaint.submit_without_email(
        "Tamilarasu",
        "9876543210",
        "Missing Email Test"
    )


def test_submit_without_contact(setup):
    driver = setup
    complaint = ComplaintAction(driver)
    complaint.submit_without_contact(
        "Tamilarasu",
        "tamil@gmail.com",
        "Missing Contact Test"
    )


def test_submit_without_description(setup):
    driver = setup
    complaint = ComplaintAction(driver)
    complaint.submit_without_description(
        "Tamilarasu",
        "tamil@gmail.com",
        "9876543210"
    )