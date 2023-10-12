import tkinter as tk

calculation = ""

def add_to_calculaton(character):
    global calculation
    if character == 'C':
        clear_field()
        return
    if character == '=':
        try:
            calculation = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        except:
            clear_field()
            text_result.insert(1.0, "Error")
    else:
        calculation += str(character)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("275x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

buttons = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "(", ")", "C", "="
]

row = 2
col = 1

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, command=lambda b=button: add_to_calculaton(b), width=11, font=("Arial", 14))
    else:
        btn = tk.Button(root, text=button, command=lambda b=button: add_to_calculaton(b), width=5, font=("Arial", 14))
    btn.grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 1
        row += 1

btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculaton("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=5, column=5)

root.mainloop()
