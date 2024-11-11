import math
# from Graph_interpheis_1 import Window
# from Window_dialogs import *

# window = Window(300, 500)
# window.run()

print(" ")
print("                      Программа для определения параметров искусственного сооружения (ОПИС)    ")
# print("                         Determining the Parameters of an Artificial Structure (DPAS)          ")
#print(" ")
print("Данная программа предназначена для определения основных параметров искусственных сооружений дорожного ")
print("                           хозяйства, имея минимальное количество исходных данных")
print(" ")

nazvanie = input("Введите название объекта: ")
gabarit = int(input("Введите габарит проезжей части: "))
while gabarit <= 0:
    gabarit = int(input("Введите габарит проезжей части: "))
n = int(input("Введите количество пролетных строений: "))
Lpr = 0  # Длина пролетного строения
zazor = 0.05  # Зазор между балками
nzazor = n - 1  # Количество зазоров на сооружение

while n <= 0:
    n = int(input("Введите количество пролетных строений: "))  # проверка корректности введенного значения n

dlinaproleta1 = 0
Lpliti1 = 0
Lpliti = []
dlinaproleta = []  # формирование списка длин пролетных строений
for prol_str in range(n):
    print("Введите длину пролетного строения №", prol_str + 1, ":")  # Запрос длины пролетных строений
    dlinaproleta1 = float(input())
    # if dlinaproleta1 == "": break  # проверка корректности введенных значений dlinaproleta1
    dlinaproleta.append(dlinaproleta1)  # Заполнение списка длин пролетных строений
    Lpliti1 = dlinaproleta1 - 2 * 0.7  # Вычисление длины плиты балки с учетом недоомоноличивания 0,7 м с каждой стороны
    Lpliti.append(Lpliti1)  # Заполнение списка длин плит балок пролетных строений
    Lpr += dlinaproleta1  # Вычисление длины всех пролетных строений, без учета зазоров

for prol_str in range(n):
    print("Длина пролетного строения №", prol_str + 1, ":", dlinaproleta[prol_str],
          "м.")  # Проверка правильности введенных данных по длине пролетных строений

shema = ' + '.join([str(int(i)) for i in dlinaproleta])  # Формирование формы записи схемы сооружения

Shirbalki = 1.4  # Ширина плиты балки
Hpliti = 0.18  # Высота плиты балки
Bplomonol = 0.7  # Длина плиты омоноличивания балки (предшовные участки и плиты доомоноличивания балок пролетного строения)
Hbalki1 = 0
Hbalki2 = []
for n_balki in range(n):
    print("Выберите высоту балки пролетного строения № ", n_balki + 1,
          "0.93 м - 1; 1.23 м - 2; 1.53 м - 3: ")  # Запрос высоты балки пролетного строения
    Hbalki1 = int(input())
    Hbalki2.append(Hbalki1)  # Заполнение списка высот балок пролетного строения

# блок подбора балок пролетного строения в зависимости от длины пролетного строения и высоты балок пролетного строения
console = 0
Hbalki = 0
osopor = 0
Vbalki = 0
mbalki = 0
harbalki = 0
matbalki = 0
Vbal = 0
Spoln = 0  # полная ширина пролетного строения
Hbalki3 = []
osopor1 = []
Vbalki1 = []
mbalki1 = []
harbalki1 = []
matbalki1 = []
for c in range(n):  # подбор балок и их характеристик по длине пролета и высоте балки. Вычисление их объема.
    if dlinaproleta[c] == 12 and Hbalki2[c] == 1:
        Hbalki = 0.93
        osopor = 0.3
        Vbalki = 6.59
        mbalki = 16.5
        harbalki = 'Б 1200.140.93'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 15 and Hbalki2[c] == 1:
        Hbalki = 0.93
        osopor = 0.3
        Vbalki = 8.40
        mbalki = 21.0
        harbalki = 'Б 1500.140.93'
        matbalki = 'B40 F300 W6'
    elif dlinaproleta[c] == 11.9 and Hbalki2[c] == 2:
        Hbalki = 1.23
        osopor = 0.3
        Vbalki = 7.54
        mbalki = 18.9
        harbalki = 'Б 1190.140.123'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 15 and Hbalki2[c] == 2:
        Hbalki = 1.23
        osopor = 0.3
        Vbalki = 9.46
        mbalki = 23.7
        harbalki = 'Б 1500.140.123'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 18 and Hbalki2[c] == 2:
        Hbalki = 1.23
        osopor = 0.3
        Vbalki = 11.63
        mbalki = 29.1
        harbalki = 'Б 1800.140.123'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 21 and Hbalki2[c] == 2:
        Hbalki = 1.23
        osopor = 0.3
        Vbalki = 13.01
        mbalki = 32.6
        harbalki = 'Б 2100.140.123'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 24 and Hbalki2[c] == 2:
        Hbalki = 1.23
        osopor = 0.3
        Vbalki = 15.18
        mbalki = 38.0
        harbalki = 'Б 2400.140.123'
        matbalki = 'B40 F300 W6'
    elif dlinaproleta[c] == 28 and Hbalki2[c] == 2:
        Hbalki = 1.23
        osopor = 0.3
        Vbalki = 18.07
        mbalki = 45.2
        harbalki = 'Б 2800.140.123'
        matbalki = 'B40 F300 W6'
    elif dlinaproleta[c] == 18 and Hbalki2[c] == 3:
        Hbalki = 1.53
        osopor = 0.3
        Vbalki = 12.42
        mbalki = 31.1
        harbalki = 'Б 1800.140.153'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 28 and Hbalki2[c] == 3:
        Hbalki = 1.53
        osopor = 0.3
        Vbalki = 19.36
        mbalki = 48.4
        harbalki = 'Б 2800.140.153'
        matbalki = 'B35 F300 W6'
    elif dlinaproleta[c] == 33 and Hbalki2[c] == 3:
        Hbalki = 1.53
        osopor = 0.4
        Vbalki = 24.35
        mbalki = 60.9
        harbalki = 'Б 3300.140.153'
        matbalki = 'B45 F300 W6'
    Vbal += Vbalki  # вычисление суммарного объема балок пролетных строений
    Hbalki3.append(Hbalki)
    osopor1.append(osopor)
    Vbalki1.append(Vbalki)
    mbalki1.append(mbalki)
    harbalki1.append(harbalki)
    matbalki1.append(matbalki)
