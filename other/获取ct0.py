# coding=utf-8
# @Author: 二次蓝
# @Created at 2023/9/8 11:34
import re

import requests

import proxy


def get_ct(auth_token):
    cookies = {
        'auth_token': auth_token,
    }

    headers = {
        'authority': 'twitter.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type': 'application/json',
        'referer': 'https://twitter.com/i/flow/login',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        # 'x-csrf-token': '3b273ac49459efedacc3ee91a99d1985',
        # 'x-guest-token': '1650413826456817664',
        # 'x-twitter-active-user': 'yes',
        # 'x-twitter-client-language': 'zh-cn',
    }

    params = {
        'variables': '{"withCommunitiesMemberships":true,"withSubscribedTab":false,"withCommunitiesCreation":true}',
        'features': '{"blue_business_profile_image_shape_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
    }

    response = requests.get('https://twitter.com/i/api/graphql/XeaGEEWXp54Km4mVNvcMmg/Viewer', params=params,
                            cookies=cookies, headers=headers, proxies=proxy.jw_proxies)
    return re.search(r"ct0=(\w+); ", response.headers.get("set-cookie"))[1]
