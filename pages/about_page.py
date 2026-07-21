from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class AboutPage(BasePage):

    ABOUT_PAGE_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="About "]'
    )

    ABOUT_PAGE_MORE_BACK_ICON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@name="About-screen"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton'
    )

    def header_visible(self):
        print("Will confirm that the About page header is visible")
        return self.is_visible(self.ABOUT_PAGE_HEADER)

    def click_about_back_icon(self):
        print("Clicking on About back icon..")
        self.click(self.ABOUT_PAGE_MORE_BACK_ICON)
        print("Clicked on About back icon")