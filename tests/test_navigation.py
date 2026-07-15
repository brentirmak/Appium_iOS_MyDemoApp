from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.webview_page import WebViewPage
from pages.login_page import LoginPage
from pages.about_page import AboutPage
from pages.products_page import ProductsPage
from pages.greenbackpack_page import GreenBackpackPage
from pages.cart_page import CartPage
from pages.reportbug_page import ReportBugPage


from utils.transaction_logger import execute_transaction


class TestNavigation:

    def test_webview_navigation(
            self,
            driver,
            mysql_logger):

        # Sequence/execution order
        home = HomePage(driver)
        menu = MenuPage(driver)
        webview = WebViewPage(driver)
        login = LoginPage(driver)
        about = AboutPage(driver)
        product = ProductsPage(driver)
        green_backpack = GreenBackpackPage(driver)
        cart = CartPage(driver)
        reportbug = ReportBugPage(driver)
        

        print("\nStarting test_01_open_menu transaction")
        execute_transaction(
            mysql_logger,
            "test_01_open_menu",
            home.open_menu
        )
        print("Ended test_01_open_menu transaction")

        print("\nStarting test_02_logout_menu_item_visible transaction")
        execute_transaction(
            mysql_logger,
            "test_02_logout_menu_item_visible",
            lambda: (
                menu.logout_visible()
                or (_ for _ in ()).throw(
                    AssertionError(
                        "Logout menu not visible"
                    )
                )
            )
        )
        print("Ended test_02_logout_menu_item_visible transaction")

        print("\nStarting test_03_navigate_to_webview transaction")
        
        execute_transaction(
            mysql_logger,
            "test_03_navigate_to_webview",
            menu.open_webview
        )
        print("Ended test_03_navigate_to_webview transaction")

        print("\nStarting test_04_webview_url_input_visible transaction")

        execute_transaction(
            mysql_logger,
            "test_04_webview_url_input_visible",
            lambda: (
                webview.url_field_visible()
                or (_ for _ in ()).throw(
                    AssertionError(
                        "URL field not visible"
                    )
                )
            )
        )

        print("Ended test_04_webview_url_input_visible transaction")

        print("\nStarting test_05_navigate_back transaction")

        execute_transaction(
            mysql_logger,
            "test_05_navigate_back",
            webview.navigate_back
        )

        print("Ended test_05_navigate_back transaction")

        print("\nStarting test_06_home_logo_visible transaction")

        execute_transaction(
            mysql_logger,
            "test_06_home_logo_visible",
            lambda: (
                home.logo_visible()
                or (_ for _ in ()).throw(
                    AssertionError(
                        "Home logo not visible"
                    )
                )
            )
        )

        print("Ended test_06_home_logo_visible transaction")

        print("\nStarting test_07_navigate_to_login_page transaction")

        execute_transaction(
            mysql_logger,
            "test_07_navigate_to_login_page",
            menu.click_login
        )

        print("Ended test_07_navigate_to_login_page transaction")

        print("\nStarting test_08_login_header_visible transaction")

        execute_transaction(
            mysql_logger,
            "test_08_login_header_visible",
            lambda: (
                login.header_visible()
                or (_ for _ in ()).throw(
                    AssertionError(
                        "Login header not visible"
                    )
                )
            )
        )

        print("Ended test_08_login_header_visible transaction")

        print("\nStarting test_09_login transaction")

        execute_transaction(
            mysql_logger,
            "test_09_login",
            lambda: (
                login.enter_username("visual@example.com"),
                login.enter_password("10203040"),
                login.click_login_button(),
                login.products_page_visible()               
            )
        )

        print("Ended test_09_login transaction")

        print("\nStarting test_10_click_about_page transaction")

        execute_transaction(
            mysql_logger,
            "test_10_click_about_page",
            lambda: (
                home.open_menu(),
                menu.click_about(),
                about.header_visible()
            )
        )

        print("Ended test_10_click_about_page transaction")

        print("\nStarting test_11_click_green_backpack_item transaction")

        execute_transaction(
            mysql_logger,
            "test_11_click_green_backpack_item",
            lambda: (
                home.click_catalog_icon(),
                product.click_green_backpack_product(),
                green_backpack.header_visible(),
                green_backpack.click_add_to_cart_button(),
                green_backpack.cart_with_one_item_visible(),
                product.click_shopping_cart_icon(),
                cart.header_visible(),
                cart.click_remove_item_button(),
                cart.no_items_in_cart_visible(),
                cart.click_go_shopping_button()
                #green_backpack.click_back_to_products_icon()
            )
        )

        print("Ended test_11_click_green_backpack_item transaction")

        
        print("\nStarting test_12_sort_product_by_ascending transaction")

        execute_transaction(
            mysql_logger,
            "test_12_sort_product_by_ascending",
            lambda: (
                home.click_sort_icon(),
                home.click_sort_by_ascending_option(),
            )
        )

        print("Ended test_12_sort_product_by_ascending transaction")

        print("\nStarting test_13_report_a_bug transaction")

        execute_transaction(
            mysql_logger,
            "test_13_report_a_bug",
            lambda: (
                home.open_menu(),
                menu.click_reportbug(),
                reportbug.enter_email(),
                reportbug.enter_mesage(),
                reportbug.click_send_button(),
                home.logo_visible()
            )
        )

        print("Ended test_13_report_a_bug transaction")
        