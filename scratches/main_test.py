import tkinter as tk
window = tk.Tk(className="calculator")

bframe = tk.Frame()
visor = tk.Label(text='', background='white', width=42, height=3, relief=tk.GROOVE)


numbers=[]
n0 = tk.Button(text='0', background='orange', width=7, height=3, relief=tk.FLAT, master=bframe)
ndot = tk.Button(text='.', background='orange', width=7, height=3, relief=tk.FLAT, master=bframe)
for ii in range(7, 10):
    numbers.append(tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=bframe))
for ii in range(4, 7):
    numbers.append(tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=bframe))
for ii in range(1, 4):
    numbers.append(tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=bframe))

operations = [tk.Button(text='=', background='grey', width=7, height=3, relief=tk.GROOVE, master=bframe),
              tk.Button(text='+', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='-', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='x', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='/', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='CE', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='sqrt', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='^', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe),
              tk.Button(text='AC', background='grey', width=7, height=3, relief=tk.FLAT, master=bframe)]


x=-1
y=1
for i in numbers:
    x+=1
    i.grid(row=y, column=x)
    if x == 2:
        x=-1
        y+=1

n0.grid(row=4, column=0)
ndot.grid(row=4, column=1)

operations[0].grid(row=4, column=2)
operations[1].grid(row=4, column=3)
operations[2].grid(row=3, column=3)
operations[3].grid(row=2, column=3)
operations[4].grid(row=1, column=3)
operations[8].grid(row=1, column=4)
operations[5].grid(row=2, column=4)
operations[6].grid(row=3, column=4)
operations[7].grid(row=4, column=4)

visor.grid()
bframe.grid()

window.mainloop()
