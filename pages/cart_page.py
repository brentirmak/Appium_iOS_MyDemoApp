from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CartPage(BasePage):

    MYCART_PAGE_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="My Cart"]')
    REMOVE_ITEM_BUTTON = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Remove Item"]')
    NO_ITEMS_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="No Items"]')
    GO_SHOPPING_BUTTON = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Go Shopping"]')
    PROCEED_TO_CHECKOUT_BUTTON = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="ProceedToCheckout"]')
    PRETAX_CART_AMOUNT_FOR_FIVE_BIKELIGHTS = (AppiumBy.ACCESSIBILITY_ID,'$49.95')
    PRETAX_CART_AMOUNT_FOR_TWO_TSHIRTS = (AppiumBy.ACCESSIBILITY_ID,'$31.98')
    PRETAX_CART_AMOUNT_FOR_TEN_ONESIES = (AppiumBy.ACCESSIBILITY_ID,'$79.90')

    def header_visible(self, timeout=30):
        print("Will confirm that the MyCart page header is visible")
        return self.is_visible(self.MYCART_PAGE_HEADER)
    
    def no_items_in_cart_visible(self, timeout=30):
        print("Will confirm that the No Items header is visible")
        return self.is_visible(self.NO_ITEMS_HEADER)
    
    def click_remove_item_button(self, timeout=30):
        print("Will click on Remove Item button")
        self.click(self.REMOVE_ITEM_BUTTON)
        print("Clicked on Remove Item button")

    def click_go_shopping_button(self, timeout=30):
        print("Will click on Go Shopping button")
        self.click(self.GO_SHOPPING_BUTTON)
        print("Clicked on Go Shopping button")

    def click_proceed_to_checkout_button(self, timeout=30):
        print("Will click on the Proceed to Checkout button")
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)
        print("Clicked on Proceed to Checkout button")

    def five_bikelights_pretax_amount_visible(self, timeout=30):
        print("Will confirm that $49.95 is visible")
        visible = self.is_visible(self.PRETAX_CART_AMOUNT_FOR_FIVE_BIKELIGHTS)
        assert visible, f"Expected pretax amount not visible using locator: {self.PRETAX_CART_AMOUNT_FOR_FIVE_BIKELIGHTS}"
        return visible

    def two_tshirts_pretax_amount_visible(self, timeout=30):
        print("Will confirm that $31.98 is visible")
        visible = self.is_visible(self.PRETAX_CART_AMOUNT_FOR_TWO_TSHIRTS)
        assert visible, f"Expected pretax amount not visible using locator: {self.PRETAX_CART_AMOUNT_FOR_TWO_TSHIRTS}"
        return visible

    def ten_onesies_pretax_amount_visible(self, timeout=30):
        print("Will confirm that $79.90 is visible")
        visible = self.is_visible(self.PRETAX_CART_AMOUNT_FOR_TEN_ONESIES)
        assert visible, f"Expected pretax amount not visible using locator: {self.PRETAX_CART_AMOUNT_FOR_TEN_ONESIES}"
        return visible