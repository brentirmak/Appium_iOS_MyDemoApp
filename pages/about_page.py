from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class AboutPage(BasePage):

    ABOUT_PAGE_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="About "]'
    )

    def header_visible(self):
        print("Will confirm that the About page header is visible")
        return self.is_visible(self.ABOUT_PAGE_HEADER)