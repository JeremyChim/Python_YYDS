# -*- coding: utf-8 -*-
# @Time ： 2023/6/4 4:28
# @Auth ： JeremyChim
# @File ：win.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import ttkbootstrap as ttk

class app(ttk.Frame):

    def __init__(self, win):
        super().__init__(win)
        self.pack()

if __name__ == '__main__':

    w = ttk.Window()
    a = app(w)
    w.mainloop()

    '''上面代码作用如下'''
    # w = ttk.Window()
    # a = ttk.Frame(w)
    # a.pack()
    # w.mainloop()