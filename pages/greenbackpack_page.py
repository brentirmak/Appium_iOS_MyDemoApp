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

    CART_WITH_ONE_ITEM = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="1"]'
    )

    ADD_TO_CART_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Add To Cart"]'
    )

    def header_visible(self):
        return self.is_visible(self.GREEN_BACKBACK_HEADER)
    
    def cart_with_one_item_visible(self):
        return self.is_visible(self.CART_WITH_ONE_ITEM)
    
    def click_green_backpack_product(self):
        print("Will click on the green backpack image")
        self.click(self.GREEN_BACKPACK_IMAGE)
        print("Clicked on the green backpack image")

    def click_add_to_cart_button(self):
        print("Will click on the Add To Cart button")
        self.click(self.ADD_TO_CART_BUTTON)
        print("Clicked on the Add To Cart button")

    def click_back_to_products_icon(self):
        print("Will click on the products back icon")
        self.click(self.PRODUCTS_LINK)
        print("Clicked on the products back icon")