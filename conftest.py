
import pytest
import os
import subprocess

from dotenv import load_dotenv
from pathlib import Path

from appium import webdriver
from appium.options.common.base import AppiumOptions

from utils.db import MySQLLogger
from utils.screenshot_manager import capture_screenshot
try:
    from utils.resend_email import send_failure_email
except ImportError as exc:
    send_failure_email = None
    print(f"[Alert] Resend email disabled: {exc}")


# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

# Existing local MySQL configuration
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

# Resend configuration:
# Jenkins supplies RESEND_ENV_FILE through Secret File binding.
# Local execution uses resend.env.

resend_env_path = os.getenv("RESEND_ENV_FILE")

if resend_env_path:
    load_dotenv(dotenv_path=resend_env_path, override=False)
else:
    load_dotenv(
        dotenv_path=PROJECT_ROOT / "resend.env",
        override=False
    )


MYSQL_HOST = os.getenv("MYSQL_URL")
MYSQL_USER = os.getenv("MYSQL_USERNAME")
MYSQL_PASS = os.getenv("MYSQL_PASSWORD")


APPIUM_SERVER_URL = "http://127.0.0.1:4723"


# ---------------------------------------------------------
# APPIUM CAPABILITIES
# ---------------------------------------------------------

CAPABILITIES = {
    "platformName": "ios",
    "appium:automationName": "xcuitest",
    "appium:autoDismissAlerts": True,
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
# RUN TYPE
# ---------------------------------------------------------

def get_run_type():

    jenkins_env_vars = [
        "JENKINS_URL",
        "BUILD_NUMBER",
        "JENKINS_HOME"
    ]

    if any(var in os.environ for var in jenkins_env_vars):
        return "Jenkins"

    return "Local"


# ---------------------------------------------------------
# APPIUM DRIVER FIXTURE
# ---------------------------------------------------------

###@pytest.fixture(scope="class") Removed as part of refactoring efforts
@pytest.fixture(scope="session") 
def driver():

    options = AppiumOptions()
    options.load_capabilities(CAPABILITIES)

    _driver = webdriver.Remote(
        APPIUM_SERVER_URL,
        options=options
    )

    yield _driver

    _driver.quit()


# ---------------------------------------------------------
# MYSQL LOGGER FIXTURE
# ---------------------------------------------------------

@pytest.fixture(scope="session")
def db_logger():

    logger = MySQLLogger(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        database="appium"
    )

    logger.connect()

    yield logger

    logger.close()


# ---------------------------------------------------------
# FIRST FAILURE ALERT
# ---------------------------------------------------------

def trigger_first_failure_alert(item, report):

    # Session-level flag.
    # Resets automatically for every new pytest execution.

    if getattr(item.config, "_first_failure_alert_sent", False):
        print("[Alert] First failure alert already attempted.")
        return

    # Set flag BEFORE attempting screenshot or email.
    # This prevents duplicate alerts even if either operation fails.

    item.config._first_failure_alert_sent = True

    print("")
    print("==========================================")
    print("FIRST TEST FAILURE DETECTED")
    print("==========================================")

    test_name = item.name
    test_script = Path(str(item.path)).name

    error_message = getattr(
        report,
        "longreprtext",
        "Unknown test failure"
    )

    # Retrieve the existing Appium driver.
    driver_instance = item.funcargs.get("driver")

    # Capture screenshot.
    screenshot_path = capture_screenshot(
        driver=driver_instance,
        test_name=test_name,
        output_dir=PROJECT_ROOT / "screenshots"
    )
    if send_failure_email is None:
        return
    # Send one Resend email.
    try:

        send_failure_email(
            test_name=test_name,
            test_script=test_script,
            error_message=error_message,
            screenshot_path=screenshot_path
        )

        print("[Alert] First failure email sent.")

    except Exception as exc:

        # Email failures must never interrupt pytest execution.

        print("[Alert] Unable to send Resend notification.")
        print(f"[Alert] Reason: {exc}")


# ---------------------------------------------------------
# PYTEST REPORTING HOOK
# ---------------------------------------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    run_type = get_run_type()

    # -----------------------------------------------------
    # FIRST FAILURE SCREENSHOT + EMAIL
    # -----------------------------------------------------

    if report.failed and report.when in ("setup", "call"):

        trigger_first_failure_alert(item, report)

    # -----------------------------------------------------
    # EXISTING MYSQL TEST RESULT LOGGING
    # -----------------------------------------------------

    if report.when == "call":

        duration = report.duration

        if report.passed:

            status = "PASS"
            error_message = None

        elif report.failed:

            status = "FAIL"
            error_message = (
                str(call.excinfo.value)
                if call.excinfo
                else "Unknown Error"
            )

        else:

            status = "SKIPPED"
            error_message = None

        logger = item.funcargs.get("db_logger", None)

        if logger:

            logger.log_result(
                test_name=item.name,
                test_script=Path(str(item.path)).name,
                status=status,
                duration=duration,
                error_message=error_message,
                run_type=run_type
            )


# ---------------------------------------------------------
# REGISTER MYSQL FIXTURE
# ---------------------------------------------------------

def pytest_configure(config):

    config.addinivalue_line(
        "usefixtures",
        "db_logger"
    )


# ---------------------------------------------------------
# MYSQL LOGGER FIXTURE
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# OPEN IOS SIMULATOR GUI
# ---------------------------------------------------------

@pytest.fixture(scope="session", autouse=True)
def open_simulator_gui():

    subprocess.run(
        ["open", "-a", "Simulator"],
        check=False
    )

    yield
