from mobil.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def apply_promo_code(self, promo_code):
        self.fill_text_by_id("ShoppingCartItemsAdapter_PromoGiftCodeEditText", promo_code, 10)
        self.touch_element_by_xpath("//*[@text='APPLY']", 10)
