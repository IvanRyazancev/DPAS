# zazor = 0.05  # зазор между балками пролетных строений min=0.15 м
# osopr = 0.3  # ось опирания балки до 33 м - 0.3 м, для 33 м -0.4 м
# boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
# bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
# Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
# Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м
# Vpodf3 = 0  # промежуточный общий объем подферменников
# n = int(input("Введите кол-во пролетных строений: "))
# nbalok1 = int(input("Введите количество балок в пролетном строении: "))
# shagbal = float(input("Введите шаг балок: "))
# nopor1 = n + 1  # количество опор на сооружение
# nopor2 = 0
#
# nopor = []
#
# for i in range(nopor1):
#     nopor2 = nopor2 + 1
#     nopor.append(nopor2)  # количестов промежуточных опор
# nprom = nopor[1:-1]
# nust = [nopor[0], nopor[-1]]
#
#
# Bpodf = zazor + 2 * osopr + boporchast + 2 * bfasroch
# Lpodf = Lpoproch + 2 * Lpoppodf
# hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
# Vpodfbaz = hpodfbaz * Bpodf * Lpodf
# otmrigust = []
# poperuclust = []
# otmpodfbaz = []
#
# for i in range(len(nust)):
#     print("Введите отметку верха насадки устоя № ", nopor[i])
#     otmrig1 = float(input())
#     otmrigust.append(otmrig1)
#     print("Введите поперечный уклон над опорой № ", nust[i], ":")
#     poperuclust1 = float(input())
#     poperuclust.append(poperuclust1)
#     otmpodfbaz1 = otmrigust[i] + 0.15  # отметка наименьшей подферменной площадки на опоре
#     otmpodfbaz.append(otmpodfbaz1)
#
#     Vpodf1 = 0  # объем подферменной площадки одной
#     Vpodf = 0  # общий объем подферменных площадок на опору
#
#     nshag2 = []
#     otmpodf = []  # список отметок подферменных площадок
#     Vpodf2 = []
#
#
#
# # for i in range(len(nust)):
#
# # print("Введите поперечный уклон над опорой № ", nopor[i], ":")
# # poperucl1 = float(input())
# # poperucl.append(poperucl1)
#
# Bpodf = zazor + 2 * osopr + boporchast + 2 * bfasroch
# Lpodf = Lpoproch + 2 * Lpoppodf
# hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
# hpodf1 = hpodfbaz
# nshag1 = 0
# nshag2 = []
# otmpodf = []
# Vpodf2 = []
# if nbalok1 % 2 == 0:
#     otmrigust2 = []
#     poperuclust2 = []
#     for i in range((nbalok1 - 2) // 2):
#         poperuclust2.append(poperuclust)
#         otmrigust2.append(otmrigust)
#     for i in range((nbalok1 - 2) // 2):
#         nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#         nshag2.append(nshag1)
#
#     Vpodf = 0
#     hprir = []  # список превышений на каждой подферменной площадке
#     hpodf = []  # список высот подферменных площадок
#     # hprir1 = shagbal * nshag2 * poperuclust2
#     for i in range(len(nshag2)):  # расчет высот подферменников с учетом порядкового номера каждого
#         hprir1 = shagbal * nshag2[i] * poperuclust2[i]
#         hprir.append(hprir1)
#         hpodf1 = hpodfbaz + hprir[i]
#         hpodf.append(hpodf1)
#         otmpodf1 = otmrigust2[i] + hpodf[i]
#         otmpodf.append(otmpodf1)
#         Vpodf1 = hpodf[i] * Bpodf * Lpodf
#         Vpodf2.append(Vpodf1)
#         Vpodf += Vpodf1 * 2
# else:
#     otmrigust2 = []
#     poperuclust2 = []
#     for i in range((nbalok1 - 2) // 2):
#         poperuclust2.append(poperuclust)
#         otmrigust2.append(otmrigust)
#     for i in range((nbalok1 - 1) // 2):
#         nshag1 = float(nshag1 + 1)  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#         nshag2.append(nshag1)
#     hpodf1 = hpodfbaz
#     hprir1 = 0
#     hprir = []  # список превышений на каждой подферменной площадке
#     hpodf = []  # список высот подферменных площадок
#     for i in range(len(nshag2)):  # расчет высот подферменников с учетом порядкового номера каждого
#         hprir1 = shagbal * nshag2[i] * poperuclust2[i]
#         hprir.append(hprir1)
#         hpodf1 = hpodfbaz + hprir[i]
#         hpodf.append(hpodf1)
#         otmpodf1 = otmrigust2[i] + hpodf[i]
#         otmpodf.append(otmpodf1)
#         Vpodf1 = hpodf[i] * Bpodf * Lpodf
#         Vpodf2.append(Vpodf1)
#         Vpodf3 += (Vpodf1 * 2)
#         Vpodf = Vpodf3 - Vpodf2[-1]
#
#     # print("Высота подферменной площадки № ", nshag2[0], ":", hpodfbaz, "м.")
# for i in range(len(nust)):
#     print("Отметка насадки устоя № ", nust[i], ":", otmrigust[i])
#     print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz[i], 3))
# print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbaz, "м3")
# if nbalok1 % 2 == 0:
#     for i in range((nbalok1 - 2) // 2):
#         # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
#         print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
#         print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
#     print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
# else:
#     for i in range((nbalok1 - 1) // 2):
#         # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
#         print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
#         print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
#     print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
#
# print("Отметка насадки устоя № ", nopor[-1], ":", otmrigust[-1])
# print("Отметка подферменной площадки № ", nshag2[0], ":", round(otmpodfbaz[-1], 3))
# print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbaz, "м3")
# if nbalok1 % 2 == 0:
#     for i in range((nbalok1 - 2) // 2):
#         # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
#         print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
#         print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
#     print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
# else:
#     for i in range((nbalok1 - 1) // 2):
#         # print("Высота подферменной площадки № ", i + 2, ":", round(hpodf[i], 4), "м.")
#         print("Отметка подферменной площадки № ", i + 2, ":", round(otmpodf[i], 3))
#         print("Объем подферменной площадки № ", i + 2, ":", round(Vpodf2[i], 3), "м3")
#     print("Суммарный объем подферменных площадок на опору :", round(Vpodf + 2 * Vpodfbaz, 3), "м3")
nprom1 = int(input("Введите количество промежуточных опор: "))
nbalok1 = int(input("Введите количество балок в пролетном строении: "))
shagbal = float(input("Введите шаг балок: "))
nprom2 = 0
nprom = []
for i in range(nprom1):
    nprom2 = nprom2 + 1
    nprom.append(nprom2)

