n = int(input("Введите кол-во пролетных строений: "))
nopor1 = n + 1
shagbal = float(input("Введите шаг балок: "))
nbalok1 = int(input("Введите количество балок в пролетном строении: "))
hpodfbaz = 0.15  # минимальная высота подферменной площадки

for i in range(nopor1):
    print("Введите отметку ригеля на опоре №: ", i + 1)
    otmrig = float(input())
    print("Введите поперечный уклон над опорой №: ", i + 1)
    poperucl = float(input())
    otmpodfbaz = otmrig + hpodfbaz  # отметка минимальной подферменной площадки
    nbalok2 = 0
    nbalok = []
    otmpodf1 = 0
    otmpodf = []
    if nbalok1 % 2 == 0:
        for i in range((nbalok1 - 2) // 2):
            nbalok2 = nbalok2 + 1
            nbalok.append(nbalok2)
            otmpodf1 = round(otmpodfbaz + shagbal * poperucl * nbalok[i],
                             3)  # вычисление отметки i-й подферменной площадки
            otmpodf.append(otmpodf1)
    else:
        for i in range((nbalok1 - 1) // 2):
            nbalok2 = nbalok2 + 1
            nbalok.append(nbalok2)
            otmpodf1 = round(otmpodfbaz + shagbal * poperucl * nbalok[i],
                             3)  # вычисление отметки i-й подферменной площадки
            otmpodf.append(otmpodf1)

    print("Отметка верха ригеля опоры:", otmrig)
    print("Отметка подферменной площадки № ", nbalok[0], ":", otmpodfbaz)
    for i in range(len(nbalok)):
        print("Отметка подферменной площадки № ", i + 2, ":", otmpodf[i])
