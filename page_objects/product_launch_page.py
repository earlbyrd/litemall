from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class ProductLaunchPage(BasePage):

    _INPUT_PRODUCT_CODE = (By.XPATH, "//label[@for='goodsSn']/../div/div/input")
    _INPUT_PRODUCT_NAME = (By.XPATH, "//label[@for='name']/../div/div/input")
    _INPUT_PRODUCT_PRICE = (By.XPATH, "//label[@for='counterPrice']/../div/div/input")
    _RADIO_HOT = (By.XPATH, "//span[contains(text(), '热卖')]")
    _BUTTON_LAUNCH = (By.XPATH, "//div[@class='op-container']//span[contains(text(), '上架')]")

    def product_launch(self):
        self.do_send_keys('1234567890', *self._INPUT_PRODUCT_CODE)
        self.do_send_keys('Hogwarts666', *self._INPUT_PRODUCT_NAME)
        self.do_send_keys('666', *self._INPUT_PRODUCT_PRICE)
        self.do_click(*self._RADIO_HOT)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        self.do_click(*self._BUTTON_LAUNCH)

        from page_objects.product_list_page import ProductListPage
        return ProductListPage(self.driver)