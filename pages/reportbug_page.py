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
        print("Will confirm that the header is visible")
        return self.is_visible(self.FEEDBACK_HEADER)
    
    def enter_email(self):
        print("Will click on Email field")
        email_field = self.find(self.FEEDBACK_FROM_FIELD)
        email_field.clear()
        print("Will enter email into the Email field")
        email_field.send_keys("brent.irmak@gmail.com")
        print("Email has been entered")

    def enter_message(self):
        print("Will click on the message field")
        email_message = self.find(self.FEEDBACK_FIELD)
        print("Will enter the message")
        email_message.send_keys("This is a test")
        print("Message has been entered")

    def click_send_button(self):
        print("Will click on the Send button")
        self.click(self.SEND_BUTTON)
        print("Clicked on the Send button")
        


    