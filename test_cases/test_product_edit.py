import pytest

from page_objects.login_page import LoginPage


class TestProductEdit():

    @pytest.mark.parametrize("new_name", ["Hogwarts777"])
    def test_edit_product(self, new_name):
        name = LoginPage().login().go_to_product_list().edit_first_product().edit_product_name(new_name).get_product_name()
        assert  name == new_name

