# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client pytest
# Run with: pytest test_demo_app.py -v

import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


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


class TestDemoApp:

    def test_open_menu(self, driver):
        """Tap the menu icon to open the side/hamburger menu."""
        driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Menu Icons"]').click()

    def test_logout_menu_item_visible(self, driver):
        """Confirm the LogOut menu item is visible after opening the menu."""
        element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="LogOut-menu-item"]')
        assert element is not None, "LogOut menu item was not found"

    def test_navigate_to_webview(self, driver):
        """Tap the Webview menu item to navigate to the Webview screen."""
        driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Webview"]').click()

    def test_webview_url_input_visible(self, driver):
        """Confirm the URL input label is present on the Webview screen."""
        element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Enter an https URL"]')
        assert element is not None, "Enter an https URL item was not found"

    def test_navigate_back(self, driver):
        """Tap the Back button to return to the home screen."""
        driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="BackButton Icons"]').click()

    def test_home_logo_visible(self, driver):
        """Confirm the My DemoApp logo is visible on the home screen."""
        element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="AppTitle Icons"]')
        assert element is not None, "My DemoApp logo was not found"