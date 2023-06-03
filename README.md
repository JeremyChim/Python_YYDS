# Python_YYDS
小铭用来记录下Python技巧的一个小本子🤣

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




