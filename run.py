#导入基本库
import pyautogui
import time
import tkinter as tk
from datetime import datetime
import threading
from tkinter import messagebox
from pynput import mouse


prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'
#文本框内容转换
def PChange(pnum):
    global prompts
    if pnum == 100:
        #初始
        prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'
        #获取输入框位置期间
    elif pnum == 101:
            prompts = '请点击你的鼠标左键到微信的输入框上'
        #获取发送按钮位置期间
    elif pnum == 102:
            prompts = '请点击你的鼠标左键到微信的发送按钮上'
    else:
        prompts = '点击获取基本位置后输入你需要执行的时间 然后点击执行来准备执行操作'



#获取基本鼠标位置
sendPx = 0
sendPy = 0
inputPx = 0
inputPy = 0
def gP():
    global sendPx, sendPy, inputPx, inputPy
    #如果左键按下则获取鼠标位置
    PChange(101)
    if pyautogui.mouseDown():
        inputPx, inputPy = pyautogui.position()
    # 如果左键按下则获取鼠标位置
    PChange(102)
    if pyautogui.mouseDown():
        sendPx, sendPy = pyautogui.position()
    PChange(100)
    print(inputPx, inputPy, sendPx, sendPy)





#gui
window = tk.Tk()
window.title('微信定点回复')
tips = tk.Label(window, text=prompts).pack()
gpb = tk.Button(window, text='获取基本位置', width=15, height=2, command = gP)
#日期时间输入框(24小时制)
#performT = tk.Label(window, text='请输入你需要执行的时间').place(x=10, y=50)

l = tk.Label(window, text="请输入日期和时间 (格式: 年/月/日/时/分/秒): ")
l.pack()

e = tk.Entry(window)
e.pack()

b = tk.Button(window, text="提交", command=submit)
b.pack()





gpb.pack()
window.mainloop()

