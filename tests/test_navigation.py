from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.webview_page import WebViewPage
from pages.login_page import LoginPage
from pages.about_page import AboutPage


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
        

        execute_transaction(
            mysql_logger,
            "test_01_open_menu",
            home.open_menu
        )

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

        execute_transaction(
            mysql_logger,
            "test_03_navigate_to_webview",
            menu.open_webview
        )

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

        execute_transaction(
            mysql_logger,
            "test_05_navigate_back",
            webview.navigate_back
        )

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

        execute_transaction(
            mysql_logger,
            "test_07_navigate_to_login_page",
            menu.click_login
        )

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

        execute_transaction(
            mysql_logger,
            "test_10_click_about_page",
            lambda: (
                home.open_menu(),
                menu.click_about(),
                about.header_visible()
            )
        )
    