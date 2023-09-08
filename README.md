## 说明

使用 requests 登录 twitter，获取 auth_token。可批量。

- 支持验证手机号码登录，但不支持邮箱验证码登录。

## 使用

1. 按以下格式生成一个 txt，提供账号信息：

```text
username password phone proxy_server
```

- proxy_server 为避免风控，最好修改使用一个【**干净**】的代理。否则账号易被锁、封。proxy_server 是调用某 **r 代理。（**⚠**： 因为本人没有可用 **r 服务器，没有测试过代码是否正常。）
- 也可以不提供此参数，修改 proxy.py 的 `jw_proxies` 函数，可使用 http 代理。

2. 修改 login_twitter.py 的 `file` 值为上面的文件路径，以及如果使用 proxy_server 则配置一下端口密码，启动。
3. 程序将单线程登录，最终输出一个 cookie 文本文件。

## 其他

[获取ct0.py](other%2F%BB%F1%C8%A1ct0.py)：获取 `ct0`（`x-csrf-token`）。

[生成sess.py](other%2F%C9%FA%B3%C9sess.py)：分析时的中间产物，应该没用。`_twitter_sess`

[提取用户数字id.py](other%2F%CC%E1%C8%A1%D3%C3%BB%A7%CA%FD%D7%D6id.py)：不登录，将账号（`account`）成数字（`rest_id`）。

[更换cookie.user.js](other%2F%B8%FC%BB%BBcookie.user.js)：油猴脚本，点击一个悬浮按钮，直接切换已登录账号（代码内配置的账号cookie，未做风控处理，风险自担）

- 2023/09/08：init
