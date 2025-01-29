from tkinter import *

res_str = "0"
button_dict = {
    "0": None,
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "7": None,
    "8": None,
    "9": None,
    "+": None,
    "-": None,
    "*": None,
    "/": None,
    "=": None
}

root = Tk()
root.title("Calculator")
root.geometry("500x500")
label = Label(root, text=res_str, font=("Arial", 50))
label.grid(row=0, column=0)

def button_clicked(button_val):
    global res_str
    global label
    res_str += button_val

def generate_buttons():
    button_vals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "="]

    for i in button_dict:
        for j in range(len(button_vals)):
            button_dict[i] = Button(root, text=button_vals[j], command=button_clicked(button_vals[j]), font=("Arial", 12))
            button_dict[i].grid(row=1, column=j)
generate_buttons()






root.mainloop()