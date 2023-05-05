import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

F = simpledialog.askinteger(title="Input",prompt="Gib die Temperatur in Fahrenheit an: ")
C = (F-32)/1.8
print (C)
messagebox.showinfo("Temperatur", C)