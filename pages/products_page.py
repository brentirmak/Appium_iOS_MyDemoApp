from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductsPage(BasePage):

    GREEN_BACKPACK_IMAGE = (
        AppiumBy.XPATH,
        '(//XCUIElementTypeImage[@name="Product Image"])[2]'
    )

    def click_green_backpack_product(self):
        print("\nClicking on green backpack product")
        self.click(self.GREEN_BACKPACK_IMAGE)
        print("\nClicked green backpack product")
