from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            # 在命令窗口中执行chrome --remote-debugging-port=8888 ， 启动指定调试端口的浏览器，在代码中指定开放的端口，即可复用浏览器，不用重复打开新浏览器
            chrome_options = Options()
            chrome_options.debugger_address = '127.0.0.1:8888'
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, condition):
        WebDriverWait(self._driver, 10).until(condition)
