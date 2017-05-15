import unittest
import requests

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.url='http://test.xdaili.cn:10005/ipagent/user/register'
        self.h={
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        'Host': 'www.xdaili.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
         }

    def test_null(self):
        '''所有参数为空'''
        params = {'mobile':'','password':'','validatacode':''}
        r = requests.get(self.url,params=params,headers=self.h)
        self.result =r.json()
        # print(r.text)
        # print(r.status_code)
        self.assertEqual(self.result['msg'],'手机号不能为空！')

    def test_password_null(self):
        '''密码为空'''
        params = {'mobile':'18329176957','password':'','validatacode':''}
        r = requests.get(self.url,params=params,headers=self.h)
        self.result = r.json()
        self.assertEqual(self.result['msg'],'密码不能为空！')

    def test_mobile_error(self):
        '''手机号码错误'''
        params = {'mobile':'1111@o11','password':'','validatacode':''}
        r =requests.get(self.url,params=params,headers=self.h)
        self.result = r.json()
        self.assertEqual(self.result['msg'],'请输入正确的手机号！')


if __name__=='__main__':
    # unittest.main()
    test_cases = unittest.TestLoader().loadTestsFromTestCase( LoginTest)
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    print('testsRun:%s'%test_result.testsRun)
    print('failures:%s'%len(test_result.failures))
    print('error:%s'%len(test_result.errors))
    print('skipped:%s'%len(test_result.skipped))