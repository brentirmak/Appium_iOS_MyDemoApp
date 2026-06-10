class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def is_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()