# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:41:37 2020

@author: ryazantsev_ia
"""

# from tkinter import *
#
# root = Tk()
# root.title('ОПИС') # ОПИС - определение параметров искусственных сооружений
# root.geometry('1000x600')
# My_label = Label(text='Ввод исходных данных', font=('Arial', 16, 'bold'))
# My_label.pack()
#
# My_label = Label(root, text='Название объекта:', font=('Arial', 10, 'bold'))
# My_label.place(x=30, y=25)
#
# My_label = Label(root, text='Габарит сооружения:', font=('Arial', 10, 'bold'))
# My_label.place(x=30, y=50)
#
# r1 = Entry(width=30)
# r1.pack()
#
# h1 = Entry(width=30)
# h1.pack()
#
# label = Label(root, text='Ответ', font=('Arial', 16, 'bold'))
# label.pack()
#
# entry = Entry(root, justify='center', bd=5)
# entry.pack()
#
# import math
#
# def cylinder(r, h):
#     print('cylinder')
#     print(r, h)
#     r = float(r)
#     h = float(h)
#     # площадь боковой поверхности цилиндра:
#     side = 2 * math.pi * r * h
#     # площадь одного основания цилиндра:
#     circle = math.pi * r ** 2
#     # полная площадь цилиндра:
#     full = side + 2 * circle
#     return full
#
# def Green():
#     entry.delete(0, END)
#     result = cylinder(r1.get(), h1.get())
#     entry.insert(0, result)
#
# button = Button(width=16, bg='Green', command=Green, text='Enter')
# button.pack()
#
# root.mainloop()
import openpyxl
import math

# from DPAS_graf_interf import *
# import json

# from data_exit_Excel import*

print(" ")
print("                      Программа для определения параметров искусственного сооружения (ОПИС)    ")
print("                         Determining the Parameters of an Artificial Structure (DPAS)          ")
print(" ")
print("Данная программа предназначена для определения основных параметров искусственных сооружений дорожного ")
print("                           хозяйства, имея минимальное количество исходных данных")
print(" ")

# data_enter = []

nazvanie = input("Введите название объекта: ")
gabarit = int(input("Введите габарит проезжей части: "))
while gabarit <= 0:
    gabarit = int(input("Введите габарит проезжей части: "))
n = int(input("Введите количество пролетных строений: "))
Lpr = 0
zazor = 0.05
nzazor = n - 1

while n <= 0:
    n = int(input("Введите количество пролетных строений: "))

# Введение длины пролетных строений
dlinaproleta1 = []

for i in range(n):
    print("Введите длину пролетного строения №", i + 1, ":")
    dlinaproleta = float(input())
    if dlinaproleta == "": break
    dlinaproleta1.append(dlinaproleta)
    Lpr += dlinaproleta
dlinaproleta1.append(dlinaproleta)
# shema = (dlinaproleta1[i] "+" dlinaproleta1[i + 1])

# Проверка читаемости введенных значений длины пролетных строений
for i in range(n):
    print("Длина пролетного строения №", i + 1, ":", dlinaproleta1[i], "м.")

shema = '+'.join([str(i) for i in dlinaproleta1])

# Выбор типа балок
print("Выбор марки балок: ")
print("Выберите из списка балки пролетных строений")

# парамеры балки
# if dlinaproleta==15:

Shirbalki = 1.4
Hbalki1 = int(input("Выберите высоту балки 0.93 м - 1; 1.23 м - 2; 1.53 м - 3: "))
Hpliti = 0.18
Bplomonol = 0.7
Lpliti = dlinaproleta - 2 * 0.7

if dlinaproleta == 12 and Hbalki1 == 1:
    Hbalki = 0.93
    osopor = 0.3
    Vbalki = 6.59
    mbalki = 16.5
    harbalki = ("Б 1200.140.93")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 15 and Hbalki1 == 1:
    Hbalki = 0.93
    osopor = 0.3
    Vbalki = 8.40
    mbalki = 21.0
    harbalki = ("Б 1500.140.93")
    matbalki = ("B40 F300 W6")
elif dlinaproleta == 11.9 and Hbalki1 == 2:
    Hbalki = 1.23
    osopor = 0.3
    Vbalki = 7.54
    mbalki = 18.9
    harbalki = ("Б 1190.140.123")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 15 and Hbalki1 == 2:
    Hbalki = 1.23
    osopor = 0.3
    Vbalki = 9.46
    mbalki = 23.7
    harbalki = ("Б 1500.140.123")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 18 and Hbalki1 == 2:
    Hbalki = 1.23
    osopor = 0.3
    Vbalki = 11.63
    mbalki = 29.1
    harbalki = ("Б 1800.140.123")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 21 and Hbalki1 == 2:
    Hbalki = 1.23
    osopor = 0.3
    Vbalki = 13.01
    mbalki = 32.6
    harbalki = ("Б 2100.140.123")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 24 and Hbalki1 == 2:
    Hbalki = 1.23
    osopor = 0.3
    Vbalki = 15.18
    mbalki = 38.0
    harbalki = ("Б 2400.140.123")
    matbalki = ("B40 F300 W6")
elif dlinaproleta == 28 and Hbalki1 == 2:
    Hbalki = 1.23
    osopor = 0.3
    Vbalki = 18.07
    mbalki = 45.2
    harbalki = ("Б 2800.140.123")
    matbalki = ("B40 F300 W6")
elif dlinaproleta == 18 and Hbalki1 == 3:
    Hbalki = 1.53
    osopor = 0.3
    Vbalki = 12.42
    mbalki = 31.1
    harbalki = ("Б 1800.140.153")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 28 and Hbalki1 == 3:
    Hbalki = 1.53
    osopor = 0.3
    Vbalki = 19.36
    mbalki = 48.4
    harbalki = ("Б 2800.140.153")
    matbalki = ("B35 F300 W6")
elif dlinaproleta == 33 and Hbalki1 == 3:
    Hbalki = 1.53
    osopor = 0.4
    Vbalki = 24.35
    mbalki = 60.9
    harbalki = ("Б 3300.140.153")
    matbalki = ("B45 F300 W6")

# Вычисление схемы сооружения
# resultString = dlinaproleta
# for i in range(n - 1):
# resultString = resultString, "+", dlinaproleta1[i]

# ввод типа дорожного ограждения
tipogr = int(input("Выберите тип дорожного ограждения: 1 - барьерное ограждение; 2- парапетное ж/б ограждение "))
while tipogr != 1 and tipogr != 2:
    tipogr = int(input("Выберите тип дорожного ограждения: 1 - барьерное ограждение; 2- парапетное ж/б ограждение "))
if tipogr == 1:
    shirogr = 0.41
    massogr = 49
    ogrsoob = "металлическое барьерное ограждение."
else:
    shirogr = 0.48
    massogr = 620
    ogrsoob = "парапетное ж/б ограждение."

# ввод типа тротуаров
trotuari = int(input("Имеются ли на пролетном строении тротуары или служебные проходы: 1 - да; 2 - нет. "))
while trotuari != 1 and trotuari != 2:
    trotuari = int(input("Имеются ли на пролетном строении тротуары или служебные проходы: 1 - да; 2 - нет. "))
if trotuari == 1:
    bortomon = 0.25
    tiptrot = int(input("Это тротуар или служебный проход? 1 - тротуар; 2 - служебный проход. "))
    while tiptrot != 1 and tiptrot != 2:
        tiptrot = input("Это тротуар или служебный проход? 1 - тротуар; 2 - служебный проход. ")
    if tiptrot == 1:
        shirtrot = float(input("Введите ширину тротуара: "))
    else:
        shirtrot = 0.75
    Spoln = gabarit + 2 * (shirogr + shirtrot + bortomon)
else:
    shirtrot = 0
    console = int(input(
        "Имеется ли на пролетном строении тротуарные консоли? 1 - да; 2 - нет. "))  # определение наличия консолей на пролетном строении
    while console != 1 and console != 2:
        console = int(input("Имеется ли на пролетном строении тротуарные консоли? 1 - да; 2 - нет. "))
    if console == 1:
        bortomon = 0
        shirconsole = float(input("Введите ширину тротуарной консоли: "))
        while shirconsole < 0:
            shirconsole = float(input("Введите ширину тротуарной консоли: "))
        if shirconsole > 0:
            Spoln = gabarit + 2 * (shirogr + shirtrot + shirconsole)
    else:
        shirconsole = 0
        bortomon = 0.25
        Spoln = gabarit + 2 * (shirogr + shirtrot + bortomon)

# блок расчета кол-ва балок, их шага и объем балок и средних участков омоноличивания

# shagbalkimin = float(input("Введите минимальный шаг балок: "))
# while shagbalkimin > 2.25 or shagbalkimin < 1.75:
#     shagbalkimin = float(input("Введите минимиальный шаг балок: "))
# shagbalkimax = float(input("Введите максимальный шаг балок: "))
# while shagbalkimax > 2.25 or shagbalkimax < 1.75:
#     shagbalkimax = float(input("Введите максимальный шаг балок: "))
# while shagbalkimin > shagbalkimax:
#     print("Введенные значения неверны!")
#     shagbalkimin = float(input("Введите минимальный шаг балок: "))
#     while shagbalkimin > 2.25 or shagbalkimin < 1.75:
#         shagbalkimin = float(input("Введите максимальный шаг балок: "))
#     shagbalkimax = float(input("Введите максимальный шаг балок: "))
#     while shagbalkimax > 2.25 or shagbalkimax < 1.75:
#         shagbalkimax = float(input("Введите максимальный шаг балок: "))

# nbalok1 = (gabarit + shirogr) // Shirbalki
# shirinaomon1 = round(((gabarit + shirogr) - (nbalok1 * Shirbalki)) / (nbalok1 + 1), 3)
# shagbalok1 = shirinaomon1 + Shirbalki

# shagbalok1 = (shagbalkimin + shagbalkimax) / 2
# nbalok1 = (gabarit + shirogr) / shagbalok1
# shirinaomon1 = round((((gabarit + shirogr) - (nbalok1 * Shirbalki)) / (nbalok1 + 1)), 3)

# shirprolstr = gabarit + 2 * shirogr + 2 * shirtrot + 2 * bortomon

if trotuari == 1 and shirtrot > 3.15:  # когда тротуар больше 3,15 м
    nbalok1 = (gabarit + 2 * shirogr + Shirbalki) // Shirbalki
    shirinaomon1 = round(((gabarit + 2 * shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)

    while shirinaomon1 < 0.35:
        nbalok1 = nbalok1 - 1
        shirinaomon1 = round(((gabarit + 2 * shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)

    shagbalok1 = round(shirinaomon1 + Shirbalki, 3)

    if shagbalok1 > 2.25 or shagbalok1 < 1.75:
        print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")

    nbalok2 = ((Spoln - (
            gabarit + 2 * shirogr + Shirbalki)) / 2) // Shirbalki
    shirinaomon2 = round((((0.5 * Spoln - (
            0.5 * gabarit + shirogr + 0.5 * Shirbalki)) - (nbalok2 * Shirbalki)) / (nbalok2)), 3)

    while shirinaomon2 < 0.35:
        nbalok2 = nbalok2 - 1
        shirinaomon2 = round((((0.5 * Spoln - (
                0.5 * gabarit + shirogr + 0.5 * Shirbalki)) - (nbalok2 * Shirbalki)) / (nbalok2)), 3)

    shagbalok2 = round(shirinaomon2 + Shirbalki, 3)

    if shagbalok2 > 2.25 or shagbalok2 < 1.75:
        print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")

    nbalok = math.ceil(nbalok1 + 2 * nbalok2)
    # nbalok2 = (shirtrot + 0.5 * shirogr + bortomon) // Shirbalki
    # shirinaomon2 = round((((shirtrot + 0.5 * shirogr + bortomon) - (nbalok2 * Shirbalki)) / (nbalok2)), 3)
    # nbalok = math.ceil(nbalok1 + 2 * nbalok2)
    nmonuch2 = nbalok2
    nmonuch1 = nbalok1 - 1
    nmonuch = nmonuch1 + nmonuch2

elif shirtrot > 0.75 and shirtrot < 3.15:  # когда тротуар больше 0,75 м и меньше 3,15 м
    nbalok1 = Spoln // Shirbalki
    shirinaomon1 = round(((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1)), 3)
    while shirinaomon1 < 0.35:
        nbalok1 = nbalok1 - 1
        shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
    nmonuch1 = nbalok1 - 1
    nmonuch = nmonuch1
    nmonuch2 = 0
    shirinaomon2 = 0
    nbalok = nbalok1
    shagbalok1 = round(shirinaomon1 + Shirbalki, 3)

elif shirtrot == 0.75:  # когда вместо тротуаров служебные проходы

    nbalok1 = Spoln // Shirbalki
    shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
    while shirinaomon1 < 0.35:
        nbalok1 = nbalok1 - 1
        shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)

    shagbalok1 = round(shirinaomon1 + Shirbalki, 3)
    nbalok = nbalok1
    nmonuch1 = nbalok1 - 1
    nmonuch2 = 0
    shirinaomon2 = 0
    nmonuch = nmonuch1

else:
    if console == 1:  # когда тротуаров и служебных проходов на пролетном строении нет, но есть тротуарные консоли
        nbalok1 = Spoln // Shirbalki
        shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
        while shirinaomon1 < 0.35:
            nbalok1 = nbalok1 - 1
            shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
        shagbalok1 = round(shirinaomon1 + Shirbalki, 3)
    else:  # когда тротуаров и служебных проходов на пролетном строении нет и нет тротуарных консолей
        nbalok1 = Spoln // Shirbalki
        shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
        while shirinaomon1 < 0.35:
            nbalok1 = nbalok1 - 1
            shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
        shagbalok1 = round(shirinaomon1 + Shirbalki, 3)

    shagbalok1 = round(shirinaomon1 + Shirbalki, 3)
    nbalok = nbalok1
    nmonuch1 = nbalok1 - 1
    nmonuch2 = 0
    shirinaomon2 = 0
    nmonuch = nmonuch1

# Расчет объемов

Vbal = round(nbalok * Vbalki * n, 2)
Vplitomon = round(Spoln * Bplomonol * Hpliti * (n + 1), 2)
if trotuari == 1:
    Vmonuch = round((Hpliti * Lpliti * shirinaomon1 * nmonuch1) + (Hpliti * Lpliti * shirinaomon1 * nmonuch2), 2)
else:
    Vmonuch = round((Hpliti * Lpliti * shirinaomon1 * nmonuch1) + (Hpliti * Lpliti * shirinaomon1), 2)

# Вычисление основных параметров пролетного строения
Ltotal = Lpr + nzazor * zazor

# Начало блока расчета параметров опор сооружения
import math

print(' ')
print("-----------------------=== Начало блока расчета параметров опор сооружения ===---------------------------------")
print(' ')

nopor = n + 1  # количество опор на сооружение
nust = 2  # количество устоев на сооружение
nprom = nopor - nust  # количестов промежуточных опор
nrochust = nbalok  # количество опорных частей на 1 устой
nrochprom = 2 * nbalok  # количество опорных частей на 1 промежуточную опору
Lrigprom = 0
Bfasrigprom = 0
Vrigprom = 0
# блок расчета параметров насадки устоя
# количество опор на сооружение
boporch = 0.4  # ширина опорной части в поперечнике (Например, РОЧ 250х400 или для балок длиной 33м РОЧ 300х400)
bfasroch = 0.25  # ширина опорной части в поперечнике (Например, РОЧ 250х400 или для балок длиной 33м РОЧ 300х400)
bfaspodf = 0.15  # расстояние от передней грани РОЧ до передней грани подферменной площадки - min 0.15 м.
bfasrig = 0.25  # расстояние от передней грани подферменника до передней грани ригеля - для балок до 33 м. - 0.15 м.,
# для балок длиной 33 м - 0.25 м.
hroch = 0.052  # высота опорной части
bshkaf = 0.3
Lrigust = Spoln
Bfasrigust = round(osopor + zazor + bshkaf + 0.5 * bfasroch + bfaspodf + bfasrig, 2)
if dlinaproleta < 21:
    Hrig = 0.8
elif dlinaproleta > 21 and dlinaproleta < 27:
    Hrig = 1.0
else:
    Hrig = 1.2
Vrigust = round(
    Hrig * Lrigust * Bfasrigust + 0.5 * (((Bfasrigust - bshkaf) * 0.1) * (Bfasrigust - bshkaf)) * Lrigust, 2)

# Блок расчета промежуточных опор
# Блок расчета ригелей промежуточных опор
bpodferm = 0.15  # расстояние между боковой гранью РОЧ и боковой гранью подферменной площадки - min 0.15 м.
brigbok = 0.25  # расстояние от боковой грани подферменной площадки до торца ригеля - min 0.25 м.
if nprom != 0:
    Lrig1 = (nbalok - 1) * shagbalok1
    Lrigprom = Lrig1 + boporch + 2 * (bpodferm + brigbok)
    Bfasrigprom = round(zazor + bfasroch + 2 * (bfaspodf + bfasrig + osopor), 2)
    Vrigprom = round(Hrig * Lrigprom * Bfasrigprom - (Bfasrigprom * (2 * (0.5 * 0.4 * 1.2))), 2)

#  Блок расчета стоек опоры

print(" ")
print("---------------------------------=== Блок расчета стоек опоры ===-------------------------------")
print(" ")

if (Lrigust - 3) <= 6:
    nstoekust = 2
elif (Lrigust - 3) > 6 and (Lrigust - 3) <= 12:
    nstoekust = 3
elif (Lrigust - 3) > 12 and (Lrigust - 3) <= 18:
    nstoekust = 4
elif (Lrigust - 3) > 18 and (Lrigust - 3) <= 24:
    nstoekust = 5
elif (Lrigust - 3) > 24 and (Lrigust - 3) <= 30:
    nstoekust = 6
else:
    nstoekust = 7

if nprom != 0:
    if (Lrigprom - 3) <= 6:
        nstoekprom = 2
    elif (Lrigprom - 3) > 6 and (Lrigprom - 3) <= 12:
        nstoekprom = 3
    elif (Lrigprom - 3) > 12 and (Lrigprom - 3) <= 18:
        nstoekprom = 4
    elif (Lrigprom - 3) > 18 and (Lrigprom - 3) <= 24:
        nstoekprom = 5
    elif (Lrigprom - 3) > 24 and (Lrigprom - 3) <= 30:
        nstoekprom = 6
    else:
        nstoekprom = 7

    shagstoekprom = round(((Lrigprom - 3) / (nstoekprom - 1)), 3)

nstoek = nstoekust
shagstoekust = round(((Lrigust - 3) / (nstoekust - 1)), 3)

# if nprom != 0:
#     shagstoekprom = round((Lrigprom / nstoekprom), 2)

poperucl = float(input("Введите поперечный уклон проезжей части: "))
hdo = float(input("Введите толщину а/б покрытия проезжей части: "))
hzashsl = float(input("Введите толщину защитного слоя проезжей части: "))
hgidroiz = float(input("Введите толщину гидроизоляции проезжей части: "))
hvirsl = float(input("Введите толщину выравнивающего слоя проезжей части: "))
zaglublrostv = float(input("Введите величину заглубления ростверка в грунт: "))
hpodf = 0.15  # минимальная высота подферменной площадки
Hstr = round((poperucl * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalki), 2)

otmpch1 = []

for i in range(n):
    print("Введите отметку проезжей части над опорой № ", i + 1, ":")
    otmpch = float(input())
    if otmpch == "": break
    otmpch1.append(otmpch)

otmpch1.append(otmpch)

# shema = (dlinaproleta1[i] "+" dlinaproleta1[i + 1])

# Проверка читаемости введенных значений длины пролетных строений
# otmpch = float(input("Введите отметку проезжей части над опорой № : "))
otmzeli = float(input("Введите отметку земли: "))
otmrig = round((otmpch - Hstr - hroch - hpodf - Hrig), 2)
otmrostv = otmzeli - zaglublrostv
Lstoek = round((otmrig - otmrostv), 2)
if Lstoek <= 6:
    Dstoiki = 0.8
elif Lstoek > 6 and Lstoek <= 10:
    Dstoiki = 1.0
elif Lstoek > 10 and Lstoek <= 15:
    Dstoiki = 1.2
Sstoek1 = round(math.pi * ((Dstoiki ** 2) / 4), 2)
Sstgidro = round(((2 * math.pi * (0.5 * Dstoiki)) * zaglublrostv * nstoek), 2)
Vstoek1 = Lstoek * Sstoek1 * nstoek
Vstoek = round((Vstoek1 * nopor), 2)

#  Блок определения параметров ростверка
Lrostvust = (shagstoekust * (nstoek - 1)) + Dstoiki + 2 * 1.2  # расчет длины ростверка устоев

Brostv = round((Dstoiki + 2 * 1.15), 2)  # расчет ширины ростверка по фасаду
if Lstoek < 4 and Lstoek > 1:  # условие определения высоты ростверка
    Hrostv = 0.8
elif Lstoek > 4 and Lstoek < 6:
    Hrostv = 1.0
elif Lstoek > 6 and Lstoek < 10:
    Hrostv = 1.2
else:
    Hrostv = 1.5
Vrostvust = round((Lrostvust + Brostv + Hrostv), 2)  # расчет объема ростверка
Srosgidroust = round((2 * (Brostv * Hrostv) + 2 * (Lrostvust * Hrostv) + (Brostv * Lrostvust - Sstoek1 * nstoek)), 2)
if nprom != 0:
    Lrostvprom = (shagstoekprom * (nstoek - 1)) + Dstoiki + 2 * 1.2  # расчет длины ростверка промежуточных опор
    Vrostvprom = round((Lrostvprom + Brostv + Hrostv), 2)  # расчет объема ростверка
    Srosgidroprom = round(
        (2 * (Brostv * Hrostv) + 2 * (Lrostvprom * Hrostv) + (Brostv * Lrostvprom - Sstoek1 * nstoek)), 2)

#  блок расчета количества свай

bsvai = float(input("Введите размер стороны сваи: "))  # запрос размера стороны сваи
Lsvai = int(input("Введите длину сваи: "))  # запрос длины сваи
Ssvai = round((bsvai ** 2), 2)  # расчет площади поперечного сечения сваи
Vsvai = Ssvai * Lsvai  # расчет объема одной сваи
shagsvai = 1.2  # шаг сваи
nsvaib = round((Brostv - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай по фасаду
nsvailust = round((Lrostvust - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай вдоль ростверка

if nprom != 0:
    nsvailprom = round((Lrostvprom - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай вдоль ростверка
    nsvaiprom = nsvaib * nsvailprom  # общее кол-во свай на одну промежуточную опору

nsvaiust = nsvaib * nsvailust  # общее кол-во свай на один устой
otmnizrost = round((otmrostv - Hrostv), 3)  # расчет отметки низа ростверка
otmsvai = round((otmnizrost - Lsvai), 3)  # расчет отметки низа свай

# data_ish = 'data_enter.json'
# with open(data_ish, 'w')as dish:
#     json.dump(data_enter, dish)

# filename = 'nums.json'
# with open(filename, 'w')as f:
#     json.dump(nums, f)
# Вывод промежуточных результатов расчета параметров пролетного строения
print(' ')
print("                             Промежуточные результаты расчетов по объекту: ", nazvanie)
print("Габарит проезжей части сооружения: Г - ", gabarit)
print('Схема сооружения: ', shema)
print("Количество пролетных строений: ", n, "шт.")
print("Длина пролетных строений L(пр) = ", Ltotal, "м.")
print("Тип дорожного ограждения: ", ogrsoob)
print("Масса дорожного ограждения: ", massogr * dlinaproleta, "кг")
print("Ширина дорожного ограждения: ", shirogr, "м.")
print("Ширина тротуара/служебного прохода: ", shirtrot, "м.")
print("Полная ширина пролетного строения: ", Spoln, "м.")
print("Количество балок в пролетном строении: ", nbalok, "шт.")
print("Шаг балок пролетного строения: ", shagbalok1, "м.")

if shirtrot > 3.15:
    print("Шаг балок пролетного строения под тротуарами: ", shagbalok2, "м.")

print("Объем балок пролетного строения: ", Vbal, "м3")
print("Общая масса балок пролетного строения: ", round((mbalki * nbalok), 2), "т.")
print("Марка балок пролетного строения: ", harbalki)
print("Характеристики материала балок пролетного строения: ", matbalki)
print("Ширина монолитных участков под проезжей частью: ", shirinaomon1, "м.")
if trotuari == 1:
    print("Ширина монолитных участков под тротуарами: ", shirinaomon2, "м.")
print("Объем средних монолитных участков пролетного строения: ", Vmonuch, "м3")
print("Объем плит омоноличивания балок: ", Vplitomon, "м3")
#  Блок вывода промежуточных расчетных данных опор сооружения
print("Кол-во опор сооружения:", nopor, "шт.")
print("Количество устоев: ", nust, "шт.")
print("Количество опорных частей на устои: ", (nrochust * nust), "шт.")

if nprom != 0:
    print("-----------------------------------------------------------------------------------------")
    print("Количество промежуточных опор: ", nprom, "шт.")
    print("Ширина ригеля промежуточной опоры в поперечнике: ", Lrigprom, "м.")
    print("Ширина ригеля промежуточной опоры по фасаду: ", Bfasrigprom, "м.")
    print("Объем ригелей промежуточных опор: ", Vrigprom * nprom, "м3")
    print("Количество опорных частей на промежуточные опоры: ", (nrochprom * nprom), "шт.")
    print("Количество опорных частей на сооружение: ", (nrochust * nust) + (nrochprom * nprom), "шт.")

print(" ")
print("-----------===Геометрические парметры опор===-------------")
print(" ")
print("Ширина насадки устоя в поперечнике: ", Lrigust, "м.")
print("Ширина насадки устоя по фасаду: ", Bfasrigust, "м.")
print("Высота ригеля: ", Hrig, "м.")
print("Объем насадок устоев: ", Vrigust * nust, "м3")
#  Блок вывода промежуточных результатов расчета стоек опор
print("Количество стоек опор: ", nstoek, "шт.")

if nprom != 0:
    print("Шаг стоек промежуточной опоры: ", shagstoekprom, "м.")

print("Шаг стоек устоев: ", shagstoekust, "м.")
print("Отметка проезжей части: ", otmpch)
print("Строительная высота: ", Hstr, "м.")
print("Отметка низа ригеля: ", otmrig)
print("Отметка верха ростверка: ", otmrostv)
print("Высота стоек: ", Lstoek, "м.")
print("Диаметр стоек Dst: ", Dstoiki, "м.")
print("Объем стоек: ", Vstoek, "м3")
print("Площадь поверхности гидроизоляции: ", Sstgidro, "м2")
print(" ")
print("---------------------------------=== Конец расчета стоек ===--------------------------")
print(" ")
#  блок вывода промежуточных расчетных данных ростверка
print("Ширина ростверка по фасаду: ", Brostv, "м.")
print("Высота ростверка: ", Hrostv, "м.")
print("Длина ростверка устоя: ", round(Lrostvust, 2), "м.")
print("Площадь гидроизоляции ростверка устоя: ", round(Srosgidroust, 2), "м2")
print("Объем ростверка устоя: ", round(Vrostvust, 2), "м3")
print("Суммарная площадь гидроизоляции ростверков: ", round((Srosgidroust * nust), 2), "м2")
print("Суммарный объем ростверков: ", round((Vrostvust * nust), 2), "м3")

if nprom != 0:
    print("Длина ростверка промежуточной опоры: ", round(Lrostvprom, 2), "м.")
    print("Площадь гидроизоляции ростверка промежуточной опоры: ", round(Srosgidroprom, 2), "м2")
    print("Объем ростверка промежуточной опоры: ", round(Vrostvprom, 2), "м3")
    print("Суммарная площадь гидроизоляции ростверков: ", round((Srosgidroust * nust) + (Srosgidroprom * nprom), 2),
          "м2")
    print("Суммарный объем ростверков: ", round((Vrostvust * nust) + (Vrostvprom * nprom), 2), "м3")

# блок вывода промежуточных расчетных значений свай
print("Количество свай по фасаду: ", nsvaib, "шт.")
print("Количество свай вдоль ростверка устоя: ", nsvailust, "шт.")
print("Общее количество свай на устой: ", nsvaiust, "шт.")
print("Общее количество свай на сооружение: ", (nsvaiust * nust), "шт.")
print("Объем сваи: ", Vsvai, "м3")
print("Объем свай на один устой: ", round((Vsvai* nsvaiust), 2), "м3")
print("Объем свай на сооружение: ", round((Vsvai * (nsvaiust * nust)), 2), "м3")
print("Отметка низа ростверка: ", otmnizrost)
print("Отметка низа свай: ", otmsvai)

if nprom != 0:
    print("Количество свай вдоль ростверка промежуточной опоры: ", nsvailprom, "шт.")
    print("Общее количество свай на промежуточную опору: ", nsvaiprom, "шт.")
    print("Общее количество свай на сооружение: ", (nsvaiust * nust) + (nsvaiprom * nprom), "шт.")
    print("Объем свай на оду промежуточную опору: ", round((Vsvai * nsvaiprom), 2), "м3")
    print("Объем свай на сооружение: ", round((Vsvai * ((nsvaiust * nust) + (nsvaiprom * nprom))), 2), "м3")

print(" ")
print("--------------------=== Конец расчета параметров опор ===------------------------")
print(" ")

# Вывод расчетных данных в файл Excel

# data_exp = 'data_exp.json'
# with open(data_exp)as de:
#     data_exp_new = json.load(de)
#
# print(data_exp_new)

book = openpyxl.Workbook()

# from data_exit_Excel import*

sheet = book.active

book.save("data_exit.xlsx")
book.close()
