#coding=utf-8
from HTMLTestRunner  import HTMLTestRunner
import unittest

if __name__ =='__main__':
    testunit=unittest.TestSuite()
    fp=open('result.html','wb')
    runner=HTMLTestRunner (stream=fp,
                           title= '讯代理测试',
                           description= '用例执行情况：')
    discover=unittest.defaultTestLoader.discover('E:\\porttest\\yongli',pattern='*_test.py')
    runner.run(discover)
    fp.close()