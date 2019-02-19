#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 上午10:21
# @Author  : wudizhangzhi

import requests
try:
    requests.packages.urllib3.disable_warnings()
except ImportError:
    pass
from duokan import load_cookie, DuoKan
from views.DuokanMenu import DuokanMenu

if __name__ == '__main__':
    cookie = load_cookie('cookie.txt')
    duokan = DuoKan(cookie)
    duokan.current_book_id = 'b64829f41e6d11e2ad8a00163e0123ac'
    menu = DuokanMenu(duokan)
    # # menu.draw()
    # # converted = menu.convert2screen(test_pos_data, 158, 33)
    # # for c in converted:
    # #     char, pos = c
    # #     menu.addstr(pos[0], pos[1], char, menu.normal)
    # menu.content_data = test_pos_data
    menu.nextPage()
    # menu.draw()
    menu.listen()
