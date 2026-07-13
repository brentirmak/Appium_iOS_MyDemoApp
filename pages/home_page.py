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
    
    CATALOG_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Catalog"]'
    )


    def open_menu(self):
        print("Will click on Menu button")
        self.click(self.MENU_BUTTON)
        print("Clicked on Menu button")

    def logo_visible(self):
        print("Will verify app logo")
        return self.is_visible(self.APP_LOGO)

    
    def click_catalog_icon(self):
        print("Will click on catalog icon")
        self.click(self.CATALOG_ICON)
        print("Clicked catalog icon")