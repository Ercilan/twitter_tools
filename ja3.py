# coding=utf-8
# @Author: 二次蓝
# @Created at 2022/11/28 14:16
import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

# 代码来源网上
ORIGIN_CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES')


class DESAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        # 在请求中重新启用 3DES 支持的 TransportAdapter
        CIPHERS = ORIGIN_CIPHERS.split(":")
        random.shuffle(CIPHERS)
        # print("1:", CIPHERS)
        CIPHERS = ":".join(CIPHERS)
        # print("2:", CIPHERS)
        self.COPHERS = CIPHERS + ":!aNULL:!eNULL:!MD5"
        super(DESAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.COPHERS)
        kwargs["ssl_context"] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.COPHERS)
        kwargs["ssl_context"] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)


if __name__ == '__main__':
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}
    # s = requests.Session()
    # # s.headers.update(headers)
    #
    # for _ in range(5):
    #     s.mount("https://tls.peet.ws/", DESAdapter())
    #     response = s.get("https://tls.peet.ws/api/all", verify=False).json()
    #     print(response)
    #     print(response['tls']['ja3_hash'])
    # exit()

    # 或者直接使用：pip install curl_cffi，可信真实的指纹
    # from curl_cffi import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }
    # response = requests.get("http://www.douyin.com", impersonate="chrome110", headers=headers)
    response = requests.get("http://www.douyin.com", headers=headers)

    # chrome99
    # chrome100
    # chrome101
    # chrome104
    # chrome107
    # chrome110
    # chrome99_android
    # edge99
    # edge101
    # safari15_3
    # safari15_5

    print(response.text)
    print(response.headers)
