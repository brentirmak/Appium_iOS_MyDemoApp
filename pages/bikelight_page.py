from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BikeLightPage(BasePage):

    BIKE_LIGHT_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Sauce Labs Bike Light"]')
    PRODUCTS_LINK = (AppiumBy.XPATH,'//XCUIElementTypeImage[@name="BackButton Icons"]')
    CART_WITH_FIVE_ITEMS = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="5"]')
    ADD_TO_CART_BUTTON = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Add To Cart"]')
    PLUS_ICON = (AppiumBy.ACCESSIBILITY_ID,'AddPlus Icons')
    QUANTITY = (AppiumBy.ACCESSIBILITY_ID,'Amount')

    def header_visible(self, timeout=30):
        print("Will confirm that the Bike Light page header is visible")
        return self.is_visible(self.BIKE_LIGHT_HEADER)

    def click_plus_icon(self, timeout=30):
        print("Will click on the plus icon")
        self.click(self.PLUS_ICON)
        print("Clicked on the plus icon")
    
    def cart_with_five_items_visible(self, timeout=30):
        print("Will confirm that the cart with five items is visible")
        return self.is_visible(self.CART_WITH_FIVE_ITEMS)
    
    def click_add_to_cart_button(self, timeout=30):
        print("Will click on the Add To Cart button")
        self.click(self.ADD_TO_CART_BUTTON)
        print("Clicked on the Add To Cart button")

    def click_back_to_products_icon(self, timeout=30):
        print("Will click on the products back icon")
        self.click(self.PRODUCTS_LINK)
        print("Clicked on the products back icon")

    def quantity_value(self, timeout=30):
        print("Will return the quantity of the bike lights")
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.QUANTITY))
        # On iOS/Appium, quantity text often lives in `text`, `value`, or `label`
        value = (element.text or element.get_attribute("value") or element.get_attribute("label")or "").strip()
        print(f"Quantity value: {value}")
        assert value == "5", f"Expected quantity to be 5, but got '{value}'"
        return value
    