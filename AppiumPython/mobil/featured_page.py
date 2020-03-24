from mobil.base_page import BasePage
from mobil.search_page import SearchPage


class FeaturedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_search_button(self):
        #self.click_element(*HomeLocators.SOME_BUTTON)
        self.touch_element_by_id("StoreMenu_search", 10)

    def search(self, text_to_search):
        self.tap_search_button()
        self.fill_text_by_id("search_src_text", text_to_search, 10)
        self.driver.press_keycode(66);  # Enter
        return SearchPage(self.driver)