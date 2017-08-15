#!/usr/bin/env python
#coding: utf-8
'''
unittest interface
@author: zhang_jin
@version: 1.0
@see:http://www.python-requests.org/en/master/
'''

import unittest
import json
#import traceback
import requests
#import time
#import result_statistics
#import config as cf
#from com_logger import  match_Logger


class ZhiLuApiTest(unittest.TestCase):
    
    submitToken = ''
    userToken = ''
    """docstring for MyTestSuite"""
    #@classmethod
    def sedUp(self):

        print "start..."
         
    #login test case
    def test_login(self):
        url = "http://apptest.e-zhilu.com:80/login/login"
        querystring = json.dumps({
            "phoneNo":"18701082122",
            "smsCode":"111111",
        })

        headers = {
            'Content-Type': "application/json;charset=UTF-8",
            'OPERATOR_TOKEN':self.userToken,
            'Submit_token': self.submitToken
        }


        response = requests.request("POST", url, headers=headers, data=querystring)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            results = json.loads(response.text)
            print 'results=', json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
            self.submitToken = results['result']['submitToken']
            self.userToken = results['result']['userToken']
            resultType = results['resultType']
            self.assertEqual(resultType, u'SUCCESS', resultType)
            print 'userTokn=', self.userToken, 'submitToken=', self.submitToken
            #预期结果与实际结果校验，调用result_statistics模块
            #result_statistics.test_result(results,196)
        else:
            print "http error info:%s" %response.status_code

        #match_Logger.info("start image_query22222")
        #self.assertEqual(results['total'], 888)

        '''
        try:
            self.assertEqual(results['total'], 888)
        except:
            match_Logger.error(traceback.format_exc())
        #print results['total']
        '''

    #文字匹配数据统计
    def test_charging(self):

        text_url = "http://apptest.e-zhilu.com:80/apppay/unifiedorder"

        querystring = {
            "chargeType":"1",
            "phoneNo":"18701082122",
            "chargeMoney":"100",
            "moneyPay":"100",
            "balancePay":"0",
            "payType":"1",
            "ip":"10.4.98.23"
        }
        headers = {
            'Content-Type': "application/json;charset=UTF-8",
            'OPERATOR_TOKEN':self.userToken,
            'Submit_token': self.submitToken
        }
        print 'userTokn=', self.userToken, 'submitToken=', self.submitToken
        response = requests.request("POST", text_url, headers=headers, data=querystring)

        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            results = json.loads(response.text)
            print 'results=', json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
            #预期结果与实际结果校验，调用result_statistics模块
            #result_statistics.test_result(results,190)
            resultType = results['resultType']
            self.assertEqual(resultType, u'SUCCESS', resultType)
        else:
            print "http error info:%s" %response.status_code

        #print(response.text)

    def tearDown(self): 
        pass

if __name__ == '__main__':
    #image_match_Logger = ALogger('image_match', log_level='INFO')

    #构造测试集合
    suite=unittest.TestSuite()
    suite.addTest(ZhiLuApiTest("test_login"))
    suite.addTest(ZhiLuApiTest("test_charging"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #print "success case:",result_statistics.num_success
    #print "fail case:",result_statistics.num_fail
    #unittest.main()