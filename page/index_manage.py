#coding: utf-8
#author = hewangtong
#date = 2020/10/18
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage


class IndexManage(BasePage):
    """档案管理PO"""

    def goto_serach(self):
        """
        搜索
        :return:
        """
        # self.find(By.CSS_SELECTOR, "#root input").send_keys("会计凭证")
        self._driver.find_element(By.CSS_SELECTOR, "#root input").send_keys("会计凭证")
        return True



