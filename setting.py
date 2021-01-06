# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting.py
   Description :   配置文件
   Author :        JHao
   date：          2019/2/15
-------------------------------------------------
   Change Activity:
                   2019/2/15:
-------------------------------------------------
"""

BANNER = r"""
****************************************************************
*** ______  ********************* ______ *********** _  ********
*** | ___ \_ ******************** | ___ \ ********* | | ********
*** | |_/ / \__ __   __  _ __   _ | |_/ /___ * ___  | | ********
*** |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | | ********
*** | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___  ****
*** \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____/ ****
****                       __ / /                          *****
************************* /___ / *******************************
*************************       ********************************
****************************************************************
"""

VERSION = "2.1.1"

# ############### server config ###############
HOST = "0.0.0.0"

PORT = 5010

# ############### database config ###################
# db connection uri
# example:
#      Redis: redis://:password@ip:port/db
#      Ssdb:  ssdb://:password@ip:port
DB_CONN = 'redis://:langke@127.0.0.1:6379/0'

# proxy table name
TABLE_NAME = 'proxy_pool'


# ###### config the proxy fetch function ######
PROXY_FETCHER = [
    "proxylist"
#    "freeProxy01",
#    "freeProxy02",
#    # "freeProxy03",
#    "freeProxy04",
#    "freeProxy05",
#    "freeProxy06",
#    "freeProxy07",
#    # "freeProxy08",
#    "freeProxy09",
#    "freeProxy13",
#    "freeProxy14"
]

# ############# proxy validator #################
VERIFY_URL = "http://www.baidu.com"
VERIFY_SRC_URL = "https://api.shodan.io/tools/myip?key=yK0AfFxENdV4bzGQtQZOPE0ExNJ1jS2y"

VERIFY_TIMEOUT = 10

MAX_FAIL_COUNT = 0


# ############# scheduler config #################

# Set the timezone for the scheduler forcely (optional)
# If it is running on a VM, and 
#   "ValueError: Timezone offset does not match system offset" 
#   was raised during scheduling.
# Please uncomment the following line and set a timezone for the scheduler.
# Otherwise it will detect the timezone from the system automatically.

# TIMEZONE = "Asia/Shanghai"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
           'Accept': '*/*',
           'Connection': 'keep-alive',
           'Accept-Language': 'zh-CN,zh;q=0.8'
           }