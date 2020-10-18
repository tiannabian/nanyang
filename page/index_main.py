#coding: utf-8
#author = hewangtong
#date = 2020/10/18
from page.basepage import BasePage
from selenium.webdriver.common.by import By

from page.index_manage import IndexManage

class IndexMain(BasePage):
    """首页PO"""

    def goto_manage(self):
        """
        档案管理页面
        :return:
        """
        #self.find(By.CSS_SELECTOR, "[class='menu-item-icon']")
        self._driver.find_element(By.CSS_SELECTOR, "[class='menu-item-icon']")
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
