from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class MenuPage(BasePage):

    LOGOUT_MENU = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="LogOut-menu-item"]'
    )

    WEBVIEW_MENU = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Webview"]'
    )

    LOGIN_MENU_ITEM = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="LogOut-menu-item"]'
    )

    def logout_visible(self):
        return self.is_visible(self.LOGOUT_MENU)

    def open_webview(self):
        self.click(self.WEBVIEW_MENU)

    def click_login(self):
        self.click(self.LOGIN_MENU_ITEM)