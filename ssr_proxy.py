# pip install requests[socks]
import subprocess

import psutil
import requests
from loguru import logger

ssr_client_local_path = r"F:\shadowsocksr-3.2.1"
LOCAL_LISTEN_IP = "127.0.0.1"
LOCAL_PORT = 1080
proxies = {
    'http': f'socks5h://{LOCAL_LISTEN_IP}:{LOCAL_PORT}',
    'https': f'socks5h://{LOCAL_LISTEN_IP}:{LOCAL_PORT}'
}


def kill_process_by_port(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            connections = proc.connections()
            for conn in connections:
                if conn.status == 'LISTEN' and conn.laddr.port == port:
                    logger.info(f"Killing process {proc.pid} - {proc.name()}")
                    proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def start_program(program_path, server_ip, server_port, password=None, no_log=True):
    try:
        kill_process_by_port(LOCAL_PORT)
        # 可以在此处，自行添加启动参数，比如修改协议等
        default_args = ["python", rf'{ssr_client_local_path}\shadowsocks\local.py',
                        '-b', LOCAL_LISTEN_IP, '-l', str(LOCAL_PORT),
                        '-s', server_ip, '-p', str(server_port), '-k', password]
        if no_log:
            subprocess.Popen(default_args, shell=True, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(default_args, shell=True)
        logger.info(f"启动程序: {program_path}")
    except subprocess.CalledProcessError:
        logger.info("执行命令时出现错误")


def start_proxy(server_ip, server_port, password):
    """
    启动ssr代理
    :param server_ip: 远端服务器ip。
    :param server_port: 远端服务器端口。
    :param password: 远端密码。
    """
    start_program(rf"{ssr_client_local_path}", server_ip=server_ip, server_port=server_port,
                  password=password, no_log=False)


def check_ip():
    url = "http://cip.cc"
    # url = "http://www.google.com"
    page = requests.get(url, proxies=proxies, headers={
        "User-Agent": "curl/7.83.1"
    })
    logger.info(page.text)


if __name__ == '__main__':
    start_proxy("160.999.999.999", server_port=5443, password="password")
    check_ip()
