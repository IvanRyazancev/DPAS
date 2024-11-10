# import math
#
# gabarit = int(input("Введите габарит сооружения: "))
# shirtrot = float(input("Введите ширину тротуара: "))
# shirogr = 0.48
# Shirbalki = 1.4
# bortomon = 0.25
#
# nbalok1 = (gabarit + shirogr + Shirbalki) // Shirbalki
# shirinaomon1 = round(((gabarit + shirogr) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
#
# while shirinaomon1 < 0.35:
#     nbalok1 = nbalok1 - 1
#     shirinaomon1 = round(((gabarit + shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
#
# shagbalok1 = shirinaomon1 + Shirbalki
#
# if shagbalok1 > 2.25:
#     print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")
#
# nbalok2 = (shirtrot + bortomon) // Shirbalki
# shirinaomon2 = round((((shirtrot + bortomon) - (nbalok2 * Shirbalki)) / (nbalok2 + 1)), 3)
#
# while shirinaomon2 < 0.35:
#     nbalok2 = nbalok2 - 1
#     shirinaomon2 = round((((shirtrot + bortomon) - (nbalok2 * Shirbalki)) / (nbalok2 + 1)), 3)
#
# shagbalok2 = shirinaomon2 + Shirbalki
#
# if shagbalok2>2.25:
#     print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")
#
# nbalok = math.ceil(nbalok1 + 2 * nbalok2)
#
# print("Количество балок в пролетном строении под проезжей частью:", nbalok1)
# print("Ширина монолитных участков под проезжей части:", shirinaomon1)
# print("Шаг балок под проезжей частью:", shagbalok1)
# print("Количество балок в пролетном строении под тротуарами:", 2 * nbalok2)
# print("Ширина монолитных участков под тротуарами:", shirinaomon2)
# print("Шаг балок под тротуарами:", shagbalok2)
# print("Общее количество балок на пролетное строение", nbalok)

# import math

# gabarit = int(input("Введите габарит сооружения: "))
# shirtrot = float(input("Введите ширину тротуара: "))
# shirogr = 0.48
# Shirbalki = 1.4
# bortomon = 0.25
#
# shirprolstr = gabarit + 2 * shirogr + 2 * shirtrot + 2 * bortomon
#
# nbalok1 = (gabarit + 2 * shirogr + Shirbalki) // Shirbalki
# shirinaomon1 = round(((gabarit + 2 * shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
#
# while shirinaomon1 < 0.35:
#     nbalok1 = nbalok1 - 1
#     shirinaomon1 = round(((gabarit + 2 * shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
#
# shagbalok1 = round(shirinaomon1 + Shirbalki, 3)
#
# if shagbalok1 > 2.25 or shagbalok1 < 1.75:
#     print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")
#
# nbalok2 = ((shirprolstr - (
#         gabarit + 2 * shirogr + Shirbalki)) / 2) // Shirbalki
# shirinaomon2 = round((((0.5*shirprolstr - (
#         0.5*gabarit + shirogr + 0.5*Shirbalki)) - (nbalok2 * Shirbalki)) / (nbalok2)), 3)
#
# while shirinaomon2 < 0.35:
#     nbalok2 = nbalok2 - 1
#     shirinaomon2 = round((((0.5 * shirprolstr - (
#             0.5 * gabarit + shirogr + 0.5 * Shirbalki)) - (nbalok2 * Shirbalki)) / (nbalok2)), 3)
#
# shagbalok2 = round(shirinaomon2 + Shirbalki, 3)
#
# if shagbalok2 > 2.25 or shagbalok2 < 1.75:
#     print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")
#
# nbalok = math.ceil(nbalok1 + 2 * nbalok2)
#
# print("Ширина пролетного строения: ", shirprolstr)
# print("Ширина под тротуарные части: ", round((0.5*shirprolstr - (
#         0.5*gabarit + shirogr + 0.5*Shirbalki)),2))
# print("Количество балок в пролетном строении под проезжей частью:", nbalok1)
# print("Ширина монолитных участков под проезжей части:", shirinaomon1)
# print("Шаг балок под проезжей частью:", shagbalok1)
# print("Количество балок в пролетном строении под тротуарами:", 2 * nbalok2)
# print("Ширина монолитных участков под тротуарами:", shirinaomon2)
# print("Шаг балок под тротуарами:", shagbalok2)
# print("Общее количество балок на пролетное строение", nbalok)

