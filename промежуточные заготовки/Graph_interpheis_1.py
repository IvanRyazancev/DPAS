from tkinter import *
from Child_window import Childwindow


class Window:
    def __init__(self, width, height, title="DPAS", resizable=(True, True), icon=None):
        self.root = Tk()
        self.root.title(title)
        # # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        #  сайт для подбора цветов (bg) - Color Picker
        self.label = Label(self.root, text="DPAS", bg="#e84ae5", relief=FLAT, wraplength=200, font="Consolas 15")
        # .pgm, .ppm, .gif, .png
        # self.paint_Label = PhotoImage(file=r"paint_Label.png")
        # self.label = Label(self.root, image=self.paint_Label)
        # self.label.image = self.paint_Label

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        # top_frame = Frame(self.root, borderwidth=30, relief=SUNKEN, width=300, height=200)
        # bottom_frame = Frame(self.root, borderwidth=30, relief=SUNKEN, width=300, height=200)
        # top_frame.pack()
        # bottom_frame.pack()

        # l1 = Label(self.root, width=300, height=20, bg="red", text="First")
        # l2 = Label(self.root, width=30, height=2, bg="orange", text="Second")

        # l1.place(x=10, y=10)
        # l2.place(in_=l1, x=10, y=10)

        # self.label.pack(anchor=NW, padx=20, pady=30)
        # self.label.pack()

        # Label(self.root, width=30, height=2, bg="red", text="First").grid(row=0, column=0, sticky=S + N)
        # Label(self.root, width=30, height=2, bg="red", text="First").grid(row=0, column=1)

        l1 = Label(self.root, width=30, height=2, bg="yellow", text="Second")
        l2 = Label(self.root, width=30, height=2, bg="orange", text="Third")
        l3 = Label(self.root, width=30, height=2, bg="green", text="Fourth")

        l1.grid(row=0, column=0)
        l2.grid(row=0, column=1)
        l3.grid(row=1, column=0, columnspan=2)
        Label(self.root, width=30, height=2, bg="red", text="First").grid(row=2, column=0)

        # l1.grid_remove()
        # l1.grid_forget()
        # l1.grid()

        print(l1.grid_info())
        print(self.root.grid_size())
        print(self.root.grid_location(x=20, y=50))

        # Label(self.root, width=30, height=2, bg="yellow", text="Second").grid(row=0, column=0, padx=10)
        # Label(self.root, width=30, height=2, bg="yellow", text="Second").grid(row=0, column=1, pady=20)
        # # Label(self.root, width=30, height=2, bg="orange", text="Third").grid(row=1, column=0)
        # # Label(self.root, width=30, height=2, bg="green", text="Fourth").grid(row=1, column=1)
        # Label(self.root, width=30, height=2, bg="cyan", text="Fifth").grid(row=1, column=0, columnspan=2,sticky=W+E)

    def create_child(self, width, height, title="Child", resizable=(True, True), icon=None):
        Childwindow(self.root, width, height, title, resizable, icon=None)


if __name__ == "__main__":
    window = Window(500, 500, "DPAS")
    # window.create_child(200, 100)
    window.run()
