#!/usr/bin/python
calories =  [i for i in open("input1.txt",'r').read().split('\n')]

mx = [0,0,0]
tmp = 0

for i in calories:
    if not i:
        if tmp > mx[2]:
            mx[2] = tmp
            mx.sort(reverse = True)
        tmp = 0
    else:
        tmp += int(i)

print(mx[0]) #Part 1
print(sum(mx)) #Part 2

