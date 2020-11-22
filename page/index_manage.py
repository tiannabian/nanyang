#coding: utf-8
#author = hewangtong
#date = 2020/10/18
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.basepage import BasePage


class IndexManage(BasePage):
    """档案管理PO"""
    _base_url = "https://idoc.yonyoucloud.com/Archives"
    def goto_search(self):
        """
        搜索
        :return:
        """
        # self.find(By.CSS_SELECTOR, "#root input").send_keys("会计凭证")
        print('003')
        self._driver.find_element(By.XPATH, "//*[@id='main-wrap']/div[2]/div/div/div/div[1]/div/div[1]/span/input").send_keys("会计凭证")
        print('004')
        return True



