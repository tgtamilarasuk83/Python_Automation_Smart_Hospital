import pytest
import os
from selenium import webdriver
from utilities.config_reader import get_value

# ---------------------------
# Paths
# ---------------------------
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")
SCREENSHOT_FOLDER = os.path.join(os.getcwd(), "Screenshots")


# ---------------------------
# WebDriver Setup Fixture
# ---------------------------
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


# ---------------------------
# Screenshot on Failure Hook
# ---------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup", None)

        if driver:
            os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

            screenshot_name = f"{item.name}.png"
            screenshot_path = os.path.join(SCREENSHOT_FOLDER, screenshot_name)

            driver.save_screenshot(screenshot_path)

            # Attach screenshot to HTML report (if pytest-html installed)
            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html and hasattr(report, "extra"):
                report.extra.append(
                    pytest_html.extras.image(screenshot_path)
                )