import pytest
import time
from db import MySQLLogger
from dotenv import load_dotenv
import os

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Retrieve the secrets using os.getenv()
webdriver_remote_url = os.getenv("MYSQL_URL")
webdriver_username = os.getenv("MYSQL_USERNAME")
webdriver_password = os.getenv("MYSQL_PASSWORD")

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

CAPABILITIES = {
    "platformName": "ios",
    "appium:automationName": "xcuitest",
    "appium:deviceName": "iPhone 17 Pro",
    "appium:platformVersion": "26.5",
    "appium:udid": "89681D14-673F-445A-80AA-351832829080",
    "appium:noReset": True,
    "appium:fullReset": False,
    "appium:printPageSourceOnFindFailure": False,
    "appium:app": "/Users/seiwa/Desktop/my-demo-app-ios-main/build/Build/Products/Debug-iphonesimulator/My Demo App.app",
    "appium:waitForQuiescence": False,
    "appium:includeSafariInWebviews": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
}

@pytest.fixture(scope="class")
def driver():
    """Set up and tear down the Appium driver for the test session."""
    options = AppiumOptions()
    options.load_capabilities(CAPABILITIES)
    _driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield _driver
    _driver.quit()

#@pytest.fixture(scope="session")
#def db_logger():
#    logger = MySQLLogger(
#        host=webdriver_remote_url,
#        user=webdriver_username,
#        password=webdriver_password,
#        database="appium"
#    )
#    yield logger
#    logger.close()

logger = MySQLLogger(
    host=webdriver_remote_url,
    user=webdriver_username,
    password=webdriver_password,
    database="appium"
)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):



    outcome = yield
    report = outcome.get_result()

    # Only log actual test execution phase
    if report.when == "call":

        duration = report.duration

        if report.passed:
            status = "PASS"
            error_message = None

        elif report.failed:
            status = "FAIL"

            if call.excinfo:
                error_message = str(call.excinfo.value)
            else:
                error_message = "Unknown Error"

        else:
            status = "SKIPPED"
            error_message = None

        logger.log_result(
            test_name=item.name,
            status=status,
            duration=duration,
            error_message=error_message
        )


def pytest_sessionfinish(session, exitstatus):
    logger.close()