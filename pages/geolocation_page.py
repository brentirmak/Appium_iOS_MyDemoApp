from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class GeoLocationPage(BasePage):

    GEO_LOCATION_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Geo Location"]'
    )

    def header_visible(self):
        print("Will check if Geo Location header is visible")
        return self.is_visible(self.GEO_LOCATION_HEADER)