# Lrigprom
# if (Lrigprom - 3) <= 6:
#     nstoekprom = 2
# elif (Lrigprom - 3) > 6 and (Lrigprom - 3) <= 12:
#     nstoekprom = 3
# elif (Lrigprom - 3) > 12 and (Lrigprom - 3) <= 18:
#     nstoekprom = 4
# elif (Lrigprom - 3) > 18 and (Lrigprom - 3) <= 24:
#     nstoekprom = 5
# elif (Lrigprom - 3) > 24 and (Lrigprom - 3) <= 30:
#     nstoekprom = 6
# else:
#     nstoekprom = 7
#
# nstoekust = nstoekprom
# nstoek = nstoekust
# shagstoekust = round((Lrigust / nstoekust), 2)
#
# print("Ширина пролетного строения: ", Spoln)
# print("Количество стоек опоры:", nstoek)
# print("Шаг стоек: ", shagstoekust)

# парамеры балки


# dlinaproleta = float(input("введите "))
# Shirbalki = 1.4
# Hbalki1 = int(input("Выберите высоту балки 0.93 м - 1; 1.23 м - 2; 1.53 м - 3: "))
# Hpliti = 0.18
# Bplomonol = 0.7
# Lpliti = dlinaproleta - 2 * 0.7
#
# # file = open('data_balk.txt', encoding='utf-8')
# # if dlinaproleta == 12 and Hbalki1 == 1:
# #     Hbalki = 0.93
# #     osopor = 0.3
# #     Vbalki = 6.59
# #     mbalki = 16.5
# #     harbalki = file.readline(1)
# #     matbalki = 'B35 F300 W6'
#
# if dlinaproleta == 12 and Hbalki1 == 1:
#     Hbalki = 0.93
#     osopor = 0.3
#     Vbalki = 6.59
#     mbalki = 16.5
#     harbalki = ("Б 1200.140.93")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 15 and Hbalki1 == 1:
#     Hbalki = 0.93
#     osopor = 0.3
#     Vbalki = 8.40
#     mbalki = 21.0
#     harbalki = ("Б 1500.140.93")
#     matbalki = 'B40 F300 W6'
# elif dlinaproleta == 11.9 and Hbalki1 == 2:
#     Hbalki = 1.23
#     osopor = 0.3
#     Vbalki = 7.54
#     mbalki = 18.9
#     harbalki = ("Б 1190.140.123")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 15 and Hbalki1 == 2:
#     Hbalki = 1.23
#     osopor = 0.3
#     Vbalki = 9.46
#     mbalki = 23.7
#     harbalki = ("Б 1500.140.123")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 18 and Hbalki1 == 2:
#     Hbalki = 1.23
#     osopor = 0.3
#     Vbalki = 11.63
#     mbalki = 29.1
#     harbalki = ("Б 1800.140.123")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 21 and Hbalki1 == 2:
#     Hbalki = 1.23
#     osopor = 0.3
#     Vbalki = 13.01
#     mbalki = 32.6
#     harbalki = ("Б 2100.140.123")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 24 and Hbalki1 == 2:
#     Hbalki = 1.23
#     osopor = 0.3
#     Vbalki = 15.18
#     mbalki = 38.0
#     harbalki = ("Б 2400.140.123")
#     matbalki = 'B40 F300 W6'
# elif dlinaproleta == 28 and Hbalki1 == 2:
#     Hbalki = 1.23
#     osopor = 0.3
#     Vbalki = 18.07
#     mbalki = 45.2
#     harbalki = ("Б 2800.140.123")
#     matbalki = 'B40 F300 W6'
# elif dlinaproleta == 18 and Hbalki1 == 3:
#     Hbalki = 1.53
#     osopor = 0.3
#     Vbalki = 12.42
#     mbalki = 31.1
#     harbalki = ("Б 1800.140.153")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 28 and Hbalki1 == 3:
#     Hbalki = 1.53
#     osopor = 0.3
#     Vbalki = 19.36
#     mbalki = 48.4
#     harbalki = ("Б 2800.140.153")
#     matbalki = 'B35 F300 W6'
# elif dlinaproleta == 33 and Hbalki1 == 3:
#     Hbalki = 1.53
#     osopor = 0.4
#     Vbalki = 24.35
#     mbalki = 60.9
#     harbalki = ("Б 3300.140.153")
#     matbalki = 'B45 F300 W6'
#
#
# print(Hbalki)
# print(osopor)
# print(Vbalki)
# print(mbalki)
# print(harbalki)
# print(matbalki)


