otmrig = float(input("Введите отметку ригеля: "))
shagbal = float(input("Введите шаг балок: "))
nbalok1 = int(input("Введите количество балок в пролетном строении: "))
hpodfbaz = 0.15  # минимальная высота подферменной площадки
nbalok2 = 0
nbalok = []
otmpodfbaz = otmrig + hpodfbaz  # отметка минимальной подферменной площадки
otmpodf1 = 0
otmpodf = []
if nbalok1 % 2 == 0:
    poperucl = float(input("Введите поперечный уклон над опорой: "))
    for i in range((nbalok1 - 2) // 2):
        nbalok2 = nbalok2 + 1
        nbalok.append(nbalok2)
        otmpodf1 = round(otmpodfbaz + shagbal * poperucl * nbalok[i],3)  # вычисление отметки i-й подферменной площадки
        otmpodf.append(otmpodf1),

    print("Отметка верха ригеля опоры:", otmrig)
    print("Отметка подферменной площадки № ", nbalok[0], ":", otmpodfbaz)
    for i in range(len(nbalok)):
        print("Отметка подферменной площадки № ", i + 2, ":", otmpodf[i])

else:
    for i in range((nbalok1 - 1) // 2):
        nbalok2 = nbalok2 + 1
        nbalok.append(nbalok2)
        otmpodf1 = round(otmpodfbaz + shagbal * poperucl * nbalok[i],3)  # вычисление отметки i-й подферменной площадки
        otmpodf.append(otmpodf1)

    print("Отметка верха ригеля опоры:", otmrig)
    print("Отметка подферменной площадки № ", nbalok[0], ":", otmpodfbaz)
    for i in range(len(nbalok)):
        print("Отметка подферменной площадки № ", i + 2, ":", otmpodf[i])
