import openpyxl
import math
import builtins

print(" ")
print("                      Программа для определения параметров искусственного сооружения (ОПИС)    ")
print("                         Determining the Parameters of an Artificial Structure (DPAS)          ")
print(" ")
print("Данная программа предназначена для определения основных параметров искусственных сооружений дорожного ")
print("                           хозяйства, имея минимальное количество исходных данных")
print(" ")

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

dlinaproleta1 = []

for i in range(n):
    print("Введите длину пролетного строения №", i + 1, ":")
    dlinaproleta = float(input())
    if dlinaproleta == "": break
    dlinaproleta1.append(dlinaproleta)
    Lpr += dlinaproleta

for i in range(n):
    print("Длина пролетного строения №", i + 1, ":", dlinaproleta1[i], "м.")

shema = ' + '.join([str(int(i)) for i in dlinaproleta1])

# Выбор типа балок
print("Выбор марки балок: ")
print("Выберите из списка балки пролетных строений")

Shirbalki = 1.4
Hbalki1 = 0
Hbalki2 = []
for i in range(n):
    print("Выберите высоту балки пролетного строения № ", i + 1, "0.93 м - 1; 1.23 м - 2; 1.53 м - 3: ")
    Hbalki1 = int(input())
    Hbalki2.append(Hbalki1)
Hpliti = 0.18
Bplomonol = 0.7
Lpliti = dlinaproleta - 2 * 0.7

Hbalki = 0
osopor = 0
Vbalki = 0
mbalki = 0
harbalki = 0
matbalki = 0
Vbal = 0
Hbalki3 = []
osopor1 = []
Vbalki1 = []
mbalki1 = []
harbalki1 = []
matbalki1 = []
for i in range(n):
    if dlinaproleta1[i] == 12 and Hbalki2[i] == 1:
        Hbalki = 0.93
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 6.59
        Vbalki1.append(Vbalki)
        mbalki = 16.5
        mbalki1.append(mbalki)
        harbalki = 'Б 1200.140.93'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 15 and Hbalki2[i] == 1:
        Hbalki = 0.93
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 8.40
        Vbalki1.append(Vbalki)
        mbalki = 21.0
        mbalki1.append(mbalki)
        harbalki = 'Б 1500.140.93'
        harbalki1.append(harbalki)
        matbalki = 'B40 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 11.9 and Hbalki2[i] == 2:
        Hbalki = 1.23
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 7.54
        Vbalki1.append(Vbalki)
        mbalki = 18.9
        mbalki1.append(mbalki)
        harbalki = 'Б 1190.140.123'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 15 and Hbalki2[i] == 2:
        Hbalki = 1.23
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 9.46
        Vbalki1.append(Vbalki)
        mbalki = 23.7
        mbalki1.append(mbalki)
        harbalki = 'Б 1500.140.123'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 18 and Hbalki2[i] == 2:
        Hbalki = 1.23
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 11.63
        Vbalki1.append(Vbalki)
        mbalki = 29.1
        mbalki1.append(mbalki)
        harbalki = 'Б 1800.140.123'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 21 and Hbalki2[i] == 2:
        Hbalki = 1.23
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 13.01
        Vbalki1.append(Vbalki)
        mbalki = 32.6
        mbalki1.append(mbalki)
        harbalki = 'Б 2100.140.123'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 24 and Hbalki2[i] == 2:
        Hbalki = 1.23
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 15.18
        Vbalki1.append(Vbalki)
        mbalki = 38.0
        mbalki1.append(mbalki)
        harbalki = 'Б 2400.140.123'
        harbalki1.append(harbalki)
        matbalki = 'B40 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 28 and Hbalki2[i] == 2:
        Hbalki = 1.23
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 18.07
        Vbalki1.append(Vbalki)
        mbalki = 45.2
        mbalki1.append(mbalki)
        harbalki = 'Б 2800.140.123'
        harbalki1.append(harbalki)
        matbalki = 'B40 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 18 and Hbalki2[i] == 3:
        Hbalki = 1.53
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 12.42
        Vbalki1.append(Vbalki)
        mbalki = 31.1
        mbalki1.append(mbalki)
        harbalki = 'Б 1800.140.153'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 28 and Hbalki2[i] == 3:
        Hbalki = 1.53
        Hbalki3.append(Hbalki)
        osopor = 0.3
        osopor1.append(osopor)
        Vbalki = 19.36
        Vbalki1.append(Vbalki)
        mbalki = 48.4
        mbalki1.append(mbalki)
        harbalki = 'Б 2800.140.153'
        harbalki1.append(harbalki)
        matbalki = 'B35 F300 W6'
        matbalki1.append(matbalki)
    elif dlinaproleta1[i] == 33 and Hbalki2[i] == 3:
        Hbalki = 1.53
        Hbalki3.append(Hbalki)
        osopor = 0.4
        osopor1.append(osopor)
        Vbalki = 24.35
        Vbalki1.append(Vbalki)
        mbalki = 60.9
        mbalki1.append(mbalki)
        harbalki = 'Б 3300.140.153'
        harbalki1.append(harbalki)
        matbalki = 'B45 F300 W6'
        matbalki1.append(matbalki)
    Vbal += Vbalki
