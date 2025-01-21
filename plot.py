#!/usr/bin/env python3
#
# MVC model (Model, View, Control)
# widgets, layout (View)
# control, command (Control)
# data (Model)
#
import os
import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as pyplot
from PIL import ImageTk

class Plotter(tk.Frame):    # inherit from Frame
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f = tkFont.Font(size = 16, family = "Courier New")

        self.lb1X = tk.Label(self, text="x:", height = 1, width = 3, font = f)
        self.txtX = tk.Text(self,  height=1,  width = 40, font = f)

        self.lb1Y = tk.Label(self, text="y:", height = 1, width = 3, font = f)
        self.txtY = tk.Text(self,  height=1,  width = 40, font = f)

        self.btnLoad = tk.Button(self, text = "plot!", height = 1, width = 5, font = f,
                                 command=self.clickBtnLoad)
        self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")

        # layout
        # row (y), column (x)
        # +-------> x
        # |
        # |
        # v
        # y
        self.lb1X.grid(column=0, row = 0, sticky = tk.E)
        self.txtX.grid(column=1, row = 0, sticky = tk.NE + tk.SW)

        self.lb1Y.grid(column=0, row = 1, sticky = tk.E)
        self.txtY.grid(column=1, row = 1, sticky = tk.NE + tk.SW)

        self.btnLoad.grid(column=2, row = 0, rowspan = 2, sticky = tk.NE + tk.SW)
        self.cvsMain.grid(column=0, row = 2, columnspan = 3, sticky = tk.NE + tk.SW)

    def makeScatter(self, x, y):
        pyplot.figure()
        pyplot.plot(x, y, 'bo')
        pyplot.ylim(min(y) - 10, max(y) + 10)

        pyplot.savefig('temp.png')


    def clickBtnLoad(self):
        x = self.txtX.get("1.0", tk.END).split(",")
        for i in range(len(x)):
            x[i] = float(x[i])

        y = self.txtY.get("1.0", tk.END).split(",")
        for i in range(len(y)):
            y[i] = float(y[i])

        self.makeScatter(x, y)  # create "temp.png"
        self.imageMain = ImageTk.PhotoImage(file = "temp.png")
        self.cvsMain.create_image(400, 300, image = self.imageMain, anchor = tk.CENTER)
        os.system("rm temp.png")


def main():
    pl = Plotter()
    pl.master.title("My Plotter v3.0")
    pl.mainloop()


if __name__ == "__main__":
    main()

