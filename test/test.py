#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 下午4:14
# @Author  : wudizhangzhi
import curses

import time


def convert2screen(pos_data, width, height):
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

        converted.append((char, (y + addition_lines, x)))

    return converted


def test():
    content = """公牛队给了他展现自我的机会。他们给他增加了许多戏份：他进攻端中挡拆处理球的比例（32.9）已经接近在华盛顿时（12.7）的三倍。值得确定的是，仍然由许多条件限制了波特成为一名进攻主导者。他不是一名精英级别的球员，他没有像米德尔顿和英格尔斯那样强壮的力量和坚实的臂膀，他们两个可以无视身材矮小的球员"""
    # 转化为pos_data
    pos_data = []
    for i, char in enumerate(content):
        pos_data.append((char, (0, i // 100, i % 100, 0)))


    screen = curses.initscr()
    curses.noecho()
    curses.start_color()

    screen_rows, screen_cols = screen.getmaxyx()

    for char, pos in convert2screen(pos_data, screen_cols, screen_cols):
        screen.addstr(pos[0], pos[1], char)

    # for i, char in enumerate(content):
    #     # i *= 2
    #     screen.addstr(i // screen_cols, i % screen_cols, char)

    # screen.addstr(0, 0, '测')
    # screen.addstr(0, 1, '试')
    # screen.addstr(0, 2, '测')
    # screen.addstr(0, 3, '试')
    # screen.addstr(0, screen_cols - 4, '测')
    # screen.addstr(0, screen_cols - 2, '试')
    # screen.addstr(1, 0, '第')
    # screen.addstr(1, screen_cols - 2, '二')

    screen.refresh()

    time.sleep(5)

    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    test()
