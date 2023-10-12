import tkinter as tk

calculation = ""


def add_to_calculaton(number):
    global calculation
    calculation += str(number)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaulate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("275x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculaton(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculaton(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculaton(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculaton(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculaton(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculaton(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculaton(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculaton(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculaton(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculaton(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculaton("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculaton("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculaton("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculaton("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculaton("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculaton(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaulate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)
root.mainloop()



import tkinter as tk

calculation = []

def add_to_calculation(char):
    calculation.append(char)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, ''.join(calculation))

def evaluate_calculation():
    try:
        result = str(eval(''.join(calculation)))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    calculation.clear()
    text_result.delete(1.0, "end")

def create_button(root, text, row, column, width=5):
    return tk.Button(root, text=text, command=lambda: add_to_calculation(text), width=width, font=("Arial", 14))

root = tk.Tk()
root.geometry("275x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

buttons = [
    create_button(root, "1", 2, 1),
    create_button(root, "2", 2, 2),
    create_button(root, "3", 2, 3),
    create_button(root, "4", 3, 1),
    create_button(root, "5", 3, 2),
    create_button(root, "6", 3, 3),
    create_button(root, "7", 4, 1),
    create_button(root, "8", 4, 2),
    create_button(root, "9", 4, 3),
    create_button(root, "0", 5, 2),
    create_button(root, "+", 2, 4),
    create_button(root, "-", 3, 4),
    create_button(root, "*", 4, 4),
    create_button(root, "/", 5, 4),
    create_button(root, "(", 5, 1),
    create_button(root, ")", 5, 3),
]

for button in buttons:
    button.grid()

btn_clear = create_button(root, "C", 6, 1, width=11)
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals = create_button(root, "=", 6, 3, width=11)
btn_equals.config(command=evaluate_calculation)
btn_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()
