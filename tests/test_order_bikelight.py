from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.bikelight_page import BikeLightPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.transaction_logger import execute_transaction

def test_01_GoToBikeLightProductPage(driver):
    print("\nStarting test_01_GoToBikeLightProductPage transaction")
    product_page = ProductsPage(driver)
    bike_light_page = BikeLightPage(driver)
    product_page.select_bike_light()
    assert bike_light_page.header_visible(), "Bike Light page header is not visible"
    print("Ended test_01_GoToBikeLightProductPage transaction")

def test_02_AddFiveBikeLightsToCart(driver):
    print("\nStarting test_02_AddFiveBikeLightsToCart transaction")
    bike_light_page = BikeLightPage(driver)
    bike_light_page.click_plus_icon(5)
    bike_light_page.verify_quantity_value()
    bike_light_page.click_add_to_cart_button()
    assert bike_light_page.cart_with_five_items_visible(),"Cart with 5 items is not visible"
    print("Ended test_02_AddFiveBikeLightsToCart transaction")

def test_03_GoToShoppingCart(driver):
    print("\nStarting test_03_GoToShoppingCart transaction")
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    product_page.click_shopping_cart_icon()
    cart_page.header_visible()
    assert cart_page.five_bikelights_pretax_amount_visible(), "Cart with 5 bike lights pretax amount is not visible or correct"
    print("Ended test_03_GoToShoppingCart transaction")

def test_04_ProceedToCheckOut(driver):
    print("\nStarting test_04_ProceedToCheckOut transaction")
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    cart_page.click_proceed_to_checkout_button()
    assert login_page.header_visible(), "Login page header is not visible"
    print("Login header is visible")
    print("Ended test_04_ProceedToCheckOut transaction")

def test_05_Login(driver):
    print("\nStarting test_05_Login transaction")
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.enter_username("visual@example.com")
    login_page.enter_password("10203040")
    login_page.click_login_button()
    assert checkout_page.header_visible(), "Checkout page header is not visible"
    print("Checkout header is visible")
    print("Ended test_05_Login transaction")

