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
    

    def scroll_down_to_element(self, locator, max_swipes=25):
        """Scrolls down on iOS, using smaller drags near the bottom to catch edge items."""
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]

        for attempt in range(max_swipes):
            for el in self.driver.find_elements(*locator):
                if el.is_displayed():
                    return el

            before_source = self.driver.page_source

            # Drag finger upward (from 75% down to 30% down) to move content up
            self.driver.execute_script(
                "mobile: dragFromToForDuration",
                {
                    "fromX": width * 0.5,
                    "fromY": height * 0.75,
                    "toX": width * 0.5,
                    "toY": height * 0.30,
                    "duration": 0.4,
                },
            )

            # If we stopped moving, try one gentle nudge from 60% to 35%
            after_source = self.driver.page_source
            if after_source == before_source:
                self.driver.execute_script(
                    "mobile: dragFromToForDuration",
                    {
                        "fromX": width * 0.5,
                        "fromY": height * 0.60,
                        "toX": width * 0.5,
                        "toY": height * 0.35,
                        "duration": 0.3,
                    },
                )
                for el in self.driver.find_elements(*locator):
                    if el.is_displayed():
                        return el
                if self.driver.page_source == after_source:
                    break

        raise TimeoutException(
            f"Could not find visible element at bottom for {locator} after {max_swipes} attempts."
        )

    def select_bike_light(self, max_swipes=30):
        print("Scrolling down to find 'Sauce Labs Bike Light'")
        self.scroll_down_to_element(self.BIKE_LIGHT_ITEM, max_swipes=max_swipes)
        print("Clicking 'Sauce Labs Bike Light'")
        self.click(self.BIKE_LIGHT_ITEM)

    def select_onesie(self, max_swipes=30):
        print("Scrolling down to find 'Sauce Labs Onesie'")
        self.scroll_down_to_element(self.ONESIE_ITEM, max_swipes=max_swipes)
        print("Clicking 'Sauce Labs Onesie'")
        self.click(self.ONESIE_ITEM)

    def select_pink_fleece(self, max_swipes=30):
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
