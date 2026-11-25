from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.fleece_page import FleecePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.transaction_logger import execute_transaction


def test_01_SelectPinkFleeceProduct(driver):
    print("\nStarting test_01_SelectPinkFleeceProduct transaction")
    product_page = ProductsPage(driver)
    fleece_page = FleecePage(driver)
    product_page.select_pink_fleece()
    assert fleece_page.header_visible(), "Fleece page header is not visible"
    print("Ended test_01_SelectPinkFleeceProduct transaction")

def test_02_SetPinkFleeceQuantity(driver):
    print("\nStarting test_02_SetPinkFleeceQuantity transaction")
    fleece_page = FleecePage(driver)
    fleece_page.click_plus_icon(14)
    fleece_page.quantity_value()
    print("Ended test_02_SetPinkFleeceQuantity transaction")

def test_03_AddFleeceToCart(driver):
    print("\nStarting test_03_AddFleeceToCart transaction")
    fleece_page = FleecePage(driver)
    fleece_page.click_add_to_cart_button()
    assert fleece_page.cart_with_fifteen_items_visible(), "Cart with 15 items is not visible"
    print("Ended test_03_AddFleeceToCart transaction")

def test_04_GoToShoppingCart(driver):
    print("\nStarting test_04_GoToShoppingCart transaction")
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    product_page.click_shopping_cart_icon()
    assert cart_page.header_visible(),"Cart page header is not visible"
    assert cart_page.fifteen_fleece_pretax_amount_visible(),"Fleece pretax amount is not visible"
    print("Ended test_04_GoToShoppingCart transaction")

def test_05_ProceedToCheckout(driver):
    print("\nStarting test_05_ProceedToCheckout transaction")
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    cart_page.click_proceed_to_checkout_button()
    assert login_page.header_visible(), "Login page header is not visible"
    print("Login header is visible")
    print("Ended test_05_ProceedToCheckout transaction")

def test_06_Login(driver):
    print("\nStarting test_06_Login transaction")
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.enter_username("bob@example.com")
    login_page.enter_password("10203040")
    login_page.click_login_button()
    assert checkout_page.header_visible(),"Checkout page header is not visible"
    print("Checkout header is visible")
    print("Ended test_06_Login transaction")

def test_07_EnterShippingInfo(driver):
    print("\nStarting test_07_EnterShippingInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_fullname("Ben Michael")
    checkout_page.enter_address_line_1("555 Middle St")
    checkout_page.enter_address_line_2("Apt X10")
    checkout_page.enter_city("San Jose")
    checkout_page.enter_state("California")
    checkout_page.enter_zipcode("95112")
    checkout_page.enter_country("USA")
    checkout_page.click_to_payment_button()
    assert checkout_page.enter_payment_method_header_visible(),"Enter payment method header is not visible"
    print("Enter payment method header is visible")
    print("Ended test_07_EnterShippingInfo transaction")

def test_08_EnterPaymentInfo(driver):
    print("\nStarting test_08_EnterPaymentInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_creditcard_fullname("Jenny Smith"),
    checkout_page.enter_creditcard_number("4444444444444444"),
    checkout_page.enter_creditcard_exp_date("03/27"),
    checkout_page.enter_creditcard_security_code("777"),
    checkout_page.click_review_order_button(),
    checkout_page.review_your_order_header_visible(),
    assert checkout_page.fifteen_fleece_posttax_amount_visible(),"The posttax amount is not visible or is incorrect"
    print("Review your order header is visible")
    print("Ended test_08_EnterPaymentInfo transaction")

def test_09_PlaceOrder(driver):
    print("\nStarting test_09_PlaceOrder transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.click_place_order_button(),
    assert checkout_page.checkout_complete_header_visible(),"Checkout complete header is not visible"
    print("Ended test_09_PlaceOrder transaction")

def test_10_Cleanup(driver):
    print("\nStarting test_10_Cleanup transaction")     
    checkout_page = CheckoutPage(driver)
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)
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
    assert login_page.header_visible(), "Login page geader is not visible"
    print("Login header is visible")
    print("Ended test_10_Cleanup transaction")
    
