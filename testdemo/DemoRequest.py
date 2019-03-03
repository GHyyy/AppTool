#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/7/17.
import exception as exception
import requests
import json

URL_GET = 'http://www.imooc.com/course/list?c=python'
URL = 'https://api.github.com'


def use_simple_requests():
    resposes = requests.get(URL_GET)
    print(resposes.headers)
    print('text:' + resposes.text)


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_start():
    response = requests.get(build_uri('users/imoocdemo'))
    print(better_print(response.text))


def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)


def json_request():
    response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'),
                              json={'name': 'babymooc2', 'email': 'hello-world@imooc.org'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)


def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exception.Timeout as e:
        print(e.message)

    else:
        print(response.text)
        print(response.status_code)


def download_image():
    """
        demo: 下载图片，文件
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532624840778&di=9843305b33f0052559dbd89340742c02&imgtype=0&src=http%3A%2F%2Fmedia-cdn.tripadvisor.com%2Fmedia%2Fphoto-s%2F03%2F2b%2F29%2Fc7%2Ftupuna-safari.jpg'
    response = requests.get(url, headers=headers, stream=True)
    with open('demo.jpg', 'wb') as  fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
            print(chunk)  # image转换为2进制流


def download_image_improved():
    """
        demo: 下载图片，文件
    """
    headers = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532624840778&di=9843305b33f0052559dbd89340742c02&imgtype=0&src=http%3A%2F%2Fmedia-cdn.tripadvisor.com%2Fmedia%2Fphoto-s%2F03%2F2b%2F29%2Fc7%2Ftupuna-safari.jpg'
    response = requests.get(url, headers=headers, stream=True)
    # 获取上下文，使用链接后并 关闭连接，节省资源
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每 128 写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


def get_kek_info(response, *args, **kwargs):
    """
        回调函数
    """
    print(response.headers['Content-Type'])


def main_request():
    """
        主函数
    """
    url = 'https://api.github.com'
    requests.get(url=url, hooks=dict(response=get_kek_info))


if __name__ == '__main__':
    main_request()
