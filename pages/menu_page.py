from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class MenuPage(BasePage):

    LOGOUT_MENU_ITEM = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="LogOut-menu-item"]'
    )

    WEBVIEW_MENU_ITEM = (
        AppiumBy.ACCESSIBILITY_ID,
        "Webview-menu-item"
    )

    QRCODE_SCANNER_MENU_ITEM = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="QrCodeScanner-menu-item"]'
    )

    LOGIN_MENU_ITEM = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="LogOut-menu-item"]'
    )

    MYDEMOAPP_LOGO = (
        AppiumBy.XPATH,
        '//XCUIElementTypeImage[@name="AppTitle Icons"]'
    )
    ABOUT_MENU_ITEM = (
        AppiumBy.ACCESSIBILITY_ID,
        "About-menu-item"
    )

    REPORT_BUG_MENU_ITEM = (
        AppiumBy.ACCESSIBILITY_ID,
        "Report a Bug"
    )

    def logout_visible(self):
        print("Will check if Logout menu is visible")
        return self.is_visible(self.LOGOUT_MENU)

    def open_webview(self):
        print("Will click on Webview menu item")
        self.click(self.WEBVIEW_MENU_ITEM)
        print("Clicked on Webview meu item")

    def click_qrcodescanner(self):
        print("Will click on the QR Code Scanner menu item")
        self.click(self.QRCODE_SCANNER_MENU_ITEM)
        print("Clicked on QR Code Scanner menu item")

    def click_login(self):
        print("Will click on Login menu item")
        self.click(self.LOGIN_MENU_ITEM)
        print("Clicked on Login meu item")

    def click_logout(self):
        print("Will click on Logout menu item")
        self.click(self.LOGOUT_MENU_ITEM)
        print("Clicked on Logout menu item")
    
    def click_about(self):
        print("Will click on About menu item")
        self.click(self.ABOUT_MENU_ITEM)
        print("Clicked on About menu item")

    def click_reportbug(self):
        print("Will click on Report a Bug menu item")
        report_bug_button = self.driver.find_element(*self.REPORT_BUG_MENU_ITEM)
        report_bug_button.click()
        print("Clicked on Report a Bug menu item")

    def mydemoapp_logo_visible(self):
        print("Will check if the MyDemoApp logo is visible")
        return self.is_visible(self.MYDEMOAPP_LOGO)