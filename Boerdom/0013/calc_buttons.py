import main
from tkinter import *

def generate_buttons():
    button_vals = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "="]

    for i in main.button_dict:
        for j in range(len(button_vals)):
            main.button_dict[i] = Button(main.root, text=button_vals[j], command=main.button_clicked(button_vals[j]), font=("Arial", 12))
            main.button_dict[i].grid(row=1, column=j)