Hbalki3.append(Hbalki3[
                   -1])  # добавление в конец списка высот балок значения высоты балки крайнего пролетного строения, так как высота балки на опоре 3 будет равна высоте балки на опоре 4 (например)
#  Конец подбора балок пролетного строения

# Выбор типа дорожного ограждения

tipogr = int(input(
    "Выберите тип дорожного ограждения: 1 - барьерное ограждение; 2- парапетное ж/б ограждение "))  # запрос типа дорожного ограждения
while tipogr != 1 and tipogr != 2:
    tipogr = int(input(
        "Выберите тип дорожного ограждения: 1 - барьерное ограждение; 2- парапетное ж/б ограждение "))  # проверка введенного значения типа дорожного ограждения
if tipogr == 1:
    shirogr = 0.4
    massogr = 49
    ogrsoob = "металлическое барьерное ограждение."
else:
    shirogr = 0.48
    massogr = 620
    ogrsoob = "парапетное ж/б ограждение."

# Конец подбора  типа дорожного ограждения

# Определение типа тротуаров и геометрических параметров пролетного строения

trotuari = int(input(
    "Имеются ли на пролетном строении тротуары или служебные проходы: 1 - да; 2 - нет. "))  # Запрос наличия/отсутствия служебных проходов/тротуаров
while trotuari != 1 and trotuari != 2:
    trotuari = int(input(
        "Имеются ли на пролетном строении тротуары или служебные проходы: 1 - да; 2 - нет. "))  # проверка корректности введенных значений
if trotuari == 1:  # если тротуары/служебные проходы есть
    bortomon = 0.25  # ширина бортика омоноличивания
    tiptrot = int(input(
        "Это тротуар или служебный проход? 1 - тротуар; 2 - служебный проход. "))  # запрос типа прохода - тротуар/служебный проход
    while tiptrot != 1 and tiptrot != 2:
        tiptrot = input("Это тротуар или служебный проход? 1 - тротуар; 2 - служебный проход. ")
    if tiptrot == 1:
        shirtrot = float(input("Введите ширину тротуара: "))  # запрос ширины тротуаров
    else:
        shirtrot = 0.75  # ширина служебного прохода
    Spoln = gabarit + 2 * (shirogr + shirtrot + bortomon)
else:
    shirtrot = 0  # если тротуара/служебного прохода нет
    console = int(input(
        "Имеется ли на пролетном строении тротуарные консоли? 1 - да; 2 - нет. "))  # определение наличия консолей на пролетном строении
    while console != 1 and console != 2:  # проверка корректности введенных данных
        console = int(input("Имеется ли на пролетном строении тротуарные консоли? 1 - да; 2 - нет. "))
    if console == 1:  # если тротуара/служебного прохода нет и есть консоль
        bortomon = 0  # бортик омоноличивания отсутствует
        shirconsole = float(input("Введите ширину тротуарной консоли: "))  # запрос ширины тротуарной консоли
        while shirconsole < 0:
            shirconsole = float(input("Введите ширину тротуарной консоли: "))
        if shirconsole > 0:
            Spoln = gabarit + 2 * (shirogr + shirtrot + shirconsole)  # Определение полной ширины пролетного строения
    else:  # если тротуара/служебного прохода нет и нет консоли
        shirconsole = 0  # Случай, когда на пролетном строении нет тротуаров/служебных проходов и тротуарных консолей
        bortomon = 0.25
        Spoln = gabarit + 2 * (shirogr + shirtrot + bortomon)  # Определение полной ширины пролетного строения

