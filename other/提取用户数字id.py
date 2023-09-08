# coding=utf-8
# @Author: 二次蓝
# @Created at 2023/8/16 14:23
import re

import requests
from loguru import logger

import proxy

target_list = """https://twitter.com/elonmusk
https://twitter.com/BillGates
"""


def get_guest_token():
    url = "https://api.twitter.com/1.1/guest/activate.json"
    page = requests.post(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        },
        proxies=proxy.jw_proxies,
    )
    logger.debug(page.json())

# 这个无效，可以从浏览器上直接获取一个，自动获取还未分析
# guest_token = get_guest_token()


def get_uid(account: str):
    headers = {
        'authority': 'api.twitter.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type': 'application/json',
        # 'cookie': 'guest_id_marketing=v1%3A169355928600422319; guest_id_ads=v1%3A169355928600422319; personalization_id="v1_ci5E97E/cXKZeonjnquTBg=="; guest_id=v1%3A169355929229680748',
        'origin': 'https://twitter.com',
        'referer': 'https://twitter.com/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-client-transaction-id': 'h5xF4IISVh8VlLr6wQgyUnFICrhBSLMn/fI3lorH1/3K7wLtB6aB6o6cLlcaIJ+iSPDBJYe8BRdD7Zmf83+/N/9c1+IShg',
        'x-csrf-token': '82e801465bcc9d08e684342dfd1d8301',
        # 先手动获取，修改这个值
        'x-guest-token': '1698875781475430619',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'zh-cn',
    }

    params = {
        'variables': f'{{"screen_name":"{account}","withSafetyModeUserFields":true}}',
        'features': '{"hidden_profile_likes_enabled":true,"hidden_profile_subscriptions_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"subscriptions_verification_info_is_identity_verified_enabled":false,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
        'fieldToggles': '{"withAuxiliaryUserLabels":false}',
    }
    # 提子用户信息接口，不登录有少量用户信息
    response = requests.get(
        'https://api.twitter.com/graphql/G3KGOASz96M-Qu0nwmGXNg/UserByScreenName',
        params=params,
        # cookies=cookies,
        headers=headers,
        proxies=proxy.jw_proxies
    )
    # rest_id
    # print(response.headers)
    # print("=" * 75)
    # print(response.text)
    return response.json()["data"]["user"]["result"]["rest_id"]


results = []
for line in target_list.split("\n"):
    line = line.strip()
    if not line:
        continue

    try:
        if line.startswith("http"):
            line = re.search(r"https://twitter\.com/(.+)", line).group(1)

        uid = get_uid(line)
    except Exception as e:
        logger.error(e)
        new_line = f"{line}\t"
        print(new_line)
        results.append(new_line)
        exit()
    else:
        url = uid
        # if uid:
        #     url = f"https://twitter.com/i/api/graphql/DhQ8lYnLh5T5K8aVUgHVnQ/UserTweets?variables=%7B%22userId%22%3A%22{uid}%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withBirdwatchPivots%22%3Afalse%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Afalse%2C%22__fs_interactive_text%22%3Afalse%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%7D"
        # else:
        #     url = ""
        new_line = f"{line}\t{url}"
        print(new_line)
        results.append(new_line)
with open(r"uids.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))
