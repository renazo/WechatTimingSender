#导入基本库
import pyautogui
import time
from datetime import datetime
import threading
from pynput import mouse

def validate_date(date_text):
    try:
        if date_text != '':
            datetime.strptime(date_text, '%Y/%m/%d/%H/%M/%S')
        return True
    except ValueError:
        return False

def execute_code():
    # 在这里添加你想在指定时间执行的代码
    print("执行代码")

def schedule_execution(input_time):
    if validate_date(input_time):
        target_time = datetime.strptime(input_time, '%Y/%m/%d/%H/%M/%S')
        delay = (target_time - datetime.now()).total_seconds()
        if delay > 0:
            threading.Timer(delay, execute_code).start()
            messagebox.showinfo("成功", "代码将在指定时间执行")
        else:
            messagebox.showinfo("错误", "输入的时间已过去，请输入未来的时间")
    else:
        messagebox.showinfo("错误", "输入的日期时间格式不正确，请按照 '年/月/日/时/分/秒' 的格式输入")

def submit():
    input_time = e.get()
    schedule_execution(input_time)

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
