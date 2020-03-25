import pytest
from mobil.welcome_page import WelcomePage


@pytest.mark.usefixtures("driver_get")
class TestInvalidPromoCode:

    comic_detail_page = None

    @pytest.mark.dependency()
    def test_01_add_commic_to_cart(self):#search_name, commic_name):
        welcome_page = WelcomePage(self.driver)

        featured_page = welcome_page.tap_no_yet_link()

        search_page = featured_page.search("free")

        self.__class__.comic_detail_page = search_page.tap_result_with_name("Free")

        expected_synopsis = "Kayrin is the best student in the class, fulfills its tasks, has the best grades " \
                            "and 100% of frequency. With a future guaranteed ahead it begins to doubt that life " \
                            "after meeting a boy named Erick, who has quite peculiar philosophies but interesting " \
                            "about life time, so Kayrin will start to see things in a new way, but what kind of " \
                            "problems this new insight will bring?"
        assert self.comic_detail_page.synopsis() == expected_synopsis

        self.comic_detail_page.add_to_cart()

    @pytest.mark.dependency(depends=["TestInvalidPromoCode::test_01_add_commic_to_cart"])
    def test_02_add_invalid_promo_code(self):

        fake_promo_code = "Promo code"
        cart_page = self.comic_detail_page.tap_view_cart()
        cart_page.apply_promo_code(fake_promo_code)

        current_text = cart_page.is_text_displayed_by_id("ShoppingCartItemsAdapter_PromoGiftCodeErrorText", 20).strip()
        expected_error_message ="We\'re sorry. We do not recognize the code you entered. " \
                                "Please check the code and try again."
        assert current_text == expected_error_message