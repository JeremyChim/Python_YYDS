# Python_YYDS

小铭用来记录下Python技巧的一个小本子🤣

# 安装Python环境

1. 下载[Python](https://www.python.org/downloads/windows/)

2. 下载[PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

3. 下载[Git](https://git-scm.com/downloads)

4. 下载[Github Desktop](https://desktop.github.com/)

5. 安装PyCharm插件
   
   > Chinese (Simplified) Language Pack / 中文语言包
   > 
   > One Dark theme
   > 
   > CMD Support

6. 新建PycharmProject项目
   
   > 选择：先前配置的解释器
   > 
   > 不勾选：创建main.py

7. 添加PyCharm镜像源
   
   > 文件 > 设置 > 项目 > Python解释器 > + > 管理仓库
   > 
   > | 镜像源 | 网址                                        | 推荐度   | 免翻墙 |
   > |:--- |:----------------------------------------- |:----- |:---:|
   > | 中科大 | https://pypi.mirrors.ustc.edu.cn/simple/  | ★★★★★ | √   |
   > | 国外1 | https://pypi.sdutlinux.org                | ★★★★★ |     |
   > | 国外2 | https://pypi.org/simple                   | ★★★★  |     |
   > | 阿里云 | http://mirrors.aliyun.com/pypi/simple/    | ★★★   | √   |
   > | 豆瓣  | http://pypi.douban.com/simple/            | ★★★   | √   |
   > | 清华  | https://pypi.tuna.tsinghua.edu.cn/simple/ | ★★★   | √   |
   > | 中科技 | http://pypi.mirrors.ustc.edu.cn/simple/   | ★★★   | √   |

8. 安装常用环境包
   
   > 文件 > 设置 > 项目 > Python解释器 > +
   > 
   > | 包名           | 用途       |
   > | ------------ | -------- |
   > | pyinstaller  | 封装exe    |
   > | ttkbootstrap | GUI界面    |
   > | PyQt5        | GUI界面    |
   > | openpyxl     | 读写 Excel |
   > | folium       | 地图可视化    |

9. 添加PyCharm签名
   
   > 设置 > 编辑器 > 文件和代码模版 > Python Script
   > 
   > ```python
   > # -*- coding: utf-8 -*-
   > # @Time ： ${DATE} ${TIME}
   > # @Auth ： JeremyChim
   > # @File ：${NAME}.py
   > # @IDE ：${PRODUCT_NAME}
   > # @Github ：https://github.com/JeremyChim/
   > ```

# 使用UPX技术优化封装包

1. 下载[UPX](https://upx.github.io/)

2. 解压（只需要upx.exe文件）

3. 放入路径：D:\Python\Scripts\upx.exe（和pyinstaller.exe同级）

4. 执行封装指令

> 实测数据
> 
> | 测试包                | 优化前     | 优化后     | 优化空间   |
> | ------------------ | ------- | ------- | ------ |
> | 以太网报文解析工具v2.50.exe | 23.5 MB | 16.4 MB | 7.1MB  |
> | Great Wall.exe     | 22.5 MB | 15.5 MB | 7 MB   |
> | layout.exe         | 34.6 MB | 27.0 MB | 7.6 MB |

# 封装py文件的bat脚本

```batch
Pyinstaller -F -w -i app.ico app.py
Pyinstaller -D -w -i app.ico app.py
pause 使用UPX技术优化封装包
```

# ttk的ui使用super()函数的原理

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
