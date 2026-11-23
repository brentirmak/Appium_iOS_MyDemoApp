from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):

    GREEN_BACKPACK_IMAGE = (AppiumBy.XPATH,'(//XCUIElementTypeImage[@name="Product Image"])[2]')
    
    BIKE_LIGHT_ITEM = (AppiumBy.XPATH,'//*[contains(@name, "Bike Light") or contains(@label, "Bike Light")]',)
    ONESIE_ITEM = (AppiumBy.XPATH,'//*[contains(@name, "Onesie") or contains(@label, "Onesie")]',)
    PINK_FLEECE_ITEM = (AppiumBy.XPATH,'//*[contains(@name, "Fleece Jacket - Pink") or contains(@label, "Fleece Jacket - Pink")]',)


    SCROLL_CONTAINER = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeScrollView[1]")

    SHOPPING_CART_ICON = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="Cart-tab-item"]')
    MORE_ICON = (AppiumBy.ACCESSIBILITY_ID,"More-tab-item")
    PRODUCTS_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="title"]')
    PRODUCT_SORT_ICON = (AppiumBy.IOS_PREDICATE,'**/XCUIElementTypeStaticText[`name == "Button"`]')
    ASCENDING_BY_PRICE_OPTION = (AppiumBy.XPATH,'//XCUIElementTypeButton[@name="Price - Ascending"]')
    BLACK_TSHIRT_IMAGE = (AppiumBy.IOS_PREDICATE, 'name == "Product Name" AND label == "Sauce Labs Bolt T-Shirt - Black"')
    

    def scroll_down_to_element(self, locator, max_swipes=6, timeout_per_check=1.5):
        """Scrolls down on iOS until `locator` is present/visible or `max_swipes` is reached."""
        for _ in range(max_swipes):
            try:
                element = WebDriverWait(self.driver, timeout_per_check).until(
                    EC.presence_of_element_located(locator)
                )
                # Scroll to center if needed so it isn't clipped by bars
                self.driver.execute_script("mobile: scroll", {"elementId": element.id, "toVisible": True})
                return element
            except TimeoutException:
                try:
                    scroll_view = self.driver.find_element(*self.SCROLL_CONTAINER)
                    self.driver.execute_script(
                        "mobile: scroll",
                        {"elementId": scroll_view.id, "direction": "down"},
                    )
                except Exception:
                    # Fallback if there is no explicit XCUIElementTypeScrollView wrapper
                    self.driver.execute_script("mobile: scroll", {"direction": "down"})

        raise TimeoutException(f"Could not find element {locator} after {max_swipes} scroll attempts.")

    def select_bike_light(self, max_swipes=6):
        print("Scrolling down to find 'Sauce Labs Bike Light'")
        self.scroll_down_to_element(self.BIKE_LIGHT_ITEM, max_swipes=max_swipes)
        print("Clicking 'Sauce Labs Bike Light'")
        self.click(self.BIKE_LIGHT_ITEM)

    def select_onesie(self, max_swipes=6):
        print("Scrolling down to find 'Sauce Labs Onesie'")
        self.scroll_down_to_element(self.ONESIE_ITEM, max_swipes=max_swipes)
        print("Clicking 'Sauce Labs Onesie'")
        self.click(self.ONESIE_ITEM)

    def select_pink_fleece(self, max_swipes=10):
        print("Scrolling down to find 'Sauce Labs Fleece Jacket - Pink'")
        self.scroll_down_to_element(self.PINK_FLEECE_ITEM, max_swipes=max_swipes)
        print("Clicking 'Sauce Labs Fleece Jacket - Pink")
        self.click(self.PINK_FLEECE_ITEM)

    def click_green_backpack_product(self, timeout=30):
        print("Clicking on green backpack product")
        self.click(self.GREEN_BACKPACK_IMAGE)
        print("Clicked green backpack product")

    def click_shopping_cart_icon(self, timeout=30):
        print("Clicking on shopping cart icon")
        self.click(self.SHOPPING_CART_ICON)
        print("Clicked on shopping cart icon")

    def click_more_icon(self, timeout=30):
        print("Will click on More icon")
        self.click(self.MORE_ICON)
        print("Clicked on More icon")

    def products_header_visible(self, timeout=30):
        print("Will check if the Products header is visible")
        return self.is_visible(self.PRODUCTS_HEADER)

    def click_product_sort_icon(self, x, y, timeout=30):
        print("Will click on the Product sort icon using x,y coordinates")
        self.driver.execute_script("mobile: tap", {"x": x,"y": y})
        print("Clicked on the Product sort icon using x,y coordinates")

    def click_ascending_by_price_option(self, timeout=30):
        print("Will click on the ascending by price option")
        self.click(self.ASCENDING_BY_PRICE_OPTION)
        print("Clicked on the Ascending by Price option")

    def sauce_labs_bolt_tshirt_visible(self, timeout=30):
        print("Will check if the Sauce Labs Bolt Tshirt is visible")
        return self.is_visible(self.BLACK_TSHIRT_IMAGE)

    def click_black_tshirt_image(self, timeout=30):
        print("Will click on the Black TShirt image")
        self.click(self.BLACK_TSHIRT_IMAGE)
        print("Clicked on the Black TShirt image")