Hbalki3.append(Hbalki)
osopor1.append(osopor)
Vbalki1.append(Vbalki)
mbalki1.append(mbalki)
harbalki1.append(harbalki)
matbalki1.append(matbalki)

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
elif 21 < dlinaproleta < 27:
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
    Lrigprom = Lrig1 + boporch + 2 * (bpodferm + brigbok)  # ширина ригеля в поперечнике
    Bfasrigprom = round(zazor + bfasroch + 2 * (bfaspodf + bfasrig + osopor), 2)  # ширина ригеля по фасаду
    Vrigprom = round(Hrig * Lrigprom * Bfasrigprom - (Bfasrigprom * (2 * (0.5 * 0.4 * 1.2))), 2)  # объем ригеля

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

otmpch = 0
poperucl = 0
otmzeli = 0

otmpch1 = []
poperucl1 = []
otmzeli1 = []

for i in range(nopor):
    print("Введите отметку проезжей части над опорой № ", i + 1, ":")
    otmpch = float(input())
    if otmpch == "": break
    otmpch1.append(otmpch)

    print("Введите поперечный уклон проезжей части над опорой № ", i + 1)
    poperucl = float(input())
    if poperucl == "": break
    poperucl1.append(poperucl)

    print("Введите отметку земли у опоры № ", i + 1)
    otmzeli = float(input())
    if otmzeli == "": break
    otmzeli1.append(otmzeli)

otmpch1.append(otmpch)
poperucl1.append(poperucl)
otmzeli1.append(otmzeli)

hdo = float(input("Введите толщину а/б покрытия проезжей части: "))
hzashsl = float(input("Введите толщину защитного слоя проезжей части: "))
hgidroiz = float(input("Введите толщину гидроизоляции проезжей части: "))
hvirsl = float(input("Введите толщину выравнивающего слоя проезжей части: "))
zaglublrostv = float(input("Введите величину заглубления ростверка в грунт: "))
hpodf = 0.15  # минимальная высота подферменной площадки

Hstr = 0
Hstr1 = []
for i in range(nopor):
    Hstr = round((poperucl1[i] * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalki3[i]), 2)
    Hstr1.append(Hstr)

otmrig = 0
otmrostv = 0
otmrig1 = []
otmrostv1 = []

for i in range(nopor):
    otmrig = round((otmpch1[i] - Hstr1[i] - hroch - hpodf - Hrig), 3)
    otmrig1.append(otmrig)

    otmrostv = otmzeli1[i] - zaglublrostv
    otmrostv1.append(otmrostv)

otmrig1.append(otmrig)
otmrostv1.append(otmrostv)

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

for i in range(nopor):
    Lstoek = round((otmrig1[i] - otmrostv1[i]), 2)
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

Lstoek1.append(Lstoek)
Dstoiki1.append(Dstoiki)
Sstoek2.append(Sstoek1)
Sstgidro1.append(Sstgidro)

#  Блок определения параметров ростверка

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
for i in range(nopor):
    Vstoek1 = Lstoek1[i] * Sstoek1 * nstoek
    Vstoek2.append(Vstoek1)
    Vstoek += round(Vstoek1, 2)
    Lrostvust = (shagstoekust * (nstoek - 1)) + Dstoiki1[i] + 2 * 1.2  # расчет длины ростверка устоев
    Lrostvust1.append(Lrostvust)
    Brostv = round((Dstoiki1[i] + 2 * 1.15), 2)  # расчет ширины ростверка по фасаду
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
    Vrostvust = round((Lrostvust1[i] + Brostv1[i] + Hrostv1[i]), 2)  # расчет объема ростверка
    Vrostvust1.append(Vrostvust)
    Srosgidroust = round((2 * (Brostv1[i] * Hrostv1[i]) + 2 * (Lrostvust1[i] * Hrostv1[i]) + (
            Brostv1[i] * Lrostvust1[i] - Sstoek2[i] * nstoek)),
                         2)
    Srosgidroust1.append(Srosgidroust)
