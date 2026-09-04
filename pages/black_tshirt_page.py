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

    CART_WITH_TWO_ITEMS = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="2"]'
    )

    ADD_TO_CART_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Add To Cart"]'
    )

    PRODUCT_CART_PLUS_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="AddPlus Icons"]'
    )

    PRODUCT_DESCRIPTION = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextView[@value="Get your testing superhero on with the Sauce Labs '
        'bolt T-Shirt. From American Apparel, 100% ringspun combed cotton gray red bolt."]'
    )

    PRODUCT_QUANTITY_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Amount"]'
    )

    def header_visible(self):
        print("Will confirm that the Black TShirt page header is visible")
        return self.is_visible(self.BLACK_TSHIRT_HEADER)
    
    def cart_with_one_item_visible(self):
        print("Will confirm that the cart with one item is visible")
        return self.is_visible(self.CART_WITH_ONE_ITEM)

    def cart_with_two_items_visible(self):
        print("Will confirm that the cart with two items is visible")
        return self.is_visible(self.CART_WITH_TWO_ITEMS)

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

    def click_product_plus_button(self):
        print("Will click on the '+' associated with the product quantity")
        self.click(self.PRODUCT_CART_PLUS_BUTTON)
        print("Added the quantity by 1")                       

    def capture_product_quantity(self):
        print("Will capture the product quantity that's been added")
        item_quantity = self.driver.find_element(*self.PRODUCT_QUANTITY_FIELD).get_attribute("value")
        print("Captured the product quantity that's been added")
        if item_quantity == "2":
            print("The expected number of tshirts have been added")
        else:        
            raise AssertionError(
                f"Expected quantity to be 2 but got {item_quantity}"
            )


