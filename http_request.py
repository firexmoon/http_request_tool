from tkinter import Tk, Entry, Button, END
from tkinter.scrolledtext import ScrolledText
import requests
import time


demo_URL = 'http://10.1.72.98:7080/TSM/mobileType/checkMobile'
demo_headers = '''{
    "Content-Type": "application/json"
}'''
demo_request = '''{
    "cpuType": "armeabi-v7a",
    "terminalType": "ALP-AL00",
    "terminlaOs": "10",
    "terminlaProvider": "HUAWEI"
}'''



#获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time


def func_clear():
    txt_recv.delete(1.0, END)

def func_send():
    url = txt_url.get().strip()
    body = txt_body.get(1.0, END).strip()
    headers = txt_headers.get(1.0, END).strip()

    try:
        if headers:
            e_headers = eval(headers)
        else:
            e_headers = None

        if e_headers and "Content-Type" in e_headers and e_headers["Content-Type"] == "application/json":
            resp = requests.post(url, headers=e_headers, json=eval(body))
        else:
            resp = requests.post(url, headers=e_headers, data=eval(body))

        r_text = resp.text
        r_headers = str(resp.headers)
        r_status_code = str(resp.status_code)
        log = get_current_time() + '\n' + '-----URL-----\n' + url + '\n-----headers-----\n' + headers + '\n-----body-----\n' + body + '\n\n-----status_code-----\n' + r_status_code + '\n-----headers-----\n' + r_headers + '\n-----text-----\n' + r_text +'\n\n\n'
    except requests.exceptions.ConnectionError:
        log = get_current_time() + '\n' + '-----URL-----\n' + url + '\n-----Error-----\nConnectionError\n\n\n'
        
    txt_recv.insert(1.0, log)
    return


root = Tk()
root.title('http request tool')

txt_url = Entry(root, width=60)
txt_url.insert(0, demo_URL)
txt_headers = ScrolledText(root, width=70, height=3)
txt_headers.insert(1.0, demo_headers)
txt_body = ScrolledText(root, width=70, height=50)
txt_body.insert(1.0, demo_request)
bt_send = Button(root, text='send', width=10, command=func_send)
bt_clear = Button(root, text='clear', width=10, command=func_clear)
txt_recv = ScrolledText(root, width=70, height=50)


txt_url.grid(row=0, column=0, padx=10, pady=10)
bt_clear.grid(row=0, column=2, padx=10, pady=10)
txt_headers.grid(row=1, column=0, padx=10, pady=2)
txt_body.grid(row=2, column=0, padx=10, pady=2)
bt_send.grid(row=2, column=1, padx=10, pady=10)
txt_recv.grid(row=2, column=2, padx=10, pady=10)


root.mainloop()