if nbalok1 % 2 == 0:
    nbalok2 = 0
    nbalok = []
    for i in range((nbalok1 - 2) // 2):
        nbalok2 = nbalok2 + 1
        nbalok.append(nbalok2)
else:
    nbalok2 = 0
    nbalok = []
    for i in range((nbalok1 - 1) // 2):
        nbalok2 = nbalok2 + 1
        nbalok.append(nbalok2)
a1 = nbalok
a = []
for i in range(len(nprom)):
    a.append(a1)
print(a)

hpodfbaz = 0.15
otmpodfbaz = otmrig + hpodfbaz
otmpodf = otmpodfbaz + shagbal * poperucl * nbalok[i]

# otmpodf1 = 0
# poperucl1 = 0
# otmpodfbaz1 = 0
# otmrigprom = []
# otmpodfbaz = []
# poperucl = []
# otmpodf = []
# for i in range(len(nprom)):
#     print("Введите отметку верха ригеля на опоре № ", i + 2, ": ")
#     otmrigprom1 = float(input())
#     otmrigprom.append(otmrigprom1)
#     otmpodfbaz1 = otmrigprom[i] + 0.15
#     otmpodfbaz.append(otmpodfbaz1)
#     print("Введите поперечный уклон опоре № ", i + 2, ": ")
#     poperucl1 = float(input())
#     poperucl.append(poperucl1)
#     # for i in range(len(nbalok)):
#     otmpodf1 = otmrigprom[i] + 0.15 + (shagbal * nbalok[i] * poperucl[i])
#     otmpodf.append(otmpodf1)
# for i in range(len(nprom)):
#     print("Поперечный уклон над опорой № ", i + 2, ": ", poperucl[i])
#     print("Отметка верха ригеля на опоре №", i + 2, ": ", otmrigprom[i])
#     print("Отметка подферменной площадки №", nbalok[0], "на опоре № ", i + 2, ": ", otmpodfbaz[i])
#     for i in range((nbalok1-2)//2):
#         print("Отметка подферменной площадки №", nbalok[i], "на опоре № ", i , ": ", otmpodf[i])
#         # for i in range(len(nprom)):
#         #     print("Отметка подферменной площадки №", nbalok[i + 1], "на опоре № ", nprom[1:], ": ", otmpodf[i])
