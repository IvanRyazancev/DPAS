n = int(input("Введите кол-во пролетных строений: "))
nbalok1 = int(input("Введите количество балок в пролетном строении: "))
shagbal = float(input("Введите шаг балок: "))
nopor1 = n + 1  # количество опор на сооружение
nopor2 = 0
nopor = []
hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
zazor = 0.05  # зазор между балками пролетных строений min=0.15 м
osopr = 0.3  # ось опирания балки до 33 м - 0.3 м, для 33 м -0.4 м
boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м
Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
Bpodfust = zazor + osopr + 0.5 * boporchast + bfasroch
Bpodfprom = zazor + 2 * osopr + boporchast + 2 * bfasroch
Lpodf = Lpoproch + 2 * Lpoppodf
Vpodf1 = 0  # объем подферменной площадки одной
Vpodf2 = 0  # объем подферменной площадки одной
Vpodfs1 = 0  # общий объем подферменных площадок на опору
Vpodfs2 = 0  # общий объем подферменных площадок на опору
Vpodf3 = 0  # промежуточный общий объем подферменников
Vpodfbazust = round(hpodfbaz * Bpodfust * Lpodf, 3)
Vpodfbazprom = round(hpodfbaz * Bpodfprom * Lpodf, 3)

for l in range(nopor1):
    nopor2 = nopor2 + 1
    nopor.append(nopor2)  # количестов промежуточных опор
nprom = nopor[1:-1]
nust = [nopor[0], nopor[-1]]

otmrigust1 = 0
poperuclust1 = 0
otmpodfbazust1 = 0
otmrigust = []
poperuclust = []
otmpodfbazust = []
for o in range(len(nust)):
    print("Введите отметку верха насадки устоя № ", nust[o])
    otmrigust1 = float(input())
    otmrigust.append(otmrigust1)
    print("Введите поперечный уклон над опорой № ", nust[o], ":")
    poperuclust1 = float(input())
    poperuclust.append(poperuclust1)
    otmpodfbazust1 = otmrigust[o] + 0.15  # отметка наименьшей подферменной площадки на опоре
    otmpodfbazust.append(otmpodfbazust1)

otmrigust_1 = otmrigust[0]
otmrigust_2 = otmrigust[-1]
poperuclust_1 = poperuclust[0]
poperuclust_2 = poperuclust[-1]

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
        hprir1 = shagbal * nshag2[u] * poperuclust_1
        hprir_1.append(hprir1)
        hprir2 = shagbal * nshag2[u] * poperuclust_2
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
        Vpodfs2 = sum(Vpodf_2)


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
        hprir1 = shagbal * nshag2[t] * poperuclust_1
        hprir_1.append(hprir1)
        hprir2 = shagbal * nshag2[t] * poperuclust_2
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

