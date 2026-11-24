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
from utils.retry import retry_action
import time


def test_01_ProoductsLandingPage(driver):
    print("\nStarting test_01_ProoductsLandingPage transaction")
    home_page = HomePage(driver)
    menu_page = MenuPage(driver)
    home_page.open_menu()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_01_ProoductsLandingPage transaction")

def test_02_WebviewPage(driver):
    print("\nStarting test_02_WebviewPage transaction")
    menu_page = MenuPage(driver)
    webview_page = WebViewPage(driver)
    menu_page.open_webview()
    assert webview_page.url_field_visible(), "URL field is not visible"
    webview_page.navigate_back()
    menu_page.mydemoapp_logo_visible()
    print("\nEnded test_02_WebviewPage transaction")

def test_03_QRCodeScannerPage(driver):
    print("\nStarting test_03_QRCodeScannerPage transaction")
    menu_page = MenuPage(driver)
    qrcodescanner_page = QRCodeScannerPage(driver)
    menu_page.click_qrcodescanner()
    qrcodescanner_page.header_visible()
    qrcodescanner_page.click_back_button()
    menu_page.mydemoapp_logo_visible()
    print("\nEnded test_03_QRCodeScannerPage transaction")

def test_04_GeoLocationPage(driver):
    print("\nStarting test_04_GeoLocationPage transaction")
    home_page = HomePage(driver)
    menu_page = MenuPage(driver)
    geolocation_page = GeoLocationPage(driver)
    home_page.open_menu()
    menu_page.click_geo_location()
    geolocation_page.header_visible()
    time.sleep(2)
    geolocation_page.click_back_icon() 
    menu_page.mydemoapp_logo_visible()
    print("Checked for the logo being visible")
    menu_page.drawing_menu_item_visible()
    print("\nEnded test_04_GeoLocationPage transaction")

def test_05_DrawingPage(driver):
    print("\nStarting test_05_DrawingPage transaction")
    menu_page = MenuPage(driver)
    webview_page = WebViewPage(driver)
    drawing_page = DrawingPage(driver)
    menu_page.click_drawing()
    drawing_page.header_visible()
    webview_page.navigate_back()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_04_drawing_page transaction")

def test_06_ReportBugPage(driver):
    print("\nStarting test_06_ReportBugPage transaction")
    menu_page = MenuPage(driver)
    reportbug_page = ReportBugPage(driver)
    menu_page.click_reportbug()
    reportbug_page.header_visible()
    reportbug_page.click_cancel_icon()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_06_ReportBugPage transaction")

def test_07_ReportBugDebugPage(driver):
    print("\nStarting test_07_ReportBugDebugPage transaction")
    menu_page = MenuPage(driver)
    reportbug_debug_page = ReportBugDebugPage(driver)
    menu_page.click_reportbug_debug()
    reportbug_debug_page.header_visible()
    reportbug_debug_page.click_debug_back_icon()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_07_ReportBugDebugPage transaction")

def test_08_PushNotificationsPage(driver):
    print("\nStarting test_08_PushNotificationsPage transaction")
    menu_page = MenuPage(driver)
    push_notifications_page = PushNotificationsPage(driver)
    menu_page.click_push_notifications()
    push_notifications_page.header_visible()
    push_notifications_page.click_back_icon()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_08_PushNotificationsPage transaction")

def test_09_AboutPage(driver):
    print("\nStarting test_09_AboutPage transaction")
    menu_page = MenuPage(driver)
    about_page = AboutPage(driver)
    menu_page.click_about()
    about_page.header_visible()
    about_page.about_page_text_visible()
    about_page.click_about_back_icon()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_09_AboutPage transaction")

def test_10_FaceIDPage(driver):
    print("\nStarting test_10_FaceIDPage transaction")
    menu_page = MenuPage(driver)
    faceid_page = FaceIDPage(driver)
    menu_page.click_faceid()
    faceid_page.header_visible()
    faceid_page.click_faceid_back_icon()
    menu_page.mydemoapp_logo_visible()
    print("Ended test_10_FaceIDPage transaction")

def test_11_LoginPage(driver):
    print("\nStarting test_11_LoginPage transaction")
    menu_page = MenuPage(driver)
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    menu_page.click_login()
    login_page.header_visible()
    login_page.enter_username("visual@example.com")
    login_page.enter_password("10203040")
    login_page.click_login_button()
    products_page.products_header_visible()
