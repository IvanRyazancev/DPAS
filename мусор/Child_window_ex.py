from tkinter import *

class ChildWindow:
    def __init__(self, width, height, title="DPAS - результаты", resizable=(False, False), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()