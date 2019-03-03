#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/6.


import requests

url_get = 'https://www.baidu.com'
url_post = 'http://platform-test.tclclouds.com/api/v1/config/keys'
params_from = {'keys':'ad_drawer_small_card_pos|ad_search_main_page_pos|ad_boost_result_pos|ad_left_screen_pos_one|ad_left_screen_pos_two',
               'country':'US','model':'6045K','pkg':'com.tct.launcher','sign':'605390a6339d26fa5a17fc5cbb94b8cd'}

def http_get(url):
    """
        get
    :param url:
    :return:
    """
    response = requests.get(url=url)
    print(response.text)
    print(url)
    print(response.status_code)


def http_post_from(url, params):
    """
        表单提交
    :param url:
    :param params:
    :return:
    """
    response = requests.post(url,params)
    print(response.text)
    print(url)
    print(response.status_code)


def http_post_json(url, params):
    """
        json 串提交
    :param url:
    :param params:
    :return:
    """
    response = requests.post(url, params)
    print(response.text)
    print(response.url)
    print(response.status_code)

if __name__ == '__main__':
    # http_get(url=url_get)
    http_post_from(url_post,params_from)
