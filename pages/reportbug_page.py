from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ReportBugPage(BasePage):

    FEEDBACK_HEADER = (
        AppiumBy.XPATH,
        '//XCUIElementTypeStaticText[@name="Feedback"]'
    )

    FEEDBACK_FROM_FIELD = (
        AppiumBy.CLASS_NAME,
        'XCUIElementTypeTextField'
    )

    FEEDBACK_FIELD = (
        AppiumBy.CLASS_NAME,
        'XCUIElementTypeTextView'
    )

    SEND_BUTTON = (
        AppiumBy.XPATH,
        '//XCUIElementTypeButton[@name="Send"]'
    )

    def header_visible(self):
        return self.is_visible(self.FEEDBACK_HEADER)
    
    def enter_email(self):
        print("Will click on Email field")
        #self.click(self.FEEDBACK_FROM_FIELD)
        email_field = self.find(self.FEEDBACK_FROM_FIELD)
        email_field.clear()
        email_field.send_keys("brent.irmak@gmail.com")
        print("Clicked on Email field")

    def enter_message(self):
        email_message = self.find(self.FEEDBACK_FIELD)
        email_message.send_keys("This is a test")

    def click_send_button(self):
        self.click(self.SEND_BUTTON)
        


    