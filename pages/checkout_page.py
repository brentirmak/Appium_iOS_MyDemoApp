from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


def _field_below_label(label, screen=None):
    """The TextField that follows a StaticText label (label -> following sibling wrapper ->
    XCUIElementTypeTextField), optionally scoped to a screen by its accessibility name.
    Verified against the shipping and payment page sources."""
    scope = f'//XCUIElementTypeOther[@name="{screen}"]' if screen else ""
    return (AppiumBy.XPATH,
            f'{scope}//XCUIElementTypeStaticText[@name="{label}"]'
            f'/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeTextField')


class CheckoutPage(BasePage):

    # Shipping and payment fields use label-relative locators on the real TextFields
    # (verified against shipping_page.xml and payment_page.xml), so fill() verifies what
    # was typed. Both sets are scoped to their screen container ("ShippingAddress-screen" /
    # "Payment-screen"), because labels such as "Full Name*" appear on both pages.
    CHECKOUT_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Checkout"]')
    FULLNAME_FIELD = _field_below_label("Full Name*", screen="ShippingAddress-screen")
    ADDRESS_1_FIELD = _field_below_label("Address Line 1*", screen="ShippingAddress-screen")
    ADDRESS_2_FIELD = _field_below_label("Address Line 2", screen="ShippingAddress-screen")
    CITY_FIELD = _field_below_label("City*", screen="ShippingAddress-screen")
    STATE_FIELD = _field_below_label("State/Region", screen="ShippingAddress-screen")
    ZIPCODE_FIELD = _field_below_label("Zip Code*", screen="ShippingAddress-screen")
    COUNTRY_FIELD = _field_below_label("Country*", screen="ShippingAddress-screen")
    TO_PAYMENT_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="To Payment"]')
    ENTER_PAYMENT_METHOD_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Enter a payment method"]')
    PAYMENT_FULLNAME_FIELD = _field_below_label("Full Name*", screen="Payment-screen")
    PAYMENT_CARDNUMBER_FIELD = _field_below_label("Card Number*", screen="Payment-screen")
    PAYMENT_CARDNUMBER_EXP_DATE_FIELD = _field_below_label("Expiration Date*", screen="Payment-screen")
    PAYMENT_CARDNUMBER_EXP_DATE_CLEAR_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeTextField/XCUIElementTypeButton')
    PAYMENT_CARDNUMBER_SEC_CODE_FIELD = _field_below_label("Security Code*", screen="Payment-screen")
    REVIEW_ORDER_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Review Order"]')
    REVIEW_YOUR_ORDER_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Review your order"]')
    PLACE_ORDER_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Place Order"]')
    CHECKOUT_COMPLETE_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Checkout Complete"]')
    CONTINUE_SHOPPING_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ContinueShopping"]')
    SHIPPING_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Enter a shipping address"]')

    # Tapping a text field dismisses the keyboard in this app (this is what the original
    # "click Address Line 2" workaround relied on). First displayed target is tapped:
    # Address Line 2 on the shipping page; on the payment page that label does not exist,
    # so the payment Full Name field (the field the original workaround hit there) is used.
    KEYBOARD_DISMISS_TARGETS = (ADDRESS_2_FIELD, PAYMENT_FULLNAME_FIELD)

    # ---------------------------
    # Shipping address
    # ---------------------------
    def enter_fullname(self, fullname, timeout=15):
        print("Entering Full Name")
        self.fill(self.FULLNAME_FIELD, fullname, name="Full Name", timeout=timeout)

    def enter_address_line_1(self, address_1, timeout=15):
        print("Entering Address Line 1")
        self.fill(self.ADDRESS_1_FIELD, address_1, name="Address Line 1", timeout=timeout)

    def enter_address_line_2(self, address_2, timeout=15):
        print("Entering Address Line 2")
        self.fill(self.ADDRESS_2_FIELD, address_2, name="Address Line 2", timeout=timeout)

    def enter_city(self, city, timeout=15):
        print("Entering City")
        self.fill(self.CITY_FIELD, city, name="City", timeout=timeout)

    def enter_state(self, state, timeout=15):
        print("Entering State")
        self.fill(self.STATE_FIELD, state, name="State", timeout=timeout)

    def enter_zipcode(self, zipcode, timeout=15):
        print("Entering Zip Code")
        self.fill(self.ZIPCODE_FIELD, zipcode, name="Zip Code", timeout=timeout)

    def enter_country(self, country, timeout=15):
        print("Entering Country")
        self.fill(self.COUNTRY_FIELD, country, name="Country", timeout=timeout)

    def click_address_line_2_field(self, timeout=15):
        # Kept so existing tests keep working. This used to tap Address Line 2,
        # which re-focused a text field and left it as the default target for stray
        # keystrokes. It now just dismisses the keyboard.
        print("Dismissing keyboard")
        self.hide_keyboard()

    def click_to_payment_button(self, timeout=15):
        print("Will click on To Payment button")
        self.hide_keyboard()
        self.click_when_ready(self.TO_PAYMENT_BUTTON, timeout)
        # Fail here, not three steps later, if the tap did not navigate
        self.enter_payment_method_header_visible(timeout)
        print("Payment page is displayed")

    # ---------------------------
    # Headers / page checks (these now raise AssertionError on failure)
    # ---------------------------
    def header_visible(self, timeout=30):
        print("Will check if Checkout header is visible")
        return self.assert_visible(self.CHECKOUT_HEADER, timeout,
                                   "Checkout page did not appear")

    def click_header(self, timeout=15):
        print("Will click on Checkout header")
        self.click(self.CHECKOUT_HEADER, timeout)

    def enter_payment_method_header_visible(self, timeout=15):
        print("Will check that payment method header is visible")
        return self.assert_visible(self.ENTER_PAYMENT_METHOD_HEADER, timeout,
                                   "Payment page did not appear after tapping To Payment")

    def review_your_order_header_visible(self, timeout=15):
        print("Will check if Review your order header is visible")
        return self.assert_visible(self.REVIEW_YOUR_ORDER_HEADER, timeout,
                                   "Review your order page did not appear")

    def checkout_complete_header_visible(self, timeout=30):
        print("Will check if Checkout Complete header is visible")
        return self.assert_visible(self.CHECKOUT_COMPLETE_HEADER, timeout,
                                   "Checkout Complete page did not appear")

    # ---------------------------
    # Payment
    # ---------------------------
    def enter_creditcard_fullname(self, creditcard_fullname, timeout=15):
        print("Entering Credit Card Full Name")
        self.fill(self.PAYMENT_FULLNAME_FIELD, creditcard_fullname,
                  name="Credit Card Full Name", timeout=timeout)

    def enter_creditcard_number(self, creditcard_number, timeout=15):
        print("Entering Credit Card Number")
        self.fill(self.PAYMENT_CARDNUMBER_FIELD, creditcard_number,
                  name="Credit Card Number", timeout=timeout)

    def click_clear_expiration_date_button(self, timeout=10):
        print("Will click on the clear button associated with the Credit Card expiration date")
        self.click(self.PAYMENT_CARDNUMBER_EXP_DATE_CLEAR_BUTTON, timeout)

    def enter_creditcard_exp_date(self, creditcard_exp_date, timeout=15):
        print("Entering Credit Card Expiration Date")
        # Type digits only. Typing "03/28" left the field showing "03": the "/" appears to
        # stall the input (numeric keypad has no "/" key), so "28" was never entered.
        # The field's mask is expected to insert the "/" itself.
        digits = "".join(ch for ch in creditcard_exp_date if ch.isdigit())
        element = self.fill(self.PAYMENT_CARDNUMBER_EXP_DATE_FIELD, digits,
                            name="Expiration Date", timeout=timeout)
        try:
            print(f"Expiration Date field now shows {element.get_attribute('value')!r}")
        except Exception:
            pass

    def enter_creditcard_security_code(self, creditcard_security_code, timeout=15):
        print("Entering Credit Card Security Code")
        self.fill(self.PAYMENT_CARDNUMBER_SEC_CODE_FIELD, creditcard_security_code,
                  name="Security Code", timeout=timeout)

    # Original (misspelled) name kept so the existing test keeps working
    enter_creditcard_secuirty_code = enter_creditcard_security_code

    def click_creditcard_number_field(self, timeout=15):
        # Previously tapped the Address 2 locator, which on this screen is the payment
        # Full Name field. Now only dismisses the keyboard.
        print("Dismissing keyboard")
        self.hide_keyboard()

    def click_review_order_button(self, timeout=15):
        print("Will click on Review Order button")
        self.hide_keyboard()
        self.click_when_ready(self.REVIEW_ORDER_BUTTON, timeout)
        self.review_your_order_header_visible(timeout)

    # ---------------------------
    # Place order
    # ---------------------------
    def click_place_order_button(self, timeout=15):
        print("Will click on Place Order button")
        self.click_when_ready(self.PLACE_ORDER_BUTTON, timeout)
        self.checkout_complete_header_visible()

    def click_continue_shopping_button(self, timeout=15):
        print("Will click on Continue Shopping button")
        self.click(self.CONTINUE_SHOPPING_BUTTON, timeout)