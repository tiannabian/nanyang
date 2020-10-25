#coding: utf-8
#author = hewangtong
#date = 2020/10/18
from time import sleep

from page.basepage import BasePage
from selenium.webdriver.common.by import By

from page.index_manage import IndexManage

class IndexMain(BasePage):
    """首页PO"""
    _base_url = "https://idocpreprod.yonyoucloud.com/"

    def goto_manage(self):
        """
        档案管理页面
        :return:
        """
        sleep(3)
        #self.find(By.CSS_SELECTOR, "[class='menu-item-icon']")  /html/body/div/div/div[2]/div/div/div[1]/div/div[1]/div/p
        print('001')
        self._driver.find_element(By.XPATH, "//*[@id='main-wrap']/div[2]/div/div/div[1]/div/div[1]/div/p")
        print('002')
        sleep(3)
        return IndexManage(self._driver)

    def goto_query(self):
        """
        档案查询页面
        :return:
        """
        pass

    def goto_displayboard(self):
        """
        统计展板页面
        :return:
        """
        pass

    def goto_borrow(self):
        """
        档案借阅页面
        :return:
        """
        pass

    def goto_applicationtransfer(self):
        """
        移交申请页面
        :return:
        """
        pass

    def goto_borrowfrom(self):
        """
        档案外借页面
        :return:
        """
        pass

    def goto_processmanage(self):
        """
        流程管理页面
        :return:
        """
        pass
