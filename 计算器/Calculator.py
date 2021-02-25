import tkinter as tk
from decimal import Decimal

all_input = ""
result = 0
number_list = []
symbol_list = []
dec_type = type(Decimal("1").quantize(Decimal("0")))
int_type = type(1)

# 计算器主界面
window = tk.Tk()
window.title("计算器")
window.geometry("450x600")
window['background'] = 'black'

# 显示框
show_result_text = tk.Text(window, width=430, height=3, font=("黑体", 35, "bold"), bg="black", fg="white")
show_result_text.place(x=0, y=10)

# 归零键点击时执行的函数
def guiling():
    global all_input, number_list, symbol_list
    show_result_text.delete('1.0', 'end')
    all_input = ""
    number_list = []
    symbol_list = []

#  等号键，归零键以外的其他键点击时执行的函数
def click(x):
    global all_input, symbol
    if x in "+-×÷％±":
        if x == "％":
            show_result_text.delete("1.0", "end")
            show_result_text.insert("end", eval(all_input+"/100"))
            # 更新all_input的值
            all_input = str(eval(all_input + "/100"))
        if x == "±":
            show_result_text.delete("1.0", "end")
            if "-" in all_input:
                all_input = all_input.replace("-","")
                show_result_text.insert("end", all_input)
            else:
                all_input = "-" + all_input
                show_result_text.insert("end", all_input)
        if x in "+-×÷":
            # 加减乘除键点击时改变背景颜色和字体颜色
            if x == "+":
                calculate_button_jia['bg'] = "white"
                calculate_button_jia['fg'] = "orange"
            elif x == "÷":
                calculate_button_chu['bg'] = "white"
                calculate_button_chu['fg'] = "orange"
            elif x == "×":
                calculate_button_cheng['bg'] = "white"
                calculate_button_cheng['fg'] = "orange"
            elif x == "-":
                calculate_button_jian['bg'] = "white"
                calculate_button_jian['fg'] = "orange"
            show_result_text.delete("1.0", "end")
            number_list.append(all_input)
            print(all_input)
            symbol_list.append(x)
            all_input = ""
    else:
        # 点击数字键时，恢复加减乘除键的背景颜色和字体颜色
        if len(symbol_list) > 0:
            if symbol_list[-1] == "+":
                calculate_button_jia['bg'] = "#FF9900"
                calculate_button_jia['fg'] = "white"
            elif symbol_list[-1] == "-":
                calculate_button_jian['bg'] = "#FF9900"
                calculate_button_jian['fg'] = "white"
            elif symbol_list[-1] == "×":
                calculate_button_cheng['bg'] = "#FF9900"
                calculate_button_cheng['fg'] = "white"
            elif symbol_list[-1] == "÷":
                calculate_button_chu['bg'] = "#FF9900"
                calculate_button_chu['fg'] = "white"

        show_result_text.insert("end", x)
        all_input += x

# 等号键点击时执行的函数
def equals(x):
    global result
    show_result_text.delete("1.0", "end")
    # 将式子中的最后一个数添加到number列表中
    number_list.append(all_input)

    # 先计算式子中的乘法和除法
    for symbol in symbol_list:
        if symbol == "×":
            index = symbol_list.index(symbol)
            x = number_list[index]
            y = number_list[index+1]
            # 如果不是整数，则计算小数的位数，使用Decimal根据小数位数规范精度问题
            if "." in x:
                x_dot = len(x.split(".")[-1]) * "0"
                x = Decimal(x).quantize(Decimal("0."+ x_dot))
            # 如果是整数,则直接转换为int类型
            else:
                x = int(number_list[index])
            # 和上面的操作相同
            if "." in y:
                y_dot = len(y.split(".")[-1]) * "0"
                y = Decimal(y).quantize(Decimal("0." + y_dot))
            else:
                y = int(number_list[index+1])
            # 乘号两侧两个数的运算结果
            result = x * y
            # 删除运算后的两个数
            number_list.pop(index)
            number_list.pop(index)
            # 删除运算后的符号
            symbol_list.pop(index)
            # 将result添加到number列表中，如果报错说明此时number列表为空，也就表明式子运算完毕
            try:
                number_list.insert(index,result)
            except:
                number_list[0] = result

    for symbol in symbol_list:
        if symbol == "÷":
            index = symbol_list.index(symbol)
            x = number_list[index]
            y = number_list[index + 1]
            # int类型和Decimal类型不能遍历
            try:
                # 如果不是整数，则计算小数的位数，使用Decimal根据小数位数规范精度问题
                if "." in x:
                    x_dot = len(x.split(".")[-1])
                    x = Decimal(x).quantize(Decimal("0." + "0" * x_dot))
                # 如果是整数,则直接转换为int类型
                else:
                    x = int(number_list[index])
            except:
                pass
            # int类型和Decimal类型不能遍历
            try:
                # 和上面的操作相同
                if "." in y:
                    y_dot = len(y.split(".")[-1])
                    y = Decimal(y).quantize(Decimal("0." + "0" * y_dot))
                else:
                    y = int(number_list[index+1])
            except:
                pass
            # 除号两侧两个数的运算结果
            result = x / y
            # 删除运算后的两个数
            number_list.pop(index)
            number_list.pop(index)
            # 删除运算后的符号
            symbol_list.pop(index)
            # 将result添加到number列表中，如果报错说明此时number列表为空，也就表明式子运算完毕
            try:
                number_list.insert(index,result)
            except:
                number_list[0] = result

    # 再然后计算式子中的加法和减法
    for symbol in symbol_list:
        if symbol == "-":
            index = symbol_list.index(symbol)
            x = number_list[index]
            y = number_list[index + 1]
            if type(x) != dec_type and type(x) != int_type:
                if "." in x:
                    x_dot = len(x.split(".")[-1])
                    x = Decimal(x).quantize(Decimal("0." + "0" * x_dot))
                else:
                    x = int(number_list[index])
            if type(y) != dec_type and type(y) != int_type:
                if "." in y:
                    y_dot = len(y.split(".")[-1])
                    y = Decimal(y).quantize(Decimal("0." + "0" * y_dot))
                else:
                    y = int(number_list[index+1])
            # 减号两侧两个数的运算结果
            result = x - y
            # 删除运算后的两个数
            number_list.pop(index)
            number_list.pop(index)
            # 将result添加到number列表中，如果报错说明此时number列表为空，也就表明式子运算完毕
            try:
                number_list.insert(index,result)
            except:
                number_list[0] = result
            # 删除运算后的符号
            symbol_list.pop(index)

    for symbol in symbol_list:
        if symbol == "+":
            index = symbol_list.index(symbol)
            x = number_list[index]
            y = number_list[index+1]
            if type(x) != dec_type and type(x) != int_type:
                if "." in x:
                    x_dot = len(x.split(".")[-1])
                    x = Decimal(x).quantize(Decimal("0." + "0" * x_dot))
                else:
                    x = int(number_list[index])
            if type(y) != dec_type and type(y) != int_type:
                if "." in y:
                    y_dot = len(y.split(".")[-1])
                    y = Decimal(y).quantize(Decimal("0." + "0" * y_dot))
                else:
                    y = int(number_list[index+1])
            # 加号两侧两个数的运算结果
            result = x + y
            # 删除运算后的两个数
            number_list.pop(index)
            number_list.pop(index)
            # 将result添加到number列表中，如果报错说明此时number列表为空，也就表明式子运算完毕
            try:
                number_list.insert(index,result)
            except:
                number_list[0] = result
            # 删除运算后的符号
            symbol_list.pop(index)

    # 最后的结果就是number列表中仅剩的数
    show_result_text.insert("end",number_list[0])

