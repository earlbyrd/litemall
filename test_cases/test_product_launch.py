from page_objects.login_page import LoginPage


class TestProductLaunch():

    def test_product_launch(self):
        name = LoginPage().login().go_to_product_lunch().product_launch().get_product_name()
        assert  name == "Hogwarts666"

