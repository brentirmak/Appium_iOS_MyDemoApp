from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):

    MENU_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="Menu Icons"]'
    )

    APP_LOGO = (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="AppTitle Icons"]'
    )

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def logo_visible(self):
        return self.is_visible(self.APP_LOGO)