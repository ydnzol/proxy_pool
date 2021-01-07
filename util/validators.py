# -*- coding: utf-8 -*-
import os
import requests

from re import findall
from handler.configHandler import ConfigHandler


conf = ConfigHandler()
validators = []


def validator(func):
    validators.append(func)
    return func


@validator
def formatValidator(proxy):
    """
    检查代理格式
    :param proxy:
    :return:
    """
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    _proxy = findall(verify_regex, proxy)
    return True if len(_proxy) == 1 and _proxy[0] == proxy else False


@validator
def timeOutValidator(proxy):
    """
    检测超时
    :param proxy:
    :return:
    """

    proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}

    try:
        r = requests.head(conf.verifyUrl, headers=conf.headers, proxies=proxies, timeout=conf.verifyTimeout, verify=False)
        if r.status_code == 200:
            return True
    except Exception as e:
        print(e)
    return False


@validator
def customValidator(proxy):
    """
    自定义validator函数，校验代理是否可用
    :param proxy:
    :return:
    """
    os.environ['NO_PROXY'] = 'api.shodan.io'
    no_local_proxies = {
        "http": None,
        "https": None
    }
    proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy), 'socks': 'socks5://{proxy}'.format(proxy=proxy)}
    no_local_proxies_ip = send_request(no_local_proxies)
    http_proxies_ip = send_request(proxies, is_http=True)
    https_proxies_ip = send_request(proxies, is_http=False)
    if isinstance(no_local_proxies_ip, str) and isinstance(http_proxies_ip, str) and isinstance(https_proxies_ip, str) and (no_local_proxies_ip not in http_proxies_ip or no_local_proxies_ip not in https_proxies_ip):
        return True

def send_request(proxy, is_http=False):
    url = conf.verifySrcUrl
    if is_http:
        url = url.replace("https", "http")
    try:
        r = requests.get(conf.verifySrcUrl, headers=conf.headers, proxies=proxy, timeout=conf.verifyTimeout, verify=False)
    except Exception as e:
        print(e)
    else:
        if r.status_code == 200 and len(r.text) > 0:
            print(r.text)
            return r.text

