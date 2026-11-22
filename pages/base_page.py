import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    DEFAULT_TIMEOUT = 10

    # Element types where get_attribute("value") reflects the typed text,
    # so a post-typing verification is meaningful.
    TEXT_INPUT_TYPES = (
        "XCUIElementTypeTextField",
        "XCUIElementTypeSecureTextField",
        "XCUIElementTypeTextView",
    )

    # Static (non-input) elements a page can tap to dismiss the keyboard. In React
    # Native scroll views a tap outside the focused input dismisses the keyboard, and
    # unlike pressing Return it does not move focus to the next field. Pages override
    # this with locators for labels/headers that stay visible above the keyboard.
    KEYBOARD_DISMISS_TARGETS = ()

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
    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def wait_and_click(self, locator, timeout=DEFAULT_TIMEOUT):
        self.click(locator, timeout)

    def click_when_ready(self, locator, timeout=DEFAULT_TIMEOUT):
        """Click an element that may be off screen or behind the keyboard:
        wait for it to exist, clear the keyboard, bring it into view, then click."""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        if not element.is_displayed():
            self.hide_keyboard()
            self.bring_into_view(locator)
        wait.until(EC.element_to_be_clickable(locator)).click()

    # ---------------------------
    # Typing helpers (legacy - prefer fill())
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
    def is_visible(self, locator, timeout=10):
        """Conditional check. Returns True/False and NEVER raises.
        Do not use this as a test assertion - use assert_visible()."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def assert_visible(self, locator, timeout=DEFAULT_TIMEOUT, message=None):
        """Assertion. Raises AssertionError if the element is not visible in time."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(
                message or f"Element not visible after {timeout}s: {locator}"
            ) from None

    # ---------------------------
    # Keyboard helpers
    # ---------------------------
    def _keyboard_shown(self):
        """True/False, or None if the driver cannot tell."""
        try:
            return bool(self.driver.execute_script("mobile: isKeyboardShown"))
        except Exception:
            return None

    def hide_keyboard(self):
        """Dismiss the soft keyboard by tapping the first displayed element in
        KEYBOARD_DISMISS_TARGETS (one tap, no polling).

        mobile: isKeyboardShown is deliberately NOT consulted: in this app it kept
        reporting True after the keyboard was gone, and polling it cost 4-50 s per call.
        mobile: hideKeyboard is only a fallback for pages that define no targets (it
        fails on these keyboards). Pressing Return is avoided because it moves focus
        to the next field.
        """
        started = time.perf_counter()
        outcome = None

        for locator in self.KEYBOARD_DISMISS_TARGETS:
            try:
                targets = self.finds(locator)
                if targets and targets[0].is_displayed():
                    targets[0].click()
                    outcome = f"tapped ...{locator[1][-45:]}"
                    break
            except Exception:
                continue

        if outcome is None and not self.KEYBOARD_DISMISS_TARGETS:
            try:
                self.driver.execute_script("mobile: hideKeyboard")
                outcome = "mobile: hideKeyboard"
            except Exception as e:
                first_line = (str(e).splitlines() or [""])[0][:80]
                outcome = f"FAILED ({type(e).__name__}: {first_line})"

        if outcome is None:
            outcome = "no dismiss target displayed"

        print(f"hide_keyboard: {outcome} in {time.perf_counter() - started:.1f}s")

    # ---------------------------
    # Scrolling helpers
    # ---------------------------
    def scroll_into_view(self, element):
        """mobile: scroll toVisible. WebDriverAgent only supports this for table /
        collection cells, so it fails on plain containers; kept for cell-based screens."""
        try:
            self.driver.execute_script(
                "mobile: scroll", {"elementId": element.id, "toVisible": True}
            )
        except Exception as e:
            first_line = (str(e).splitlines() or [""])[0][:100]
            print(f"scroll_into_view: mobile: scroll failed ({type(e).__name__}: {first_line})")

    def reveal(self, locator, max_swipes=4):
        """Swipe the form's scroll view until the element is displayed.
        Direction is chosen by comparing the element to the scroll view's bounds."""
        for _ in range(max_swipes):
            try:
                element = self.find(locator)
                if element.is_displayed():
                    return True
                scroll_view = self.find((AppiumBy.XPATH, "//XCUIElementTypeScrollView"))
                sv, el = scroll_view.rect, element.rect
                if el["y"] + el["height"] <= sv["y"]:
                    direction = "down"   # element is above the viewport
                else:
                    direction = "up"     # element is below the viewport
                self.driver.execute_script(
                    "mobile: swipe", {"elementId": scroll_view.id, "direction": direction}
                )
            except Exception as e:
                first_line = (str(e).splitlines() or [""])[0][:100]
                print(f"reveal: {type(e).__name__}: {first_line}")
                return False
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def bring_into_view(self, locator):
        """Make an element displayed by swiping its scroll view if necessary."""
        try:
            if self.find(locator).is_displayed():
                return True
        except Exception:
            pass
        return self.reveal(locator)

    # ---------------------------
    # Verified text entry
    # ---------------------------
    @staticmethod
    def _normalize(text):
        # Ignore masking/formatting differences (spaces, dashes, slashes, '#')
        return "".join(ch for ch in (text or "") if ch.isalnum())

    @staticmethod
    def _clear(element):
        try:
            element.clear()
        except Exception:
            current = element.get_attribute("value") or ""
            if current:
                element.send_keys("\b" * len(current))

    def _diagnose(self, locator):
        """Say why a field could not be used, for the failure message."""
        try:
            matches = self.finds(locator)
            if not matches:
                return "element is not in the UI tree"
            element = matches[0]
            info = f"{len(matches)} match(es), displayed={element.is_displayed()}, rect={element.rect}"
            try:
                info += f", window={self.driver.get_window_size()}"
            except Exception:
                pass
            info += f", keyboard_shown={self._keyboard_shown()}"
            return info
        except Exception as e:
            return f"could not inspect: {type(e).__name__}"

    def fill(self, locator, value, name=None, timeout=DEFAULT_TIMEOUT,
             retries=3, verify=True, dismiss_keyboard=True):
        """Focus a field, clear it, type, and confirm the field holds the value.

        Raises AssertionError if the value cannot be set after `retries` attempts,
        so a failure surfaces at the field that caused it instead of several
        steps later. Use verify=False for secure fields (the value is masked).
        """
        label = name or str(locator[1])
        wait = WebDriverWait(self.driver, timeout)
        last_problem = None

        for attempt in range(1, retries + 1):
            try:
                # 1. The element only has to exist at first; it may be off screen or
                #    covered by the keyboard, which makes it "not clickable" yet.
                element = wait.until(EC.presence_of_element_located(locator))

                # 2. If it is not displayed, clear the keyboard and bring it into view.
                if attempt > 1 or not element.is_displayed():
                    self.hide_keyboard()
                    self.bring_into_view(locator)

                # 3. Now require that it can actually be tapped.
                element = wait.until(EC.element_to_be_clickable(locator))
                element.click()
                self._clear(element)
                element.send_keys(value)

                # Leave the keyboard down so the next field starts from a known state
                if dismiss_keyboard:
                    self.hide_keyboard()

                if not verify:
                    return element

                element_type = element.get_attribute("type")
                if element_type not in self.TEXT_INPUT_TYPES:
                    print(f"WARNING: '{label}' locator resolves to {element_type}, "
                          f"not a text field - cannot verify the typed value. "
                          f"Switch to a locator for the actual text field.")
                    return element

                actual = element.get_attribute("value")
                if self._normalize(actual) == self._normalize(value):
                    return element
                last_problem = f"expected {value!r} but field shows {actual!r}"

            except (TimeoutException, StaleElementReferenceException,
                    NoSuchElementException, ElementNotInteractableException) as e:
                last_problem = f"{type(e).__name__} ({self._diagnose(locator)})"

            print(f"fill('{label}') attempt {attempt}/{retries} failed: {last_problem}")

        raise AssertionError(f"Could not set '{label}': {last_problem}")

    # ---------------------------
    # Context switching (manual only)
    # ---------------------------
    def switch_to_native(self):
        self.driver.switch_to.context("NATIVE_APP")