zazor = 0.05  # зазор между балками пролетных строений min=0.15 м
osopr = 0.3  # ось опирания балки до 33 м - 0.3 м, для 33 м -0.4 м
boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м
hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
nshag1 = 0
Bpodf = zazor + 2 * osopr + boporchast + 2 * bfasroch
Lpodf = Lpoproch + 2 * Lpoppodf
Vpodf1 = 0  # объем подферменной площадки одной
Vpodf = 0  # общий объем подферменных площадок на опору
Vpodf3 = 0  # промежуточный общий объем подферменников
Vpodfbaz = hpodfbaz * Bpodf * Lpodf

n = int(input("Введите кол-во пролетных строений: "))
nbalok1 = int(input("Введите количество балок в пролетном строении: "))
shagbal = float(input("Введите шаг балок: "))
nopor1 = n + 1  # количество опор на сооружение

nopor2 = 0
nopor = []
for i in range(nopor1):
    nopor2 = nopor2 + 1
    nopor.append(nopor2)  # количестов промежуточных опор
nprom = nopor[1:-1]
nust = [nopor[0], nopor[-1]]

nshag2 = []

otmrigust = []
poperuclust = []
otmpodfbazust = []

otmpodf1 = 0
Vpodf1 = 0
otmpodf = []  # список отметок подферменных площадок
Vpodf2 = []

