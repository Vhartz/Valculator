#!/usr/bin/env python3

import tkinter as tk

def press(key):
    if key == '=':
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erro")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("Calculadora Vhartz")
root.geometry("240x300")

entry = tk.Entry(root, width=16, font=('Arial', 18), bd=5, insertwidth=2, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    action = lambda x=button: press(x)
    tk.Button(root, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 12),
              command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
