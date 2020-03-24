from mobil.base_page import BasePage
from mobil.featured_page import FeaturedPage


class WelcomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tap_no_yet_link(self):
        self.touch_element_by_id("not_yet", 10)
        return FeaturedPage(self.driver)
