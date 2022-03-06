from page_objects.login_page import LoginPage


class TestProductDeleteComment():

    def test_delete_comment(self):
        status = LoginPage().login().go_to_product_comment().delete_first_comment()
        assert status == "成功"
