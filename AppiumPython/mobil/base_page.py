from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_text_displayed_by_id(self, id, time):
        text = self.__find_element(MobileBy.ID, id, time).text
        print(text)
        return text

    def touch_element_by_xpath(self, xpath, time):
        element = self.__find_element(MobileBy.XPATH, xpath, time)
        element.click()

    def touch_element_by_id(self, id, time):
        element = self.__find_element(MobileBy.ID, id, time)
        element.click()

    def fill_text_by_id(self, id, text, time):
        text_field = self.__find_element(MobileBy.ID, id, time)
        text_field.send_keys(text)

    def __wait_for_element_located(self, selector, value_to_search, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((selector, value_to_search)))

    def __find_element(self, selector, value_to_search, time):
        self.__wait_for_element_located(selector, value_to_search, time)
        return self.driver.find_element(selector, value_to_search)