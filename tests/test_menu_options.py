from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.webview_page import WebViewPage
from pages.qrcodescanner_page import QRCodeScannerPage
from pages.geolocation_page import GeoLocationPage
from pages.drawing_page import DrawingPage
from pages.reportbug_page import ReportBugPage
from pages.reportbug_debug_page import ReportBugDebugPage
from pages.push_notifications_page import PushNotificationsPage
from pages.about_page import AboutPage
from pages.faceid_page import FaceIDPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.transaction_logger import execute_transaction
import time

class Test_Menu_Options:

    def test_webview_navigation(
            self,
            driver,
            mysql_logger):

        # Sequence/execution order
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        webview_page = WebViewPage(driver)
        qrcodescanner_page = QRCodeScannerPage(driver)
        geolocation_page = GeoLocationPage(driver)
        drawing_page = DrawingPage(driver)
        reportbug_page = ReportBugPage(driver)
        reportbug_debug_page = ReportBugDebugPage(driver)
        push_notifications_page = PushNotificationsPage(driver)
        about_page = AboutPage(driver)
        faceid_page = FaceIDPage(driver)
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)

        print("\nStarting test_01_webview_page transaction")

        execute_transaction(
            mysql_logger,
            "test_01_webview_page",
            lambda: (
                home_page.open_menu(),
                menu_page.mydemoapp_logo_visible(),
                menu_page.open_webview(),
                webview_page.url_field_visible(),
                webview_page.navigate_back(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_01_webview_page transaction")

        print("\nStarting test_02_qrcodescanner_page transaction")

        execute_transaction(
            mysql_logger,
            "test_02_qrcodescanner_page",
            lambda: (
                menu_page.click_qrcodescanner(),
                qrcodescanner_page.header_visible(),
                #qrcodescanner_page.click_do_not_allow_button(),
                #qrcodescanner_page.click_access_denied_ok_button(),
                qrcodescanner_page.click_back_button(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_02_qrcodescanner_page transaction")

        print("\nStarting test_03_geolocation_page transaction")

        execute_transaction(
            mysql_logger,
            "test_03_geolocation_page",
            lambda: (
                print(driver.page_source),
                home_page.open_menu(),
                menu_page.click_geo_location(),
                geolocation_page.header_visible(),
                webview_page.navigate_back(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_03_geolocation_page transaction")

        print("\nStarting test_04_drawing_page transaction")

        execute_transaction(
            mysql_logger,
            "test_04_drawing_page",
            lambda: (
                menu_page.click_drawing(),
                drawing_page.header_visible(),
                webview_page.navigate_back(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_04_drawing_page transaction")

        print("\nStarting test_05_reportbug_page transaction")

        execute_transaction(
            mysql_logger,
            "test_05_reportbug_page",
            lambda: (
                menu_page.click_reportbug(),
                reportbug_page.header_visible(),
                reportbug_page.click_cancel_icon(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_05_reportbug_page transaction")

        print("\nStarting test_06_reportbug_debug_page transaction")

        execute_transaction(
            mysql_logger,
            "test_06_reportbug_debug_page",
            lambda: (
                menu_page.click_reportbug_debug(),
                reportbug_debug_page.header_visible(),
                reportbug_debug_page.click_debug_back_icon(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_06_reportbug_debug_page transaction")

        print("\nStarting test_07_push_notifications_page transaction")

        execute_transaction(
            mysql_logger,
            "test_07_push_notifications_page",
            lambda: (
                menu_page.click_push_notifications(),
                push_notifications_page.header_visible(),
                push_notifications_page.click_back_icon(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_07_push_notifications_page transaction")

        print("\nStarting test_08_about_page transaction")

        execute_transaction(
            mysql_logger,
            "test_08_about_page",
            lambda: (
                menu_page.click_about(),
                about_page.header_visible(),
                about_page.click_about_back_icon(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_08_about_page transaction")

        print("\nStarting test_09_faceID_page transaction")

        execute_transaction(
            mysql_logger,
            "test_09_faceID_page",
            lambda: (
                menu_page.click_faceid(),
                faceid_page.header_visible(),
                faceid_page.click_faceid_back_icon(),
                menu_page.mydemoapp_logo_visible()
            )
        )

        print("Ended test_09_faceID_page transaction")

        print("\nStarting test_10_login_page transaction")

        execute_transaction(
            mysql_logger,
            "test_10_login_page",
            lambda: (
                menu_page.click_login(),
                login_page.header_visible(),
                login_page.enter_username("visual@example.com"),
                login_page.enter_password("10203040"),
                login_page.click_login_button(),
                products_page.products_header_visible()
            )
        )

        print("Ended test_10_login_page transaction")
    