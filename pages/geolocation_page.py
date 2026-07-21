from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class GeoLocationPage(BasePage):

    GEO_LOCATION_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Geo Location"]'
    )

    BACK_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@name="GeoLocation-screen"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton'
    )

    def header_visible(self):
        print("Will check if Geo Location header is visible")
        return self.is_visible(self.GEO_LOCATION_HEADER)

    def click_back_icon(self):
        print("Will click on Back arrow")
        self.click(self.BACK_ICON)
        print("Clicked on Back arrow")

