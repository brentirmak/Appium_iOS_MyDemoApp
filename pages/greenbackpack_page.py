from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class GreenBackpackPage(BasePage):

    GREEN_BACKBACK_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Sauce Labs Backpack - Green"]'
    )

    #def click_green_backpack_product(self):
    #    self.click(self.GREEN_BACKPACK_IMAGE)

    def header_visible(self):
        return self.is_visible(self.GREEN_BACKBACK_HEADER)
        print("\nConfirmed green backpack header is visible")