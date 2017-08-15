# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest
from test import test_baidu
from test import test_youdao
from test import test_json
#构造测试集
suite = unittest.TestSuite()
suite.addTest(test_baidu.BaiduTest('test_baidu'))
suite.addTest(test_youdao.YoudaoTest('test_youdao'))
suite.addTest(test_json.MyTestSuite("test_image_match_001"))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)