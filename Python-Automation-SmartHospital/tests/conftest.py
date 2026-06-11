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
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(get_value("config.ini", "info", "url"))

    yield driver

    driver.quit()