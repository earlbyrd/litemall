from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    _INPUT_USERNAME = (By.XPATH, "//*[@name='username']")
    _INPUT_PASSWORD = (By.XPATH, "//*[@name='password']")
    _BUTTON_LOGIN = (By.CSS_SELECTOR, "button.el-button")

    def login(self):

        self.do_send_keys("admin123", *self._INPUT_USERNAME)
        self.do_send_keys("admin123", *self._INPUT_PASSWORD)
        self.do_click(*self._BUTTON_LOGIN)

        from page_objects.home_page import HomePage
        return HomePage(self.driver)
