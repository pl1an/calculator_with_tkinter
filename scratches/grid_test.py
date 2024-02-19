import tkinter as tk
window = tk.Tk(className="calculator")

bframe = tk.Frame()

buttons=[]
for ii in range(7, 10):
    buttons.append(tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=bframe))
for ii in range(4, 7):
    buttons.append(tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=bframe))
for ii in range(1, 4):
    buttons.append(tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=bframe))

x=-1
y=1
for i in buttons:
    x+=1
    i.grid(row=y, column=x)
    if x == 2:
        x=-1
        y+=1

visor = tk.Label(text='', background='grey', width=50, height=3)
visor.grid()

bframe.grid()

window.mainloop()