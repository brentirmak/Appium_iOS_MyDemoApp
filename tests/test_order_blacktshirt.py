from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.black_tshirt_page import BlackTShirtPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.transaction_logger import execute_transaction
#from pathlib import Path


def test_01_SortProductByPrice(driver):
    print("\nStarting test_01_SortProductByPrice transaction")
    product_page = ProductsPage(driver)
    product_page.click_product_sort_icon(376, 89)
    product_page.click_ascending_by_price_option()
    assert product_page.sauce_labs_bolt_tshirt_visible(),"Bolt Tshirt is not visible"
    print("Black TShirt image is visible")
    print("Ended test_01_SortProductByPrice transaction")

def test_02_SelectBlackTshirt(driver):
    print("\nStarting test_02_SelectBlackTshirt transaction")
    product_page = ProductsPage(driver)
    black_tshirt_page = BlackTShirtPage(driver)
    product_page.click_black_tshirt_image()
    assert black_tshirt_page.header_visible(),"Black Tshirt page header is not visible"
    print("Black TShirt header is visible")
    print("Ended test_02_SelectBlackTshirt transaction")

def test_03_ScrollToViewBlackTshirtDesc(driver):
    print("\nStarting test_03_ScrollToViewBlackTshirtDesc transaction")
    black_tshirt_page = BlackTShirtPage(driver)
    black_tshirt_page.scroll_to_bottom_of_page()
    assert black_tshirt_page.product_description_visible(),"Product Description is not visible"
    print("Black TShirt description is visible")
    print("\nEnded test_03_ScrollToViewBlackTshirtDesc transaction")
            
def test_04_AddBlackTshirtsToCart(driver):
    print("\nStarting test_04_AddBlackTshirtsToCart")        
    black_tshirt_page = BlackTShirtPage(driver)
    black_tshirt_page.click_product_plus_button()
    black_tshirt_page.capture_product_quantity()
    black_tshirt_page.click_add_to_cart_button()
    assert black_tshirt_page.cart_with_two_items_visible(),"Cart with 2 items is not visible"
    print("Cart with two items is visible")
    print("Added Black TShirts to cart")
    print("\nEnded test_04_AddBlackTshirtsToCart")   

def test_05_ProceedToCheckout(driver):
    print("\nStarting test_05_ProceedToCheckout")        
    product_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)
    product_page.click_shopping_cart_icon()
    assert cart_page.header_visible(), "Cart page header is not visible"
    assert cart_page.two_tshirts_pretax_amount_visible(), "2 tshirts pretax amount is not visible"
    cart_page.click_proceed_to_checkout_button()
    assert login_page.header_visible(), "Login page header is not visible"
    print("Login header is visible")
    print("\nEnded test_05_ProceedToCheckout")        

def test_06_Login(driver):
    print("\nStarting test_06_Login transaction")
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)
    login_page.enter_username("bob@example.com"),
    login_page.enter_password("10203040"),
    login_page.click_login_button(),
    assert checkout_page.header_visible(),"Checkout page header is not visible"
    #Path("shipping_page.xml").write_text(driver.page_source),
    print("Checkout header is visible")
    print("Ended test_06_Login transaction")

def test_07_EnterShippingInfo(driver):
    print("\nStarting test_07_EnterShippingInfo transaction")
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
    print("\nEnded test_07_EnterShippingInfo transaction")

def test_08_EnterPaymentInfo(driver):
    print("\nStarting test_08_EnterPaymentInfo transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_creditcard_fullname("Test User")
    checkout_page.enter_creditcard_number("1234123412341234")
    checkout_page.enter_creditcard_exp_date("03/28")
    checkout_page.enter_creditcard_security_code("123")
    checkout_page.click_review_order_button()
    assert checkout_page.two_tshirts_posttax_amount_visible(), "2 Tshirts posttax amount is not visible or correct"
    assert checkout_page.review_your_order_header_visible(), "Review your order header is not visible"
    print("Review your order header is visible")
    print("\nEnded test_08_EnterPaymentInfo transaction")

def test_09_PlaceOrder(driver):
    print("\nStarting test_09_PlaceOrder transaction")
    checkout_page = CheckoutPage(driver)
    checkout_page.click_place_order_button()
    assert checkout_page.checkout_complete_header_visible(),"Checkout Complete header is not visible"
    print("Ended test_09_PlaceOrder transaction")
    
def test_10_Cleanup(driver):
    print("\nStarting test_10_Cleanup transaction")
    checkout_page = CheckoutPage(driver)
    cart_page = CartPage(driver)
    product_page = ProductsPage(driver)
    menu_page = MenuPage(driver)
    login_page = LoginPage(driver)
    checkout_page.click_continue_shopping_button()
    product_page.click_shopping_cart_icon()
    cart_page.click_remove_item_button()
    assert cart_page.no_items_in_cart_visible(), "No items in cart is not visible"
    cart_page.click_go_shopping_button()
    product_page.click_more_icon()
    assert menu_page.mydemoapp_logo_visible(), "MyDemoApp logo is not viaible"
    menu_page.click_logout()
    assert login_page.header_visible(),"Login page header is not visible"
    print("Login header is visible")
    print("Ended test_10_Cleanup transaction")
