from mobil.base_page import BasePage
from mobil.comic_detail_page import ComicDetailPage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_result_with_name(self, text_to_search):
        self.touch_element_by_xpath("//*[@text='"+text_to_search+"']", 20)
        return ComicDetailPage(self.driver)
