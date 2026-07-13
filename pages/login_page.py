from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[@name="Login"]'
    )

    USERNAME_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeTextField'
    )

    PASSWORD_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeSecureTextField'
    )

    LOGIN_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Login"]'
    )

    NOT_NOW_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Not Now"]'
    )

    PRODUCTS_PAGE_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeOther[@name="Catalog-screen"]/XCUIElementTypeOther[1]'
    )

 
    def enter_username(self, username):
        print("Will click on Username field")
        self.click(self.USERNAME_FIELD)
        print("Clicked on Username field")
        print("Will enter username into the Username field")
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        print("Entered username into the Username field")
    
    def enter_password(self, password):
        print("Will click on Password field")
        self.click(self.PASSWORD_FIELD)
        print("Clicked on Password field")
        print("Will enter password into the Password field")
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        print("Entered password into the Password field")
        self.click(self.USERNAME_FIELD)
        print("Clicked on Username field again")

    def click_login_button(self):
        print("Will click on Login button")
        self.click(self.LOGIN_BUTTON)
        print("Clicked on Login button")
    
    def products_page_visible(self):
        print("Will click on Products page header")
        self.click(self.PRODUCTS_PAGE_HEADER)
        print("Clicked on Products page header")
    
    def header_visible(self):
        print("Will check if Login header is visible")
        return self.is_visible(self.LOGIN_HEADER)