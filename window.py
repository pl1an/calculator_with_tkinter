class Calculator:

    def __init__(self):
        import tkinter as tk
        from functools import partial

        self.window = tk.Tk(className="calculator")
        self.window.resizable = (False, False)

        self.bframe = tk.Frame()
        self.visor = tk.Label(text='', background='white', width=42, height=3, relief=tk.GROOVE)

        self.operation_list = ["+", "-", "x", "/", "^"]

        self.operation_sign_in_screen = False
        self.dotted = False
        self.lone_signs = False
        self.adding_sign = False
        self.operating = False
        self.added_signs_plus_or_minus = 0

        self.numbers = []
        self.n0 = tk.Button(text='0', background='orange', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                            command=partial(self.button_press, "0"))
        self.ndot = tk.Button(text='.', background='orange', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                              command=partial(self.button_press, "."))
        for ii in range(7, 10):
            self.numbers.append(
                tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                          command=partial(self.button_press, str(ii))))
        for ii in range(4, 7):
            self.numbers.append(
                tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                          command=partial(self.button_press, str(ii))))
        for ii in range(1, 4):
            self.numbers.append(
                tk.Button(text=str(ii), background='orange', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                          command=partial(self.button_press, str(ii))))

        self.operations = [
            tk.Button(text='=', background='grey', width=7, height=3, relief=tk.GROOVE, master=self.bframe,
                      command=partial(self.button_press, "=")),
            tk.Button(text='+', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "+")),
            tk.Button(text='-', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "-")),
            tk.Button(text='x', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "x")),
            tk.Button(text='/', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "/")),
            tk.Button(text='CE', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "AC")),
            tk.Button(text='sqrt', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "sqrt")),
            tk.Button(text='^', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "^")),
            tk.Button(text='AC', background='grey', width=7, height=3, relief=tk.FLAT, master=self.bframe,
                      command=partial(self.button_press, "AC"))]

    def show(self):
        x = -1
        y = 1
        for i in self.numbers:
            x += 1
            i.grid(row=y, column=x)
            if x == 2:
                x = -1
                y += 1

        self.n0.grid(row=4, column=0)
        self.ndot.grid(row=4, column=1)

        self.operations[0].grid(row=4, column=2)
        self.operations[1].grid(row=4, column=3)
        self.operations[2].grid(row=3, column=3)
        self.operations[3].grid(row=2, column=3)
        self.operations[4].grid(row=1, column=3)
        self.operations[8].grid(row=1, column=4)
        self.operations[5].grid(row=2, column=4)
        self.operations[6].grid(row=3, column=4)
        self.operations[7].grid(row=4, column=4)

        self.visor.grid()
        self.bframe.grid()

    def event_loop(self):
        self.window.mainloop()

    def button_press(self, button_pressed):
        if self.visor["text"] == "infinity" or self.visor["text"] == "imaginary domain not supported":
            self.visor["text"] = " "

        try:
            int(button_pressed)
            if self.visor["text"] != "" and self.visor["text"][-1] in self.operation_list:
                self.visor["text"] += " " + button_pressed
            else:
                self.visor["text"] += button_pressed
            self.lone_signs = False
            self.operating = False
            self.added_signs_plus_or_minus = 0

        except ValueError:
            if button_pressed == "AC":
                self.visor["text"] = ""
                self.operation_sign_in_screen = False
                self.lone_signs = False
                self.added_signs_plus_or_minus = 0

            if button_pressed == "." and "." not in self.visor["text"][-1] and self.visor["text"][-1] != " " and not self.dotted:
                self.visor["text"] += button_pressed
                self.dotted = True

            if (button_pressed == "-" or button_pressed == "+") and self.visor["text"] == "":
                print("debug1")
                self.added_signs_plus_or_minus += 1
                self.operation_sign_in_screen = True
                self.visor["text"] += button_pressed + " "
                self.lone_signs = True
            elif (button_pressed == "-" or button_pressed == "+") and self.operation_sign_in_screen:
                self.added_signs_plus_or_minus += 1
                print("debug2")
                if self.lone_signs:
                    self.visor["text"] += button_pressed + " "
                else:
                    self.visor["text"] += " " + button_pressed
            elif button_pressed in self.operation_list and self.visor["text"] != "" and self.visor["text"][-1] != "." and not self.lone_signs:
                print("debug3")
                self.adding_sign = True
                if self.operation_sign_in_screen and self.visor["text"][-1] == " ":
                    if self.visor["text"][-2] == "+" or self.visor["text"][-2] == "-":
                        self.adding_sign = False
                    else:
                        self.visor["text"] = self.visor["text"][:-2:]
                if self.adding_sign:
                    if (self.visor["text"][-1] in self.operation_list[2::] and button_pressed in self.operation_list[2::]) or self.operating:
                        pass
                    else:
                        self.visor["text"] += " " + button_pressed
                        self.operation_sign_in_screen = True
                        self.operating = True
                        self.dotted = False
                        self.adding_sign = False

            if button_pressed == "=":
                self.calculate(do_sqrt=False)
            if button_pressed == "sqrt":
                self.calculate(do_sqrt=True)

    def calculate(self, do_sqrt):
        calculation = ""
        result = ""

        for i in self.visor["text"].split(" "):
            if i == "x":
                calculation += "*"
            elif i == "^":
                calculation += "**"
            else:
                calculation += i

        try:
            result = eval(calculation)
            if do_sqrt:
                from math import sqrt
                result = sqrt(result)
        except ZeroDivisionError:
            result = "infinity"
        except SyntaxError:
            pass
        except ValueError:
            result = "imaginary domain not supported"

        if result == "infinity" or result == "imaginary domain not supported":
            pass
        elif result < 0:
            result = "- " + str(result)[1::]

        if self.visor["text"] != "" and self.visor["text"][-1] != " ":
            self.visor["text"] = str(result)
