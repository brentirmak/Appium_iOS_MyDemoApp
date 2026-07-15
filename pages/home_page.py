from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):

    MENU_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "More-tab-item"
    )

    APP_LOGO = (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="AppTitle Icons"]'
    )
    
    #CATALOG_ICON = (
    #    AppiumBy.XPATH,
    #    '//XCUIElementTypeStaticText[@name="Catalog"]'
    #)

    CATALOG_ICON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Catalog-tab-item"
    )

    PRODUCT_SORT_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Button"]'
    )

    PRODUCT_SORT_BY_ASCENDING_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Name - Ascending"]'
    )

    def open_menu(self):
        print("Will click on Menu button")
        #print("CURRENT CONTEXT:", self.driver.current_context)
        #print(self.driver.page_source)
        self.click(self.MENU_BUTTON)
        print("Clicked on Menu button")

          # >>> ADD THIS DIAGNOSTIC HERE <<<
        print("CURRENT CONTEXT:", self.driver.current_context)
        print(self.driver.page_source)

    def logo_visible(self):
        print("Will verify app logo")
        return self.is_visible(self.APP_LOGO)

    def click_catalog_icon(self):
        print("Will click on catalog icon")
        self.click(self.CATALOG_ICON)
        print("Clicked catalog icon")

    def click_sort_icon(self):
        print("Will click on sort icon")
        self.click(self.PRODUCT_SORT_ICON)
        print("Clicked on sort icon")

    def click_sort_by_ascending_option(self):
        print("Will click on sort by ascending option icon")
        self.click(self.PRODUCT_SORT_BY_ASCENDING_ICON)
        print("Clicked on sort by ascending option icon")
    
    def sort_by_ascending_icon_visible(self):
        print("Confirming that sort by ascending is visible")
        return self.is_visible(self.PRODUCT_SORT_BY_ASCENDING_ICON)