# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test.py  
   Description :  
   Author :       JHao
   date：          2017/3/7
-------------------------------------------------
   Change Activity:
                   2017/3/7: 
-------------------------------------------------
"""
__author__ = 'JHao'

from util.validators import validators

from test import testConfigHandler
from test import testLogHandler
from test import testDbClient

if __name__ == '__main__':
    # print("ConfigHandler:")
    # testConfigHandler.testConfig()

    # print("LogHandler:")
    # testLogHandler.testLogHandler()

    # print("DbClient:")
    # testDbClient.testDbClient()
    proxy = '139.196.218.89:3128'
    for func in validators:
        if not func(proxy):
            print('False')