if trotuari == 1 and shirtrot > 3.15:  # когда тротуар больше 3,15 м
    nbalok1 = int((gabarit + 2 * shirogr + Shirbalki) // Shirbalki)
    shirinaomon1 = round(((gabarit + 2 * shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)

    while shirinaomon1 < 0.35:
        nbalok1 = nbalok1 - 1
        shirinaomon1 = round(((gabarit + 2 * shirogr + Shirbalki) - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)

    shagbalok1 = round(shirinaomon1 + Shirbalki, 3)

    if shagbalok1 > 2.25 or shagbalok1 < 1.75:
        print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")

    nbalok2 = int(((Spoln - (
            gabarit + 2 * shirogr + Shirbalki)) / 2) // Shirbalki)
    shirinaomon2 = round((((0.5 * Spoln - (
            0.5 * gabarit + shirogr + 0.5 * Shirbalki)) - (nbalok2 * Shirbalki)) / nbalok2), 3)

    while shirinaomon2 < 0.35:
        nbalok2 = nbalok2 - 1
        shirinaomon2 = round((((0.5 * Spoln - (
                0.5 * gabarit + shirogr + 0.5 * Shirbalki)) - (nbalok2 * Shirbalki)) / nbalok2), 3)

    shagbalok2 = round(shirinaomon2 + Shirbalki, 3)

    if shagbalok2 > 2.25 or shagbalok2 < 1.75:
        print("При данных исходных параметрах подобрать шаг балок нельзя! Измените марку балки, либо ширину тротуара!")

    nbalok = math.ceil(nbalok1 + 2 * nbalok2)
    nmonuch2 = nbalok2
    nmonuch1 = nbalok1 - 1
    nmonuch = nmonuch1 + nmonuch2

elif shirtrot > 0.75 and shirtrot < 3.15:  # когда тротуар больше 0,75 м и меньше 3,15 м
    nbalok1 = int(Spoln // Shirbalki)
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

    nbalok1 = int(Spoln // Shirbalki)
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
        nbalok1 = int(Spoln // Shirbalki)
        shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
        while shirinaomon1 < 0.35:
            nbalok1 = nbalok1 - 1
            shirinaomon1 = round((Spoln - (nbalok1 * Shirbalki)) / (nbalok1 - 1), 3)
        shagbalok1 = round(shirinaomon1 + Shirbalki, 3)
    else:  # когда тротуаров и служебных проходов на пролетном строении нет и нет тротуарных консолей
        nbalok1 = int(Spoln // Shirbalki)
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

# Расчет объемов пролетного строения
Vplitomon1 = 0
Vmonuch1 = 0
Vmonuch = []
Vplitomon = []
for i in range(n):
    Vplitomon1 = round(Spoln * Bplomonol * Hpliti * (n + 1), 2)
    Vplitomon.append(Vplitomon1)
    if trotuari == 1:
        Vmonuch = round((Hpliti * Lpliti[i] * shirinaomon1 * nmonuch1) + (Hpliti * Lpliti[i] * shirinaomon1 * nmonuch2),
                        2)
    else:
        Vmonuch = round((Hpliti * Lpliti[i] * shirinaomon1 * nmonuch1) + (Hpliti * Lpliti[i] * shirinaomon1), 2)
        Vmonuch.append(Vmonuch1)

# Вычисление основных параметров пролетного строения

Ltotal = Lpr + nzazor * zazor

# Начало блока расчета параметров опор сооружения

print(' ')
print("-----------------------=== Начало блока расчета параметров опор сооружения ===---------------------------------")
print(' ')

nopor1 = n + 1  # количество опор на сооружение
nopor2 = 0
nopor = []

for v in range(nopor1):
    nopor2 = nopor2 + 1
    nopor.append(nopor2)  # количестов промежуточных опор
nprom = nopor[1:-1]
nust = [nopor[0], nopor[-1]]
nomera = "№".join([str(int(b)) for b in nprom])

nrochust = nbalok  # количество опорных частей на 1 устой
nrochprom = 2 * nbalok  # количество опорных частей на 1 промежуточную опору
Bfasrigprom = 0
# Vrigprom = 0

# блок расчета параметров насадки устоя
# количество опор на сооружение

boporch = 0.4  # ширина опорной части в поперечнике (Например, РОЧ 250х400 или для балок длиной 33м РОЧ 300х400)
bfasroch = 0.25  # ширина опорной части в поперечнике (Например, РОЧ 250х400 или для балок длиной 33м РОЧ 300х400)
bfaspodf = 0.15  # расстояние от передней грани РОЧ до передней грани подферменной площадки - min 0.15 м.
bfasrig = 0.25  # расстояние от передней грани подферменника до передней грани ригеля - для балок до 33 м. - 0.15 м.,
# для балок длиной 33 м - 0.25 м.
hroch = 0.052  # высота опорной части
bshkaf = 0.3  # ширина шкафной стенки
Lrigust = Spoln  # ширина насадки устоя в поперечнике
Bfasrigust1 = 0  # ширина насадки устоя по фасаду
Vrigust1 = 0  # объем насадки
Hrig1 = 0  # Высота насадки устоя
osoporust = [osopor1[0], osopor1[-1]]  # количество и величина растояния от торца балки до оси опирания на устоях
Bfasrigust = []
Vrigust = []
if dlinaproleta1 < 21:
    Hrig1 = 0.8
elif 21 < dlinaproleta1 < 27:
    Hrig1 = 1.0
else:
    Hrig1 = 1.2
for v in range(len(nust)):
    Bfasrigust1 = round(osoporust[v] + zazor + bshkaf + 0.5 * bfasroch + bfaspodf + bfasrig, 2)
    Bfasrigust.append(Bfasrigust1)
    Vrigust1 = round(Hrig1 * Lrigust * Bfasrigust[v] + 0.5 * (
            ((Bfasrigust[v] - bshkaf) * 0.1) * (Bfasrigust[v] - bshkaf)) * Lrigust, 2)
    Vrigust.append(Vrigust1)

print(" ")
print("------------------------=== Блок расчета параметров подферменных площадок ===---------------------")
print(" ")

otmpch = 0
poperucl = 0
otmzeli = 0
otmpch1 = []
poperucl1 = []
otmzeli1 = []
for m in range(nopor1):
    print("Введите отметку проезжей части над опорой № ", m + 1, ":")
    otmpch = float(input())
    if otmpch == "": break

    print("Введите поперечный уклон проезжей части над опорой № ", m + 1)
    poperucl = float(input())
    if poperucl == "": break

    print("Введите отметку земли у опоры № ", m + 1)
    otmzeli = float(input())
    if otmzeli == "": break

    otmpch1.append(otmpch)
    poperucl1.append(poperucl)
    otmzeli1.append(otmzeli)

hdo = float(input("Введите толщину а/б покрытия проезжей части: "))
hzashsl = float(input("Введите толщину защитного слоя проезжей части: "))
hgidroiz = float(input("Введите толщину гидроизоляции проезжей части: "))
hvirsl = float(input("Введите толщину выравнивающего слоя проезжей части: "))
zaglublrostv = float(input("Введите величину заглубления ростверка в грунт: "))
hpodfbaz = 0.15  # минимальная высота подферменной площадки

# расчет строительной высоты пролетного строения

Hstr1 = 0
Hstr = []
for a in range(len(nopor)):
    Hstr1 = round((poperucl1[a] * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalki3[a]), 2)
    Hstr.append(Hstr1)

# конец расчета строительной высоты пролетного строения

# начало модуля расчета параметров подферменных площадок

boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м
Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
Bpodfust = zazor + osopor + 0.5 * boporchast + bfasroch
Bpodfprom = zazor + 2 * osopor + boporchast + 2 * bfasroch
Lpodf = Lpoproch + 2 * Lpoppodf
Vpodf1 = 0  # объем подферменной площадки одной
Vpodf2 = 0  # объем подферменной площадки одной
Vpodfs1 = 0  # общий объем подферменных площадок на опору
Vpodfs2 = 0  # общий объем подферменных площадок на опору
Vpodf3 = 0  # промежуточный общий объем подферменников
Vpodfbazust = round(hpodfbaz * Bpodfust * Lpodf, 3)
Vpodfbazprom = round(hpodfbaz * Bpodfprom * Lpodf, 3)

nbalokpol = int(round((nbalok - 1) // 2))
otmpodfbaz = 0
otmrig1 = 0
otmrostv = 0
otmrig = []
otmpodfbaz1 = []
otmrostv1 = []
for f in range(len(nopor)):
    otmrig1 = otmpch1[f] - Hstr[f] - hroch - hpodfbaz  # отметка верха ригеля на каждой опоре
    otmpodfbaz = otmpch1[f] - Hstr[f] - hroch  # отметка наименьшей подферменной площадки на каждой опоре
    otmrostv = otmzeli1[f] - zaglublrostv
    otmrig.append(otmrig1)
    otmpodfbaz1.append(otmpodfbaz)
    otmrostv1.append(otmrostv)

otmrigust_1 = otmrig[0]
otmrigust_2 = otmrig[-1]
poperuclust_1 = poperucl1[0]
poperuclust_2 = poperucl1[-1]

if nbalok1 % 2 == 0:
    nshag1 = 0
    hprir1 = 0
    hprir2 = 0
    hpodf1 = 0
    hpodf2 = 0
    otmpodf1 = 0
    otmpodf2 = 0
    Vpodf1 = 0
    Vpodf2 = 0
    Vpodfobsh1 = 0
    Vpodfobsh2 = 0
    hprir_1 = []  # список превышений на каждой подферменной площадке
    hprir_2 = []
    hpodf_1 = []  # список высот подферменных площадок
    hpodf_2 = []  # список высот подферменных площадок
    otmpodf_1 = []  # список отметок подферменных площадок на устое №1
    otmpodf_2 = []  # список отметок подферменных площадок на устое №2
    Vpodf_1 = []
    Vpodf_2 = []
    nshag2 = []
    for u in range((nbalok1 - 2) // 2):
        nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
        nshag2.append(nshag1)
        hprir1 = shagbalok1 * nshag2[u] * poperuclust_1
        hprir_1.append(hprir1)
        hprir2 = shagbalok1 * nshag2[u] * poperuclust_2
        hprir_2.append(hprir2)
        hpodf1 = hpodfbaz + hprir_1[u]
        hpodf_1.append(hpodf1)
        hpodf2 = hpodfbaz + hprir_2[u]
        hpodf_2.append(hpodf2)
        otmpodf1 = otmrigust_1 + hpodf_1[u]
        otmpodf_1.append(otmpodf1)
        otmpodf2 = otmrigust_2 + hpodf_2[u]
        otmpodf_2.append(otmpodf2)
        Vpodf1 = round(hpodf_1[u] * Bpodfust * Lpodf, 3)
        Vpodf_1.append(Vpodf1)
        Vpodf2 = round(hpodf_2[u] * Bpodfust * Lpodf, 3)
        Vpodf_2.append(Vpodf2)
        Vpodfs1 = sum(Vpodf_1)
        Vpodfobsh1 = round(((Vpodfs1 + Vpodfbazust) * 2), 3)
        Vpodfs2 = sum(Vpodf_2)
        Vpodfobsh2 = round(((Vpodfs2 + Vpodfbazust) * 2), 3)
else:
    nshag1 = 0
    hprir1 = 0
    hprir2 = 0
    hpodf1 = 0
    hpodf2 = 0
    otmpodf1 = 0
    otmpodf2 = 0
    Vpodf1 = 0
    Vpodf2 = 0
    Vpodfobsh1 = 0
    Vpodfobsh2 = 0
    hprir_1 = []  # список превышений на каждой подферменной площадке
    hprir_2 = []
    hpodf_1 = []  # список высот подферменных площадок
    hpodf_2 = []  # список высот подферменных площадок
    otmpodf_1 = []  # список отметок подферменных площадок на устое №1
    otmpodf_2 = []  # список отметок подферменных площадок на устое №2
    Vpodf_1 = []
    Vpodf_2 = []
    nshag2 = []
    for t in range((nbalok1 - 1) // 2):
        nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
        nshag2.append(nshag1)
        hprir1 = shagbalok1 * nshag2[t] * poperuclust_1
        hprir_1.append(hprir1)
        hprir2 = shagbalok1 * nshag2[t] * poperuclust_2
        hprir_2.append(hprir2)
        hpodf1 = hpodfbaz + hprir_1[t]
        hpodf_1.append(hpodf1)
        hpodf2 = hpodfbaz + hprir_2[t]
        hpodf_2.append(hpodf2)
        otmpodf1 = otmrigust_1 + hpodf_1[t]
        otmpodf_1.append(otmpodf1)
        otmpodf2 = otmrigust_2 + hpodf_2[t]
        otmpodf_2.append(otmpodf2)
        Vpodf1 = round(hpodf_1[t] * Bpodfust * Lpodf, 3)
        Vpodf_1.append(Vpodf1)
        Vpodf2 = round(hpodf_2[t] * Bpodfust * Lpodf, 3)
        Vpodf_2.append(Vpodf2)
        Vpodfs1 += Vpodf1
        Vpodfobsh1 = round(((Vpodfs1 + Vpodfbazust) * 2) - Vpodf_1[-1], 3)
        Vpodfs2 += Vpodf2
        Vpodfobsh2 = round(((Vpodfs2 + Vpodfbazust) * 2) - Vpodf_2[-1], 3)

print("Отметка верха насадки на устое № ", nust[0], ":", round(otmrig[0], 3))
print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz1[0], 3))
print("Объем подферменной площадки № ", nshag2[0], ":", round(Vpodfbazust, 3), "м3")
if nbalok1 % 2 == 0:
    for r in range((nbalok1 - 2) // 2):
        print("Отметка подферменной площадки № ", r + 2, ":", round(otmpodf_1[r], 3))
        print("Объем подферменной площадки № ", r + 2, ":", round(Vpodf_1[r], 3), "м3")
    print("Суммарный объем подферменников на устое № ", nust[0], ":", round(((Vpodfs1 + Vpodfbazust) * 2), 3), "м3")
else:
    for e in range((nbalok1 - 1) // 2):
        print("Отметка подферменной площадки № ", e + 2, ":", round(otmpodf_1[e], 3))
        print("Объем подферменной площадки № ", e + 2, ":", round(Vpodf_1[e], 3), "м3")
    print("Суммарный объем подферменников на устое № ", nust[0], ":", round(Vpodfobsh1, 3), "м3")
print("")

if len(nprom) != 0:
    hpodfbaz = 0.15  # минимальная высота подферменной площадки
    otmrigprom1 = otmrig[1:-1]
    poperuclprom1 = poperucl1[1:-1]
    otmpodfbazprom1 = 0
    poperuclprom = []
    otmrigprom = []
    otmpodfbazprom = []
    for p in range(len(nprom)):
        poperuclprom.append(poperuclprom1[p])
        otmpodfbazprom1 = otmrigprom1[p] + hpodfbaz  # отметка минимальной подферменной площадки
        otmpodfprom1 = 0
        hpodfprom1 = 0
        Vpodfprom1 = 0
        Vpodfobshprom3 = 0
        Vpodfsprom2 = 0
        otmpodfprom = []
        hpodfprom = []
        Vpodfprom = []
        if nbalok1 % 2 == 0:
            poperuclpromop = []
            otmpodfbazpromop = []
            for k in range((nbalok1 - 2) // 2):
                otmpodfbazpromop.append(otmpodfbazprom1)
                poperuclpromop.append(poperuclprom[p])

                otmpodfprom1 = round(otmpodfbazpromop[k] + shagbalok1 * poperuclpromop[k] * nshag2[k],
                                     3)  # вычисление отметки i-й подферменной площадки
                otmpodfprom.append(otmpodfprom1)
                hpodfprom1 = hpodfbaz + shagbalok1 * poperuclpromop[k] * nshag2[k]
                hpodfprom.append(hpodfprom1)
                Vpodfprom1 = round(hpodfprom[k] * Bpodfprom * Lpodf, 3)
                Vpodfprom.append(Vpodfprom1)
                Vpodfsprom2 += Vpodfprom1
                Vpodfobshprom3 = round(((Vpodfsprom2 + Vpodfbazprom) * 2), 3)

        else:

            poperuclpromop = []
            otmpodfbazpromop = []
            for m in range((nbalok1 - 1) // 2):
                otmpodfbazpromop.append(otmpodfbazprom1)
                poperuclpromop.append(poperuclprom[p])
                otmpodfprom1 = round(otmpodfbazpromop[m] + shagbalok1 * poperuclpromop[m] * nshag2[m],
                                     3)  # вычисление отметки i-й подферменной площадки
                otmpodfprom.append(otmpodfprom1)
                hpodfprom1 = hpodfbaz + shagbalok1 * poperuclpromop[m] * nshag2[m]
                hpodfprom.append(hpodfprom1)
                Vpodfprom1 = round(hpodfprom[m] * Bpodfprom * Lpodf, 3)
                Vpodfprom.append(Vpodfprom1)
                Vpodfsprom2 += Vpodfprom1
                Vpodfobshprom3 = round(((Vpodfsprom2 + Vpodfbazprom) * 2) - Vpodfprom[-1], 3)
        # # print(otmpodfbazprom)
        # # print(otmpodfbazprom1)
        # print(otmpodfbazpromop)
        # print(poperuclprom)
        print("Отметка верха ригеля промежуточной опоры № ", p + 2, ":", round(otmrigprom1[p], 3))
        print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbazpromop[p], 3))
        print("Объем подферменной площадки № ", nshag2[0], ":", round(Vpodfbazprom, 3), "м3")
        for y in range(len(nshag2)):
            print("Отметка подферменной площадки № ", y + 2, ":", round(otmpodfprom[y], 3))
            print("Объем подферменной площадки № ", y + 2, ":", round(Vpodfprom[y], 3), "м3")
        if nbalok1 % 2 == 0:
            print("Суммарный объем подферменных площадок на промежуточной опоре № ", p + 2, ":",
                  round(Vpodfobshprom3, 3), "м3")
        else:
            print("Суммарный объем подферменных площадок на промежуточной опоре № ", p + 2, ":",
                  round(Vpodfobshprom3, 3), "м3")
        print("")

print("Отметка верха насадки на устое № ", nust[-1], ":", round(otmrig[-1], 3))
print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz1[-1], 3))
print("Объем подферменной площадки № ", nshag2[0], ":", round(Vpodfbazust, 3), "м3")
if nbalok1 % 2 == 0:
    for w in range((nbalok1 - 2) // 2):
        print("Отметка подферменной площадки № ", w + 2, ":", round(otmpodf_2[w], 3))
        print("Объем подферменной площадки № ", w + 2, ":", round(Vpodf_2[w], 3), "м3")
    print("Суммарный объем подферменников на устое № ", nust[-1], ":", round((Vpodfs2 + Vpodfbazust) * 2, 3), "м3")
else:
    for q in range((nbalok1 - 1) // 2):
        print("Отметка подферменной площадки № ", q + 2, ":", round(otmpodf_2[q], 3))
        print("Объем подферменной площадки № ", q + 2, ":", round(Vpodf_2[q], 3), "м3")
    print("Суммарный объем подферменников на устое № ", nust[-1], ":", round(Vpodfobsh2, 3), "м3")

# конец модуля расчета параметров подферменных площадок и ригелей/насадок

# начало модуля расчета параметров стоек опор

print(" ")
print("---------------------------------=== Блок расчета стоек опоры ===-------------------------------")
print(" ")

bpodferm = 0.15  # расстояние между боковой гранью РОЧ и боковой гранью подферменной площадки - min 0.15 м.
brigbok = 0.25  # расстояние от боковой грани подферменной площадки до торца ригеля - min 0.25 м.
# Vrigprom1 = 0
# Vrigprom = []

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

if len(nprom) != 0:
    Lrig1 = (nbalok - 1) * shagbalok1
    Lrigprom = Lrig1 + boporch + 2 * (bpodferm + brigbok)  # ширина ригеля в поперечнике
    Bfasrigprom = round(zazor + bfasroch + 2 * (bfaspodf + bfasrig + osopor), 2)  # ширина ригеля по фасаду
    Vrigprom = round(Hrig1 * Lrigprom * Bfasrigprom - (Bfasrigprom * (2 * (0.5 * 0.4 * 1.2))), 2)  # объем ригеля

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

Vstoek = 0
Vstoek1 = 0
Lstoek = 0
Dstoiki = 0
Sstoek1 = 0
Sstgidro = 0
Lstoek1 = []
Dstoiki1 = []
Sstoek2 = []
Sstgidro1 = []
Vstoek2 = []

for g in range(nopor1):
    Lstoek = round((otmrig[g] - otmrostv1[g]), 2)
    Lstoek1.append(Lstoek)

    if Lstoek <= 6:
        Dstoiki = 0.8
    elif Lstoek > 6 and Lstoek <= 10:
        Dstoiki = 1.0
    elif Lstoek > 10 and Lstoek <= 15:
        Dstoiki = 1.2
    Dstoiki1.append(Dstoiki)

    Sstoek1 = round(math.pi * ((Dstoiki ** 2) / 4), 2)
    Sstoek2.append(Sstoek1)

    Sstgidro = round(((2 * math.pi * (0.5 * Dstoiki)) * zaglublrostv * nstoek), 2)
    Sstgidro1.append(Sstgidro)

#  Конец блока расчета параметров стоек

#  Начало блока расчета парметров ростверка

Lrostvust = 0
Vrostvust = 0
Brostv = 0
Hrostv = 0
Srosgidroust = 0
Lrostvust1 = []
Vrostvust1 = []
Brostv1 = []
Hrostv1 = []
Srosgidroust1 = []
for h in range(nopor1):
    Vstoek1 = Lstoek1[h] * Sstoek1 * nstoek
    Vstoek2.append(Vstoek1)
    Vstoek += round(Vstoek1, 2)
    Lrostvust = (shagstoekust * (nstoek - 1)) + Dstoiki1[h] + 2 * 1.2  # расчет длины ростверка устоев
    Lrostvust1.append(Lrostvust)
    Brostv = round((Dstoiki1[h] + 2 * 1.15), 2)  # расчет ширины ростверка по фасаду
    Brostv1.append(Brostv)
    if Lstoek < 4 and Lstoek > 1:  # условие определения высоты ростверка
        Hrostv = 0.8
    elif Lstoek > 4 and Lstoek < 6:
        Hrostv = 1.0
    elif Lstoek > 6 and Lstoek < 10:
        Hrostv = 1.2
    else:
        Hrostv = 1.5
    Hrostv1.append(Hrostv)
    Vrostvust = round((Lrostvust1[h] + Brostv1[h] + Hrostv1[h]), 2)  # расчет объема ростверка
    Vrostvust1.append(Vrostvust)
    Srosgidroust = round((2 * (Brostv1[h] * Hrostv1[h]) + 2 * (Lrostvust1[h] * Hrostv1[h]) + (
            Brostv1[h] * Lrostvust1[h] - Sstoek2[h] * nstoek)),
                         2)
    Srosgidroust1.append(Srosgidroust)

Brostv2 = Brostv1[1:-1]
Hrostv2 = Hrostv1[1:-1]
if len(nprom) != 0:
    Lrostvprom = 0
    Vrostvprom = 0
    Srosgidroprom = 0
    Lrostvprom1 = []
    Vrostvprom1 = []
    Srosgidroprom1 = []
    Sstoek3 = Sstoek2[1:-1]
    for j in range(len(nprom)):
        Lrostvprom = (shagstoekprom * (
                nstoekprom - 1)) + Dstoiki + 2 * 1.2  # расчет длины ростверка промежуточных опор
        Lrostvprom1.append(Lrostvprom)
        Vrostvprom = round((Lrostvprom + Brostv + Hrostv), 2)  # расчет объема ростверка
        Vrostvprom1.append(Vrostvprom)
        Srosgidroprom = round(
            (2 * (Brostv2[j] * Hrostv2[j]) + 2 * (Lrostvprom1[j] * Hrostv2[j]) + (
                    Brostv2[j] * Lrostvprom1[j] - Sstoek1 * nstoekprom)), 2)
        Srosgidroprom1.append(Srosgidroprom)

# Конец блока определения параметров ростверка

# Начало блока определения параметров свай

bsvai = float(input("Введите размер стороны сваи: "))  # запрос размера стороны сваи
Lsvai = int(input("Введите длину сваи: "))  # запрос длины сваи
Ssvai = round((bsvai ** 2), 2)  # расчет площади поперечного сечения сваи
Vsvai = Ssvai * Lsvai  # расчет объема одной сваи
shagsvai = 1.2  # шаг сваи

nsvaibust = 0
nsvailust = 0
nsvaibust1 = []
nsvailust1 = []

for az in range(nopor1):
    nsvaibust = round((Brostv - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай по фасаду
    nsvaibust1.append(nsvaibust)
    nsvailust = round((Lrostvust - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай вдоль ростверка
    nsvailust1.append(nsvailust)

if len(nprom) != 0:
    nsvaibprom = 0
    nsvailprom = 0
    nsvaibprom1 = []
    nsvailprom1 = []
    for ax in range(len(nprom)):
        nsvaibprom = round((Brostv - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай по фасаду
        nsvaibprom1.append(nsvaibprom)
        nsvailprom = round((Lrostvprom1[ax] - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай вдоль ростверка
        nsvailprom1.append(nsvailprom)

# Конец блока определения параметров свай

# Начало блока расчета отметок свай и низа ростверков

otmnizrostust = 0
otmsvaiust = 0
otmnizrostust1 = []
otmsvaiust1 = []
for ac in range(nopor1):
    otmnizrostust = round((otmrostv1[ac] - Hrostv), 3)  # расчет отметки низа ростверка
    otmnizrostust1.append(otmnizrostust)
    otmsvaiust = round((otmnizrostust1[ac] - Lsvai), 3)  # расчет отметки низа свай
    otmsvaiust1.append(otmsvaiust)
otmnizrostust2 = [otmnizrostust1[0], otmnizrostust1[-1]]
otmsvaiust2 = [otmsvaiust1[0], otmsvaiust1[-1]]

if len(nprom) != 0:
    otmnizrostprom1 = otmnizrostust1[1:-1]
    otmsvaiprom1 = otmsvaiust1[1:-1]

# конец блока расчета отметок свай и низа ростверков

# начало блока вывода предварительных результатов расчетов елементов сооружения

print("---------------------------------------------------------------")
print("Результаты определния параметров пролетного строения по объекту: ", nazvanie)
print("---------------------------------------------------------------")
print("")

print("----------=== Блок результатов пролетного строения ===---------")
print("")
print("Схема сооружения: ", shema)
print("Габарит проезжей части: Г -", gabarit)
print("Ширина барьерного ограждения: ", shirogr, "м.")
print("Полная ширина пролетного строения: ", Spoln, "м.")
print("Количество балок в пролетном строении: ", nbalok, "шт.")
if shirtrot > 3.15:
    print("Шаг балок под проезжей частью: ", shagbalok1, "м.")
    print("Шаг балок под тротуарами/служебными проходами: ", shagbalok2, "м.")
else:
    print("Шаг балок под проезжей частью: ", shagbalok1, "м.")
print("Полная длина пролетного строения: ", Ltotal, "м.")
for ab in range(n):
    print("Объем балок пролетного строения № ", ab + 1, ":", round(Vbalki1[ab] * nbalok, 2), "м3")
    print("Общая масса балок пролетного строения: ", round((mbalki1[ab] * nbalok), 2), "т.")
    print("Марка балок пролетного строения: ", harbalki1[ab])
    print("Характеристика материала балок пролетного строения: ", matbalki1[ab])
    print("Строительная высота пролетного строения № ", ab + 1, ":", Hstr[ab])
print("Объем балок на сооружение: ", round(Vbal * nbalok, 2), "м3")
print("Ширина монолитных участков под проезжей частью: ", shirinaomon1, "м.")
if trotuari == 1:
    print("Ширина монолитных участков под тротуарами: ", shirinaomon2, "м.")
print("Объем средних монолитных участков пролетного строения: ", Vmonuch, "м3")
print("Объем плит омоноличивания балок: ", Vplitomon, "м3")
print("Масса дорожного ограждения: ", round(massogr * Ltotal * 2, 2), "кг")

print("")
print("---------=== Конец блока результатов пролетного строения ===----------")
print("")

print("Количество опор на сооружение: ", len(nopor), "шт.")
print("Количество устоев: ", 2, "шт.")
print("Количество промежуточных опор: ", len(nprom), "шт.")

print(" ")
print("-------------------=== Характеристики устоев ===-------------------------")
print(" ")

print("Ширина насадки устоя в поперечнике: ", round(Lrigust, 2), "м.")
print("Ширина насадки устоя по фасаду: ", Bfasrigust, "м.")
print("Высота ригеля: ", Hrig1, "м.")
print("Объем насадок устоев: ", round(sum(Vrigust), 2), "м3")

#  Блок вывода промежуточных результатов расчета стоек опор
print("Количество стоек опор: ", nstoek, "шт.")

print("Шаг стоек устоев: ", shagstoekust, "м.")

if len(nprom) != 0:
    print("Шаг стоек промежуточной опоры: ", shagstoekprom, "м.")

print(" ")
print("------------------------------------------------------------------------")
print(" ")

if len(nprom) != 0:
    print(" ")
    print("-------------------=== Характеристики промежуточных опор ===-------------------------")
    print(" ")
    print("Количество промежуточных опор: ", len(nprom), "шт.")
    print("Ширина ригеля промежуточной опоры в поперечнике:", round(Lrigprom, 2), "м.")
    print("Ширина ригеля промежуточной опоры по фасаду: ", Bfasrigprom, "м.")
    print("Суммарный объем ригелей промежуточных опор: ", round(Vrigprom * len(nprom), 2), "м3")
    print("Количество опорных частей на промежуточные опоры: ", (nrochprom * len(nprom)), "шт.")

print(" ")
print("---------------------------------------------------------")
print(" ")
print("Суммарный объем бетона стоек на сооружение: ", round(Vstoek, 2), "м3")

print("Объем подферменных площадок на устое № ", nopor[0], ":", Vpodfobsh1, "м3")
print("Длина ростверка устоя № ", nopor[0], ":", round(Lrostvust1[0], 2), "м.")
print("Площадь гидроизоляции ростверка устоя № ", nopor[0], ":", Srosgidroust1[0], "м2")
print("Количество свай в ширину на устое № ", nopor[0], ":", nsvaibust1[0], "шт.")
print("Количество свай в длину на устое № ", nopor[0], ":", nsvailust1[0], "шт.")
print("Количество свай на устое № ", nopor[0], ":", nsvaibust1[0] * nsvailust1[0], "шт.")
print("Отметка оси проезжей части на устое № ", nopor[0], ":", otmpch1[0])
print("Отметки подферменников на устое № ", nopor[0], ":     ", otmpodf_1[:])
print("Отметка верха насадки на устое № ", nopor[0], ":      ", otmrig[0])
print("Отметка низа насадки на устое № ", nopor[0], ":      ", otmrig[0] - Hrig1)
print("Отметка верха ростверка на устое № ", nopor[0], ":   ", otmrostv1[0])
print("Отметка низа ростверка на устое № ", nopor[0], ":    ", otmnizrostust1[0])
print("Отметка низа свай на устое № ", nopor[0], ":         ", otmsvaiust1[0])

print("Объем подферменных площадок на устое № ", nopor[-1], ":", Vpodfobsh2, "м3")
print("Длина ростверка устоя № ", nopor[-1], ":", round(Lrostvust1[-1], 2), "м.")
print("Площадь гидроизоляции ростверка устоя № ", nopor[-1], ":", Srosgidroust1[-1], "м2")
print("Количество свай в ширину на устое № ", nopor[-1], ":", nsvaibust1[-1], "шт.")
print("Количество свай в длину на устое № ", nopor[-1], ":", nsvailust1[-1], "шт.")
print("Количество свай на устое № ", nopor[-1], ":", nsvaibust1[-1] * nsvailust1[-1], "шт.")
print("Отметка оси проезжей части на устое № ", nopor[-1], ":", otmpch1[-1])
print("Отметки подферменников на устое № ", nopor[-1], ":     ", otmpodf_2[:])
print("Отметка верха насадки на устое № ", nopor[-1], ":      ", otmrig[-1])
print("Отметка низа насадки на устое № ", nopor[-1], ":      ", otmrig[-1] - Hrig1)
print("Отметка верха ростверка на устое № ", nopor[-1], ":   ", otmrostv1[-1])
print("Отметка низа ростверка на устое № ", nopor[-1], ":    ", otmnizrostust1[-1])
print("Отметка низа свай на устое № ", nopor[-1], ":         ", otmsvaiust1[-1])

# print("Количество свай на промежуточных опорах на сооружение", i + 1, ":", sum(nsvaibprom1[i]*nsvailprom1[i])*nprom, "шт.")
print("Общее количество свай на устоях на сооружение :",
      nsvaibust1[az] * nsvailust1[az] + nsvaibust1[az] * nsvailust1[az], "шт.")
print("Количество опорных частей на сооружение: ", (nrochust * 2) + (nrochprom * len(nprom)), "шт.")

if len(nprom) != 0:
    for an in range(len(nprom)):
        # print("Объем подферменных площадок на промежуточной опоре № ", nprom[an], ":", Vpodfobshprom3, "м3")
        print("Длина ростверка промежуточной опоры № ", an + 1, ":", round(Lrostvprom1[an], 2), "м.")
        print("Площадь гидроизоляции ростверка промежуточной опоры № ", an + 1, ":", Srosgidroprom1[an],
              "м2")
        print("Количество свай в ширину на промежуточной опоре № ", an + 1, ":", nsvaibprom1[an], "шт.")
        print("Количество свай в длину на промежуточной опоре № ", an + 1, ":", nsvailprom1[an], "шт.")
        print("Количество свай на промежуточной опоре № ", an + 1, ":",
              nsvaibprom1[an] * nsvailprom1[an],
              "шт.")
        # print("Отметка оси проезжей части на промежуточной опоре № ", nopor[an], ":", otmpch1[an])
        # for i in range(nbalokpol):
        #     print("Отметки подферменников на промежуточной опоре № ", nopor[i + 1], ":     ", otmpodfprom[1:-1])
        print("Отметка верха ригеля на промежуточной опоре № ", an + 1, ":       ", otmrig[an] + Hrig1)
        print("Отметка низа ригеля на промежуточной опоре № ", an + 1, ":       ", otmrig[an])
        print("Отметка верха ростверка на промежуточной опоре № ", an + 1, ":   ", otmrostv1[an])
        print("Отметка низа ростверка на промежуточной опоре № ", an + 1, ":    ", otmnizrostprom1[an])
        print("Отметка низа свай на промежуточной опоре № ", an + 1, ":         ", otmsvaiprom1[an])
    print("Общее количество свай на промежуточных опорах на сооружение :",
          (nsvaibprom1[ax] * nsvailprom1[ax]) * len(nprom),
          "шт.")
