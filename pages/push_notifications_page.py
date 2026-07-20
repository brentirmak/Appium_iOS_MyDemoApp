from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class PushNotificationsPage(BasePage):

    PUSH_NOTIFICATIONS_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Push Notifications"]'
    )

    BACK_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeApplication[@name="My Demo App"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
    )

    def header_visible(self):
        print("Will confirm that the Push Notifications header is visible")
        return self.is_visible(self.PUSH_NOTIFICATIONS_HEADER)
    
    def click_back_icon(self):
        print("Clicking on back icon")
        self.click(self.BACK_ICON)
        print("Clicked on back icon")
    