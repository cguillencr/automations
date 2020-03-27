import pytest
from mobil.ios.first_page import FirstPage


@pytest.mark.usefixtures("driver_ios_get")
class TestBasicClick:

    @pytest.mark.dependency()
    def test_01_add_commic_to_cart(self):

        first_page = FirstPage(self.driver)
        first_page.button_text()

        currentButtonText = first_page.button_text()

        first_page.tap_second_page()

        second_page = first_page.tap_second_page()

        first_page2 = second_page.tap_first_page()

        currentButtonText2 = first_page2.button_text()

        assert currentButtonText == currentButtonText2