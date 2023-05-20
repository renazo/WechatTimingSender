#导入gui库
import tkinter as tk
from tkinter import messagebox

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

