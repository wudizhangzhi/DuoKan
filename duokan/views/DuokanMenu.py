#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 下午8:17
# @Author  : wudizhangzhi
import re

from six import PY3
import time
import curses

from logging import getLogger

from views.BaseMenu import BaseMenu, bind_event

log = getLogger(__name__)

HELPER_LINES = [
    'j         Down           下移',
    'k         Up             上移',
    'space     Enter          进入',
    'q         Quit           退出',
    'Ctrl-C           退出文字直播',
]


class DuokanMenu(BaseMenu):
    def __init__(self, engine, title=None, body_title=None, addition_title=None):
        super(DuokanMenu, self).__init__(title, body_title, addition_title)
        self.engine = engine
        self.page_no = engine.current_page

        self.title = '多看阅读 Proudly presented by JRs.'
        self.body_title = '书名: %s, 页码: %s'
        self.addition_title = '帮助信息:'
        self.addition_items = HELPER_LINES
        self.content_data = None  # 内容

    def draw(self):
        """
        draw screen
        """
        self.clear_screen()
        rows = 0  # 行数
        if self.title is not None:
            self.addstr(rows, 2, self.title, curses.color_pair(5))
            rows += 2

        if self.addition_title:
            self.addstr(rows, 2, self.addition_title, curses.color_pair(6))
            rows += 1
            addition_start_row = rows
            for index, item in enumerate(self.addition_items):
                self.addstr(addition_start_row + index, 4, item)
                rows += 1
            rows += 1

        if self.body_title is not None:
            # TODO
            self.addstr(rows, 2, self.body_title % ('', self.page_no), curses.A_BOLD)
            rows += 2

        # 每次重新获取屏幕的大小, 获取范围
        screen_rows, screen_cols = self.screen.getmaxyx()
        row_max = screen_rows - rows - 1
        show_end = self.current_option + 1 if self.current_option >= row_max else row_max
        show_start = show_end - row_max if show_end > row_max else 0

        height, width = self.screen.getmaxyx()
        for char, pos in self.convert2screen(self.content_data, width, height):
            self.addstr(rows + pos[0], pos[1], char, self.normal)
        # arrow = ' ->  '
        # for index, item in enumerate(self.items[show_start:show_end]):
        #     if self.current_option == index + show_start:
        #         text_style = self.highlight
        #         self.addstr(rows + index, 4, arrow + str(item), text_style)
        #     else:
        #         text_style = self.normal
        #         self.addstr(rows + index, 4, ' ' * len(arrow) + str(item), text_style)
        self.screen.refresh()

    @bind_event([' ', curses.KEY_ENTER])
    def enter(self):
        # TODO delete
        chapters = [{
            "page_range": [
                1,
                1
            ],
            "number": 1,
            "cid": "f06797d5-0377-4c96-ab6d-a70375481e7b"
        },
            {
                "page_range": [
                    2,
                    2
                ],
                "number": 2,
                "cid": "8eb5c675-fda8-4283-a47c-71edc58b0976"
            },
            {
                "page_range": [
                    3,
                    3
                ],
                "number": 3,
                "cid": "0939216f-e6bc-4051-9d2b-50db2f26e740"
            }, ]
        current_chapter = chapters[self.current_option]
        # 获取当前章节的内容
        ret = self.engine.fetchPageContent('b64829f41e6d11e2ad8a00163e0123ac', self.page_no)
        # 替换内容
        self.items = [ret]
        self.page_no += 1

    @bind_event(['n', curses.KEY_RIGHT])
    def nextPage(self):
        """
        下一页
        Returns:

        """
        self.page_no += 1
        self.content_data = self.engine.fetchPageContent(self.engine.current_book_id, self.page_no)
        self.draw()

    @bind_event(['p', curses.KEY_LEFT])
    def perviousPage(self):
        """
        上一页
        Returns:

        """
        self.page_no -= 1
        self.content_data = self.engine.fetchPageContent(self.engine.current_book_id, self.page_no)
        self.draw()

    def convert2screen(self, pos_data, width, height):
        """将多看的位置显示转化为当前屏幕的位置显示
        当前屏幕：y, x = 33, 158
        对象:
            堆 [5, 26, 96, 5640]
        Args:
            pos_data: 
            width: 
            height: 

        Returns:

        """
        # x乘以2
        pos_data = [(char, (pos[0], pos[1], pos[2] * 2, pos[3])) for char, pos in pos_data]

        y_list = [i[1][1] for i in pos_data]
        x_list = [i[1][2] for i in pos_data]
        min_y, max_y = min(y_list), max(y_list)
        min_x, max_x = min(x_list), max(x_list)

        converted = []
        addition_lines_dict = {}
        for char, pos in pos_data:
            _, y, x, _ = pos

            y -= min_y
            x -= min_x

            next_line = x // width
            addition_lines_dict[y] = next_line
            lines = list(addition_lines_dict.values())
            addition_lines = sum(lines) if lines else 0
            x = x % width

            # TODO
            if y + addition_lines > height:
                break

            converted.append((char, (y + addition_lines, x)))

        return converted
