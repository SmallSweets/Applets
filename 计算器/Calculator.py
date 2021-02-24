import tkinter as tk

all_input = ""
end_result = 0
dot_number = 0
symbol = ""

# 计算器主界面
window = tk.Tk()
window.title("计算器")
window.geometry("450x600")

# 显示框
show_result_text = tk.Text(window, width=430, height=5, font=20)
show_result_text.place(x=0, y=10)

def guiling():
    global all_input, end_result, dot_number
    show_result_text.delete('1.0', 'end')
    all_input = ""
    end_result = 0
    dot_number = 0


def click(x):
    global all_input, dot_number, symbol
    show_result_text.insert("end", x)
    if x == "÷":
        x = "/"
    elif x == "×":
        x = "*"
    #    获取用户输入的总的小数位数
    if x in "+-*/" and symbol != "":
        if "." in all_input:
            dot_number += len(all_input.split(symbol)[-1].split(".")[-1])
        all_input += x
    elif x in "+-*/" and symbol == "":
        if "." in all_input:
            dot_number += len(all_input.split(".")[-1])
        all_input += x
    else:
        all_input += x
    if x in "+-*/":
        symbol = x

def equals(x):
    global end_result, dot_number
    if "." in all_input:
        dot_number += len(all_input.split(symbol)[-1].split(".")[-1])
    show_result_text.insert("end", x)
    end_result = eval(all_input)
    # 如果用户输入的总的小数位数不为零，则根据小数位数格式化结果的精度
    if dot_number != 0:
        show_result_text.insert("end", "%.{}f".format(dot_number) % end_result)
    #     如果总的小数位数等于零，则直接将结果转化为int类型
    else:
        show_result_text.insert("end", int(end_result))
    print(dot_number)


# 按钮
calculate_button_1 = tk.Button(window, text="1", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("1"))))
calculate_button_1.place(x=10, y=410)
calculate_button_2 = tk.Button(window, text="2", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("2"))))
calculate_button_2.place(x=120, y=410)
calculate_button_3 = tk.Button(window, text="3", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("3"))))
calculate_button_3.place(x=230, y=410)
calculate_button_4 = tk.Button(window, text="4", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("4"))))
calculate_button_4.place(x=10, y=320)
calculate_button_5 = tk.Button(window, text="5", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("5"))))
calculate_button_5.place(x=120, y=320)
calculate_button_6 = tk.Button(window, text="6", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("6"))))
calculate_button_6.place(x=230, y=320)
calculate_button_7 = tk.Button(window, text="7", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("7"))))
calculate_button_7.place(x=10, y=230)
calculate_button_8 = tk.Button(window, text="8", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("8"))))
calculate_button_8.place(x=120, y=230)
calculate_button_9 = tk.Button(window, text="9", width=9, height=3, bg="#666666", font=20, command=(lambda : (click("9"))))
calculate_button_9.place(x=230, y=230)
calculate_button_0 = tk.Button(window, text="0", width=20, height=3, bg="#666666", font=20, command=(lambda : (click("0"))))
calculate_button_0.place(x=10, y=500)

calculate_button_dian = tk.Button(window, text=".", width=9, height=3, bg="#CCCCCC", font=20, command=(lambda : (click("."))))
calculate_button_dian.place(x=230, y=500)
calculate_button_jia = tk.Button(window, text="÷", width=9, height=3, bg="#FF9900", font=20, command=(lambda :(click("÷"))))
calculate_button_jia.place(x=340, y=140)
calculate_button_jian = tk.Button(window, text="×", width=9, height=3, bg="#FF9900", font=20, command=(lambda :(click("×"))))
calculate_button_jian.place(x=340, y=230)
calculate_button_cheng = tk.Button(window, text="-", width=9, height=3, bg="#FF9900", font=20, command=(lambda :(click("-"))))
calculate_button_cheng.place(x=340, y=320)
calculate_button_chu = tk.Button(window, text="+", width=9, height=3, bg="#FF9900", font=20, command=(lambda :(click("+"))))
calculate_button_chu.place(x=340, y=410)
calculate_button_deng = tk.Button(window, text="=", width=9, height=3, bg="#FF9900", font=20, command=(lambda :(equals("="))))
calculate_button_deng.place(x=340, y=500)

calculate_button_bai = tk.Button(window, text="％", width=9, height=3, bg="#CCCCCC", font=20)
calculate_button_bai.place(x=230, y=140)
calculate_button_fu = tk.Button(window, text="±", width=9, height=3, bg="#CCCCCC", font=20)
calculate_button_fu.place(x=120, y=140)
calculate_button_guil = tk.Button(window, text="C", width=9, height=3, bg="#CCCCCC", font=20, command=guiling)
calculate_button_guil.place(x=10, y=140)


window.mainloop()