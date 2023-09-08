# coding=utf-8
# @Author: 二次蓝
# @Created at 2023/4/24 17:00

"""无用，如有需要，自行修改"""
import httpx
import requests

import proxy

cookies = {
    'guest_id_ads': 'v1%%3A168204227716003679',
    'guest_id_marketing': 'v1%%3A168204227716003679',
    'gt': '1649230964318128512',
    'personalization_id': '"v1_jQYUr6w0TfxF+LvbuBBPVA=="',
    'guest_id': 'v1%%3A168204227716003679',
    'ct0': '81aefbf280f0ac4e443a6339c8ca9930',
    'att': '1-7WsSfxiPOPUuvX6xbB2ABsQzgoF8l7Fu2Qssq4cx',
}

headers = {
    'Host': 'twitter.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://twitter.com/i/flow/login',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'guest_id_ads=v1%%3A168204227776003679; guest_id_marketing=v1%%3A168204227776003679; gt=1649230964328128512; personalization_id="v1_jQYUr6w0TfxF+LvbuRAPVA=="; guest_id=v1%%3A168204227776003679; ct0=81aefbf280f0ac4e443a6339c8ca9930; att=1-7WsSfxiPOPUuvX6xbB2ABsQzgoF8l7Fu2Qssq4cx',
}

params = {
    'c_name': 'ui_metrics',
}

# response = requests.get('https://twitter.com/i/js_inst', params=params, cookies=cookies, headers=headers, verify=False)
with httpx.Client(http2=True, proxies=proxy.jw_proxies_httpx) as client:
    response = client.get('https://twitter.com/i/js_inst', params=params, cookies=cookies, headers=headers)
# 此js动态生成了一些input，提交的时候需要带上。还设置了一些定时器
print(response.headers)
print("=" * 75)
print(response.text)
