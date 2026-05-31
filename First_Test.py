# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
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
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
	# //XCUIElementTypeImage[@name="Menu Icons"]
	driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="Menu Icons"]').click()

	# Confirm that there's a Login link
	element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="LogOut-menu-item"]')
	assert element is not None, "LogOut menu item was not found"

	# Click on Webview menu item
	driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Webview"]').click()

	# Confirm Enter an https URL item label is found
	element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Enter an https URL"]')
	assert element is not None, "Enter an https URL item was not found"

	# Click on the Back button
	element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="BackButton Icons"]').click()

	# Confirm that My DemoApp logo is found
	element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="AppTitle Icons"]')
	assert element is not None, "My DemoApp logo was not found"
	
finally:
	driver.quit()