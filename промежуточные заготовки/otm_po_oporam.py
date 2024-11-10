import openpyxl
import math

gabarit = int(input("Введите габарит проезжей части: "))
while gabarit <= 0:
    gabarit = int(input("Введите габарит проезжей части: "))
n = int(input("Введите количество пролетных строений: "))
nopor = n + 1
nust = 2
nprom = nopor - nust
zazor = 0.05
nzazor = nprom
Lpr = 0
zaglublrostv = float(input("Введите величину заглубления ростверка в грунт: "))
hroch = 0.052  # высота опорной части
hpodf = 0.15

Shirbalki = 1.4
Hbalki1 = int(input("Выберите высоту балки 0.93 м - 1; 1.23 м - 2; 1.53 м - 3: "))
Hpliti = 0.18
Bplomonol = 0.7


hdo = float(input("Введите толщину а/б покрытия проезжей части: "))
hzashsl = float(input("Введите толщину защитного слоя проезжей части: "))
hgidroiz = float(input("Введите толщину гидроизоляции проезжей части: "))
hvirsl = float(input("Введите толщину выравнивающего слоя проезжей части: "))

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
Lrigust = Spoln

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

dlinaproleta1 = []
otmpch_all = []
otmzeli_all = []

for i in range(n):
    print("Введите длину пролетного строения №", i + 1, ":")
    dlinaproleta = float(input())
    if dlinaproleta == "": break
    dlinaproleta1.append(dlinaproleta)
    Lpr += dlinaproleta

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

    print("Введите отметку оси проезжей части над опорой №", i + 1, ":")
    otmpch = float(input())
    if otmpch == "": break
    otmpch_all.append(otmpch)

    print("Введите отметку земли у опоры №", i + 1, ":")
    otmzeli = float(input())
    if otmzeli == "": break
    otmzeli_all.append(otmzeli)

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

    if dlinaproleta < 21:
        Hrig = 0.8
    elif dlinaproleta > 21 and dlinaproleta < 27:
        Hrig = 1.0
    else:
        Hrig = 1.2
    Vrigust = round(
        Hrig * Lrigust * Bfasrigust + 0.5 * (((Bfasrigust - bshkaf) * 0.1) * (Bfasrigust - bshkaf)) * Lrigust, 2)

    Lpliti = dlinaproleta - 2 * 0.7


    poperucl = float(input("Введите поперечный уклон проезжей части: "))

    Hstr = round((poperucl * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalki), 2)

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

dlinaproleta1.append(dlinaproleta)
otmpch_all.append(otmpch)
otmzeli_all.append(otmzeli)


print("Количество пролетных строений: ", n)
print("Количество опор: ", nopor)
print("Длина пролетных строений: ", Lpr + nzazor * zazor)
print("Длина зазоров", nzazor * zazor)
for i in range(n):
    print("Отметка оси проезжей части над опорой №", i + 1, ":", otmpch)
    print("Отметка земли у опоры №", i + 1, ":", otmzeli)
