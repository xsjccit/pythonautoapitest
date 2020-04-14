# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/29
@Author  : xushanjun
@Site    : minivision
@File    : base_request.py
@Software: PyCharm
@Theme   : request方法封装
"""
import sys
import os
import configparser
import requests
import json
from UtilApi.handle_cookie import write_cookie
from UtilApi.handle_json import get_value
from UtilApi.handle_init import handle_ini

# 获取当前文件路径
# project_path = os.getcwd() # 获取文件所在目录
base_path = "D:/python_learning/StarRingCloud_Project_Master"
sys.path.append(base_path)

# 定义封装类，外部统一调用
class BaseRequest:
    def send_post(self, url, data, cookie=None, get_cookie=None, header=None):
        """
        发送post请求
        """
        response = requests.post(url=url, data=data, cookies=cookie, headers=header)
        if get_cookie != None:
            """
            {"is_cookie":"app"}
            """
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res
    
    def send_get(self, url, data, cookie=None, get_cookie=None, header=None):
        """
        发送get请求
        """
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res
    
    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None):
        """
        执行方法，传递method、url、data参数
        """
        # return get_value(url)
        base_url = handle_ini.get_value('server_host')
        if 'http' not in url:
            url = base_url+url
        
        if method == 'get':
            res = self.send_get(url, data, cookie, get_cookie, header)
        else:
            res = self.send_post(url, data, cookie, get_cookie, header)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        print("用例执行返回结果—--->", res)
        return res

# 实例化对象（外部调用）
request = BaseRequest()

# if __name__ == "__main__":
#     request = BaseRequest()
#     request.run_main('get', 'http://www.baidu.com/login', "{'username':'11111'}")