#  блок для создания интерфейса

# print("Блок разработки графического интерфейса программы DPAS")
# import math
# from tkinter import *
#
# root = Tk()
# root.title('DPAS')
# root.geometry('1000x900')
# My_label = Label(root, text='ОПИС', font=('Times New Roman', 16, 'bold'))
# My_label.pack()
#
# My_label = Label(root, text='Название объекта', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=20)
#
# My_label = Label(root, text='Габарит проезжей части', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=40)
#
# My_label = Label(root, text='Введите кол-во пролетных строений', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=60)
#
# My_label = Label(root, text='Введите длину пролетного строения № ', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=80)
#
# My_label = Label(root, text='Ширина дорожного ограждения', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=100)
#
# My_label = Label(root, text='Ширина тротуара ', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=120)
#
# My_label = Label(root, text='Ширина бортика омоноличивания ', font=('Times New Roman', 12, 'bold'))
# My_label.place(x=10, y=140)
#
# nazvanie = Entry(width=20)
# nazvanie.pack()
#
# gabarit = Entry(width=20)
# gabarit.pack()
#
# n = Entry(width=20)
# n.pack()
#
# dlinaproleta = Entry(width=20)
# dlinaproleta.pack()
#
# shirogr = Entry(width=20)
# shirogr.pack()
#
# shirtrot = Entry(width=20)
# shirtrot.pack()
#
# bortomon = Entry(width=20)
# bortomon.pack()
#
# label = Label(root, text='Ширина пролетного строения', font=('Times New Roman', 16, 'bold'))
# label.pack()
#
# entry = Entry(root, justify='left', bd=5)
# entry.pack()
#
#
# def Spoln(gabarit, shirogr, shirtrot, bortomon):
#     print(gabarit, shirogr, shirtrot, bortomon)
#     gabarit = float(gabarit)
#     shirogr = float(shirogr)
#     shirtrot = float(shirtrot)
#     bortomon = float(bortomon)
#     Spol = gabarit + 2 * shirogr + 2 * shirtrot + 2 * bortomon
#     # print('cylinder')
#     # print(r, h)
#     # r = float(r)
#     # h = float(h)
#     # # площадь боковой поверхности цилиндра:
#     # side = 2 * math.pi * r * h
#     # # площадь одного основания цилиндра:
#     # circle = math.pi * r ** 2
#     # # полная площадь цилиндра:
#     # full = side + 2 * circle
#     return Spol
#
#
# def Green():
#     entry.delete(0, END)
#     result = Spoln(gabarit.get(), shirogr.get(), shirtrot.get(), bortomon.get())
#     entry.insert(0, result)
#
#
# button = Button(width=16, bg='Green', command=Green, text='Enter')
# button.pack()
#
# root.mainloop()


