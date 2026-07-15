from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    # ---------------------------
    # Core element lookup
    # ---------------------------
    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    # ---------------------------
    # Wait helpers
    # ---------------------------
    def wait_for_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # ---------------------------
    # Click helpers
    # ---------------------------
    def click(self, locator):
        self.wait_for_clickable(locator)
        self.driver.find_element(*locator).click()

    def wait_and_click(self, locator):
        el = self.wait_for_clickable(locator)
        el.click()

    # ---------------------------
    # Typing helpers
    # ---------------------------
    def type(self, locator, value):
        el = self.wait_for_visible(locator)
        el.send_keys(value)

    def clear_and_type(self, locator, value):
        el = self.wait_for_visible(locator)
        el.clear()
        el.send_keys(value)

    def safe_send_keys(self, locator, value):
        el = self.wait_for_visible(locator)
        try:
            el.clear()
        except Exception:
            el.send_keys("\b" * 50)
        el.send_keys(value)

    # ---------------------------
    # Visibility checks
    # ---------------------------
    def is_visible(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except Exception:
            return False

    # ---------------------------
    # Context switching (manual only)
    # ---------------------------
    def switch_to_native(self):
        self.driver.switch_to.context("NATIVE_APP")
