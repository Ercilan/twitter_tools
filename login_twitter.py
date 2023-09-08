# coding=utf-8
# @Author: 二次蓝
# @Created at 2023/6/19 11:54
import os.path
import random
import re
import sys
import time

import requests
import urllib3
from loguru import logger

from ja3 import DESAdapter
from proxy import jw_proxies
from ssr_proxy import start_proxy
from utils import get_flow_token

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger.remove(handler_id=None)
logger.add(sys.stdout, format="<level>{message}</level>")

AUTHORIZATION = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"


def login(proxy):
    session = requests.Session()
    session.mount("https://", DESAdapter())
    session.proxies.update(proxy)
    session.verify = False
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache, no-store",
        # "If-Modified-Since": "Sat, 1 Jan 2000 00:00:00 GMT",
        "Referer": "https://twitter.com/",
    }
    page = session.get("https://twitter.com/i/flow/login", headers=headers)

    match = re.search(r"document\.cookie=\"gt=(.+?);", page.text, flags=re.DOTALL)
    if match is not None:
        guest_token = match[1]
    else:
        logger.error("未获取到guest_token")
        return

    headers["content-type"] = "application/json"
    headers["AUTHORIZATION"] = AUTHORIZATION
    headers["x-guest-token"] = guest_token

    body = {
        "input_flow_data": {
            "flow_context": {
                "debug_overrides": {},
                "start_location": {"location": "manual_link"},
            }
        },
        "subtask_versions": {
            "action_list": 2,
            "alert_dialog": 1,
            "app_download_cta": 1,
            "check_logged_in_account": 1,
            "choice_selection": 3,
            "contacts_live_sync_permission_prompt": 0,
            "cta": 7,
            "email_verification": 2,
            "end_flow": 1,
            "enter_date": 1,
            "enter_email": 2,
            "enter_password": 5,
            "enter_phone": 2,
            "enter_recaptcha": 1,
            "enter_text": 5,
            "enter_username": 2,
            "generic_urt": 3,
            "in_app_notification": 1,
            "interest_picker": 3,
            "js_instrumentation": 1,
            "menu_dialog": 1,
            "notifications_permission_prompt": 2,
            "open_account": 2,
            "open_home_timeline": 1,
            "open_link": 1,
            "phone_verification": 4,
            "privacy_options": 1,
            "security_key": 3,
            "select_avatar": 4,
            "select_banner": 2,
            "settings_list": 7,
            "show_code": 1,
            "sign_up": 2,
            "sign_up_review": 4,
            "tweet_selection_urt": 1,
            "update_users": 1,
            "upload_media": 1,
            "user_recommendations_list": 4,
            "user_recommendations_urt": 1,
            "wait_spinner": 3,
            "web_modal": 1,
        },
    }
    page = session.post("https://api.twitter.com/1.1/onboarding/task.json?flow_name=login", json=body,
                        headers=headers)
    # 响应头有att等cookie，session自动处理
    # print(f"att: {page.text}")
    flow_token = get_flow_token(page)

    body = {"flow_token": flow_token, "subtask_inputs": []}
    page = session.post("https://api.twitter.com/1.1/onboarding/task.json", json=body, headers=headers)
    # invalid ATT for the flow
    flow_token = get_flow_token(page)

    body = {
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "LoginEnterUserIdentifierSSO",
                "settings_list": {
                    "setting_responses": [
                        {
                            "key": "user_identifier",
                            "response_data": {"text_data": {"result": username}},
                        }
                    ],
                    "link": "next_link",
                },
            }
        ],
    }
    page = session.post("https://api.twitter.com/1.1/onboarding/task.json", json=body, headers=headers)
    if page.status_code != 200:
        logger.error(f"账号异常：{page.text}")
        return None, None
    flow_token = get_flow_token(page)

    if "LoginEnterAlternateIdentifierSubtask" in page.text:
        logger.info("切换邮箱登录")
        body = {
            "flow_token": flow_token,
            "subtask_inputs": [
                {
                    "subtask_id": "LoginEnterAlternateIdentifierSubtask",
                    "enter_text": {"text": phone, "link": "next_link"},
                }
            ],
        }
        page = session.post("https://api.twitter.com/1.1/onboarding/task.json", json=body, headers=headers)
        flow_token = get_flow_token(page)

    body = {
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "LoginEnterPassword",
                "enter_password": {"password": password, "link": "next_link"},
            }
        ],
    }
    page = session.post("https://api.twitter.com/1.1/onboarding/task.json", json=body, headers=headers)
    if "errors" in page.text:
        logger.error(f"密码错误：{page.text}")
        return None, None
    flow_token = get_flow_token(page)

    body = {
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "subtask_id": "AccountDuplicationCheck",
                "check_logged_in_account": {"link": "AccountDuplicationCheck_false"},
            }
        ],
    }
    page = session.post("https://api.twitter.com/1.1/onboarding/task.json", json=body, headers=headers)

    if "secondary_text" in page.text:
        data = page.json()
        header_ = data["subtasks"][0]["enter_text"]["header"]
        primary_text = header_["primary_text"]["text"]
        secondary_text = header_["secondary_text"]["text"]
        if secondary_text.startswith("Verify your identity by entering the phone number"):
            logger.error(f"需要验证手机号：{primary_text}\n{secondary_text}")
            flow_token = get_flow_token(page)
            body = {
                "flow_token": flow_token,
                "subtask_inputs": [
                    {
                        "subtask_id": "LoginAcid",
                        "enter_text": {"text": phone, "link": "next_link"},
                    }
                ],
            }

            page = session.post("https://api.twitter.com/1.1/onboarding/task.json", json=body, headers=headers)
            # logger.debug(page.text)
        else:
            logger.error(f"需要验证码：{primary_text}\n{secondary_text}")
            return None, None

    set_cookie = page.headers["set-cookie"]
    # logger.debug(set_cookie)

    global csrf_token, auth_token
    csrf_token = re.search(r"ct0=(.+?); ", set_cookie)[1]
    auth_token = re.search(r"auth_token=(.*?); ", set_cookie)[1]

    del headers["content-type"]
    page = session.get(
        "https://twitter.com/i/api/graphql/XeaGEEWXp54Km4mVNvcMmg/Viewer?variables=%7B%22withCommunitiesMemberships%22%3Atrue%2C%22withSubscribedTab%22%3Atrue%2C%22withCommunitiesCreation%22%3Atrue%7D&features=%7B%22blue_business_profile_image_shape_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D",
        headers=headers
    )

    match = re.search("ct0=(.+?); ", page.headers["set-cookie"])
    csrf_token = match[1]
    return auth_token, csrf_token