# Создание списка опор и нумерация опор и пролетных строений

# gabarit = int(input("Введите габарит проезжей части Г - "))
# n = int(input("Введите количество пролетных строений: "))
#
# nopor1 = n + 1  # количество опор на сооружение
# nopor2 = 0
# nopor = []
#
# for i in range(nopor1):
#     nopor2 = nopor2 + 1
#     nopor.append(nopor2)  # количестов промежуточных опор
# nprom = nopor[1:-1]
# nomera = "№".join([str(int(i)) for i in nprom])
# print("Номера устоев сооружения: №", nopor[0], "; №", nopor[-1])
# print("Номера промежуточных опор сооружения: №", *nomera)
# print("Количество устоев на сооружение: ", 2, "шт.")
# print("Количество промежуточных опор сооружения: ", len(nopor[1:-1]), "шт.")
#
# otmpch = 0
# poperucl = 0
# otmzeli = 0
#
# otmpch1 = []
# poperucl1 = []
# otmzeli1 = []
#
# for i in range(nopor1):
#     print("Введите отметку проезжей части над опорой № ", i + 1, ":")
#     otmpch = float(input())
#     if otmpch == "": break
#     otmpch1.append(otmpch)
#
#     print("Введите поперечный уклон проезжей части над опорой № ", i + 1)
#     poperucl = float(input())
#     if poperucl == "": break
#     poperucl1.append(poperucl)
#
#     print("Введите отметку земли у опоры № ", i + 1)
#     otmzeli = float(input())
#     if otmzeli == "": break
#     otmzeli1.append(otmzeli)
#
# otmpch1.append(otmpch)
# poperucl1.append(poperucl)
# otmzeli1.append(otmzeli)
#
# hdo = float(input("Введите толщину а/б покрытия проезжей части: "))
# hzashsl = float(input("Введите толщину защитного слоя проезжей части: "))
# hgidroiz = float(input("Введите толщину гидроизоляции проезжей части: "))
# hvirsl = float(input("Введите толщину выравнивающего слоя проезжей части: "))
# zaglublrostv = float(input("Введите величину заглубления ростверка в грунт: "))
# hpodf = 0.15  # минимальная высота подферменной площадки
#
# Hstr = 0
# Hstr1 = []
# for i in range(nopor1):
#     Hstr = round((poperucl1[i] * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalki3[i]), 2)
#     Hstr1.append(Hstr)
#
# otmrig = 0
# otmrostv = 0
# otmrig1 = []
# otmrostv1 = []
#
# for i in range(nopor1):
#     otmrig = round((otmpch1[i] - Hstr1[i] - hroch - hpodf - Hrig), 3)
#     otmrig1.append(otmrig)
#
#     otmrostv = otmzeli1[i] - zaglublrostv
#     otmrostv1.append(otmrostv)
#
# otmrig1.append(otmrig)
# otmrostv1.append(otmrostv)


# print("Номера промежуточных опор сооружения: ")
# for i in range(len(nprom)):
#     print("№", nprom[i], end="; ")


# m=02
# n = []
#
# m = int(input("Введите количество пролетных строений "))
# for i in range(m):
#     # n1=n1+1
#     n.append(m)
#     # n2 = len(n)
#     # n3=list(n2)
# print (n)
# nopor1=0
# nopor=[]
# for i in n2:
#     nopor1 = n2 + 1  # количество опор на сооружение
#     nopor.append(nopor1)
# print ("Опора № ", nopor[i])
# print(nopor)
# nust = 2  # количество устоев на сооружение
# nprom = nopor - nust

# nust = []
# for i in range(2):
#     # a=i+1
#     nust.append(i)
# print(nust[0], nust[i])
#
# nprom = []
# for i in range(nopor - len(nust)):
#     # a=i+1
#     nprom.append(i)
# print(nprom[1:i])

# for i in range(n):
#     print(nopor)

