import pytest
import os
import base64
from selenium import webdriver
from utilities.config_reader import get_value

DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")
SCREENSHOT_FOLDER = "Screenshots"

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

    # IMPORTANT FIX FOR JENKINS
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(get_value("config.ini", "info", "url"))

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:

            os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

            screenshot_file = os.path.join(
                SCREENSHOT_FOLDER,
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_file)

            print(f"\nScreenshot Saved : {screenshot_file}")

            pytest_html = item.config.pluginmanager.getplugin("html")

            with open(screenshot_file, "rb") as image_file:
                encoded_image = base64.b64encode(
                    image_file.read()
                ).decode()

            extras.append(
                pytest_html.extras.image(encoded_image)
            )

    report.extras = extras