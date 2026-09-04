from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder



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

    PRODUCTS_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="title"]'
    )

    PRODUCT_SORT_ICON = (AppiumBy.IOS_PREDICATE,'**/XCUIElementTypeStaticText[`name == "Button"`]')

    ASCENDING_BY_PRICE_OPTION = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="Price - Ascending"]')

    BLACK_TSHIRT_IMAGE = (AppiumBy.IOS_PREDICATE, 'name == "Product Name" AND label == "Sauce Labs Bolt T-Shirt - Black"')
    

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

    def products_header_visible(self):
        print("Will check if the Products header is visible")
        return self.is_visible(self.PRODUCTS_HEADER)

    def click_product_sort_icon(self, x, y):
        print("Will click on the Product sort icon using x,y coordinates")
        #self.click(self.PRODUCT_SORT_ICON)
        self.driver.execute_script("mobile: tap", {
            "x": x,
            "y": y
            })

        print("Clicked on the Product sort icon using x,y coordinates")

    def click_ascending_by_price_option(self):
        print("Will click on the ascending by price option")
        self.click(self.ASCENDING_BY_PRICE_OPTION)
        print("Clicked on the Ascending by Price option")

    def sauce_labs_bolt_tshirt_visible(self):
        print("Will check if the Sauce Labs Bolt Tshirt is visible")
        return self.is_visible(self.BLACK_TSHIRT_IMAGE)

    def click_black_tshirt_image(self):
        print("Will click on the Black TShirt image")
        self.click(self.BLACK_TSHIRT_IMAGE)
        print("Clicked on the Black TShirt image")