# print("Количество пролетных строений: ", n, "шт.")
# print("Количество опор: ", nopor, "шт.")
# print("Количество устоев: ", nust, "шт.")
# print("Количество промежуточных опор: ", nprom, "шт.")


# модуль расчета отметок подферменных площадок
# nbalok = int(input("Введите какое количество балок в пролетном строении: "))
# npodferm = nbalok
#
# nazvanie = input("Введите название объекта: ")
# gabarit = int(input("Введите габарит проезжей части: "))
# while gabarit <= 0:
#     gabarit = int(input("Введите габарит проезжей части: "))
# n = int(input("Введите количество пролетных строений: "))
# Lpr = 0
# zazor = 0.05
# nzazor = n - 1
#
# while n <= 0:
#     n = int(input("Введите количество пролетных строений: "))
#
# dlinaproleta1 = []
#
# for i in range(n):
#     print("Введите длину пролетного строения №", i + 1, ":")
#     dlinaproleta = float(input())
#     if dlinaproleta == "": break
#     dlinaproleta1.append(dlinaproleta)
#     Lpr += dlinaproleta
#
# for i in range(n):
#     print("Длина пролетного строения №", i + 1, ":", dlinaproleta1[i], "м.")
#
# shema = ' + '.join([str(int(i)) for i in dlinaproleta1])
#
# # Выбор типа балок
# print("Выбор марки балок: ")
# print("Выберите из списка балки пролетных строений")
#
# Shirbalki = 1.4
# Hbalki1 = 0
# Hbalki2 = []
# for i in range(n):
#     print("Выберите высоту балки пролетного строения № ", i + 1, "0.93 м - 1; 1.23 м - 2; 1.53 м - 3: ")
#     Hbalki1 = int(input())
#     Hbalki2.append(Hbalki1)
# Hpliti = 0.18
# Bplomonol = 0.7
# Lpliti = dlinaproleta - 2 * 0.7
#
# Hbalki = 0
# osopor = 0
# Vbalki = 0
# mbalki = 0
# harbalki = 0
# matbalki = 0
# Vbal = 0
# Hbalki3 = []
# osopor1 = []
# Vbalki1 = []
# mbalki1 = []
# harbalki1 = []
# matbalki1 = []
# for i in range(n):
#     if dlinaproleta1[i] == 12 and Hbalki2[i] == 1:
#         Hbalki = 0.93
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 6.59
#         Vbalki1.append(Vbalki)
#         mbalki = 16.5
#         mbalki1.append(mbalki)
#         harbalki = 'Б 1200.140.93'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 15 and Hbalki2[i] == 1:
#         Hbalki = 0.93
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 8.40
#         Vbalki1.append(Vbalki)
#         mbalki = 21.0
#         mbalki1.append(mbalki)
#         harbalki = 'Б 1500.140.93'
#         harbalki1.append(harbalki)
#         matbalki = 'B40 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 11.9 and Hbalki2[i] == 2:
#         Hbalki = 1.23
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 7.54
#         Vbalki1.append(Vbalki)
#         mbalki = 18.9
#         mbalki1.append(mbalki)
#         harbalki = 'Б 1190.140.123'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 15 and Hbalki2[i] == 2:
#         Hbalki = 1.23
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 9.46
#         Vbalki1.append(Vbalki)
#         mbalki = 23.7
#         mbalki1.append(mbalki)
#         harbalki = 'Б 1500.140.123'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 18 and Hbalki2[i] == 2:
#         Hbalki = 1.23
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 11.63
#         Vbalki1.append(Vbalki)
#         mbalki = 29.1
#         mbalki1.append(mbalki)
#         harbalki = 'Б 1800.140.123'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 21 and Hbalki2[i] == 2:
#         Hbalki = 1.23
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 13.01
#         Vbalki1.append(Vbalki)
#         mbalki = 32.6
#         mbalki1.append(mbalki)
#         harbalki = 'Б 2100.140.123'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 24 and Hbalki2[i] == 2:
#         Hbalki = 1.23
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 15.18
#         Vbalki1.append(Vbalki)
#         mbalki = 38.0
#         mbalki1.append(mbalki)
#         harbalki = 'Б 2400.140.123'
#         harbalki1.append(harbalki)
#         matbalki = 'B40 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 28 and Hbalki2[i] == 2:
#         Hbalki = 1.23
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 18.07
#         Vbalki1.append(Vbalki)
#         mbalki = 45.2
#         mbalki1.append(mbalki)
#         harbalki = 'Б 2800.140.123'
#         harbalki1.append(harbalki)
#         matbalki = 'B40 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 18 and Hbalki2[i] == 3:
#         Hbalki = 1.53
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 12.42
#         Vbalki1.append(Vbalki)
#         mbalki = 31.1
#         mbalki1.append(mbalki)
#         harbalki = 'Б 1800.140.153'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 28 and Hbalki2[i] == 3:
#         Hbalki = 1.53
#         Hbalki3.append(Hbalki)
#         osopor = 0.3
#         osopor1.append(osopor)
#         Vbalki = 19.36
#         Vbalki1.append(Vbalki)
#         mbalki = 48.4
#         mbalki1.append(mbalki)
#         harbalki = 'Б 2800.140.153'
#         harbalki1.append(harbalki)
#         matbalki = 'B35 F300 W6'
#         matbalki1.append(matbalki)
#     elif dlinaproleta1[i] == 33 and Hbalki2[i] == 3:
#         Hbalki = 1.53
#         Hbalki3.append(Hbalki)
#         osopor = 0.4
#         osopor1.append(osopor)
#         Vbalki = 24.35
#         Vbalki1.append(Vbalki)
#         mbalki = 60.9
#         mbalki1.append(mbalki)
#         harbalki = 'Б 3300.140.153'
#         harbalki1.append(harbalki)
#         matbalki = 'B45 F300 W6'
#         matbalki1.append(matbalki)
#     Vbal += Vbalki
# Hbalki3.append(Hbalki)
# osopor1.append(osopor)
# Vbalki1.append(Vbalki)
# mbalki1.append(mbalki)
# harbalki1.append(harbalki)
# matbalki1.append(matbalki)
#
#
#
# poperucl1=[]
# if Hbalki2[i] > Hbalki2[i + 1]:
#    otmpodf=otmrig+hrig+0.15
#    otmpodf1=otmpodf+shagbalok1*poperucl1

