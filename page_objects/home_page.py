from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):

    _MENU_PRODUCT_MANAGE = (By.XPATH, "//span[contains(text(), '商品管理')]")
    _MENU_PRODUCT_LIST = (By.XPATH, "//span[contains(text(), '商品列表')]")
    _MENU_PRODUCT_LAUNCH = (By.XPATH, "//span[contains(text(), '商品上架')]")
    _MENU_PRODUCT_COMMENT = (By.XPATH, "//span[contains(text(), '商品评论')]")

    def go_to_product_launch(self):
        self.do_click(*self._MENU_PRODUCT_MANAGE)
        self.do_click(*self._MENU_PRODUCT_LAUNCH)

        from page_objects.product_launch_page import ProductLaunchPage
        return ProductLaunchPage(self.driver)

    def go_to_product_list(self):
        self.do_click(*self._MENU_PRODUCT_MANAGE)
        self.do_click(*self._MENU_PRODUCT_LIST)

        from page_objects.product_list_page import ProductListPage
        return ProductListPage(self.driver)

    def go_to_product_comment(self):
        self.do_click(*self._MENU_PRODUCT_MANAGE)
        self.do_click(*self._MENU_PRODUCT_COMMENT)

        from page_objects.product_comment_page import ProductCommentPage
        return ProductCommentPage(self.driver)