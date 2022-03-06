from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class ProductCommentPage(BasePage):
    _BUTTON_FIRST_PRODUCT_REPLY = (By.XPATH, "//span[contains(text(),'回复')][1]/..")
    _BUTTON_FIRST_PRODUCT_DELETE = (By.XPATH, "//span[contains(text(),'删除')][1]/..")
    _FORM_COMMENT_INPUT = (By.CSS_SELECTOR, ".el-dialog__body textarea")
    _BUTTON_COMMENT_SAVE = (By.CSS_SELECTOR, ".el-dialog__footer button.el-button--primary")
    _TOAST_STATUS = (By.CLASS_NAME, "el-notification__title")

    def reply_first_comment(self):
        reply_button = self.do_wait_element(10, EC.element_to_be_clickable, self._BUTTON_FIRST_PRODUCT_REPLY)
        reply_button.click()
        self.do_send_keys("comment received", *self._FORM_COMMENT_INPUT)
        self.do_click(*self._BUTTON_COMMENT_SAVE)

        toast = self.do_wait_element(10, EC.visibility_of_element_located, self._TOAST_STATUS)
        return toast.text

    def delete_first_comment(self):
        delete_button = self.do_wait_element(10, EC.element_to_be_clickable, self._BUTTON_FIRST_PRODUCT_DELETE)
        delete_button.click()

        toast = self.do_wait_element(10, EC.visibility_of_element_located, self._TOAST_STATUS)
        return toast.text