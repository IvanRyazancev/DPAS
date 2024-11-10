# n = int(input("Введите кол-во опор "))
# a = 0
# b = 0
# a1 = []
# for i in range(n):
#     a = a + 1
#     # print(a)
#     a1.append(a)
#     # b = a1[i] + 1
#     print(a1[i])


# n = int(input("Введите кол-во пролетных строений: "))
# nbalok1 = int(input("Введите количество балок в пролетном строении: "))
# shagbal = float(input("Введите шаг балок: "))
# nopor1 = n + 1  # количество опор на сооружение
# nopor2 = 0
# nopor = []
# hpodfbaz = 0.15  # размер наименьшей подферменной площадки на опоре
# zazor = 0.05  # зазор между балками пролетных строений min=0.15 м
# osopr = 0.3  # ось опирания балки до 33 м - 0.3 м, для 33 м -0.4 м
# boporchast = 0.25  # ширина опорной части по фасаду, в данном случае 0.25 м
# bfasroch = 0.15  # расстояние от лицевой грани РОЧ до лицевой части подферменника min=0.15 м
# Lpoppodf = 0.15  # Расстояние от боковых граней РОЧ до боковых граней подферменника min=0.15 м
# Lpoproch = 0.4  # Длина РОЧ в поперечнике, в данном случае 0.4 м
# Bpodfust = zazor + osopr + 0.5 * boporchast + bfasroch
# Bpodfprom = zazor + 2 * osopr + boporchast + 2 * bfasroch
# Lpodf = Lpoproch + 2 * Lpoppodf
# Vpodf1 = 0  # объем подферменной площадки одной
# Vpodf2 = 0  # объем подферменной площадки одной
# Vpodfs1 = 0  # общий объем подферменных площадок на опору
# Vpodfs2 = 0  # общий объем подферменных площадок на опору
# Vpodf3 = 0  # промежуточный общий объем подферменников
# Vpodfbazust = round(hpodfbaz * Bpodfust * Lpodf, 3)
# Vpodfbazprom = round(hpodfbaz * Bpodfprom * Lpodf, 3)
#
# for l in range(nopor1):
#     nopor2 = nopor2 + 1
#     nopor.append(nopor2)  # количестов промежуточных опор
# nprom = nopor[1:-1]
# nust = [nopor[0], nopor[-1]]
#
# otmrigust1 = 0
# poperuclust1 = 0
# otmpodfbazust1 = 0
# otmrigust = []
# poperuclust = []
# otmpodfbazust = []
# for o in range(len(nust)):
#     print("Введите отметку верха насадки устоя № ", nust[o])
#     otmrigust1 = float(input())
#     otmrigust.append(otmrigust1)
#     print("Введите поперечный уклон над опорой № ", nust[o], ":")
#     poperuclust1 = float(input())
#     poperuclust.append(poperuclust1)
#     otmpodfbazust1 = otmrigust[o] + 0.15  # отметка наименьшей подферменной площадки на опоре
#     otmpodfbazust.append(otmpodfbazust1)
#
# otmrigust_1 = otmrigust[0]
# otmrigust_2 = otmrigust[-1]
# poperuclust_1 = poperuclust[0]
# poperuclust_2 = poperuclust[-1]
#
# if nbalok1 % 2 == 0:
#     nshag1 = 0
#     hprir1 = 0
#     hprir2 = 0
#     hpodf1 = 0
#     hpodf2 = 0
#     otmpodf1 = 0
#     otmpodf2 = 0
#     Vpodf1 = 0
#     Vpodf2 = 0
#     Vpodfobsh1 = 0
#     Vpodfobsh2 = 0
#     hprir_1 = []  # список превышений на каждой подферменной площадке
#     hprir_2 = []
#     hpodf_1 = []  # список высот подферменных площадок
#     hpodf_2 = []  # список высот подферменных площадок
#     otmpodf_1 = []  # список отметок подферменных площадок на устое №1
#     otmpodf_2 = []  # список отметок подферменных площадок на устое №2
#     Vpodf_1 = []
#     Vpodf_2 = []
#     nshag2 = []
#     for u in range((nbalok1 - 2) // 2):
#         nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#         nshag2.append(nshag1)
#         hprir1 = shagbal * nshag2[u] * poperuclust_1
#         hprir_1.append(hprir1)
#         hprir2 = shagbal * nshag2[u] * poperuclust_2
#         hprir_2.append(hprir2)
#         hpodf1 = hpodfbaz + hprir_1[u]
#         hpodf_1.append(hpodf1)
#         hpodf2 = hpodfbaz + hprir_2[u]
#         hpodf_2.append(hpodf2)
#         otmpodf1 = otmrigust_1 + hpodf_1[u]
#         otmpodf_1.append(otmpodf1)
#         otmpodf2 = otmrigust_2 + hpodf_2[u]
#         otmpodf_2.append(otmpodf2)
#         Vpodf1 = round(hpodf_1[u] * Bpodfust * Lpodf, 3)
#         Vpodf_1.append(Vpodf1)
#         Vpodf2 = round(hpodf_2[u] * Bpodfust * Lpodf, 3)
#         Vpodf_2.append(Vpodf2)
#         Vpodfs1 = sum(Vpodf_1)
#         Vpodfs2 = sum(Vpodf_2)
#
#
# else:
#     nshag1 = 0
#     hprir1 = 0
#     hprir2 = 0
#     hpodf1 = 0
#     hpodf2 = 0
#     otmpodf1 = 0
#     otmpodf2 = 0
#     Vpodf1 = 0
#     Vpodf2 = 0
#     Vpodfobsh1 = 0
#     Vpodfobsh2 = 0
#     hprir_1 = []  # список превышений на каждой подферменной площадке
#     hprir_2 = []
#     hpodf_1 = []  # список высот подферменных площадок
#     hpodf_2 = []  # список высот подферменных площадок
#     otmpodf_1 = []  # список отметок подферменных площадок на устое №1
#     otmpodf_2 = []  # список отметок подферменных площадок на устое №2
#     Vpodf_1 = []
#     Vpodf_2 = []
#     nshag2 = []
#     for t in range((nbalok1 - 1) // 2):
#         nshag1 = nshag1 + 1  # определение кол - ва шагов для расчета приращения, в случае двухскатного симметричного поперечника
#         nshag2.append(nshag1)
#         hprir1 = shagbal * nshag2[t] * poperuclust_1
#         hprir_1.append(hprir1)
#         hprir2 = shagbal * nshag2[t] * poperuclust_2
#         hprir_2.append(hprir2)
#         hpodf1 = hpodfbaz + hprir_1[t]
#         hpodf_1.append(hpodf1)
#         hpodf2 = hpodfbaz + hprir_2[t]
#         hpodf_2.append(hpodf2)
#         otmpodf1 = otmrigust_1 + hpodf_1[t]
#         otmpodf_1.append(otmpodf1)
#         otmpodf2 = otmrigust_2 + hpodf_2[t]
#         otmpodf_2.append(otmpodf2)
#         Vpodf1 = round(hpodf_1[t] * Bpodfust * Lpodf, 3)
#         Vpodf_1.append(Vpodf1)
#         Vpodf2 = round(hpodf_2[t] * Bpodfust * Lpodf, 3)
#         Vpodf_2.append(Vpodf2)
#         Vpodfs1 += Vpodf1
#         Vpodfobsh1 = round(((Vpodfs1 + Vpodfbazust) * 2) - Vpodf_1[-1], 3)
#         Vpodfs2 += Vpodf2
#         Vpodfobsh2 = round(((Vpodfs2 + Vpodfbazust) * 2) - Vpodf_2[-1], 3)
#
# print("Отметка верха насадки на устое № ", nust[0], ":", otmrigust[0])
# print("Отметка подферменной площадки № ", nshag2[0], ":", otmpodfbazust[0])
# print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbazust, "м3")
# if nbalok1 % 2 == 0:
#     for r in range((nbalok1 - 2) // 2):
#         print("Отметка подферменной площадки № ", r + 2, ":", otmpodf_1[r])
#         print("Объем подферменной площадки № ", r + 2, ":", Vpodf_1[r], "м3")
#     print("Суммарный объем подферменников на устое № ", nust[0], ":", round(((Vpodfs1 + Vpodfbazust) * 2), 3), "м3")
# else:
#     for e in range((nbalok1 - 1) // 2):
#         print("Отметка подферменной площадки № ", e + 2, ":", otmpodf_1[e])
#         print("Объем подферменной площадки № ", e + 2, ":", Vpodf_1[e], "м3")
#     print("Суммарный объем подферменников на устое № ", nust[0], ":", Vpodfobsh1, "м3")
#
#     if len(nprom) != 0:
#         hpodfbaz = 0.15  # минимальная высота подферменной площадки
#         for p in range(len(nprom)):
#             print("Введите отметку ригеля на опоре №: ", p + 2)
#             otmrig = float(input())
#             print("Введите поперечный уклон над опорой №: ", p + 2)
#             poperucl = float(input())
#             otmpodfbaz = otmrig + hpodfbaz  # отметка минимальной подферменной площадки
#             nbalok2 = 0
#             otmpodf1 = 0
#             Vpodf1 = 0
#             Vpodfobsh3 = 0
#             Vpodfs2 = 0
#             nbalok = []
#             otmpodf = []
#             hpodf = []
#             Vpodf = []
#             if nbalok1 % 2 == 0:
#                 for k in range((nbalok1 - 2) // 2):
#                     nbalok2 = nbalok2 + 1
#                     nbalok.append(nbalok2)
#                     otmpodf1 = round(otmpodfbaz + shagbal * poperucl * nbalok[k],
#                                      3)  # вычисление отметки i-й подферменной площадки
#                     otmpodf.append(otmpodf1)
#                     hpodf1 = otmpodf[k] - otmrig
#                     hpodf.append(hpodf1)
#                     Vpodf1 = round(hpodf[k] * Bpodfprom * Lpodf, 3)
#                     Vpodf.append(Vpodf1)
#                     Vpodfs2 += Vpodf1
#                     Vpodfobsh3 = round(((Vpodfs2 + Vpodfbazprom) * 2), 3)
#             else:
#                 for m in range((nbalok1 - 1) // 2):
#                     nbalok2 = nbalok2 + 1
#                     nbalok.append(nbalok2)
#                     otmpodf1 = round(otmpodfbaz + shagbal * poperucl * nbalok[m],
#                                      3)  # вычисление отметки i-й подферменной площадки
#                     otmpodf.append(otmpodf1)
#                     hpodf1 = otmpodf[m] - otmrig
#                     hpodf.append(hpodf1)
#                     Vpodf1 = round(hpodf[m] * Bpodfprom * Lpodf, 3)
#                     Vpodf.append(Vpodf1)
#                     Vpodfs2 += Vpodf1
#                     Vpodfobsh3 = round(((Vpodfs2 + Vpodfbazprom) * 2) - Vpodf[-1], 3)
#             print("Отметка верха ригеля промежуточной опоры № ", p + 2, ":", otmrig)
#             print("Отметка подферменной площадки № ", nbalok[0], ":", otmpodfbaz)
#             print("Объем подферменной площадки № ", nbalok[0], ":", Vpodfbazprom, "м3")
#             for y in range(len(nbalok)):
#                 print("Отметка подферменной площадки № ", y + 2, ":", otmpodf[y])
#                 print("Объем подферменной площадки № ", y + 2, ":", Vpodf[y], "м3")
#             if nbalok1 % 2 == 0:
#                 print("Суммарный объем подферменных площадок на промежуточной опоре № ", p + 2, ":",
#                       round(Vpodfobsh3, 3), "м3")
#             else:
#                 print("Суммарный объем подферменных площадок на промежуточной опоре № ", p + 2, ":",
#                       round(Vpodfobsh3, 3), "м3")
#             print("")
#     #
# print("Отметка верха насадки на устое № ", nust[-1], ":", otmrigust[-1])
# print("Отметка подферменной площадки № ", nshag2[0], ":", otmpodfbazust[-1])
# print("Объем подферменной площадки № ", nshag2[0], ":", Vpodfbazust, "м3")
# if nbalok1 % 2 == 0:
#     for w in range((nbalok1 - 2) // 2):
#         print("Отметка подферменной площадки № ", w + 2, ":", otmpodf_2[w])
#         print("Объем подферменной площадки № ", w + 2, ":", Vpodf_2[w], "м3")
#     print("Суммарный объем подферменников на устое № ", nust[-1], ":", round((Vpodfs2 + Vpodfbazust) * 2, 3), "м3")
# else:
#     for q in range((nbalok1 - 1) // 2):
#         print("Отметка подферменной площадки № ", q + 2, ":", otmpodf_2[q])
#         print("Объем подферменной площадки № ", q + 2, ":", Vpodf_2[q], "м3")
#     print("Суммарный объем подферменников на устое № ", nust[-1], ":", Vpodfobsh2, "м3")
# n = int(input("Введите количество пролетных строений: "))
# gabarit = int(input("Введите габарит проезжей части: "))
# while gabarit <= 0:
#     gabarit = int(input("Введите габарит проезжей части: "))
# dlinaproleta1 = 0
# Lpliti1 = 0
# Lpliti = []
# dlinaproleta = []  # формирование списка длин пролетных строений
# for z in range(n):
#     print("Введите длину пролетного строения №", z + 1, ":")  # Запрос длины пролетных строений
#     dlinaproleta1 = float(input())
#     # if dlinaproleta1 == "": break  # проверка корректности введенных значений dlinaproleta1
#     dlinaproleta.append(dlinaproleta1)  # Заполнение списка длин пролетных строений
# Hbalki1 = 0
# Hbalki2 = []
# for x in range(n):
#     print("Выберите высоту балки пролетного строения № ", x + 1,
#           "0.93 м - 1; 1.23 м - 2; 1.53 м - 3: ")  # Запрос высоты балки пролетного строения
#     Hbalki1 = int(input())
#     Hbalki2.append(Hbalki1)  # Заполнение списка высот балок пролетного строения
# Vbal = 0
# Vbalki = 0
# Hbalki = 0
# Hbalki3 = []
# Vbalki1 = []
# nopor1 = n + 1  # количество опор на сооружение
# nopor2 = 0
# nopor = []
#
# for v in range(nopor1):
#     nopor2 = nopor2 + 1
#     nopor.append(nopor2)  # количестов промежуточных опор
# nprom = nopor[1:-1]
# nust = [nopor[0], nopor[-1]]
# nomera = "№".join([str(int(b)) for b in nprom])
#
# for c in range(n):  # подбор балок и их характеристик по длине пролета и высоте балки. Вычисление их объема.
#     if dlinaproleta[c] == 12 and Hbalki2[c] == 1:
#         Hbalki = 0.93
#         osopor = 0.3
#         Vbalki = 6.59
#         mbalki = 16.5
#         harbalki = 'Б 1200.140.93'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 15 and Hbalki2[c] == 1:
#         Hbalki = 0.93
#         osopor = 0.3
#         Vbalki = 8.40
#         mbalki = 21.0
#         harbalki = 'Б 1500.140.93'
#         matbalki = 'B40 F300 W6'
#     elif dlinaproleta[c] == 11.9 and Hbalki2[c] == 2:
#         Hbalki = 1.23
#         osopor = 0.3
#         Vbalki = 7.54
#         mbalki = 18.9
#         harbalki = 'Б 1190.140.123'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 15 and Hbalki2[c] == 2:
#         Hbalki = 1.23
#         osopor = 0.3
#         Vbalki = 9.46
#         mbalki = 23.7
#         harbalki = 'Б 1500.140.123'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 18 and Hbalki2[c] == 2:
#         Hbalki = 1.23
#         osopor = 0.3
#         Vbalki = 11.63
#         mbalki = 29.1
#         harbalki = 'Б 1800.140.123'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 21 and Hbalki2[c] == 2:
#         Hbalki = 1.23
#         osopor = 0.3
#         Vbalki = 13.01
#         mbalki = 32.6
#         harbalki = 'Б 2100.140.123'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 24 and Hbalki2[c] == 2:
#         Hbalki = 1.23
#         osopor = 0.3
#         Vbalki = 15.18
#         mbalki = 38.0
#         harbalki = 'Б 2400.140.123'
#         matbalki = 'B40 F300 W6'
#     elif dlinaproleta[c] == 28 and Hbalki2[c] == 2:
#         Hbalki = 1.23
#         osopor = 0.3
#         Vbalki = 18.07
#         mbalki = 45.2
#         harbalki = 'Б 2800.140.123'
#         matbalki = 'B40 F300 W6'
#     elif dlinaproleta[c] == 18 and Hbalki2[c] == 3:
#         Hbalki = 1.53
#         osopor = 0.3
#         Vbalki = 12.42
#         mbalki = 31.1
#         harbalki = 'Б 1800.140.153'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 28 and Hbalki2[c] == 3:
#         Hbalki = 1.53
#         osopor = 0.3
#         Vbalki = 19.36
#         mbalki = 48.4
#         harbalki = 'Б 2800.140.153'
#         matbalki = 'B35 F300 W6'
#     elif dlinaproleta[c] == 33 and Hbalki2[c] == 3:
#         Hbalki = 1.53
#         osopor = 0.4
#         Vbalki = 24.35
#         mbalki = 60.9
#         harbalki = 'Б 3300.140.153'
#         matbalki = 'B45 F300 W6'
#     Vbal += Vbalki  # вычисление суммарного объема балок пролетных строений
#     Hbalki3.append(Hbalki)
# Hbalki3.append(Hbalki3[-1])
# for c in range(n):
#     Vbalki1.append(Vbalki)
#     if Hbalki3[c] == Hbalki3[c + 1]:
#         otmpch = 0
#         poperucl = 0
#         otmzeli = 0
#
#         otmpch1 = []
#         poperucl1 = []
#         otmzeli1 = []
#
#         for m in range(nopor1):
#             print("Введите отметку проезжей части над опорой № ", m + 1, ":")
#             otmpch = float(input())
#             if otmpch == "": break
#
#             print("Введите поперечный уклон проезжей части над опорой № ", m + 1)
#             poperucl = float(input())
#             if poperucl == "": break
#
#             print("Введите отметку земли у опоры № ", m + 1)
#             otmzeli = float(input())
#             if otmzeli == "": break
#
#             otmpch1.append(otmpch)
#             poperucl1.append(poperucl)
#             otmzeli1.append(otmzeli)
#
#         hdo = float(input("Введите толщину а/б покрытия проезжей части: "))
#         hzashsl = float(input("Введите толщину защитного слоя проезжей части: "))
#         hgidroiz = float(input("Введите толщину гидроизоляции проезжей части: "))
#         hvirsl = float(input("Введите толщину выравнивающего слоя проезжей части: "))
#         zaglublrostv = float(input("Введите величину заглубления ростверка в грунт: "))
#         hpodfbaz = 0.15  # минимальная высота подферменной площадки
#         # if len(nprom) == 0:
#         Hbalkiust = [Hbalki3[0], Hbalki3[-1]]
#         Hstr1 = 0
#         Hstr = []
#         for a in range(len(nopor)):
#             Hstr1 = round((poperucl1[a] * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalki3[a]), 2)
#             Hstr.append(Hstr1)
#         # else:
#         #     Hbalkiust = [Hbalki3[0], Hbalki3[-1]]
#         #     Hbalkiprom = [Hbalki3[1:-1]]
#         #     Hstrust1 = 0
#         #     Hstrust = []
#         #     for s in range(len(nust)):
#         #         Hstrust1 = round((poperucl1[s] * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalkiust[s]), 2)
#         #         Hstrust.append(Hstrust1)
#         #     Hstrprom1 = 0
#         #     Hstrprom = []
#         #     for b in range(len(nprom)):
#         #         Hstrprom1 = round((poperucl1[b] * (0.5 * gabarit) + hdo + hzashsl + hgidroiz + hvirsl + Hbalkiprom[b]),
#         #                           2)
#         #         Hstrprom.append(Hstrprom1)
# l = 2
# b = 1
# c = 5
# k = 8
# a1 = 0
# a = []
# for i in range(l):
#     b = c + 1
#     a1 = b + c
#     # a.append(a1)
#     u1 = 10
#     z1 = 0
#     p1 = 0
#     # z = []
#     # p = []
# for t in range(k):
#     a.append(a1)
#     #     p1 = u1 + 10
#     #     p.append(p1)
#     #     z1 = p[k]
#     #     z.append(z1)
# print(a)