Hrostv1.append(Hrostv)
Vrostvust1.append(Vrostvust)
Lrostvust1.append(Lrostvust)
Srosgidroust1.append(Srosgidroust)
if nprom != 0:
    Lrostvprom = 0
    Vrostvprom = 0
    Srosgidroprom = 0
    Lrostvprom1 = []
    Vrostvprom1 = []
    Srosgidroprom1 = []
    for i in range(nopor - 1):
        Lrostvprom = (shagstoekprom * (nstoek - 1)) + Dstoiki + 2 * 1.2  # расчет длины ростверка промежуточных опор
        Lrostvprom1.append(Lrostvprom)
        Vrostvprom = round((Lrostvprom + Brostv + Hrostv), 2)  # расчет объема ростверка
        Vrostvprom1.append(Vrostvprom)
        Srosgidroprom = round(
            (2 * (Brostv1[i] * Hrostv1[i]) + 2 * (Lrostvprom1[i] * Hrostv1[i]) + (
                    Brostv1[i] * Lrostvprom1[i] - Sstoek1 * nstoek)), 2)
        Srosgidroprom1.append(Srosgidroprom)
    Lrostvprom1.append(Lrostvprom)
    Vrostvprom1.append(Vrostvprom)
    Srosgidroprom1.append(Srosgidroprom)
Vstoek2.append(Vstoek1)
Brostv1.append(Brostv)
Vrostvust1.append(Vrostvust)
Srosgidroust1.append(Srosgidroust)

#  блок расчета количества свай

bsvai = float(input("Введите размер стороны сваи: "))  # запрос размера стороны сваи
Lsvai = int(input("Введите длину сваи: "))  # запрос длины сваи
Ssvai = round((bsvai ** 2), 2)  # расчет площади поперечного сечения сваи
Vsvai = Ssvai * Lsvai  # расчет объема одной сваи
shagsvai = 1.2  # шаг сваи

nsvaibust = 0
nsvailust = 0
nsvaibust1 = []
nsvailust1 = []

