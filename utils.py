# coding=utf-8
# @Author: 二次蓝
# @Created at 2023/9/8 9:46
import re
import secrets

import requests
from loguru import logger


def get_guest_token(jw_proxies):
    url = "https://api.twitter.com/1.1/guest/activate.json"
    page = requests.post(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "AUTHORIZATION": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        },
        proxies=jw_proxies,
    )
    logger.debug(page.json())


def get_flow_token(page):
    return re.search(r"\"flow_token\":\"(.+?)\"", page.text, flags=re.DOTALL)[1]


def print_ck(session):
    return "".join(
        k + "=" + session.cookies.get(k) + "; " for k in session.cookies.keys()
    )


def generate_random_hex(length):
    num_bytes = length // 2  # 每个字节对应两位十六进制字符
    random_bytes = secrets.token_bytes(num_bytes)
    random_hex = random_bytes.hex()
    return random_hex


if __name__ == '__main__':
    random_hex_string = generate_random_hex(32)
    print(random_hex_string)
