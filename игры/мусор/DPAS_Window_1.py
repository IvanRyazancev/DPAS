from tkinter import *
from tkinter import messagebox as mb
# from Child_window import Childwindow


# from DPAS_29_12_2020 import *


class Window:
    def __init__(self, width, height, title="DPAS", resizable=(True, True), icon=r"ico_DPAS.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0],resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.nazvanie = Entry(self.root)
        self.gabarit = Entry(self.root)
        self.n = Entry(self.root)
        self.dlinaproleta1 = Entry(self.root)
        self.Hbalki1 = Entry(self.root)
        self.shirtrot = Entry(self.root)
        self.otmpch1 = Entry(self.root)
        self.poperucl = Entry(self.root)
        self.hdo = Entry(self.root)
        self.hzashsl = Entry(self.root)
        self.hgidroiz = Entry(self.root)
        self.hvirsl = Entry(self.root)
        self.ozaglublrostv = Entry(self.root)
        self.bsvai = Entry(self.root)
        self.Lsvai = Entry(self.root)
        self.otmzeli = Entry(self.root)

        self.choice = IntVar(value=0)
        self.choice_trotuar = IntVar(value=0)
        self.info = Label(self.root)
        self.calculation_rez = Label(self.root)

        # self.password_entry = Entry(self.root, show="*")

        # self.entry = Entry(self.root)
        # self.entry.insert(0, "Hey...")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):

        Label(self.root, text="Название объекта:", justify=LEFT).grid(row=0, column=0, sticky=W)
        self.nazvanie.grid(row=0, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите габарит проезжей части:", justify=LEFT).grid(row=1, column=0, sticky=W)
        self.gabarit.grid(row=1, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Количество пролетных строений:", justify=LEFT).grid(row=2, column=0, sticky=W)
        self.n.grid(row=2, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Длина пролетного строения:", justify=LEFT).grid(row=3, column=0, sticky=W)
        self.dlinaproleta1.grid(row=3, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Высота балки:", justify=LEFT).grid(row=4, column=0, sticky=W)
        self.Hbalki1.grid(row=4, column=1, sticky=W + E, padx=5, pady=5)
        Radiobutton(self.root, text="Барьерное ограждение", variable=self.choice, value=0, justify=LEFT, width=20,
                    height=1).grid(row=5, column=0, padx=5)
        Radiobutton(self.root, text="Парапетное ограждение", variable=self.choice, value=1, justify=LEFT, width=20,
                    height=1).grid(row=6, column=0, padx=5)
        Radiobutton(self.root, text="Тротуары", variable=self.choice_trotuar, value=0, justify=LEFT, width=20,
                    height=1).grid(
            row=5, column=1, padx=5)
        Radiobutton(self.root, text="Служебные проходы", variable=self.choice_trotuar, value=1, justify=LEFT, width=20,
                    height=1).grid(row=6, column=1, padx=5)
        Radiobutton(self.root, text="Тротуары отсутствуют", variable=self.choice_trotuar, value=2, justify=LEFT,
                    width=20,
                    height=1).grid(row=7, column=1, padx=5)
        Label(self.root, text="Ширина тротуара:", justify=LEFT).grid(row=9, column=0, sticky=W)
        self.shirtrot.grid(row=9, column=1, sticky=W + E, padx=5, pady=5)

        Label(self.root, text="Введите отметку верха проезжей части над опорой №:", justify=LEFT).grid(row=10, column=0,
                                                                                                       sticky=W)
        self.otmpch1.grid(row=10, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите поперечный уклон проезжей части над опорой №:", justify=LEFT).grid(row=11,
                                                                                                          column=0,
                                                                                                          sticky=W)
        self.poperucl.grid(row=11, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите отметку земли у опоры №:", justify=LEFT).grid(row=12,
                                                                                     column=0,
                                                                                     sticky=W)
        self.otmzeli.grid(row=12, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите толщину а/б покрытия проезжей части:", justify=LEFT).grid(row=13, column=0,
                                                                                                 sticky=W)
        self.hdo.grid(row=13, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите толщину защитного слоя проезжей части:", justify=LEFT).grid(row=14, column=0,
                                                                                                   sticky=W)
        self.hzashsl.grid(row=14, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите толщину гидроизоляции проезжей части:", justify=LEFT).grid(row=15, column=0,
                                                                                                  sticky=W)
        self.hgidroiz.grid(row=15, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите толщину выравнивающего слоя проезжей части:", justify=LEFT).grid(row=16,
                                                                                                        column=0,
                                                                                                        sticky=W)
        self.hvirsl.grid(row=16, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите величину заглубления ростверка в грунт:", justify=LEFT).grid(row=17, column=0,
                                                                                                    sticky=W)
        self.ozaglublrostv.grid(row=17, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите размер стороны сваи:", justify=LEFT).grid(row=18, column=0,
                                                                                 sticky=W)
        self.bsvai.grid(row=18, column=1, sticky=W + E, padx=5, pady=5)
        Label(self.root, text="Введите длину сваи:", justify=LEFT).grid(row=19, column=0,
                                                                        sticky=W)
        self.Lsvai.grid(row=19, column=1, sticky=W + E, padx=5, pady=5)
        # Label(self.root, text="Login:", justify=LEFT).grid(row=0, column=0, sticky=W)
        # self.login_entry.grid(row=0, column=1, sticky=W + E, padx=5, pady=5)
        # Label(self.root, text="Age:", justify=LEFT).grid(row=1, column=0, sticky=W)
        # self.age_entry.grid(row=1, column=1, sticky=W + E, padx=5, pady=5)
        # Label(self.root, text="Password:", justify=LEFT).grid(row=2, column=0, sticky=W)
        # self.password_entry.grid(row=2, column=1, sticky=W + E, padx=5, pady=5)

        # text_var = StringVar(value="Text")
        # Entry(self.root, width=30, fg="blue", font=("Verdana", 9), justify=CENTER, relief=SUNKEN, bd=3,
        #       selectbackground="green", selectforeground="yellow",textvariable=text_var).pack()

        # self.entry.pack()
        # Button(self.root, text="Show text", width=10, command=self.get_text).pack()
        # Button(self.root, text="Repeat", width=10, command=self.repeat_text).pack()
        # Button(self.root, text="Insert", width=10, command=self.insert).pack()
        # Button(self.root, text="Clear", width=10, command=self.clear).pack()
        #
        # Button(self.root, text="Расчет!", width=10, command=self.raschet).grid(row=8, justify=CENTER, padx=5)
        Button(self.root, text="Сохранить", width=10, command=self.save_data).grid(row=21, column=0, padx=5)
        Button(self.root, text="Расчет", width=10, command=self.calculation_rez, justify=CENTER).grid(row=21, column=1,
                                                                                                      sticky=W + S + N)
        Button(self.root, text="Выход", width=10, command=self.exit).grid(row=21, column=2, sticky=E)

    def exit(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")
        if choice:
            self.root.destroy()
        # choice = messagebox.askokcancel("Quit", "Do you want to quit?")
        # print(choice)

    def calculation_rez(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")

    def save_data(self):
        nazvanie = self.nazvanie.get()
        gabarit = int(self.gabarit.get())
        n = self.n.get()
        dlinaproleta1 = self.dlinaproleta1.get()
        Hbalki1 = self.Hbalki1.get()
        shirtrot = self.shirtrot.get()
        otmpch1 = self.otmpch1.get()
        poperucl = self.poperucl.get()
        otmzeli = self.otmzeli.get()
        hdo = self.hdo.get()
        hzashsl = self.hzashsl.get()
        hgidroiz = self.hgidroiz.get()
        hvirsl = self.hvirsl.get()
        ozaglublrostv = self.ozaglublrostv.get()
        bsvai = self.bsvai.get()
        Lsvai = self.Lsvai.get()

        mb.showinfo("User Data", f"{nazvanie}.Габарит проезжей части {gabarit} м.")
        mb.showinfo("User Data", f"Количество пролетных строений {n} шт.")
        # mb.showinfo("User Data",f"Длина пролетного строения {dlinaproleta1} м.")

    # def get_text(self):
    #     text = self.entry.get()
    #     mb.showinfo("Entry text", text)
    #
    # def repeat_text(self):
    #     text = self.entry.get()
    #     self.entry.insert(0, text)
    #     self.entry.insert(END, text)
    #
    # def insert(self):
    #     self.entry.insert(INSERT, "_in_")
    #     self.entry.insert(ANCHOR, "_sel_")
    #
    # def clear(self):
    #     self.entry.delete(0, END)

    # def raschet(self):

    def button_action(self):
        Label(self.root, text="New label").pack()

    # def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
    #     Childwindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "DPAS")
    # window.create_child(200,100)
    window.run()
