'''
Author: Mr.Mei
Date: 2021-10-11 11:11:19
'''

# %%
import tkinter as tk  # 导入tkinter模块。为了方便后续讲解，命名为 tk。
import tkinter.messagebox  # 引入弹窗库，防止解释器弹出报错。
# from random_select import pair
import random_select

window = tk.Tk()  # 生成主窗口，命名 window

sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

window.title('代码评审小工具')  # 定义主窗口标题

ww = 300

wh = 200

x = (sw-ww) / 2

y = (sh-wh) / 2

window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

# window.geometry('300x200')  # 定义主窗口的长宽


def getTextInput():
    result = content.get("1.0", "end").replace("\n", "")
    return result


def display_messagebox():  # 定义一个响应函数，目前内容为空
    # student = ['郑萍军', '唐鑫', '黎少忠', '余光生', '莫少华']  # 定义列表这里存放你要点名同学的名字
    student = getTextInput().split(',')
    text = random_select.pairs2(student)
    tk.messagebox.showinfo(title='结果', message=text)  # 消息提醒弹窗，点击确定返回值为 ok


# text = tk.Text(window, width=30, height=4).pack()
content = tk.Text(window, height=3)  # 创建文本框控件，并制定文本框的高度
content.pack()

str1 = '郑萍军,唐鑫,黎少忠,余光生,莫少华'

content.insert(tk.INSERT, str1)


# 定义一个按钮，用来后续触发弹窗，为了方便直接pack()吧。
tk.Button(window, text='随机配对', command=display_messagebox).place(x=100, y=100)

window.mainloop()  # 主窗口循环运行

# %% [markdown]
# ## 二、[封装](https://blog.csdn.net/lxt610/article/details/111169402)
#
# pip3 install pyinstaller
#
# 在终端中cd 到项目路径，也就是main函数所在文件main.py， 切换完成后依次输入下面命令:
#
# > * sudo pyinstaller --windowed --onefile --clean --noconfirm app.py
# > * sudo pyinstaller --clean --noconfirm --windowed --onefile app.spec
#
# * [参考](https://blog.csdn.net/lxt610/article/details/111169402)
