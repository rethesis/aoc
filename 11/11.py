#Part 1
file = [i.splitlines() for i in open('input.txt').read().split('\n\n')]

#Preprocessing
for i,data in enumerate(file):
    file[i][1] = eval('['+data[1][18:]+']')
    file[i][2] = data[2][data[2].find('=')+1:]
    file[i][3] = int(data[3][-2:])
    file[i][4] = int(data[4][-2:]) 
    file[i][5] = int(data[5][-2:])

monke = [0]*len(file) #Monkey business

for _ in range(20):
    for i in range(len(file)):
        monke[i] += len(file[i][1])
        for _ in range(len(file[i][1])):
            tmp = file[i][1].pop()
            tmp2 = eval(file[i][2].replace('old',str(tmp)))//3
            if tmp2%file[i][3]==0:
                file[file[i][4]][1].append(tmp2)
            else:
                file[file[i][5]][1].append(tmp2)

monke = sorted(monke)
print(monke[-1]*monke[-2])


#Part 2
file = [i.splitlines() for i in open('input.txt').read().split('\n\n')]

#Preprocessing
for i,data in enumerate(file):
    file[i][1] = eval('['+data[1][18:]+']')
    file[i][2] = data[2][data[2].find('=')+1:]
    file[i][3] = int(data[3][-2:])
    file[i][4] = int(data[4][-2:]) 
    file[i][5] = int(data[5][-2:])

monke = [0]*len(file) #Monkey business
mod = eval('*'.join([str(file[e][3]) for e in range(len(file))]))

for _ in range(10000):
    for i in range(len(file)):
        monke[i] += len(file[i][1])
        for _ in range(len(file[i][1])):
            worry = eval(file[i][2].replace('old',str(file[i][1].pop())))%mod
            if worry%file[i][3]==0:
                file[file[i][4]][1].append(worry)
            else:
                file[file[i][5]][1].append(worry)

monke = sorted(monke)
print(monke[-1]*monke[-2])
