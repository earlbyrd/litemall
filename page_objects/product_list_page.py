from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class ProductListPage(BasePage):
    _TEXT_PRODUCT_NAME = (By.XPATH, "//tbody/tr[1]/td[3]/div")
    _TEXT_PRODUCT_CODE = (By.XPATH, "//tbody/tr[1]/td[2]/div")
    _INPUT_SEARCH_PRODUCT_ID = (By.XPATH, "//input[@placeholder='请输入商品ID']")
    _INPUT_SEARCH_PRODUCT_CODE = (By.XPATH, "//input[@placeholder='请输入商品编号']")
    _INPUT_SEARCH_PRODUCT_NAME = (By.XPATH, "//input[@placeholder='请输入商品名称']")
    _BUTTON_SEARCH = (By.XPATH, "//i[@class='el-icon-search']/..")
    _DIV_FIRST_PRODUCT_EXPAND = (By.XPATH, "//div[@class='el-table__expand-icon'][1]")
    _SPAN_EXPANDED_PRODUCT_CODE = (By.XPATH, "//label[contains(text(),'商品编号')]/../div/span")
    _BUTTON_FIRST_PRODUCT_EDIT = (By.XPATH, "//span[contains(text(),'编辑')][1]/..")


    def get_product_name(self):
        element = self.do_wait_element(10, EC.visibility_of_element_located, self._TEXT_PRODUCT_NAME)
        return element.text

    def get_product_id(self):
        element = self.do_wait_element(10, EC.visibility_of_element_located, self._TEXT_PRODUCT_CODE)
        return element.text

    def get_product_code(self):
        element = self.do_wait_element(10, EC.visibility_of_element_located, self._SPAN_EXPANDED_PRODUCT_CODE)
        return element.text

    def input_search_id(self, id):
        self.do_send_keys(id, *self._INPUT_SEARCH_PRODUCT_ID)
        return self

    def input_seach_code(self, code):
        self.do_send_keys(code, *self._INPUT_SEARCH_PRODUCT_CODE)
        return self

    def input_search_name(self, name):
        self.do_send_keys(name, *self._INPUT_SEARCH_PRODUCT_NAME)
        return self

    def search(self):
        self.do_click(*self._BUTTON_SEARCH)
        return self

    def expand_first_product(self):
        self.do_click(*self._DIV_FIRST_PRODUCT_EXPAND)
        return self

    def edit_first_product(self):
        self.do_click(*self._BUTTON_FIRST_PRODUCT_EDIT)
        from page_objects.product_edit_page import ProductEditPage
        return ProductEditPage(self.driver)