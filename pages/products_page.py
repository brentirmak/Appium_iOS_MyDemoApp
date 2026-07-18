from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductsPage(BasePage):

    GREEN_BACKPACK_IMAGE = (
        AppiumBy.XPATH,
        '(//XCUIElementTypeImage[@name="Product Image"])[2]'
    )

    SHOPPING_CART_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Cart-tab-item"]'
    )

    MORE_ICON = (
        AppiumBy.ACCESSIBILITY_ID,
        "More-tab-item"
    )

    def click_green_backpack_product(self):
        print("Clicking on green backpack product")
        self.click(self.GREEN_BACKPACK_IMAGE)
        print("Clicked green backpack product")

    def click_shopping_cart_icon(self):
        print("Clicking on shopping cart icon")
        self.click(self.SHOPPING_CART_ICON)
        print("Clicked on shopping cart icon")

    def click_more_icon(self):
        print("Will click on More icon")
        self.click(self.MORE_ICON)
        print("Clicked on More icon")
