from mobil.base_page import BasePage
from mobil.ios.second_page import SecondPage


class FirstPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def button_text(self):
        return self.is_text_displayed_by_xpath('//XCUIElementTypeStaticText[@name="My Button"]', 10)

    def tap_second_page(self):
        self.touch_element_by_xpath('//XCUIElementTypeButton[@name="Second"]', 10)
        return SecondPage(self.driver)
