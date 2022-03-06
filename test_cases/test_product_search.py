import pytest

from page_objects.login_page import LoginPage


class TestProductSearch():

    @pytest.mark.parametrize("input_id", ["1181044"])
    def test_search_by_id(self, input_id):
        product_id = LoginPage().login().go_to_product_list().input_search_id(input_id).search().get_product_id()
        assert product_id == input_id

    @pytest.mark.parametrize("input_code", ["1234567890"])
    def test_search_by_code(self, input_code):
        product_code = LoginPage().login().go_to_product_list()\
            .input_seach_code(input_code).search().expand_first_product().get_product_code()
        assert product_code == input_code

    @pytest.mark.parametrize("input_name", ["Hogwarts666"])
    def test_search_by_name(self, input_name):
        product_name = LoginPage().login().go_to_product_list().input_search_name(input_name).search().get_product_name()
        assert product_name == input_name
