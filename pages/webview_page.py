from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class WebViewPage(BasePage):

    URL_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Enter an https URL"]'
    )

    BACK_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="BackButton Icons"]'
    )

    def url_field_visible(self):
        return self.is_visible(self.URL_FIELD)

    def navigate_back(self):
        self.click(self.BACK_BUTTON)