from tkinter import *


class Window:
    def __init__(self, width, height, title="DPAS", resizable=(True, True), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()


window = Tk()
window.title("DPAS")
window.geometry("400x500+600+300")
window.resizable(True, True)
window.iconbitmap("Пробный_ярлык_для_окна_DPAS.ico")

window.mainloop()
