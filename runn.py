import PyOfficeRobot
from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox

def merge_time():
    hour = hour_spinbox.get()
    minute = minute_spinbox.get()
    second = second_spinbox.get()
    if hour == '0':
        hour = '00'
    if minute == '0':
        minute = '00'
    if second == '0':
        second = '00'
    time = hour + ':' + minute + ':' + second
    print(time)
    return time

def timingSend():
    global person, msg
    p = person.get()
    m = msg.get()
    time = merge_time()
    if p =="" or m=="":
        print(time, p, m)
        tk.messagebox.showerror(title='错误', message='请输入发送对象和发送信息')
        return
    else:
        PyOfficeRobot.chat.send_message_by_time(who=p, message=m, time=time)



root = tk.Tk()
root.title("微信定点发送")
tk.Label(root, text="提示:执行完成后无响应是正常现象").pack()
tk.Label(root, text="请输入发送的对象名").pack()
person = tk.Entry(root)
person.pack()
tk.Label(root, text="请输入要发送的信息").pack()
msg = tk.Entry(root)
msg.pack()
tk.Label(root, text="请输入时间(时,分,秒)").pack()

hour_spinbox = tk.Spinbox(root, from_=00, to=23, width=2)
hour_spinbox.pack(side=tk.LEFT)

minute_spinbox = tk.Spinbox(root, from_=00, to=59, width=2)
minute_spinbox.pack(side=tk.LEFT)

second_spinbox = tk.Spinbox(root, from_=00, to=59, width=2)
second_spinbox.pack(side=tk.LEFT)

confirm_button = tk.Button(root, text="发送", command=timingSend)
confirm_button.pack(side=tk.LEFT)

root.mainloop()