from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DrawingPage(BasePage):

    DRAWING_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Drawing"]'
    )

    def header_visible(self):
        print("Will check if Drawing header is visible")
        return self.is_visible(self.DRAWING_HEADER)


