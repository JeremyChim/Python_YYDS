<h1 align="center">Python_YYDS</h1>
<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/Auth-Jeremy-brightgreen">
    <img alt="Static Badge" src="https://img.shields.io/badge/Version-v1.1.0-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/ILovePython-pink">
</p>

## ☕介绍

小铭用来记录下Python技巧的一个小本子🤣😃🤪🍕🍔🍟🌭🍿

## 1、安装Python环境

1. 下载[Python](https://www.python.org/downloads/windows/)

2. 下载[PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

3. 下载[Git](https://git-scm.com/downloads)

4. 下载[Github Desktop](https://desktop.github.com/)

5. 安装PyCharm插件
   
   - Chinese (Simplified) Language Pack / 中文语言包
   
   - One Dark theme
   
   - CMD Support

6. 新建PycharmProject项目
   
   - 选择：先前配置的解释器
   
   - 不勾选：创建main.py

7. 添加PyCharm镜像源
   
   - 文件 > 设置 > 项目 > Python解释器 > + > 管理仓库
     
     | 镜像源 | 网址                                        | 推荐度   | 免翻墙 |
     |:--- |:----------------------------------------- |:----- |:---:|
     | 中科大 | https://pypi.mirrors.ustc.edu.cn/simple/  | ★★★★★ | √   |
     | 国外1 | https://pypi.sdutlinux.org                | ★★★★★ |     |
     | 国外2 | https://pypi.org/simple                   | ★★★★  |     |
     | 阿里云 | http://mirrors.aliyun.com/pypi/simple/    | ★★★   | √   |
     | 豆瓣  | http://pypi.douban.com/simple/            | ★★★   | √   |
     | 清华  | https://pypi.tuna.tsinghua.edu.cn/simple/ | ★★★   | √   |
     | 中科技 | http://pypi.mirrors.ustc.edu.cn/simple/   | ★★★   | √   |

8. 安装常用环境包
   
   - pip3 install PyQt5
   
   - pip install PyQt5 -i https://pypi.douban.com/simple
   
   - 文件 > 设置 > 项目 > Python解释器 > +
     
     | 包名           | 用途       |
     | ------------ | -------- |
     | pyinstaller  | 封装exe    |
     | ttkbootstrap | GUI界面    |
     | PyQt5        | GUI界面    |
     | openpyxl     | 读写 Excel |
     | folium       | 地图可视化    |
     
     ```bat
     pip3 install pyinstaller     -i https://pypi.douban.com/simple
     pip3 install tqdm             -i https://pypi.douban.com/simple
     pip3 install windnd         -i https://pypi.douban.com/simple
     pip3 install configparser     -i https://pypi.douban.com/simple
     pip3 install numpy             -i https://pypi.douban.com/simple
     pip3 install Pandas         -i https://pypi.douban.com/simple
     pip3 install folium         -i https://pypi.douban.com/simple
     pip3 install ttkbootstrap     -i https://pypi.douban.com/simple
     pip3 install pyqt5             -i https://pypi.douban.com/simple
     pip3 install rich             -i https://pypi.douban.com/simple
     cmd
     ```

9. 添加PyCharm签名
   
   设置 > 编辑器 > 文件和代码模版 > Python Script
   
   ```python
    # version:  v3.0
    # time:     2024.03.10
   
    # -*- coding: utf-8 -*-
    """
    Time:   ${DATE} ${TIME}
    Auth:   Jeremy
    File:   ${NAME}.py
    IDE:    ${PRODUCT_NAME}
    GitHub: https://github.com/JeremyChim
    E-mail: jer888chim@outlook.com
    """
   ```
   
   ```python
   # version:  v2.0
   # time:     2024.02.02
   
   # -*- coding: utf-8 -*-
   """
   Time:   ${DATE} ${TIME}
   Auth:   Jeremy.Chim
   File:   ${NAME}.py
   IDE:    ${PRODUCT_NAME}
   GitHub: https://github.com/JeremyChim/${PROJECT_NAME}
   """
   ```
   
   ```python
   # version: v1.0
   # time : 2023.07.03
   
   """
   -*- coding: utf-8 -*-
   Time: ${DATE} ${TIME}
   Auth: Jeremy.Chim
   File: ${NAME}.py
   IDE: ${PRODUCT_NAME}
   GitHub: https://github.com/JeremyChim/${PROJECT_NAME}
   """
   ```

## 2、Python技巧

### lambda循环时的闭包问题

```python
# 这个例子展示了Python中闭包和变量作用域的行为差异
# 在第一个列表中，所有的lambda函数共享同一个变量i的引用，
# 当这些函数被调用时，i的值已经是循环结束时的最终值5

# 创建一个包含6个lambda函数的列表，每个函数都打印变量i的值
# 由于闭包的特性，所有函数共享同一个i变量的引用
fs = [lambda: print(i) for i in range(6)]
[f() for f in fs]  # 调用所有函数，输出结果为：5 5 5 5 5 5

# 通过使用默认参数x=i，将循环变量i在每次迭代时的值捕获下来
# 这样每个lambda函数都有自己独立的x变量副本
fs = [lambda x=i: print(x) for i in range(6)]
[f() for f in fs] # 调用所有函数，输出结果为：0 1 2 3 4 5
输出 0 1 2 3 4 5
```

### bat

```bat
pip freeze > requirements.txt
pip install -r requirements.txt
pyuic6.exe untitled.ui -o untitled.py
pyinstaller -F -w app.py
pyinstaller.exe app.spec
```

### Readme 自诉文件模板

```markdown
<p align="center"><img src="img\logo.png" width="200"/></p>
<h1 align="center">项目名</h1>
<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/Auth-Jeremy-brightgreen">
    <img alt="Static Badge" src="https://img.shields.io/badge/Version-v1.0.0-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/EnjoyDota-pink">
</p>

## ☕介绍
。。。


## 🌭安装
###。。。
###。。。
###。。。


## 🍕使用
###。。。
###。。。
###。。。


## 🍦联系
GitHub：[JeremyChim (github.com)](https://github.com/JeremyChim)
E-Mail：[jer888chim@outlook.com](mailto:jer888chim@outlook.com)
```

### except过于宽泛的错误

```python
# noinspection PyBroadExceptio
try：
    pass
except：
    pass
```

### QWidget继承 Qt6

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from untitled import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()  # 继承QWidget
        self.setupUi(self)  # UI初始化
        self.setWindowTitle('Title')  # 窗口标题

    def ui_init(self):
        Ui_Form.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
```

### QWidget继承

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from win import Ui_Form    # 导入UI


class Ui(Ui_Form):
    def __init__(self):
        super().__init__()


class Win(QWidget):
    def __init__(self):
        super().__init__()

    def initWindow(self):
        self.setWindowTitle('@Auth ： Jeremy.Chim')
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)    # 窗口居中
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()

    ui = Ui()
    ui.setupUi(win)

    win.initWindow()
    win.show()
    app.exec()
```

### 终端进度条 ( cmd )

```python
from rich.progress import track
from time import sleep

def do_step(step):
    sleep(0.001)

for step in track(range(1000)):
    do_step(step)
    # print(step)
```

### 循环加上进度条

tqdm :  西班牙语中 tqdm 是 te quiero demasiado ( I love you so much ) 的缩写

看来写这个函数的程序员还是个恋爱脑😂。。。

```python
from tqdm import tqdm
from time import sleep


for i in tqdm(range(100), desc='title'):
    sleep(0.1)
```

### 装饰器使用

```python
from time import time, sleep


def run_time(func):
    def wrapper(*args):
        ts1 = time()
        res = func(*args)
        ts2 = time()
        ts = ts2 - ts1
        print(f'run time : {ts:.2f} s')
        return res

    return wrapper


@run_time
def fun(max):
    for i in range(max):
        # print(i)
        sleep(0.01)

    return True


if __name__ == '__main__':

    res = fun(10)
    print(res)
```

### 将.qrc文件转换为.py(import xx_rc，运行报错)

```cmd
pyrcc5 resource.qrc -o resource_rc.py
```

### QT-Designer创建MainWindow

```python
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    Ui = Ui_MainWindow()
    Ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
```

### 外部载入QSS

```python
if __name__ == '__main__':
    class CommonHelper:
        def __init__(self):
            pass

        @staticmethod
        def readQss(style):
            with open(style, 'r') as f:
                return f.read()

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    Ui = Ui_MainWindow()
    Ui.setupUi(MainWindow)

    # Ubuntu ElegantDark MaterialDark ConsoleStyle AMOLED Aqua ManjaroMix NeonButtons MacOS
    styleFile = 'Ubuntu.qss'
    qssStyle = CommonHelper.readQss(styleFile)
    MainWindow.setStyleSheet(qssStyle)


    MainWindow.show()
    sys.exit(app.exec_())
```

### 套用qt_material

```python
if __name__ == '__main__':
    import sys
    from qt_material import apply_stylesheet

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    Ui = Ui_MainWindow()
    Ui.setupUi(MainWindow)
    apply_stylesheet(app, theme='dark_pink.xml')

    MainWindow.show()
    sys.exit(app.exec_())
```

### qt_material主题样式

```python
from qt_material import list_themes

list_themes()
```

```PYHTON
WARNING:root:qt_material must be imported after PySide or PyQt!


['dark_amber.xml',
 'dark_blue.xml',
 'dark_cyan.xml',
 'dark_lightgreen.xml',
 'dark_pink.xml',
 'dark_purple.xml',
 'dark_red.xml',
 'dark_teal.xml',
 'dark_yellow.xml',
 'light_amber.xml',
 'light_blue.xml',
 'light_cyan.xml',
 'light_cyan_500.xml',
 'light_lightgreen.xml',
 'light_pink.xml',
 'light_purple.xml',
 'light_red.xml',
 'light_teal.xml',
 'light_yellow.xml']
```

### openpyxl函数使用

```python
from openpyxl import *

wb = openpyxl.load_workbook('config.xlsx')
ws = wb['Sheet1']

v = ws.cell(1, 1).value
mr = ws.max_row
mc = ws.max_column

print(v)
print(mr)
print(mc)
```

### Pyqt5安装及使用方法

> https://zhuanlan.zhihu.com/p/162866700

### 使用UPX技术优化封装包

1. 下载[UPX](https://upx.github.io/)
2. 解压（只需要upx.exe文件）
3. 放入路径：D:\Python\Scripts\upx.exe（和pyinstaller.exe同级）
4. 封装，会发现exe包小了

> 实测数据
> 
> | 测试包                | 优化前     | 优化后     | 优化空间   |
> | ------------------ | ------- | ------- | ------ |
> | 以太网报文解析工具v2.50.exe | 23.5 MB | 16.4 MB | 7.1MB  |
> | Great Wall.exe     | 22.5 MB | 15.5 MB | 7 MB   |
> | layout.exe         | 34.6 MB | 27.0 MB | 7.6 MB |

### 封装py文件的bat脚本

```batch
Pyinstaller -F app.py
```

```batch
Pyinstaller -D app.py
```

```batch
Pyinstaller -F -w app.py
```

```batch
Pyinstaller -D -w app.py
```

```bash
Pyinstaller -F -w -i app.ico app.py
::Pyinstaller -D -w -i app.ico app.py
pause
```

### ttk的ui使用super()函数的原理

```python
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
```

### tkk模版

```python
# 外部函数调用（指定函数）
from ttkbootstrap.constants import *
from windnd import hook_dropfiles
from tkinter import filedialog
from tkinter.messagebox import showinfo
from time import sleep
from os import path as pa
from os import mkdir

import ttkbootstrap as ttk

# 自定义函数调用
# import func.flier as fl
# import func.udp17F as u17F
# import func.udp31B as u31B
# import func.udp146 as u146
# import func.udp5B3 as u5B3
# import func.rel as rel

# 类
class app(ttk.Frame):
    def __init__(self, win):
        super().__init__(win) # app = ttk.Frame(win)
        self.pack() # app.pack()

        # 容器
        self.sv = ttk.StringVar() # 主题名
        self.sv2 = ttk.StringVar() # log路径
        self.iv = ttk.IntVar(value=1) # 17F
        self.iv2 = ttk.IntVar(value=0) # 31B
        self.iv3 = ttk.IntVar(value=1) # 146
        self.iv4 = ttk.IntVar(value=0)  # rel
        self.iv5 = ttk.IntVar(value=0)  # 5B3

        # 外框
        f = ttk.Frame(padding=10)
        f.pack(fill=X, expand=YES, anchor=N)

        # 拖入读取
        hook_dropfiles(f, func=self.fun6)

        # 内框
        self.f2 = ttk.Frame(f, padding=10)
        self.lf = ttk.LabelFrame(f, text='日志', padding=10)
        self.lf2 = ttk.LabelFrame(f, text='信号', padding=10)
        self.lf3 = ttk.LabelFrame(f, text='操作', padding=10)

        self.f2.pack(fill=X, expand=YES)
        self.lf.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf2.pack(fill=X, expand=YES, pady=(0, 10))
        self.lf3.pack(fill=X, expand=YES)

        # 行
        self.row()
        self.row2()
        self.row3()
        self.row4()

    def row(self):
        '''主题栏'''
        f = self.f2
        sv = self.sv
        s = ttk.Style()
        tn = s.theme_names()
        i = tn.index(s.theme.name) # 初始索引值：morph主题为 9
        # print(i)

        b = ttk.Button(f, text='关于', command=self.fun)
        l = ttk.Label(f, text='主题')
        self.tm = ttk.Combobox(f, width=15, values=tn, textvariable=sv)
        self.tm.current(i) # 初始主题
        b2 = ttk.Button(f, text='应用', command=self.fun2)

        b.pack(side=LEFT, padx=(0,10))
        b2.pack(side=RIGHT, padx=(10,0))
        self.tm.pack(side=RIGHT, padx=(10,0))
        l.pack(side=RIGHT, padx=(10,0))
    def row2(self):
        '''日志栏'''
        lf = self.lf
        sv = self.sv2

        l = ttk.Label(lf, text='路径')
        e = ttk.Entry(lf, width=40, textvariable=sv)
        b = ttk.Button(lf, text='浏览', width=10, command=self.fun3)

        l.pack(side=LEFT, padx=10)
        e.pack(side=LEFT, padx=10, fill=X, expand=YES)
        b.pack(side=LEFT, padx=10)
    def row3(self):
        '''信号栏'''
        lf = self.lf2
        iv = self.iv
        iv2 = self.iv2
        iv3 = self.iv3
        iv4 = self.iv4
        iv5 = self.iv5

        cb = ttk.Checkbutton(lf,text='17F', variable=iv, onvalue=1, offvalue=0)
        cb2 = ttk.Checkbutton(lf,text='31B', variable=iv2, onvalue=1, offvalue=0)
        cb3 = ttk.Checkbutton(lf,text='146', variable=iv3, onvalue=1, offvalue=0)
        cb4 = ttk.Checkbutton(lf, text='REL', variable=iv4, onvalue=1, offvalue=0)
        cb5 = ttk.Checkbutton(lf, text='5B3', variable=iv5, onvalue=1, offvalue=0)

        cb.pack(side=LEFT, padx=10)
        cb3.pack(side=LEFT, padx=10)
        cb2.pack(side=LEFT, padx=10)
        cb5.pack(side=LEFT, padx=10)
        cb4.pack(side=LEFT, padx=10)
    def row4(self):
        '''操作栏'''
        lf = self.lf3

        self.b = ttk.Button(lf, text='生成csv', command=self.fun4)
        self.pb = ttk.Progressbar(lf, maximum=100, bootstyle='success-striped')

        self.b.pack(padx=10, fill=X, expand=YES)
        self.pb.pack(padx=10, fill=X, expand=YES)

    def fun(self):
        '''关于'''
        showinfo('关于 以太网报文解析工具',
                               '作者：Jer小铭😎 \n'
                               '技术支持：Mavis🤣 \n'
                               '建议提供：少基同学🤪 \n'
                               '思路提供：家文同学😏 \n'
                               '测试验证：少丽同学🤨 \n'
                               '缺陷提出：莲花同学🤓 \n'
                               '开发指导：媛媛同学🤠 \n'
                               '技术指导：坚莲大佬🧐 \n\n' 
                               '感谢各位同学和大佬的支持。^0^'
                               )
    def fun2(self):
        '''应用主题'''
        s = ttk.Style()
        cb = self.tm.get()

        s.theme_use(cb)
        print(f'应用主题:{cb}')
    def fun3(self):
        '''浏览文件'''
        sv = self.sv2
        path = filedialog.askopenfilename(title='选择日志文件')
        if path:
            sv.set(path)
    def fun4(self):
        '''生成csv'''
        t, t2, t3, t4, t5, t6, t7 = self.sv.get(), self.sv2.get(), self.iv.get(), self.iv2.get(), self.iv3.get(), self.iv4.get(), self.iv5.get()

        f = self.fun5
        pb = self.pb # 进度条
        b = self.b # 按钮

        print(f'当前设定:\n主题:{t}\n路径:{t2}\n17F:{t3}\n146:{t5}\n31B:{t4}\n5B3:{t7}\nrel:{t6}\n')

        # 创建cache文件夹
        if not pa.exists('cache'):
            mkdir('cache')

        # 过滤数据
        # fl.log_0011(t2),f(1,10,'筛选0011数据中...')
        #
        # # 创建csv文件夹
        # if not pa.exists('csv'):
        #     mkdir('csv')
        #
        # # 输出
        # if t3 == 1:
        #     fl.log_17F(),f(11,20,'17F数据处理中...')
        #     u17F.csv(),f(21,30,'17F数据生成中...')
        # if t5 == 1:
        #     fl.log_146(),f(31,40,'146数据处理中...')
        #     u146.csv(),f(41,50,'146生成处理中...')
        # if t4 == 1:
        #     fl.log_31B(),f(51,60,'31B数据处理中...')
        #     u31B.csv(),f(61,70,'31B数据生成中...')
        # if t7 == 1:
        #     fl.log_5B3(),f(71,80,'5B3数据处理中...')
        #     u5B3.csv(),f(81,90,'5B3生成处理中...')
        # if t6 == 1:
        #     if not pa.exists('cache/log_17F.txt'):
        #         fl.log_17F(), f(11, 20, '17F数据处理中...')
        #         u17F.csv(), f(21, 30, '17F数据生成中...')
        #     if not pa.exists('cache/log_146.txt'):
        #         fl.log_146(), f(31, 40, '146数据处理中...')
        #         u146.csv(), f(41, 50, '146生成处理中...')
        #     fl.log_rel()
        #     rel.csv()

        f(91,99,'csv文件生成中...')

        pb['value'] = 100
        b['text'] = 'csv文件已生成^-^'

        # 弹窗提示
        showinfo('(*^▽^*) Yeah~','csv文件已生成在根目录')
        b.config(state=NORMAL)

        # 初始化进度条
        pb['value'] = 0
        b['text'] = '生成csv'
    def fun5(self, i, j, l):
        '''进度更新'''
        pb = self.pb # 进度条
        b = self.b # 按钮
        j = j + 2
        for k in range(i,j):
            pb['value'] = k  # 修改进度
            pb.update()
            b['text'] = f'进度:{k}% {l}' # 修改按钮文本
            sleep(0.02)
    def fun6(self, a):
        '''拖入读取'''
        sv = self.sv2
        p = '\n'.join((item.decode('gbk') for item in a))
        sv.set(p)

if __name__ == '__main__':
    w = ttk.Window('----------调试窗口----------','litera')
    w.geometry('+640+340')
    app(w)
    l = ttk.Label(text='----------版本：Demo----------')
    l.pack(side=RIGHT, padx=10)
    w.mainloop()
```

### ini配置文件的使用

```ini
[mysql]
host=127.0.0.1
port=3306
user=root
password=yourpassword
dbname=test


[redis]
host=127.0.0.1
port=6379
password=88888
db=0
```

```python
import os
from configparser import ConfigParser

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "monitor_config.ini")
cf = ConfigParser()

cf.read('monitor_config.ini', encoding='utf-8')

print(cf.sections())        # ['mysql', 'redis']
print(cf.options('mysql'))  # 输出mysql下的所有配置项
print(cf.items('mysql'))    # 输出mysql下的所有键值对

print(cf.get('mysql', 'host'))  # 输出mysql 下配置项host的值
print(cf.getint('mysql', 'port'))  # 输出port
```

### 计算函数运行时间

```python
if __name__ == '__main__':
    from time import time
    ts1 = time()
    func()
    ts2 = time()
    ts = ts2 - ts1
    print(f'运行时间：{ts:.2f}秒')
```

### Subprocess函数的使用（adb交互）

```python
from subprocess import *
from byte import ret_byte
from str import ret_str


def ret_out_err(a:list):
    pop = Popen('adb shell', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    a = ret_byte(a)
    out, err = pop.communicate(input=a, timeout=1000)
    out, err = ret_str(out), ret_str(err)
    return out, err

if __name__ == '__main__':
    a = ['ls','exit']
    b = ['cat /oemdata/configs/7B120-1.cfg | grep ICCID','exit']
    c = ['cat /oemdata/configs/7B120-1.cfg | grep SN','exit']
    d = ['cat /oemdata/configs/7B120-1.cfg | grep ware','exit']
    e = ['export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` ',
         'dbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbox.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:server string:ecall_auto_num string:01056162092',
         'exit']

    out, err = ret_out_err(d)
    print(out, err)
```

```python
def ret_byte(a:list):
    a = "\n".join(a) + "\n"
    a = a.encode('utf-8')
    return a

if __name__ == '__main__':
    a = ['ls','exit']
    b = ['cat /oemdata/configs/7B120-1.cfg | grep ICCID','exit']
    c = ['cat /oemdata/configs/7B120-1.cfg | grep SN','exit']
    d = ['cat /oemdata/configs/7B120-1.cfg | grep ware','exit']
    e = ['export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` ',
         'dbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbox.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:server string:ecall_auto_num string:01056162092',
         'exit']

    print(ret_byte(d))
```

```python
def ret_str(a:bytes):
    a = a.decode('utf-8')
    a = a.replace('\r','')
    return a

if __name__ == '__main__':
    a = b'ls\r\r\nexit\r\r\n/ # ls\r\r\nWEBSERVER       etc             oemapp          run             tmp\r\r\nbin             firmware        oemappbak       sbin            usr\r\r\nboot            home            oemappbakromfs  sdcard          var\r\r\nbuild.prop      lib             oemappromfs     share\r\r\ncache           linuxrc         oemdata         sys\r\r\ndata            media           oemlog          system\r\r\ndev             mnt             proc            target\r\r\n/ # exit\r\r\n'
    b = b'cat /oemdata/configs/7B120-1.cfg | grep ICCID\r\r\nexit\r\r\n/ # cat /oemdata/configs/7B120-1.cfg | grep ICCID\r\r\n    ICCID="89860920740036750510";\r\r\n/ # exit\r\r\n'
    c = b'cat /oemdata/configs/7B120-1.cfg | grep SN\r\r\nexit\r\r\n/ # cat /oemdata/configs/7B120-1.cfg | grep SN\r\r\n    TBOXSN="C52XBDLM11190020";\r\r\n/ # exit\r\r\n'
    d = b'cat /oemdata/configs/7B120-1.cfg | grep ware\r\r\nexit\r\r\n/ # cat /oemdata/configs/7B120-1.cfg | grep ware\r\r\n      tbox_software = "1.09";\r\r\n      tbox_hardware = "1.00";\r\r\n      mcu_software = "220815V1.0";\r\r\n      um220_software="R3.6.0.0Build7723";\r\r\n      ec20_firmware = "EC20CEFARGR07A01M4G_OCPU_AMT";\r\r\n/ # exit\r\r\n'
    e = b'export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` \r\r\ndbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbox.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:server string:ecall_auto_num string:01056162092\r\r\nexit\r\r\n/ # export DBUS_SESSION_BUS_ADDRESS=`cat /tmp/.default-msgbus-session-address` \r\r\n/ # dbus-send --session --type=method_call --print-reply  --dest=com.yuantel.tbo\r\r\r\nx.file    /com/yuantel/tbox/file  com.yuantel.tbox.file.cfg_data_set string:serv\r\r\r\ner string:ecall_auto_num string:01056162092\r\r\nmethod return sender=:1.0 -> dest=:1.9 reply_serial=2\r\r\n/ # exit\r\r\n'

    print(ret_str(d))
```

### 常用的变量命名缩写

[编程语言中常用的变量命名缩写_假如我年华正好的博客-CSDN博客](https://blog.csdn.net/qq_37851620/article/details/94731227)

[.Net中控件的命名规则_基础应用_脚本之家 (jb51.net)](https://www.jb51.net/article/247298.htm)

## 🍦联系

GitHub：[JeremyChim (github.com)](https://github.com/JeremyChim)

E-Mail：[jer888chim@outlook.com](mailto:jer888chim@outlook.com)
