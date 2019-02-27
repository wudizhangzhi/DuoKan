#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 上午10:21
# @Author  : wudizhangzhi

"""DuoKan.
    Proudly presented by Hupu JRs.

Usage:
    duokan [-b BOOK_ID] [-p page]
    duokan -h | --help
    duokan -v | --version

Tips:
    Please hit Ctrl-C on the keyborad when you want to interrupt the game live.

Options:
    -b BOOK_ID --book_id=BOOK_ID            book id.
    -p PAGE --page=PAGE                     page num.
    -h --help                               Show this help message and exit.
    -v --version                            Show version.
"""

import docopt
import requests

try:
    requests.packages.urllib3.disable_warnings()
except ImportError:
    pass
from duokan import load_cookie, DuoKan
from views.DuokanMenu import DuokanMenu


def start():
    arguments = docopt.docopt(__doc__, version='DuoKan 1.0.0')
    # 处理参数
    arguments = {k.replace('--', ''): v for k, v in arguments.items()}
    cookie = load_cookie('cookie.txt')
    duokan = DuoKan(cookie)
    # 设置数据
    duokan.current_book_id = arguments['book_id']
    duokan.current_page = int(arguments['page']) if arguments['page'] else 1
    # 显示
    menu = DuokanMenu(duokan)
    menu.nextPage()
    menu.listen()


if __name__ == '__main__':
    start()