print("Отметка верха насадки на устое № ", nust[0], ":", otmrigust[0])
print("Отметка подферменной площадки № ", nshag2[0], ":", otmpodfbazust[0])
print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbazust, "м3")
if nbalok1 % 2 == 0:
    for r in range((nbalok1 - 2) // 2):
        print("Отметка подферменной площадки № ", r + 2, ":", otmpodf_1[r])
        print("Объем подферменной площадки № ", r + 2, ":", Vpodf_1[r], "м3")
    print("Суммарный объем подферменников на устое № ", nust[0], ":", round(((Vpodfs1 + Vpodfbazust) * 2), 3), "м3")
else:
    for e in range((nbalok1 - 1) // 2):
        print("Отметка подферменной площадки № ", e + 2, ":", otmpodf_1[e])
        print("Объем подферменной площадки № ", e + 2, ":", Vpodf_1[e], "м3")
    print("Суммарный объем подферменников на устое № ", nust[0], ":", Vpodfobsh1, "м3")

if len(nprom) != 0:
    hpodfbaz = 0.15  # минимальная высота подферменной площадки
    for p in range(len(nprom)):
        print("Введите отметку ригеля на опоре №: ", p + 2)
        otmrigprom = float(input())
        print("Введите поперечный уклон над опорой №: ", p + 2)
        poperuclprom = float(input())
        otmpodfbazprom = otmrigprom + hpodfbaz  # отметка минимальной подферменной площадки
        # nbalok2 = 0
        otmpodfprom1 = 0
        hpodfprom1 = 0
        Vpodfprom1 = 0
        Vpodfobshprom3 = 0
        Vpodfsprom2 = 0
        # nbalok = []
        otmpodfprom = []
        hpodfprom = []
        Vpodfprom = []
        if nbalok1 % 2 == 0:
            for k in range((nbalok1 - 2) // 2):
                # nbalok2 = nbalok2 + 1
                # nbalok.append(nbalok2)
                otmpodfprom1 = round(otmpodfbazprom + shagbal * poperuclprom * nshag2[k],
                                     3)  # вычисление отметки i-й подферменной площадки
                otmpodfprom.append(otmpodfprom1)
                hpodfprom1 = otmpodfprom[k] - otmrigprom
                hpodfprom.append(hpodfprom1)
                Vpodfprom1 = round(hpodfprom[k] * Bpodfprom * Lpodf, 3)
                Vpodfprom.append(Vpodfprom1)
                Vpodfsprom2 += Vpodfprom1
                Vpodfobshprom3 = round(((Vpodfsprom2 + Vpodfbazprom) * 2), 3)
        else:
            for m in range((nbalok1 - 1) // 2):
                # nbalok2 = nbalok2 + 1
                # nbalok.append(nbalok2)
                otmpodfprom1 = round(otmpodfbazprom + shagbal * poperuclprom * nshag2[m],
                                     3)  # вычисление отметки i-й подферменной площадки
                otmpodfprom.append(otmpodfprom1)
                hpodfprom1 = otmpodfprom[m] - otmrigprom
                hpodfprom.append(hpodfprom1)
                Vpodfprom1 = round(hpodfprom[m] * Bpodfprom * Lpodf, 3)
                Vpodfprom.append(Vpodfprom1)
                Vpodfsprom2 += Vpodfprom1
                Vpodfobshprom3 = round(((Vpodfsprom2 + Vpodfbazprom) * 2) - Vpodfprom[-1], 3)
        print("Отметка верха ригеля промежуточной опоры № ", p + 2, ":", otmrigprom)
        print("Отметка подферменной площадки № ", nshag2[0], ":", otmpodfbazprom)
        print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbazprom, "м3")
        for y in range(len(nshag2)):
            print("Отметка подферменной площадки № ", y + 2, ":", otmpodfprom[y])
            print("Объем подферменной площадки № ", y + 2, ":", Vpodfprom[y], "м3")
        if nbalok1 % 2 == 0:
            print("Суммарный объем подферменных площадок на промежуточной опоре № ", p + 2, ":",
                  round(Vpodfobshprom3, 3), "м3")
        else:
            print("Суммарный объем подферменных площадок на промежуточной опоре № ", p + 2, ":",
                  round(Vpodfobshprom3, 3), "м3")
        print("")

print("Отметка верха насадки на устое № ", nust[-1], ":", otmrigust[-1])
print("Отметка подферменной площадки № ", nshag2[0], ":", otmpodfbazust[-1])
print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbazust, "м3")
if nbalok1 % 2 == 0:
    for w in range((nbalok1 - 2) // 2):
        print("Отметка подферменной площадки № ", w + 2, ":", otmpodf_2[w])
        print("Объем подферменной площадки № ", w + 2, ":", Vpodf_2[w], "м3")
    print("Суммарный объем подферменников на устое № ", nust[-1], ":", round((Vpodfs2 + Vpodfbazust) * 2, 3), "м3")
else:
    for q in range((nbalok1 - 1) // 2):
        print("Отметка подферменной площадки № ", q + 2, ":", otmpodf_2[q])
        print("Объем подферменной площадки № ", q + 2, ":", Vpodf_2[q], "м3")
    print("Суммарный объем подферменников на устое № ", nust[-1], ":", Vpodfobsh2, "м3")
