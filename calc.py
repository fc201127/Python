#!/usr/bin/env python3
import tkinter as tk

# Calculator (child class) 繼承 tk.Frame (parent class)
# 表示 Calculator 擁有 tk.Frame 的特性 (member function, attributes)
# 可以理解成: Calculator "is a" tk.Frame
# 
class Calculator(tk.Frame):
    def __init__(self): # 所有 class 都要有一個 __init__(self) 的 func.
                        # 可以理解成, Calculator "has a" __init__ func.
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()    # cal.createWidgets()

    def createWidgets(self):
        self.lblNum  = tk.Label(self, text="0")
        self.btnNum1 = tk.Button(self, text="1")
        self.lblNum.grid(column = 0, row = 0)
        self.btnNum1.grid(column = 0, row = 1)

        
def main():
    cal = Calculator()
    cal.master.title("My Calculator v0.2")
    cal.mainloop()

if __name__ == "__main__":
    main()
