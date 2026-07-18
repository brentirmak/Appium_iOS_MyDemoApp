from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CHECKOUT_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Checkout"]'
    )

    FULLNAME_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
    )
 
    ADDRESS_1_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]'
    )

    ADDRESS_2_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]'
    )

    CITY_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther'
    )

    STATE_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther'
    )

    ZIPCODE_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther'
    )

    COUNTRY_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther'
    )

    TO_PAYMENT_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="To Payment"]'
    )

    ENTER_PAYMENT_METHOD_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Enter a payment method"]'
    )

    PAYMENT_FULLNAME_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]'
    )

    PAYMENT_CARDNUMBER_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]'
    )

    PAYMENT_CARDNUMBER_EXP_DATE_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther'
    )

    PAYMENT_CARDNUMBER_SEC_CODE_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther'
    )

    REVIEW_ORDER_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Review Order"]'
    )

    REVIEW_YOUR_ORDER_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Review your order"]'
    )

    PLACE_ORDER_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Place Order"]'
    )

    CHECKOUT_COMPLETE_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Checkout Complete"]'
    )

    CONTINUE_SHOPPING_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="ContinueShopping"]'
    )

    def enter_fullname(self, fullname):
        print("Will click on Full Name field")
        self.click(self.FULLNAME_FIELD)
        print("Clicked on Full Name field")
        print("Will enter full name into the Full Name field")
        self.driver.find_element(*self.FULLNAME_FIELD).send_keys(fullname)
        print("Entered full name into the Full Name field")
    
    def enter_address_line_1(self, address_1):
        print("Will click on Address Line 1 field")
        self.click(self.ADDRESS_1_FIELD)
        print("Clicked on Address Line 1 field")
        print("Will enter address into the Address Line 1 field")
        self.driver.find_element(*self.ADDRESS_1_FIELD).send_keys(address_1)
        print("Entered address into the Address 1 field")
    
    def enter_address_line_2(self, address_2):
        print("Will click on Address Line 2 field")
        self.click(self.ADDRESS_2_FIELD)
        print("Clicked on Address Line 2 field")
        print("Will enter address into the Address Line 2 field")
        self.driver.find_element(*self.ADDRESS_2_FIELD).send_keys(address_2)
        print("Entered address into the Address 2 field")
    
    def enter_city(self, city):
        print("Will click on Address Line 1 field")
        self.click(self.CITY_FIELD)
        print("Clicked on City field")
        print("Will enter city into the City field")
        self.driver.find_element(*self.CITY_FIELD).send_keys(city)
        print("Entered city into the City field")
    
    def enter_state(self, state):
        print("Will click on State field")
        self.click(self.STATE_FIELD)
        print("Clicked on State field")
        print("Will enter state into the State field")
        self.driver.find_element(*self.STATE_FIELD).send_keys(state)
        print("Entered state into the State field")

    def enter_zipcode(self, zipcode):
        print("Will click on ZipCode field")
        self.click(self.ZIPCODE_FIELD)
        print("Clicked on Zip Code field")
        print("Will enter zip code into the Zip Code field")
        self.driver.find_element(*self.ZIPCODE_FIELD).send_keys(zipcode)
        print("Entered zip code into the Zip Code field")

    def enter_country(self, country):
        print("Will click on Country field")
        self.click(self.COUNTRY_FIELD)
        print("Clicked on Country field")
        print("Will enter country into the Country field")
        self.driver.find_element(*self.COUNTRY_FIELD).send_keys(country)
        print("Entered country into the Country field")

    def click_address_line_2_field(self):
        print("Will click on Address 2 field to help close keyboard popup")
        self.click(self.ADDRESS_2_FIELD)
        print("Clicked on Address 2 field to help close keyboard popup")

    def click_to_payment_button(self):
        print("Will click on To Payment button")
        self.click(self.TO_PAYMENT_BUTTON)
        print("Clicked on To Payment button")
        
    def header_visible(self):
        print("Will check if Checkout header is visible")
        return self.is_visible(self.CHECKOUT_HEADER)
    
    def click_header(self):
        print("Will click on Checkout header")
        self.click(self.CHECKOUT_HEADER)
        print("Clicked on Checkout header")
    
    def enter_payment_method_header_visible(self):
        print("Will check that payment method header is visible")
        return self.is_visible(self.ENTER_PAYMENT_METHOD_HEADER)
    
    def enter_creditcard_fullname(self, creditcard_fullname):
        print("Will click on Credit Card Full Name field")
        self.click(self.PAYMENT_FULLNAME_FIELD)
        print("Clicked on Credit Card Full Name field")
        print("Will enter full name into the Credit Card Full Name field")
        self.driver.find_element(*self.PAYMENT_FULLNAME_FIELD).send_keys(creditcard_fullname)
        print("Entered full name into the Credit Card Full Name field")
    
    def enter_creditcard_number(self, creditcard_number):
        print("Will click on Credit Card Number field")
        self.click(self.PAYMENT_CARDNUMBER_FIELD)
        print("Clicked on Credit Card Number field")
        print("Will enter credit card into the Credit Card Number field")
        self.driver.find_element(*self.PAYMENT_CARDNUMBER_FIELD).send_keys(creditcard_number)
        print("Entered credit card into the Credit Card Number field")

    def click_creditcard_number_field(self):
        print("Will click on Credit Card number field to help close keyboard popup")
        self.click(self.ADDRESS_2_FIELD)
        print("Clicked on Credit Card number field to help close keyboard popup")

    def enter_creditcard_exp_date(self, creditcard_exp_date):
        print("Will click on Credit Card Expiration Date field")
        self.click(self.PAYMENT_CARDNUMBER_EXP_DATE_FIELD)
        print("Clicked on Credit Card Expiration Date field")
        print("Will enter credit card expiration date into the Credit Card Expiration Date field")
        self.driver.find_element(*self.PAYMENT_CARDNUMBER_EXP_DATE_FIELD).send_keys(creditcard_exp_date)
        print("Entered credit card expiration date into the Credit Card Expiration Date field")

    def enter_creditcard_exp_date(self, creditcard_exp_date):
        print("Will click on Credit Card Expiration Date field")
        self.click(self.PAYMENT_CARDNUMBER_EXP_DATE_FIELD)
        print("Clicked on Credit Card Expiration Date field")
        print("Will enter credit card expiration date into the Credit Card Expiration Date field")
        self.driver.find_element(*self.PAYMENT_CARDNUMBER_EXP_DATE_FIELD).send_keys(creditcard_exp_date)
        print("Entered credit card expiration date into the Credit Card Expiration Date field")

    def enter_creditcard_secuirty_code(self, creditcard_security_code):
        print("Will click on Credit Card Security Code field")
        self.click(self.PAYMENT_CARDNUMBER_SEC_CODE_FIELD)
        print("Clicked on Credit Card Security Code field")
        print("Will enter credit card security code into the Credit Card Security Code field")
        self.driver.find_element(*self.PAYMENT_CARDNUMBER_SEC_CODE_FIELD).send_keys(creditcard_security_code)
        print("Entered credit card security code into the Credit Card Security Code field")

    def click_review_order_button(self):
        print("Will click on Review Order button")
        self.click(self.REVIEW_ORDER_BUTTON)
        print("Clicked on Review Order button")

    def review_your_order_header_visible(self):
        print("Will check if Review your order header is visible")
        return self.is_visible(self.REVIEW_YOUR_ORDER_HEADER)
    
    def click_place_order_button(self):
        print("Will click on Place Order button")
        self.click(self.PLACE_ORDER_BUTTON)
        print("Clicked on Place Order button")

    def checkout_complete_header_visible(self):
        print("Will check if Checkout Complete header is visible")
        return self.is_visible(self.CHECKOUT_COMPLETE_HEADER)
    
    def click_continue_shopping_button(self):
        print("Will click on Continue Shopping button")
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        print("Clicked on Continue Shopping button")