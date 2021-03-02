import tkinter as tk
import DownloadVideo as dy

window = tk.Tk()
window.title("Watermark killer")
window.geometry("500x500")

Url_lable = tk.Label(window,text="视频链接：",font=15)
Url_lable.place(x=20,y=20)

url_input = tk.StringVar()
url_input.set("请输入视频链接")
Url_entry = tk.Entry(window,textvariable=url_input,font=15,width=30)
Url_entry.place(x=120,y=22)

Download_url_lable = tk.Label(window,text="下载路径：",font=15)
Download_url_lable.place(x=20,y=80)

download_url = tk.StringVar()
download_url.set("不输入默认为：D://")
Download_url_entry = tk.Entry(window,textvariable=download_url,font=15,width=30)
Download_url_entry.place(x=120,y=80)

type_choice = tk.IntVar()
Type_lable = tk.Label(window,text="请选择下载类型：",font=15)
Type_lable.place(x=20,y=140)

radiobutton_choice = tk.IntVar()
Type_radiobutton_1 = tk.Radiobutton(window,text="有水印",variable=radiobutton_choice,value=1,font=12)
Type_radiobutton_2 = tk.Radiobutton(window,text="无水印",variable=radiobutton_choice,value=2,font=12)
Type_radiobutton_1.place(x=200,y=140)
Type_radiobutton_2.place(x=300,y=140)

def download():
    ShowInfo_text.insert("end","---------------------------正在执行--------------------------------\n")
    url = url_input.get()
    download_local = download_url.get()
    download_type = radiobutton_choice.get()
    info = dy.do(url,download_local,download_type)
    ShowInfo_text.insert("end",info+"\n")


Download_button = tk.Button(window,text="下载",command=download,font=15)
Download_button.place(x=200,y=190)


ShowInfo_text = tk.Text(window,width=68,height=17)
ShowInfo_text.insert("end","下载提示信息\n")
ShowInfo_text.place(x=10,y=260)

window.mainloop()