# блок расчета параметров подферменных площадок

# n = int(input("Введите количество пролетных строений: "))
# nopor1=[]
# nopor = n + 1
# nopor1.append(nopor)
# nbalok1=[]
# nbalok = int(input("Введите количество балок в пролетном строении "))
# nbalok1.append(nbalok)
# shagbalok = float(input("Введите шаг балок в пролетном строении: "))
# poperucl1 = []
# for i in range(nopor):
#     poperucl = float(input("Введите поперечный уклон над опорой № " ))
#     poperucl1.append(poperucl)
# Hrig = 0.8
# hpodfbaz = 0.15
# otmrig1 = []
# otmpodfbaz = []
# for i in range(nopor):
#     otmrig = float(input("Введите отметку низа ригеля: "))
#     otmrig1.append(otmrig)
# for i in range(nopor):
#     otmpodfbaz1 = otmrig1[i] + Hrig + hpodfbaz
#     otmpodfbaz.append(otmpodfbaz1)
#
# otmpodf1=[]
# for i in range(len(nbalok1) // 2):
#     otmpodf = otmpodfbaz[i] + (shagbalok * poperucl1[i] * nbalok1[i])
#     otmpodf1.append(otmpodf)
#
# for i in range(len(nopor1)):
#     print("Отметка начального подферменника ",nopor1[i], ":",otmpodfbaz[i])
# # for i in range(len(nbalok1) // 2):
# print("Отметка подферменника № ",nbalok1,":",otmpodf1)

