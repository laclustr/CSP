from tkinter import *
import calc_buttons as cbuts

global res_str
global button_dict
global root
global label

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
cbuts.generate_buttons()

def button_clicked(button_val):
    global res_str
    res_str += button_val
    label.text=res_str







root.mainloop()