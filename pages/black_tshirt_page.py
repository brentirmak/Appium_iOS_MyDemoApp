from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class BlackTShirtPage(BasePage):

    BLACK_TSHIRT_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Sauce Labs Bolt T-Shirt - Black"]'
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

    PRODUCT_DESCRIPTION = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextView[@value="Get your testing superhero on with the Sauce Labs '
        'bolt T-Shirt. From American Apparel, 100% ringspun combed cotton gray red bolt."]'
    )

    def header_visible(self):
        print("Will confirm that the Black TShirt page header is visible")
        return self.is_visible(self.BLACK_TSHIRT_HEADER)
    
    def cart_with_one_item_visible(self):
        print("Will confirm that the cart with one item is visible")
        return self.is_visible(self.CART_WITH_ONE_ITEM)

    def click_add_to_cart_button(self):
        print("Will click on the Add To Cart button")
        self.click(self.ADD_TO_CART_BUTTON)
        print("Clicked on the Add To Cart button")

    def click_back_to_products_icon(self):
        print("Will click on the products back icon")
        self.click(self.PRODUCTS_LINK)
        print("Clicked on the products back icon")

    def scroll_to_bottom_of_page(self):
        print("Will scroll to the bottom of the page")
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        print("Scrolled to the bottom of the page")

    def product_description_visible(self):
        print("Will confirm that the product description is visible")
        return self.is_visible(self.PRODUCT_DESCRIPTION)