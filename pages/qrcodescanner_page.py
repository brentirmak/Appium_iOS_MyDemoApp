from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class QRCodeScannerPage(BasePage):

    QR_CODE_SCANNER_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="QR Code Scanner"]'
    )

    DO_NOT_ALLOW_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'
    )

    # //XCUIElementTypeAlert[@name="Camera Access Denied"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]
    # //XCUIElementTypeAlert[@name="Camera Access Denied"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]
    ACCESS_DENIED_OK_BUTTON = (
        AppiumBy.XPATH,
        #'//XCUIElementTypeButton[@name="OK"] || //XCUIElementTypeAlert[@name="Camera Access Denied"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]'
        '//XCUIElementTypeAlert[@name="Camera Access Denied"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]'
    )

    def click_do_not_allow_button(self):
        print("Will click on Don't Allow button")
        self.click(self.DO_NOT_ALLOW_BUTTON)
        print("Clicked on Don't Allow button")

    def click_access_denied_ok_button(self):
        print("Will click Camera Access Denied - OK button")
        self.click(self.ACCESS_DENIED_OK_BUTTON)
        print("Clicked on Camera Access Denied - OK button")

    def header_visible(self):
        print("Confirming that the QR Code Scanner header is visible")
        return self.is_visible(self.QR_CODE_SCANNER_HEADER)

    