for i in range(nust):
    nsvaibust = round((Brostv - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай по фасаду
    nsvaibust1.append(nsvaibust)
    nsvailust = round((Lrostvust - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай вдоль ростверка
    nsvailust1.append(nsvailust)
nsvaibust1.append(nsvaibust)
nsvailust1.append(nsvailust)

if nprom != 0:
    nsvaibprom = 0
    nsvailprom = 0
    nsvaibprom1 = []
    nsvailprom1 = []
    for i in range(nprom):
        nsvaibprom = round((Brostv - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай по фасаду
        nsvaibprom1.append(nsvaibprom)
        nsvailprom = round((Lrostvprom - 2 * 0.25 - bsvai) / shagsvai) + 1  # кол-во свай вдоль ростверка
        nsvailprom1.append(nsvailprom)
    nsvaibprom1.append(nsvaibprom)
    nsvailprom1.append(nsvailprom)

#  Расчет отметок низа свай и низа ростверков

otmnizrostust = 0
otmsvaiust = 0
otmnizrostust1 = []
otmsvaiust1 = []
for i in range(nust):
    otmnizrostust = round((otmrostv1[i] - Hrostv), 3)  # расчет отметки низа ростверка
    otmnizrostust1.append(otmnizrostust)
    otmsvaiust = round((otmnizrostust1[i] - Lsvai), 3)  # расчет отметки низа свай
    otmsvaiust1.append(otmsvaiust)
otmnizrostust1.append(otmnizrostust)
otmsvaiust1.append(otmsvaiust)

if nprom != 0:
    otmnizrostprom = 0
    otmsvaiprom = 0
    otmnizrostprom1 = []
    otmsvaiprom1 = []
    for i in range(nprom):
        otmnizrostprom = round((otmrostv1[i] - Hrostv), 3)  # расчет отметки низа ростверка
        otmnizrostprom1.append(otmnizrostprom)
        otmsvaiprom = round((otmnizrostprom1[i] - Lsvai), 3)  # расчет отметки низа свай
        otmsvaiprom1.append(otmsvaiprom)
    otmnizrostprom1.append(otmnizrostprom)
    otmsvaiprom1.append(otmsvaiprom)

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
for i in range(n):
    print("Объем балок пролетного строения № ", i + 1, ":", round(Vbalki1[i] * nbalok, 2), "м3")
    print("Общая масса балок пролетного строения: ", round((mbalki1[i] * nbalok), 2), "т.")
    print("Марка балок пролетного строения: ", harbalki1[i])
    print("Характеристика материала балок пролетного строения: ", matbalki1[i])
    print("Строительная высота пролетного строения № ", i + 1, ":", Hstr1[i])
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

print("Количество опор на сооружение: ", nopor, "шт.")
print("Количество устоев: ", nust, "шт.")
print("Количество промежуточных опор: ", nprom, "шт.")
print(" ")
print("-------------------=== Характеристики устоев ===-------------------------")
print(" ")

print("Ширина насадки устоя в поперечнике: ", round(Lrigust, 2), "м.")
print("Ширина насадки устоя по фасаду: ", Bfasrigust, "м.")
print("Высота ригеля: ", Hrig, "м.")
print("Объем насадок устоев: ", round(Vrigust * nust, 2), "м3")
#  Блок вывода промежуточных результатов расчета стоек опор
print("Количество стоек опор: ", nstoek, "шт.")

if nprom != 0:
    print("Шаг стоек промежуточной опоры: ", shagstoekprom, "м.")

print("Шаг стоек устоев: ", shagstoekust, "м.")
print(" ")
print("------------------------------------------------------------------------")
print(" ")

if nprom != 0:
    print(" ")
    print("-------------------=== Характеристики промежуточных опор ===-------------------------")
    print(" ")
    print("Количество промежуточных опор: ", nprom, "шт.")
    print("Ширина ригеля промежуточной опоры № ", i + 1, "в поперечнике:", round(Lrigprom, 2), "м.")
    print("Ширина ригеля промежуточной опоры по фасаду: ", Bfasrigprom, "м.")
    print("Объем ригелей промежуточных опор: ", round(Vrigprom * nprom, 2), "м3")
    print("Количество опорных частей на промежуточные опоры: ", (nrochprom * nprom), "шт.")

print(" ")
print("---------------------------------------------------------")
print(" ")
print("Суммарный объем бетона стоек на сооружение: ", round(Vstoek, 2), "м3")

for i in range(nust):
    print("Длина ростверка устоя № ", i + 1, ":", round(Lrostvust1[i], 2), "м.")
    print("Площадь гидроизоляции ростверка устоя № ", i + 1, ":", Srosgidroust1[i], "м2")
    print("Количество свай в ширину на устое № ", i + 1, ":", nsvaibust1[i], "шт.")
    print("Количество свай в длину на устое № ", i + 1, ":", nsvailust1[i], "шт.")
    print("Количество свай на устое № ", i + 1, ":", nsvaibust1[i] * nsvailust1[i], "шт.")
    print("Отметка оси проезжей части на устое № ", i + 1, ":", otmpch1[i])
    print("Отметка низа насадки на устое № ", i + 1, ":      ", otmrig1[i])
    print("Отметка верха ростверка на устое № ", i + 1, ":   ", otmrostv1[i])
    print("Отметка низа ростверка на устое № ", i + 1, ":    ", otmnizrostust1[i])
    print("Отметка низа свай на устое № ", i + 1, ":         ", otmsvaiust1[i])

# print("Количество свай на промежуточных опорах на сооружение", i + 1, ":", sum(nsvaibprom1[i]*nsvailprom1[i])*nprom, "шт.")
print("Общее количество свай на устях на сооружение :",
      nsvaibust1[1] * nsvailust1[1] + nsvaibust1[2] * nsvailust1[2], "шт.")
print("Количество опорных частей на сооружение: ", (nrochust * nust) + (nrochprom * nprom), "шт.")

if nprom != 0:
    for i in range(nprom):
        print("Длина ростверка промежуточной опоры № ", i + 1, ":", round(Lrostvprom1[i], 2), "м.")
        print("Площадь гидроизоляции ростверка промежуточной опоры № ", i + 1, ":", Srosgidroprom1[i], "м2")
        print("Количество свай в ширину на промежуточной опоре № ", i + 1, ":", nsvaibprom1[i], "шт.")
        print("Количество свай в длину на промежуточной опоре № ", i + 1, ":", nsvailprom1[i], "шт.")
        print("Количество свай на промежуточной опоре № ", i + 1, ":", nsvaibprom1[i] * nsvailprom1[i], "шт.")
        print("Отметка оси проезжей части на промежуточной опоре № ", i + 1, ":", otmpch1[i])
        print("Отметка низа ригеля на промежуточной опоре № ", i + 1, ":       ", otmrig1[i])
        print("Отметка верха ростверка на промежуточной опоре № ", i + 1, ":   ", otmrostv1[i])
        print("Отметка низа ростверка на промежуточной опоре № ", i + 1, ":    ", otmnizrostprom1[i])
        print("Отметка низа свай на промежуточной опоре № ", i + 1, ":         ", otmsvaiprom1[i])
    print("Общее количество свай на промежуточных опорах на сооружение :", (nsvaibprom1[i] * nsvailprom1[i]) * nprom,
          "шт.")
