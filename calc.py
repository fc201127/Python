#!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkFont
import math

# Calculator (child class) 繼承 tk.Frame (parent class)
# 表示 Calculator 擁有 tk.Frame 的特性 (member function, attributes)
# 可以理解成: Calculator "is a" tk.Frame
# 
class Calculator(tk.Frame):
    shouldReset = True

    def __init__(self): # 所有 class 都要有一個 __init__(self) 的 func.
                        # 可以理解成, Calculator "has a" __init__ func.
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()    # cal.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size=128, family="Helvetica")
        f2 = tkFont.Font(size=96, family="Helvetica")

        self.lblNum  = tk.Label(self, text="0",
                        relief="sunken", height=1, width=7, font=f1)
        self.btnNum1 = tk.Button(self, text="1",
                        command=self.clickBtnNum1, height=1, width=2, font=f2)
        self.btnNum2 = tk.Button(self, text="2",
                        command=self.clickBtnNum2, height=1, width=2, font=f2)
        self.btnNum3 = tk.Button(self, text="3",
                        command=self.clickBtnNum3, height=1, width=2, font=f2)
        self.btnNum4 = tk.Button(self, text="4",
                        command=self.clickBtnNum4, height=1, width=2, font=f2)
        self.btnNum5 = tk.Button(self, text="5",
                        command=self.clickBtnNum5, height=1, width=2, font=f2)
        self.btnNum6 = tk.Button(self, text="6",
                        command=self.clickBtnNum6, height=1, width=2, font=f2)
        self.btnNum7 = tk.Button(self, text="7",
                        command=self.clickBtnNum7, height=1, width=2, font=f2)
        self.btnNum8 = tk.Button(self, text="8",
                        command=self.clickBtnNum8, height=1, width=2, font=f2)
        self.btnNum9 = tk.Button(self, text="9",
                        command=self.clickBtnNum9, height=1, width=2, font=f2)
        self.btnNum0 = tk.Button(self, text="0",
                        command=self.clickBtnNum0, height=1, width=2, font=f2)
        self.btnSqrt = tk.Button(self, text="S",
                        command=self.clickBtnNumSqrt, height=1, width=2, font=f2)

        #
        # +--------------------> x (column)
        # |
        # |
        # |
        # v y (row)
        #
        self.lblNum.grid (column = 0, row = 0, sticky=tk.NW+tk.SE, columnspan=3)
        self.btnNum1.grid(column = 0, row = 1, sticky=tk.NW+tk.SE)
        self.btnNum2.grid(column = 1, row = 1, sticky=tk.NW+tk.SE)
        self.btnNum3.grid(column = 2, row = 1, sticky=tk.NW+tk.SE)
        self.btnNum4.grid(column = 0, row = 2, sticky=tk.NW+tk.SE)
        self.btnNum5.grid(column = 1, row = 2, sticky=tk.NW+tk.SE)
        self.btnNum6.grid(column = 2, row = 2, sticky=tk.NW+tk.SE)
        self.btnNum7.grid(column = 0, row = 3, sticky=tk.NW+tk.SE)
        self.btnNum8.grid(column = 1, row = 3, sticky=tk.NW+tk.SE)
        self.btnNum9.grid(column = 2, row = 3, sticky=tk.NW+tk.SE)
        self.btnNum0.grid(column = 0, row = 4, sticky=tk.NW+tk.SE, columnspan=2)
        self.btnSqrt.grid(column = 2, row = 4, sticky=tk.NW+tk.SE)



        
    def clickBtnNum1(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "1")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "1")

    def clickBtnNum2(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "2")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "2")

    def clickBtnNum3(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "3")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "3")

    def clickBtnNum4(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "4")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "4")

    def clickBtnNum5(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "5")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "5")
    def clickBtnNum6(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "6")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "6")

    def clickBtnNum7(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "7")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "7")

    def clickBtnNum8(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "8")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "8")

    def clickBtnNum9(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "9")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "9")

    def clickBtnNum0(self):
        if self.shouldReset == True:
            self.lblNum.configure(text= "0")
            self.shouldReset = False
        else:
            self.lblNum.configure(text=self.lblNum.cget("text") + "0")

    def clickBtnNumSqrt(self):
        v = str(round(math.sqrt(float(self.lblNum.cget("text"))), 2))
        self.lblNum.configure(text=v)
        self.shouldReset = True

def main():
    cal = Calculator()
    cal.master.title("My Calculator v1.3")
    cal.mainloop()

if __name__ == "__main__":
    main()