# модуль расчета подферменных площадок на устоях


# модуль расчета подферменных площадок на промежуточных опорах
n = int(input("Введите кол-во пролетных строений: "))
nopor1 = n + 1  # количество опор на сооружение
nopor2 = 0
nopor = []
nbalok1 = int(input("Введите количество балок в пролетном строении: "))
shagbal = float(input("Введите шаг балок: "))
for i in range(nopor1):
    nopor2 = nopor2 + 1
    nopor.append(nopor2)  # количестов промежуточных опор
nprom = nopor[1:-1]
nust = [nopor[0], nopor[-1]]
otmrig = []


zazor = 0.05  # зазор между балками пролетных строений min=0.15 м
osopr = 0.3  # ось опирания балки до 33 м - 0.3 м, для 33 м -0.4 м
boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м
for i in range(len(nust)):
    poperucl = []
    print("Введите отметку верха насадки устоя № ", nopor[i])
    otmrig1 = float(input())
    otmrig.append(otmrig1)
    print("Введите поперечный уклон над опорой № ", nopor[i], ":")
    poperucl1 = float(input())
    poperucl.append(poperucl1)
    hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
    otmpodfbaz = otmrig[0] + 0.15  # отметка наименьшей подферменной площадки на опоре
    nshag1 = 0
    Bpodf = zazor + 2 * osopr + boporchast + 2 * bfasroch
    Lpodf = Lpoproch + 2 * Lpoppodf
    Vpodf1 = 0  # объем подферменной площадки одной
    Vpodf = 0  # общий объем подферменных площадок на опору
    Vpodf3 = 0  # промежуточный общий объем подферменников
    Vpodfbaz = hpodfbaz * Bpodf * Lpodf
    nshag2 = []
    otmpodf = []  # список отметок подферменных площадок
    Vpodf2 = []
    if nbalok1 % 2 == 0:
        for i in range((nbalok1 - 2) // 2):
            nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
            nshag2.append(nshag1)
        hpodf1 = hpodfbaz
        hprir1 = 0
        hprir = []  # список превышений на каждой подферменной площадке
        hpodf = []  # список высот подферменных площадок
        for i in range((nbalok1 - 2) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
            hprir1 = shagbal * nshag2[i] * poperucl[i]
            hprir.append(hprir1)
            hpodf1 = hpodfbaz + hprir[i]
            hpodf.append(hpodf1)
            otmpodf1 = otmrig[0] + hpodf[i]
            otmpodf.append(otmpodf1)
            Vpodf1 = hpodf[i] * Bpodf * Lpodf
            Vpodf2.append(Vpodf1)
            Vpodf += Vpodf1 * 2
    else:
        for i in range((nbalok1 - 1) // 2):
            nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
            nshag2.append(nshag1)
        hpodf1 = hpodfbaz
        hprir1 = 0
        hprir = []  # список превышений на каждой подферменной площадке
        hpodf = []  # список высот подферменных площадок
        for i in range((nbalok1 - 1) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
            hprir1 = (shagbal * nshag2[i] * poperucl[i])
            hprir.append(hprir1)
            hpodf1 = hpodfbaz + hprir[i]
            hpodf.append(hpodf1)
            otmpodf1 = otmrig[0] + hpodf[i]
            otmpodf.append(otmpodf1)
            Vpodf1 = hpodf[i] * Bpodf * Lpodf
            Vpodf2.append(Vpodf1)
            Vpodf3 += (Vpodf1 * 2)
            Vpodf = Vpodf3 - Vpodf2[-1]

    # print("Высота подферменной площадки № ", nshag2[0], ":", hpodfbaz, "м.")
for i in range(len(nust)):
    print("Отметка насадки устоя № ", nust[i], ":", otmrig[i])
print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz, 3))
print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbaz, "м3")
if nbalok1 % 2 == 0:
    for i in range((nbalok1 - 2) // 2):
        # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
        print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
        print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
    print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
else:
    for i in range((nbalok1 - 1) // 2):
        # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
        print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
        print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
    print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")

print("Отметка насадки устоя № ", nopor[-1], ":", otmrig[-1])
print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz, 3))
print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbaz, "м3")
if nbalok1 % 2 == 0:
    for i in range((nbalok1 - 2) // 2):
        # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
        print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
        print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
    print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
else:
    for i in range((nbalok1 - 1) // 2):
        # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
        print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
        print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
    print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")

if len(nprom) != 0:
    poperucl = []
    for i in range(len(nprom)):

        zazor = 0.05  # зазор между балками пролетных строений min=0.15 м
        osopr = 0.3  # ось опирания балки до 33 м - 0.3 м, для 33 м -0.4 м
        boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
        bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
        Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
        Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м

        poperucl1 = float(input("Введите поперечный уклон: "))
        poperucl.append(poperucl1)

        hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
        otmpodfbaz = otmrig[i] + 0.15  # отметка наименьшей подферменной площадки на опоре
        nshag1 = 0
        Bpodf = zazor + 2 * osopr + boporchast + 2 * bfasroch
        Lpodf = Lpoproch + 2 * Lpoppodf
        Vpodf1 = 0  # объем подферменной площадки одной
        Vpodf = 0  # общий объем подферменных площадок на опору
        Vpodf3 = 0  # промежуточный общий объем подферменников
        Vpodfbaz = hpodfbaz * Bpodf * Lpodf
        nshag2 = []
        otmpodf = []  # список отметок подферменных площадок
        Vpodf2 = []

        if nbalok1 % 2 == 0:
            for i in range((nbalok1 - 2) // 2):
                nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
                nshag2.append(nshag1)
            hpodf1 = hpodfbaz
            hprir1 = 0
            hprir = []  # список превышений на каждой подферменной площадке
            hpodf = []  # список высот подферменных площадок
            for i in range((nbalok1 - 2) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
                hprir1 = shagbal * nshag2[i] * poperucl
                hprir.append(hprir1)
                hpodf1 = hpodfbaz + hprir[i]
                hpodf.append(hpodf1)
                otmpodf1 = otmrig[i] + hpodf[i]
                otmpodf.append(otmpodf1)
                Vpodf1 = hpodf[i] * Bpodf * Lpodf
                Vpodf2.append(Vpodf1)
                Vpodf += Vpodf1 * 2
        else:
            for i in range((nbalok1 - 1) // 2):
                nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
                nshag2.append(nshag1)
            hpodf1 = hpodfbaz
            hprir1 = 0
            hprir = []  # список превышений на каждой подферменной площадке
            hpodf = []  # список высот подферменных площадок
            for i in range((nbalok1 - 1) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
                hprir1 = (shagbal * nshag2[i] * poperucl)
                hprir.append(hprir1)
                hpodf1 = hpodfbaz + hprir[i]
                hpodf.append(hpodf1)
                otmpodf1 = otmrig[i] + hpodf[i]
                otmpodf.append(otmpodf1)
                Vpodf1 = hpodf[i] * Bpodf * Lpodf
                Vpodf2.append(Vpodf1)
                Vpodf3 += (Vpodf1 * 2)
                Vpodf = Vpodf3 - Vpodf2[-1]
        # print("Высота подферменной площадки № ", nshag2[0], ":", hpodfbaz, "м.")
        print("Отметка ригеля промежуточной опоры № ", nopor[i + 1], ":", otmrig[i + 1])
        print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz, 3))
        print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbaz, "м3")

        if nbalok1 % 2 == 0:
            for i in range((nbalok1 - 2) // 2):
                # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
                print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i + 1], 3))
                print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i + 1], 3), "м3")
            print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")

        else:
            for i in range((nbalok1 - 1) // 2):
                # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
                print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
                print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
            print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
