from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CartPage(BasePage):

    MYCART_PAGE_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="My Cart"]'
    )

    REMOVE_ITEM_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Remove Item"]'
    )

    NO_ITEMS_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="No Items"]'
    )

    GO_SHOPPING_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Go Shopping"]'
    )

    def header_visible(self):
        return self.is_visible(self.MYCART_PAGE_HEADER)
    
    def no_items_in_cart_visible(self):
        return self.is_visible(self.NO_ITEMS_HEADER)
    
    def click_remove_item_button(self):
        print("Will click on Remove Item button")
        self.click(self.REMOVE_ITEM_BUTTON)
        print("Clicked on Remove Item button")

    def click_go_shopping_button(self):
        print("Will click on Go Shopping button")
        self.click(self.GO_SHOPPING_BUTTON)
        print("Clicked on Go Shopping button")

    # //XCUIElementTypeCell/XCUIElementTypeStaticText[@name="2"]

    