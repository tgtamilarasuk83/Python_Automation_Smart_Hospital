import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config_reader import get_value

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": DOWNLOADS_FOLDER,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(get_value("config.ini", "info", "url"))

    yield driver

    driver.quit()