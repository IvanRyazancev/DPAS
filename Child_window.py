# from DPAS_Window_1 import Window
from tkinter import *

class ChildWindow:
    def __init__(self, parent, width, height, title="DPAS - результаты", resizable=(True, True), icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()




    # def create_child(self,width,height,title="DPAS - результаты",resizable=(True,True),icon=None):
    #     Childwindow(self.root,width,height,title,resizable,icon)


        # self.grab_focus()

    # def grab_focus(self):
    #     self.root.grab_set()
    #     self.root.focus_set()
    #     self.root.wait_window()