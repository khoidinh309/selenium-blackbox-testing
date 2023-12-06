# base.py

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
