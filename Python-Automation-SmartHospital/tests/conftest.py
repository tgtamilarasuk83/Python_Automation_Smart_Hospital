import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config_reader import get_value

@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(get_value("config.ini","info","url"))

    yield driver

    driver.quit()