def test_06_EnterShippingInfo(driver):
    print("\nStarting test_06_EnterShippingInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_fullname("John Smith")
    checkout_page.enter_address_line_1("987 End St")
    checkout_page.enter_address_line_2("Apt Z10")
    checkout_page.enter_city("San Jose")
    checkout_page.enter_state("California")
    checkout_page.enter_zipcode("95112")
    checkout_page.enter_country("USA")
    checkout_page.click_to_payment_button()
    assert checkout_page.enter_payment_method_header_visible(), "Checkout page Enter Payment Method header is not visible"
    print("Enter payment method header is visible")
    print("Ended test_06_EnterShippingInfo transaction")

def test_07_EnterPaymentInfo(driver):
    print("\nStarting test_07_EnterPaymentInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_creditcard_fullname("John Smith")
    checkout_page.enter_creditcard_number("5555555555555555")
    checkout_page.enter_creditcard_exp_date("03/27")
    checkout_page.enter_creditcard_security_code("456")
    checkout_page.click_review_order_button()
    assert checkout_page.review_your_order_header_visible(), "Review your order header is not visible"
    assert checkout_page.five_bikelights_posttax_amount_visible(), "5 Bikelights posttax amount is not visible or correct"
    print("Review your order header is visible")
    print("Ended test_07_EnterPaymentInfo transaction")

def test_08_PlaceOrder(driver):
    print("\nStarting test_08_PlaceOrder transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.click_place_order_button()
    assert checkout_page.checkout_complete_header_visible(), "Checkout complete header not visible"
    checkout_page.click_continue_shopping_button()
    print("Ended test_08_PlaceOrder transaction")

def test_09_CleanShoppingCart(driver):
    print("\nStarting test_08_PlaceOrder transaction")
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    product_page.click_shopping_cart_icon()
    cart_page.click_remove_item_button()
    assert cart_page.no_items_in_cart_visible(), "No items in cart not visible"
    cart_page.click_go_shopping_button()
    print("Ended test_09_CleanShoppingCart transaction")

def test_10_Logout(driver):
    print("\nStarting test_10_Logout transaction")
    product_page = ProductsPage(driver)
    menu_page = MenuPage(driver)
    login_page = LoginPage(driver)
    product_page.click_more_icon()
    assert menu_page.mydemoapp_logo_visible(), "MyDemoApp logo is not visible"
    menu_page.click_logout()
    assert login_page.header_visible(), "Login page header is not visible"
    print("Login header is visible")
    print("Ended test_10_Logout transaction")

    















'''
class Test_Order_BikeLight:

    def test_webview_navigation(
            self,
            driver,
            mysql_logger):

        # Sequence/execution order
        product_page = ProductsPage(driver)
        bike_light_page = BikeLightPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)
        menu_page = MenuPage(driver)

        print("\nStarting test_01_select_product transaction")
        execute_transaction(
            mysql_logger,
            "test_01_select_product",
            lambda: (
                product_page.select_bike_light(),
                bike_light_page.header_visible(),
                bike_light_page.click_plus_icon(5),
                bike_light_page.quantity_value(),
                bike_light_page.click_add_to_cart_button(),
                bike_light_page.cart_with_five_items_visible(),
                print("Cart with five items is visible")
            )
        )
        print("Ended test_01_select_product transaction")

        print("\nStarting test_02_proceed_to_checkout transaction")
        execute_transaction(
            mysql_logger,
            "test_02_proceed_to_checkout",
            lambda: (
                product_page.click_shopping_cart_icon(),
                cart_page.header_visible(),
                cart_page.five_bikelights_pretax_amount_visible(),
                cart_page.click_proceed_to_checkout_button(),
                login_page.header_visible(),
                print("Login header is visible")
            )
        )
        print("Ended test_02_proceed_to_checkout transaction")

        print("\nStarting test_03_login transaction")
        execute_transaction(
            mysql_logger,
            "test_03_login",
            lambda: (
                login_page.enter_username("visual@example.com"),
                login_page.enter_password("10203040"),
                login_page.click_login_button(),
                checkout_page.header_visible(),
                print("Checkout header is visible")
            )
        )
        print("Ended test_03_login transaction")


        print("\nStarting test_04_enter_shipping_info transaction")
        execute_transaction(
            mysql_logger,
            "test_04_enter_shipping_info",
            lambda: (
                checkout_page.enter_fullname("John Smith"),
                checkout_page.enter_address_line_1("987 End St"),
                checkout_page.enter_address_line_2("Apt Z10"),
                checkout_page.enter_city("San Jose"),
                checkout_page.enter_state("California"),
                checkout_page.enter_zipcode("95112"),
                checkout_page.enter_country("USA"),
                checkout_page.click_to_payment_button(),
                checkout_page.enter_payment_method_header_visible(),
                print("Enter payment method header is visible")
            )
        )
        print("Ended test_04_enter_shipping_info transaction")

        print("\nStarting test_05_enter_payment_info transaction")
        execute_transaction(
            mysql_logger,
            "test_05_enter_payment_info",
            lambda: (
                checkout_page.enter_creditcard_fullname("John Smith"),
                checkout_page.enter_creditcard_number("5555555555555555"),
                checkout_page.enter_creditcard_exp_date("03/27"),
                checkout_page.enter_creditcard_security_code("456"),
                checkout_page.click_review_order_button(),
                checkout_page.review_your_order_header_visible(),
                checkout_page.five_bikelights_posttax_amount_visible(),
                print("Review your order header is visible")
            )
        )
        print("Ended test_05_enter_payment_info transaction")

        print("\nStarting test_06_place_order_and_cleanup transaction")
        execute_transaction(
            mysql_logger,
            "test_06_place_order_and_cleanup",
            lambda: (
                checkout_page.click_place_order_button(),
                checkout_page.checkout_complete_header_visible(),
                checkout_page.click_continue_shopping_button(),
                product_page.click_shopping_cart_icon(),
                cart_page.click_remove_item_button(),
                cart_page.no_items_in_cart_visible(),
                cart_page.click_go_shopping_button(),
                product_page.click_more_icon(),
                menu_page.mydemoapp_logo_visible(),
                menu_page.click_logout(),
                login_page.header_visible(),
                print("Login header is visible")
            )
        )
        print("Ended test_06_place_order_and_cleanup transaction")
'''