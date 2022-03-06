from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/"

    def __init__(self, driver:WebDriver = None):
        '''
        initialize driver
        :param driver:
        '''
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(self._BASE_URL)
        else:
            self.driver = driver

    def do_click(self, by:By, locator:str):
        self.driver.find_element(by, locator).click()

    def do_send_keys(self, value:str, by:By, locator:str):
        element = self.driver.find_element(by, locator)
        element.clear()
        element.send_keys(value)

    def do_find_element(self, by:By, locator:str):
        return self.driver.find_element(by, locator)

    def do_wait_element(self, time:int, rule:EC, locator:(By, str)):
        '''
        wait for certain element and return it
        :param time: explicit wait time
        :param rule: expected condition
        :param locator: element locator tuple (By, value)
        :return:
        '''
        wait = WebDriverWait(self.driver, time)
        return wait.until(rule(locator))

    def scroll_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')