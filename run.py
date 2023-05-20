#导入gui库
import tkinter as tk
from tkinter import messagebox
import func as f
from tkcalendar import DateEntry

#方法转译
def get_position():
    f.gP()

def submit_date():
    date = date_entry.get()
    f.submit(date)

#gui
root = tk.Tk()
root.title("微信定点发送")

prompt_label = tk.Label(root, text=f.prompts)
prompt_label.pack()

position_button = tk.Button(root, text="获取基本位置", command=get_position)
position_button.pack()

date_entry = DateEntry(root)
date_entry.pack()

submit_button = tk.Button(root, text="执行", command=submit_date)
submit_button.pack()

root.mainloop()

