numbers = input() #Выбранные числа
ndata = []
tdata = []
tickets = input() #Количество билетов

tcount = int(tickets)


numdata = numbers.split(" ")

for i in range(len(numdata)):
    ndata.append(int(numdata[i]))

for i in range(0,tcount):
    tquery = input()
    tdata.append(tquery)

for i in range(len(tdata)):
    lucky = 0

    tdr = tdata[i].split(" ")
    tdra = []

    for i in range(len(tdr)):
        tdra.append(int(tdr[i]))

    for i in range(len(tdra)):
        nf = tdra[i] 

        for s in range(len(ndata)):
            if ndata[s] == nf: lucky += 1

    if lucky >= 3: print('Lucky')
    else: print('Unlucky')

