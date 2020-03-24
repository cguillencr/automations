from mobil.base_page import BasePage
from mobil.cart_page import CartPage


class ComicDetailPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def synopsis(self):
        return self.is_text_displayed_by_id("synopsis", 20)

    def add_to_cart(self):
        self.touch_element_by_xpath("//*[@text='$0.99']", 10)

    def tap_view_cart(self):
        self.touch_element_by_xpath("//*[@text='VIEW CART']", 30)
        return CartPage(self.driver)