from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class WebViewPage(BasePage):

    URL_FIELD = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Enter an https URL"]'
    )

    BACK_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "More-tab-item"
    )

    #BACK_BUTTON = (
    #    AppiumBy.XPATH,
    #    "//XCUIElementTypeOther[@name=\"Webview-screen\"]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[@name=\"More\"]"
    #)


    def url_field_visible(self):
        print("Will check that the URL field is visible")
        return self.is_visible(self.URL_FIELD)

    def navigate_back(self):
        print("Will click on the Back button")

        # Switch back to native before clicking
        self.switch_to_native()

        self.click(self.BACK_BUTTON)
        print("Clicked on the Back button")

    # ---------------------------------------------------------
    # Correct WebView context switching
    # ---------------------------------------------------------
    def wait_for_webview_context(self, timeout=15):
        """
        Wait until a WEBVIEW context appears, then switch into it.
        This is required because hybrid apps load WebViews asynchronously.
        """
        for _ in range(timeout):
            contexts = self.driver.contexts
            print("Current contexts:", contexts)

            for ctx in contexts:
                if "WEBVIEW" in ctx:
                    print("Switching to:", ctx)
                    self.driver.switch_to.context(ctx)
                    return ctx

            time.sleep(1)

        raise Exception("WEBVIEW context did not appear within timeout")

    def switch_to_webview(self):
        """
        Explicit switch — only call this inside WebViewPage methods.
        """
        return self.wait_for_webview_context()

    def switch_to_native(self):
        self.driver.switch_to.context("NATIVE_APP")