# 按钮
calculate_button_1 = tk.Button(window, text="1", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("1"))), fg='white')
calculate_button_1.place(x=10, y=425)
calculate_button_2 = tk.Button(window, text="2", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("2"))), fg='white')
calculate_button_2.place(x=120, y=425)
calculate_button_3 = tk.Button(window, text="3", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("3"))), fg='white')
calculate_button_3.place(x=230, y=425)
calculate_button_4 = tk.Button(window, text="4", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("4"))), fg='white')
calculate_button_4.place(x=10, y=335)
calculate_button_5 = tk.Button(window, text="5", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("5"))), fg='white')
calculate_button_5.place(x=120, y=335)
calculate_button_6 = tk.Button(window, text="6", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("6"))), fg='white')
calculate_button_6.place(x=230, y=335)
calculate_button_7 = tk.Button(window, text="7", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("7"))), fg='white')
calculate_button_7.place(x=10, y=245)
calculate_button_8 = tk.Button(window, text="8", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("8"))), fg='white')
calculate_button_8.place(x=120, y=245)
calculate_button_9 = tk.Button(window, text="9", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("9"))), fg='white')
calculate_button_9.place(x=230, y=245)
calculate_button_0 = tk.Button(window, text="0", width=13, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("0"))), fg='white')
calculate_button_0.place(x=10, y=515)

calculate_button_dian = tk.Button(window, text=".", width=6, height=2, bg="#666666", font=("黑体", 20, "bold"), command=(lambda : (click("."))), fg='white')
calculate_button_dian.place(x=230, y=515)
calculate_button_chu = tk.Button(window, text="÷", width=6, height=2, bg="#FF9900", font=("黑体", 20, "bold"), command=(lambda :(click("÷"))), fg='white')
calculate_button_chu.place(x=340, y=155)
calculate_button_cheng = tk.Button(window, text="×", width=6, height=2, bg="#FF9900", font=("黑体", 20, "bold"), command=(lambda :(click("×"))), fg='white')
calculate_button_cheng.place(x=340, y=245)
calculate_button_jian = tk.Button(window, text="-", width=6, height=2, bg="#FF9900", font=("黑体", 20, "bold"), command=(lambda :(click("-"))), fg='white')
calculate_button_jian.place(x=340, y=335)
calculate_button_jia = tk.Button(window, text="+", width=6, height=2, bg="#FF9900", font=("黑体", 20, "bold"), command=(lambda :(click("+"))), fg='white')
calculate_button_jia.place(x=340, y=425)
calculate_button_deng = tk.Button(window, text="=", width=6, height=2, bg="#FF9900", font=("黑体", 20, "bold"), command=(lambda :(equals("="))), fg='white')
calculate_button_deng.place(x=340, y=515)

calculate_button_bai = tk.Button(window, text="％", width=6, height=2, bg="#CCCCCC", font=("黑体", 20, "bold"), command=(lambda :(click("％"))))
calculate_button_bai.place(x=230, y=155)
calculate_button_fu = tk.Button(window, text="±", width=6, height=2, bg="#CCCCCC", font=("黑体", 20, "bold"), command=(lambda :(click("±"))))
calculate_button_fu.place(x=120, y=155)
calculate_button_guil = tk.Button(window, text="C", width=6, height=2, bg="#CCCCCC", font=("黑体", 20, "bold"), command=guiling)
calculate_button_guil.place(x=10, y=155)

print(-0.1-0.2)

window.mainloop()