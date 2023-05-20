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
