from tkinter import * 
from tkinter.scrolledtext import ScrolledText
import requests
import time


#获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time


def func_clear():
    txt_recv.delete(1.0, END)

def func_send():
    msg_send = txt_send.get(1.0, END)
    url = txt_host.get()
    msg_recv = requests.post(url, data=msg_send).text
    log = get_current_time() + '\n' + '-----URL-----\n' + url + '\n' + '-----send-----\n' + msg_send + '\n' + '-----recv-----\n' + msg_recv + '\n\n'
    txt_recv.insert(1.0, log)
    return


root = Tk()
root.title('http request tool')

txt_host = Entry(root, width=60)
txt_host.insert(0, 'http://')
txt_send = ScrolledText(root, width=70, height=50)
bt_send = Button(root, text='send', width=10, command=func_send)
bt_clear = Button(root, text='clear', width=10, command=func_clear)
txt_recv = ScrolledText(root, width=70, height=50)


txt_host.grid(row=0, column=0, padx=10, pady=10)
bt_clear.grid(row=0, column=2, padx=10, pady=10)
txt_send.grid(row=1, column=0, padx=10, pady=10)
bt_send.grid(row=1, column=1, padx=10, pady=10)
txt_recv.grid(row=1, column=2, padx=10, pady=10)


root.mainloop()