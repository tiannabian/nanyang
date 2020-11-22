#coding: utf-8
#author = hewangtong
#date = 2020/10/18
from page.index_main import IndexMain
from page.index_manage import IndexManage


class TestSearch:

    def setup(self):
        self.index_main = IndexMain()

    def test_search(self):
        """
        测试搜索
        :return:
        """
        #print("123")
        self.index_main.goto_manage().goto_search()