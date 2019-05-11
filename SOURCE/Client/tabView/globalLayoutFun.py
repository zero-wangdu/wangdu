# coding=utf-8


'''
界面常用设置功能
'''
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QFont


# 设置界面水平和垂直布局为Expanding
def SET_UI_POLICY(w):
    sizePolicy = w.sizePolicy()
    sizePolicy.setHorizontalPolicy(QSizePolicy.Expanding)
    sizePolicy.setVerticalPolicy(QSizePolicy.Expanding)
    w.setSizePolicy(sizePolicy)


def SET_UI_POLICY_ITEM(w,h_policy,v_policy):
    sizePolicy = w.sizePolicy()
    sizePolicy.setHorizontalPolicy(h_policy)
    sizePolicy.setVerticalPolicy(v_policy)
    w.setSizePolicy(sizePolicy)


def SET_UI_STRETCH(w,v,h):
    sizePolicy = w.sizePolicy()
    sizePolicy.setVerticalStretch(v)
    sizePolicy.setHorizontalStretch(h)
    w.setSizePolicy(sizePolicy)


def SET_LAYOUT_STRETCH(layout, argv):
    for i in range(len(argv)):
        layout.setStretch(i, argv[i])

# 设置字体样式
def SET_FONT_STYLE(widgets, size, weight=75, bold=False, family='Microsoft yahei'):
    font = QFont()
    font.setFamily(family)
    font.setPointSize(size)
    font.setWeight(weight)
    font.setBold(bold)

    for item in widgets:
        item.setFont(font)

# 设置字体颜色
def SET_FONT_COLOR(widgets, color):
    for item in widgets:
        item.setStyleSheet("color:%s"%(color))

# 整体设置布局为 Expanding
def SET_UI_POLICY_FUN(widget_li):
    for item in widget_li:
        SET_UI_POLICY(item)

# 设置对其方式 setAlignment
def SET_ALIGNMENT(widget_li, *args):
    for item in widget_li:
        for algin in args:
            item.setAlignment(algin)

# 设置样式 setStyleSheet
def SET_STYLE_SHEET(widget_li, style):
    for item in widget_li:
        item.setStyleSheet(style)