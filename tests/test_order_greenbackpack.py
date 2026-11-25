from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.greenbackpack_page import GreenBackpackPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.transaction_logger import execute_transaction


def test_01_SelectGreenBackpackProduct(driver):
    print("\nStarting test_01_SelectGreenBackpackProduct transaction")
    product_page = ProductsPage(driver)
    green_backpack_page = GreenBackpackPage(driver)
    product_page.click_green_backpack_product()
    assert green_backpack_page.header_visible(), "Green Backpage page header is not visible"
    print("Ended test_01_SelectGreenBackpackProduct transaction")

def test_02_AddGreenBackpackToCart(driver):
    print("\nStarting test_02_AddGreenBackpackToCart transaction")
    green_backpack_page = GreenBackpackPage(driver)
    green_backpack_page.click_add_to_cart_button()
    assert green_backpack_page.cart_with_one_item_visible(), "Cart with one item is not visible"
    print("Ended test_02_AddGreenBackpackToCart transaction")

def test_03_ProceedToCheckout(driver):
    print("\nStarting test_03_ProceedToCheckout transaction")
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    product_page.click_shopping_cart_icon()
    assert cart_page.one_greenbackpack_pretax_amount_visible(), "Pretax amount for 1 green backpack is not visible"
    assert cart_page.header_visible(), "Cart page header is not visible"
    cart_page.click_proceed_to_checkout_button()
    assert login_page.header_visible(), "Login page header is not visible"
    print("Login header is visible")
    print("Ended test_03_ProceedToCheckout transaction")

def test_04_Login(driver):
    print("\nStarting test_04_Login transaction")
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.enter_username("visual@example.com")
    login_page.enter_password("10203040")
    login_page.click_login_button()
    assert checkout_page.header_visible(),"Checkout page header is not visible"
    print("Checkout header is visible")
    print("Ended test_04_Login transaction")

def test_05_EnterShippingInfo(driver):
    print("\nStarting test_05_EnterShippingInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_fullname("Test User")
    checkout_page.enter_address_line_1("123 Street")
    checkout_page.enter_address_line_2("#456")
    checkout_page.enter_city("Sunnyvale")
    checkout_page.enter_state("California")
    checkout_page.enter_zipcode("94087")
    checkout_page.enter_country("USA")
    checkout_page.click_to_payment_button()
    assert checkout_page.enter_payment_method_header_visible(), "Enter Payment Method header is not visible"
    print("Enter payment method header is visible")
    print("Ended test_05_EnterShippingInfo transaction")

def test_06_EnterPaymentInfo(driver):
    print("\nStarting test_06_EnterPaymentInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_creditcard_fullname("Test User")
    checkout_page.enter_creditcard_number("1234123412341234")
    checkout_page.enter_creditcard_exp_date("03/28")
    checkout_page.enter_creditcard_security_code("123")
    checkout_page.click_review_order_button()
    assert checkout_page.one_backpack_posttax_amount_visible(), "Posttax amount for 1 backpack is not visible or is incorrect"
    assert checkout_page.review_your_order_header_visible(), "Review your order header is not visible"
    print("Review your order header is visible")
    print("Ended test_06_EnterPaymentInfo transaction")

def test_07_PlaceOrder(driver):
    print("\nStarting test_07_PlaceOrder transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.click_place_order_button()
    assert checkout_page.checkout_complete_header_visible(), "Checkout complete header is visible"
    print("Ended test_07_PlaceOrder transaction")

def test_08_Cleanup(driver):
    print("\nStarting test_08_Cleanup transaction")
    checkout_page = CheckoutPage(driver)
    cart_page = CartPage(driver)
    product_page = ProductsPage(driver)
    menu_page = MenuPage(driver)
    login_page = LoginPage(driver)
    checkout_page.click_continue_shopping_button()
    product_page.click_shopping_cart_icon()
    cart_page.click_remove_item_button()
    assert cart_page.no_items_in_cart_visible(), "No items in cart text is not visible"
    cart_page.click_go_shopping_button()
    product_page.click_more_icon()
    assert menu_page.mydemoapp_logo_visible(), "MyDemoApp logo is not visible"
    menu_page.click_logout()
    assert login_page.header_visible(),"Login page header is not visible"
    print("Login header is visible")
    print("Ended test_08_Cleanup transaction")
