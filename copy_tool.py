#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import pyperclip, os

path = r'C:\CC快速复制工具\文本列表.txt'

if not os.path.exists(r'C:\CC快速复制工具'): os.makedirs(r'C:\CC快速复制工具')
if not os.path.exists(path):
    file = open(path, 'w', encoding='UTF-8')
    file.write('演示内容：\n王小明\n13810001000\n20201150421\n2020级\n5班')
    file.close()

text_list = []
with open(path, "r", encoding='UTF-8') as f:
    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        text_list.append(line)  # 读取到的每行内容，都写入文字列表中
    print(text_list)
    f.close()


def Clicked(text):
    print(f'‘{text}’已被复制到剪贴板')
    pyperclip.copy(text)


# 设置窗口
win = tk.Tk()
win.title('CC快速复制工具')
win.wm_attributes('-topmost', 1)  # 置顶
win.geometry('280x300+10+50')

for inx, text in enumerate(text_list):
    tk.Button(win, width=12, height=1, text=text, anchor='w', command=lambda arg=text: Clicked(arg)) \
        .grid(row=inx % 10, column=inx // 10)
win.mainloop()
