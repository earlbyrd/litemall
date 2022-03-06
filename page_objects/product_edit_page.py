from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class ProductEditPage(BasePage):

    _INPUT_PRODUCT_NAME = (By.XPATH, "//label[@for='name']/../div/div/input")
    _BUTTON_SAVE = (By.XPATH, "//div[@class='op-container']//span[contains(text(), '更新商品')]")

    def edit_product_name(self, name):
        element = self.do_wait_element(10, EC.element_to_be_clickable, self._INPUT_PRODUCT_NAME)
        element.clear()
        element.send_keys(name)
        self.scroll_to_bottom()
        self.do_click(*self._BUTTON_SAVE)
        from page_objects.product_list_page import ProductListPage
        return ProductListPage(self.driver)