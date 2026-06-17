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
        self.click(self.USERNAME_FIELD)
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
    
    def enter_password(self, password):
        self.click(self.PASSWORD_FIELD)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.click(self.USERNAME_FIELD)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        #self.click(self.NOT_NOW_BUTTON)
    
    def products_page_visible(self):
        self.click(self.PRODUCTS_PAGE_HEADER)
    
    def header_visible(self):
        return self.is_visible(self.LOGIN_HEADER)