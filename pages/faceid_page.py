from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class FaceIDPage(BasePage):

    FACEID_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Face ID"]'
    )

    FACEID_PAGE_MORE_BACK_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@name="Biometrics-screen"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton'
    )

    def header_visible(self):
        print("Will check if FaceID header is visible")
        return self.is_visible(self.FACEID_HEADER)

    def click_faceid_back_icon(self):
        print("Clicking on FaceID back icon..")
        self.click(self.FACEID_PAGE_MORE_BACK_ICON)
        print("Clicked on FaceID back icon")