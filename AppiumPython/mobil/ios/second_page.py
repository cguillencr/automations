from mobil.base_page import BasePage
from mobil.ios.first_page import FirstPage


class SecondPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_first_page(self):
        self.touch_element_by_xpath('//XCUIElementTypeButton[@name="First"]', 10)
        return FirstPage(self.driver)
