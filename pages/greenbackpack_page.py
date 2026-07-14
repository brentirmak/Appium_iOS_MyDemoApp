from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class GreenBackpackPage(BasePage):

    GREEN_BACKBACK_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Sauce Labs Backpack - Green"]'
    )

    PRODUCTS_LINK = (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="BackButton Icons"]'
    )

    def header_visible(self):
        return self.is_visible(self.GREEN_BACKBACK_HEADER)
    
    def click_green_backpack_product(self):
        print("Will click on the green backpack image")
        self.click(self.GREEN_BACKPACK_IMAGE)
        print("Clicked on the green backpack image")

    def click_back_to_products_icon(self):
        print("Will click on the products back icon")
        self.click(self.PRODUCTS_LINK)
        print("Clicked on the products back icon")
