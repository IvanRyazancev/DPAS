# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:41:37 2020

@author: ryazantsev_ia
"""
print(" ")
print("                           Программа для определения параметров искусственного сооружения")
print(" ")
print("Данная программа предназначена для определения основных параметров искусственных сооружений дорожного ")
print("                           хозяйства, имея минимальное количество исходных данных")
print(" ")
nazvanie = input("Введите название объекта: ")
gabarit = int(input("Введите габарит проезжей части: "))
n = int(input("Введите количество пролетных строений: "))
Lpr = 0
zazor = 0.05
nzazor = n - 1

while n <= 0:
    n = int(input("Введите количество пролетных строений: "))

# Введение длины пролетных строений
dlinaproleta = 0
for i in range(n):
    dlinaproleta = int(input("Введите длину пролетного строения № "))
    Lpr += dlinaproleta

# Проверка читаемости введенных значений длины пролетных строений
for i in range(n):
    print("Длина пролетного строения №", i + 1, ":", dlinaproleta, "м.")

# Вычисление схемы сооружения
resultString = dlinaproleta
for i in range(n - 1):
    resultString = resultString, "+", dlinaproleta

# ввод типа дорожного ограждения
tipogr = int(input("Выберите тип дорожного ограждения: 1 - барьерное ограждение; 2- парапетное ж/б ограждение "))
while tipogr != 1 and tipogr != 2:
    tipogr = int(input("Выберите тип дорожного ограждения: 1 - барьерное ограждение; 2- парапетное ж/б ограждение "))
if tipogr == 1:
    shirogr = 0.41
    ogrsoob = "металлическое барьерное ограждение."
else:
    shirogr = 0.48
    ogrsoob = "парапетное ж/б ограждение."

# ввод типа тротуаров
trotuari = int(input("Имеются ли на пролетном строении тротуары или служебные проходы: 1 - да; 2 - нет. "))
while trotuari != 1 and trotuari != 2:
    trotuari = int(input("Имеются ли на пролетном строении тротуары или служебные проходы: 1 - да; 2 - нет. "))
if trotuari == 1:
    tiptrot = int(input("Это тротуар или служебный проход? 1 - тротуар; 2 - служебный проход. "))
    while tiptrot != 1 and tiptrot != 2:
        tiptrot = input("Это тротуар или служебный проход? 1 - тротуар; 2 - служебный проход. ")
    if tiptrot == 1:
        shirtrot = float(input("Введите ширину тротуара: "))
    else:
        shirtrot = 0.75
else:
    shirtrot = 0

# определение наличия консолей на пролетном строении
console = int(input("Имеется ли на пролетном строении тротуарные консоли? 1 - да; 2 - нет. "))
while console != 1 and console != 2:
    console = int(input("Имеется ли на пролетном строении тротуарные консоли? 1 - да; 2 - нет. "))
if console == 1:
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
import math

# парамеры балки
Shirbalki = 1.4
Vbalki = 10.114
Hpliti = 0.18
Bplomonol = 0.7
Lpliti = dlinaproleta - 2 * 0.7

shagbalkimin = float(input("Введите минимальный шаг балок: "))
while shagbalkimin > 2.25 or shagbalkimin < 1.75:
    shagbalkimin = float(input("Введите минимиальный шаг балок: "))
shagbalkimax = float(input("Введите максимальный шаг балок: "))
while shagbalkimax > 2.25 or shagbalkimax < 1.75:
    shagbalkimax = float(input("Введите максимальный шаг балок: "))
while shagbalkimin > shagbalkimax:
    print("Введенные значения неверны!")
    shagbalkimin = float(input("Введите минимальный шаг балок: "))
    while shagbalkimin > 2.25 or shagbalkimin < 1.75:
        shagbalkimin = float(input("Введите максимальный шаг балок: "))
    shagbalkimax = float(input("Введите максимальный шаг балок: "))
    while shagbalkimax > 2.25 or shagbalkimax < 1.75:
        shagbalkimax = float(input("Введите максимальный шаг балок: "))

shagbalok1 = (shagbalkimin + shagbalkimax) / 2
nbalok1 = (gabarit + shirogr) / shagbalok1
shirinaomon1 = round((((gabarit + shirogr) - (nbalok1 * Shirbalki)) / (nbalok1 + 1)), 3)
nbalok2 = (shirtrot + 0.5 * shirogr + bortomon) / shagbalok1
shirinaomon2 = round((((shirtrot + 0.5 * shirogr + bortomon) - (nbalok2 * Shirbalki)) / (nbalok2)), 3)
nbalok = math.ceil(nbalok1 + 2 * nbalok2)
nmonuch1 = nbalok1 + 1
nmonuch2 = nbalok2 - 1
nmonuch = nmonuch1 + nmonuch2
# Расчет объемов

Vbal = round(nbalok * Vbalki*n, 2)
Vplitomon = round((Spoln * Bplomonol * Hpliti) * (n + 1), 2)
Vmonuch = round((Hpliti * Lpliti * shirinaomon1 * nmonuch1) + (Hpliti * Lpliti * shirinaomon1 * nmonuch2), 2)

# Вычисление основных параметров пролетного строения
Ltotal = Lpr + nzazor * zazor

# Вывод промежуточных результатов расчета параметров пролетного строения
print(' ')
print("                                       Промежуточные результаты расчетов по объекту: ", nazvanie)
print("Габарит проезжей части сооружения: Г - ", gabarit)
print("Количество пролетных строений: ", n, "шт.")
print('Схема сооружения: ', resultString)
print("Длина пролетных строений L(пр) = ", Ltotal, "м.")
print("Тип дорожного ограждения: ", ogrsoob)
print("Ширина тротуара/служебного прохода: ", shirtrot, "м.")
print("Полная ширина пролетного строения: ", Spoln, "м.")
print("Ширина дорожного ограждения: ", shirogr, "м.")
print("Количество балок в пролетном строении: ", nbalok, "шт.")
print("Объем балок пролетного строения:", Vbal, "м3")
print("Ширина монолитных участков под проезжей частью: ", shirinaomon1, "м.")
print("Ширина монолитных участков под тротуарами: ", shirinaomon2, "м.")
print("Объем средних монолитных участковпролетного строения: ", Vmonuch, "м3")
print("Объем плит омоноличивания балок: ", Vplitomon, "м3")