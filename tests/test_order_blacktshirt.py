
from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.black_tshirt_page import BlackTShirtPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.transaction_logger import execute_transaction
import time

class Test_Order_BlackTShirt:

    def test_webview_navigation(
            self,
            driver,
            mysql_logger):

        # Sequence/execution order
        product_page = ProductsPage(driver)
        black_tshirt_page = BlackTShirtPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)
        menu_page = MenuPage(driver)

        
        print("\nStarting test_01_sort_product_by_price transaction")
        execute_transaction(
            mysql_logger,
            "test_01_sort_product_by_price",
            lambda: (
                product_page.click_product_sort_icon(376,89),
                product_page.click_ascending_by_price_option(),
                product_page.sauce_labs_bolt_tshirt_visible(),
                print("Black TShirt image is visible")
            )
        )
        print("Ended test_01_sort_product_by_price transaction")

        print("\nStarting test_02_click_black_tshirt transaction")
        execute_transaction(
            mysql_logger,
            "test_02_click_black_tshirt",
            lambda: (
                product_page.click_black_tshirt_image(),
                black_tshirt_page.header_visible(),
                print("Black TShirt header is visible")
            )
        )
        print("Ended test_02_click_black_tshirt transaction")

        print("\nStarting test_03_scroll_to_view_black_tshirt_desc transaction")
        execute_transaction(
            mysql_logger,
            "test_03_scroll_to_view_black_tshirt_desc",
            lambda: (
                black_tshirt_page.scroll_to_bottom_of_page(),
                black_tshirt_page.product_description_visible(),
                print("Black TShirt description is visible")
            )
        )
        print("Ended test_03_scroll_to_view_black_tshirt_desc transaction")

        print("\nStarting test_04_add_black_tshirts_to_cart transaction")
        execute_transaction(
            mysql_logger,
            "test_04_add_black_tshirts_to_cart",
            lambda: (
                black_tshirt_page.click_product_plus_button(),
                black_tshirt_page.capture_product_quantity(),
                black_tshirt_page.click_add_to_cart_button(),                
                black_tshirt_page.cart_with_two_items_visible(),
                print("Cart with two items is visible"),
                print("Added Black TShirts to cart")
            )
        )
        print("Ended test_04_add_black_tshirts_to_cart transaction")


        print("\nStarting test_05_proceed_to_checkout transaction")
        execute_transaction(
            mysql_logger,
            "test_05_proceed_to_checkout",
            lambda: (
                product_page.click_shopping_cart_icon(),
                cart_page.header_visible(),
                cart_page.click_proceed_to_checkout_button(),
                login_page.header_visible(),
                print("Login header is visible")
            )
        )
        print("Ended test_05_proceed_to_checkout transaction")
        

        print("\nStarting test_06_login transaction")
        execute_transaction(
            mysql_logger,
            "test_06_login",
            lambda: (
                login_page.enter_username("bob@example.com"),
                login_page.enter_password("10203040"),
                login_page.click_login_button(),
                checkout_page.header_visible(),
                print("Checkout header is visible")
            )
        )
        print("Ended test_06_login transaction")

        print("\nStarting test_07_enter_shipping_info transaction")
        execute_transaction(
            mysql_logger,
            "test_07_enter_shipping_info",
            lambda: (
                checkout_page.enter_fullname("Test User"),
                checkout_page.enter_address_line_1("123 Street"),
                checkout_page.enter_address_line_2("#456"),
                checkout_page.enter_city("Sunnyvale"),
                checkout_page.click_address_line_2_field(),
                checkout_page.enter_state("California"),
                checkout_page.click_address_line_2_field(),
                checkout_page.enter_zipcode("94087"),
                checkout_page.click_address_line_2_field(),
                checkout_page.enter_country("USA"),
                checkout_page.click_address_line_2_field(),
                checkout_page.click_to_payment_button(),
                checkout_page.enter_payment_method_header_visible(),
                print("Enter payment method header is visible")
            )
        )
        print("Ended test_07_enter_shipping_info transaction")

        print("\nStarting test_08_enter_payment_info transaction")
        execute_transaction(
            mysql_logger,
            "test_08_enter_payment_info",
            lambda: (
                checkout_page.enter_creditcard_fullname("Test User"),
                checkout_page.enter_creditcard_number("1234123412341234"),
                checkout_page.enter_creditcard_exp_date("03/28"),
                checkout_page.click_creditcard_number_field(),
                checkout_page.enter_creditcard_secuirty_code("123"),
                checkout_page.click_creditcard_number_field(),
                checkout_page.click_review_order_button(),
                checkout_page.review_your_order_header_visible(),
                print("Review your order header is visible")
            )
        )
        print("Ended test_08_enter_payment_info transaction")

        print("\nStarting test_09_place_order_and_cleanup transaction")
        execute_transaction(
            mysql_logger,
            "test_09_place_order_and_cleanup",
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
        print("Ended test_09_place_order_and_cleanup transaction")
        