def get_sockets_proxy():
    """
    使用socks5代理
    """
    return {
        'http': f'socks5h://:@127.0.0.1:1080',
        'https': f'socks5h://:@127.0.0.1:1080'
    }


if __name__ == "__main__":
    # python指纹被封  2023/9/1
    file = "./data/0830.txt"
    proxy_server_port = 5443
    proxy_server_password = "password"

    out = ""
    try:
        with open(file, encoding="utf-8") as f:
            # 跳过表头
            # f.readline()
            lines = f.readlines()
        for index, line in enumerate(lines):
            # 从这个打印的序号继续。
            if index + 1 < 1:
                continue

            line = line.rstrip()
            # username, password, phone, email = line.split("\t")
            # username, password, nickname, person_id, phone, source = line.split("\t")
            values = line.split("\t")
            if len(values) == 4:
                username, password, phone, proxy_server = values
                start_proxy(proxy_server, server_port=proxy_server_port, password=proxy_server_password)
                # check_ip()
                proxy = get_sockets_proxy()
            elif len(values) == 3:
                username, password, phone = values
                proxy = jw_proxies
            else:
                username, password = values
                phone = None
                proxy = jw_proxies
            logger.info(f"[{index + 1}/{len(lines)}] {username} {password} {phone}")

            auth_token, csrf_token = login(proxy=proxy)
            if auth_token is None:
                logger.error(f"{username}\t登录失败")
            else:
                logger.success(f"auth_token = {auth_token}\ncsrf_token = {csrf_token}")
            out = f"{out}{username}\t{auth_token}\n"
            time.sleep(random.randint(3, 7))
    except Exception as e:
        logger.exception(e)
    finally:
        if not out:
            exit()

        if not os.path.exists("./data"):
            os.mkdir("./data")
        output_file = f"./data/{os.path.splitext(os.path.basename(file))[0]}_cks.txt"
        mode = "at" if os.path.exists(output_file) else "wt"
        with open(output_file, encoding="utf-8", mode=mode) as f:
            f.write(out)
