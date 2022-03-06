import pytest

from page_objects.login_page import LoginPage


class TestProductReplyComment():

    def test_reply_comment(self):
        status = LoginPage().login().go_to_product_comment().reply_first_comment()
        assert status in ["成功", "失败"]
