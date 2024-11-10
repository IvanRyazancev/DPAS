from tkinter import *

root = Tk()
root.title('ОПИС')  # ОПИС - определение параметров искусственных сооружений
root.geometry('1000x600')
My_label = Label(text='Ввод исходных данных', font=('Times New Roman', 16, 'bold'))
My_label.pack()

My_label = Label(root, text='Название объекта:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=35)

My_label = Label(root, text='Габарит сооружения:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=60)

My_label = Label(root, text='Количество пролетных', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=85)

My_label = Label(root, text='строений:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=102)

My_label = Label(root, text='Введите длину пролетного', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=119)

My_label = Label(root, text='строения:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=135)

My_label = Label(root, text='Выберите ширину ограждения:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=151)

My_label = Label(root, text='Введите ширину тротуара', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=170)

My_label = Label(root, text='или служебного прохода:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=187)

My_label = Label(root, text='Ширина тротуарной консоли:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=205)

My_label = Label(root, text='Ширина бортика', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=228)

My_label = Label(root, text='омоноличивания:', font=('Times New Roman', 10, 'bold'))
My_label.place(x=18, y=245)

nazvanie = Entry(width=30)
nazvanie.place(x=200, y=37)

gabarit = Entry(width=30)
gabarit.place(x=200, y=62)

n = Entry(width=30)
n.place(x=200, y=96)

dlinaproleta1 = Entry(width=30)
dlinaproleta1.place(x=200, y=127)

shirogr = Entry(width=30)
shirogr.place(x=200, y=153)

shirtrot = Entry(width=30)
shirtrot.place(x=200, y=179)

shirconsol = Entry(width=30)
shirconsol.place(x=200, y=208)

bortomon = Entry(width=30)
bortomon.place(x=200, y=237)

label = Label(root, text='Полная ширина', font=('Times New Roman', 12, 'bold'))
label.pack()
label = Label(root, text='пролетного строения', font=('Times New Roman', 12, 'bold'))
label.pack()

entry = Entry(root, justify='center', bd=5)
entry.pack()


#
# import math
#
def Spoln(gabarit, shirtrot, shirconsol, shirogr, bortomon):
    print('Spoln')
    print(gabarit, shirtrot, shirconsol, shirogr, bortomon)
    gabarit = float(gabarit)
    shirtrot = float(shirtrot)
    shirconsol = float(shirconsol)
    shirogr = float(shirogr)
    bortomon = float(bortomon)
    # площадь боковой поверхности цилиндра:
    Spoln = gabarit + 2 * (shirogr + shirtrot + shirconsol + bortomon)
    # # площадь одного основания цилиндра:
    # circle = math.pi * r ** 2
    # # полная площадь цилиндра:
    # full = side + 2 * circle
    # return full


#
def Green():
    entry.delete(0, END)
    result = Spoln(gabarit.get(), shirogr.get(), shirtrot.get(), shirconsol.get(), bortomon.get())
    entry.insert(0, result)


button = Button(width=16, bg='Green', command=Green, text='Enter')
button.pack()

root.mainloop()