for i in range(len(nust)):
    print("Ведите отметку верха насадки на устое № ", nust[i])
    otmrigust1 = float(input())
    otmrigust.append(otmrigust1)
    print("Введите поперечный уклон над опорой № ", nust[i], ":")
    poperuclust1 = float(input())
    poperuclust.append(poperuclust1)
    otmpodfbazust1 = otmrigust1 + 0.15  # отметка наименьшей подферменной площадки на опоре
    otmpodfbazust.append(otmpodfbazust1)

    if nbalok1 % 2 == 0:

        hprir1 = 0
        hprir = []  # список превышений на каждой подферменной площадке
        hpodf = []  # список высот подферменных площадок
        hpodf1 = 0
        for i in range((nbalok1 - 2) // 2):
            nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
            nshag2.append(nshag1)
            hprir1 = shagbal * nshag2[i] * poperuclust[i]
            hprir.append(hprir1)
            hpodf1 = hpodfbaz + hprir[i]
            hpodf.append(hpodf1)
            otmpodf1 = otmrigust[i] + hpodf[i]
            otmpodf.append(otmpodf1)
            Vpodf1 = hpodf[i] * Bpodf * Lpodf
            Vpodf2.append(Vpodf1)
            Vpodf += Vpodf1 * 2

if len(nprom) != 0:
    otmrigprom1 = 0
    poperuclprom1 = 0
    otmpodfbazprom1 = 0

    otmrigprom = []
    poperuclprom = []
    otmpodfbazprom = []
    for i in range(len(nprom)):
        print("Ведите отметку верха насадки на устое № ", nprom[i])
        otmrigprom1 = float(input())
        otmrigprom.append(otmrigprom1)
        print("Введите поперечный уклон над опорой № ", nprom[i], ":")
        poperuclprom1 = float(input())
        poperuclprom.append(poperuclprom1)
        otmpodfbazprom1 = otmrigprom1 + 0.15  # отметка наименьшей подферменной площадки на опоре
        otmpodfbazprom.append(otmpodfbazprom1)

    if nbalok1 % 2 == 0:

        hprir1 = 0
        hprir = []  # список превышений на каждой подферменной площадке
        hpodf = []  # список высот подферменных площадок
        hpodf1 = 0

        for i in range((nbalok1 - 2) // 2):

            nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
            nshag2.append(nshag1)
            hprir1 = shagbal * nshag2[i] * poperuclprom[i]
            hprir.append(hprir1)
            hpodf1 = hpodfbaz + hprir[i]
            hpodf.append(hpodf1)
            otmpodf1 = otmrigprom[i] + hpodf[i]
            otmpodf.append(otmpodf1)
            Vpodf1 = hpodf[i] * Bpodf * Lpodf
            Vpodf2.append(Vpodf1)
            Vpodf += Vpodf1 * 2

for i in range(len(nust)):
    print("Отметка верха насадки на устое № ", nust[i], ":", otmrigust[i])
    # print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodf[i], 3))
    # print("Объем подферменной площадки № ", nshag2[0], ":", round(Vpodf2[i], 3), "м3")
    for i in range((nbalok1 - 2) // 2):
        print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
        print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
    # print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
#     for i in range(len(nust)):
#
#         for i in range((nbalok1 - 2) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
#             hprir1 = shagbal * nshag2[i] * poperuclust[i]
#             hprir.append(hprir1)
#             hpodf1 = hpodfbaz + hprir[i]
#             hpodf.append(hpodf1)
#             otmpodf1 = otmrigust[i] + hpodf[i]
#             otmpodf.append(otmpodf1)
#             Vpodf1 = hpodf[i] * Bpodf * Lpodf
#             Vpodf2.append(Vpodf1)
#             Vpodf += Vpodf1 * 2
# else:
#
#     for i in range((nbalok1 - 1) // 2):
#         nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#         nshag2.append(nshag1)
#         for i in range(len(nust)):
#             hpodf1 = hpodfbaz
#             hprir1 = 0
#         hprir = []  # список превышений на каждой подферменной площадке
#         hpodf = []  # список высот подферменных площадок
#         for i in range((nbalok1 - 1) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
#             hprir1 = shagbal * nshag2[i] * poperuclust[i]
#             hprir.append(hprir1)
#             hpodf1 = hpodfbaz + hprir[i]
#             hpodf.append(hpodf1)
#             otmpodf1 = otmrigust[i] + hpodf[i]
#             otmpodf.append(otmpodf1)
#             Vpodf1 = hpodf[i] * Bpodf * Lpodf
#             Vpodf2.append(Vpodf1)
#             Vpodf3 += (Vpodf1 * 2)
#             Vpodf = Vpodf3 - Vpodf2[-1]
#
# if len(nprom)!=0:
#     otmrigprom = []
#     poperuclprom = []
#     otmpodfbazprom=[]
#     for i in range(len(nprom)):
#         print("Ведите отметку верха насадки на устое № ", nprom[i])
#         otmrigprom1 = float(input())
#         otmrigprom.append(otmrigprom1)
#         print("Введите поперечный уклон над опорой № ", nprom[i], ":")
#         poperuclprom1 = float(input())
#         poperuclprom.append(poperuclprom1)
#         otmpodfbazprom1 = otmrigprom[i] + 0.15  # отметка наименьшей подферменной площадки на опоре
#         otmpodfbazprom.append(otmpodfbazprom1)
#         if nbalok1 % 2 == 0:
#             for i in range((nbalok1 - 2) // 2):
#                 nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#                 nshag2.append(nshag1)
#             hpodf1 = hpodfbaz
#             hprir1 = 0
#             hprir = []  # список превышений на каждой подферменной площадке
#             hpodf = []  # список высот подферменных площадок
#             for i in range((nbalok1 - 2) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
#                 hprir1 = shagbal * nshag2[i] * poperuclprom[i]
#                 hprir.append(hprir1)
#                 hpodf1 = hpodfbaz + hprir[i]
#                 hpodf.append(hpodf1)
#                 otmpodf1 = otmrigprom[i] + hpodf[i]
#                 otmpodf.append(otmpodf1)
#                 Vpodf1 = hpodf[i] * Bpodf * Lpodf
#                 Vpodf2.append(Vpodf1)
#                 Vpodf += Vpodf1 * 2
#         else:
#             for i in range((nbalok1 - 1) // 2):
#                 nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#                 nshag2.append(nshag1)
#             hpodf1 = hpodfbaz
#             hprir1 = 0
#             hprir = []  # список превышений на каждой подферменной площадке
#             hpodf = []  # список высот подферменных площадок
#             for i in range((nbalok1 - 1) // 2):  # расчет высот подферменников с учетом порядкового номера каждого
#                 hprir1 = (shagbal * nshag2[i] * poperuclprom[i])
#                 hprir.append(hprir1)
#                 hpodf1 = hpodfbaz + hprir[i]
#                 hpodf.append(hpodf1)
#                 otmpodf1 = otmrigprom[i] + hpodf[i]
#                 otmpodf.append(otmpodf1)
#                 Vpodf1 = hpodf[i] * Bpodf * Lpodf
#                 Vpodf2.append(Vpodf1)
#                 Vpodf3 += (Vpodf1 * 2)
#                 Vpodf = Vpodf3 - Vpodf2[-1]
#
# for i in range(len(nust)):
#     print("Отметка насадки устоя № ", nust[i], ":", otmrigust[i])
#     print("Отметка подферменной площадки № ", nshag2[i], ":", round(otmpodfbazust[i], 3))
#     print("Объем подферменной площадки № ", nshag2[i], ":", Vpodfbaz, "м3")
# if nbalok1 % 2 == 0:
#
#
# else:
#
#         for i in range((nbalok1 - 1) // 2):
#             # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
#             print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
#             print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
#         print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
#
# for i in range(len(nprom)):
#     print("Верх ригеля на промежуточной опоре № ", nprom[i], ":", otmrigprom[i + 2])
