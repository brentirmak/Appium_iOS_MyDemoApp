from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ReportBugDebugPage(BasePage):

    DEBUG_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Debug"]'
    )

    DEBUG_BACK_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeApplication[@name="My Demo App"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
    )

    def header_visible(self):
        print("Will confirm that the header is visible")
        return self.is_visible(self.DEBUG_HEADER)
    
    def click_debug_back_icon(self):
        print("Clicking on debug back icon..")
        self.click(self.DEBUG_BACK_ICON)
        print("Clicked on debug back icon")
    