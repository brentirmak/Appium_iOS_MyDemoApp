import pytest
import time
import os
import subprocess
from dotenv import load_dotenv
from pathlib import Path

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from utils.db import MySQLLogger

# ---------------------------------------------------------
# Load environment variables (.env locally, Jenkins env in CI)
# ---------------------------------------------------------
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

MYSQL_HOST = os.getenv("MYSQL_URL")
MYSQL_USER = os.getenv("MYSQL_USERNAME")
MYSQL_PASS = os.getenv("MYSQL_PASSWORD")


print("AFTER LOAD:")
print("MYSQL_HOST =", os.getenv("MYSQL_URL"))
print("MYSQL_USER =", os.getenv("MYSQL_USERNAME"))
print("MYSQL_PASS =", os.getenv("MYSQL_PASSWORD"))

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

CAPABILITIES = {
    "platformName": "ios",
    "appium:automationName": "xcuitest",
    "appium:deviceName": "iPhone 17 Pro",
    "appium:platformVersion": "26.5",
    "appium:udid": "89681D14-673F-445A-80AA-351832829080",
    "appium:autoAcceptAlerts": True,
    "appium:noReset": False,
    "appium:fullReset": False,
    "appium:printPageSourceOnFindFailure": False,
    "appium:app": "/Users/seiwa/Desktop/my-demo-app-ios-main/build/Build/Products/Debug-iphonesimulator/My Demo App.app",
    "appium:waitForQuiescence": False,
    "appium:includeSafariInWebviews": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
}

# ---------------------------------------------------------
# Appium driver fixture
# ---------------------------------------------------------
@pytest.fixture(scope="class")
def driver():
    options = AppiumOptions()
    options.load_capabilities(CAPABILITIES)
    _driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield _driver
    _driver.quit()

# ---------------------------------------------------------
# MySQL logger fixture (LAZY CONNECTION)
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def db_logger():
    logger = MySQLLogger(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        database="appium"
    )
    logger.connect()  # <-- connection happens here, NOT at import time
    yield logger
    logger.close()

# ---------------------------------------------------------
# Pytest hook: log results AFTER each test call
# ---------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        duration = report.duration

        if report.passed:
            status = "PASS"
            error_message = None
        elif report.failed:
            status = "FAIL"
            error_message = str(call.excinfo.value) if call.excinfo else "Unknown Error"
        else:
            status = "SKIPPED"
            error_message = None

        # SAFE retrieval of logger fixture
        logger = item.funcargs.get("db_logger", None)

        if logger:
            logger.log_result(
                test_name=item.name,
                status=status,
                duration=duration,
                error_message=error_message
            )
            
def pytest_configure(config):
    config.addinivalue_line("usefixtures", "db_logger")


@pytest.fixture
def mysql_logger():
    
    logger = MySQLLogger(
        host=os.getenv("MYSQL_URL"),
        user=os.getenv("MYSQL_USERNAME"),
        password=os.getenv("MYSQL_PASSWORD"),
        database="appium"
    )

    yield logger

    logger.close()

@pytest.fixture(scope="session", autouse=True)
def open_simulator_gui():
    subprocess.run(["open", "-a", "Simulator"])
    yield
