import tkinter as tk					
from tkinter import ttk


root = tk.Tk()
root.title("Tab Widget")
root.configure(background='#1e3743')
root.geometry("900x480")
root.maxsize(width=900, height=480)  
root.minsize(width=800, height=450)


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Material Hospitalar')
tabControl.add(tab2, text ='Medicamentos Hospitalar')
tabControl.pack(expand = 1, fill ="both")


root.mainloop()
