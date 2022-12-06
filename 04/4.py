#Part 1
print(sum([((int(a)<=int(c))&(int(b)>=int(d)))|((int(c)<=int(a))&(int(d)>=int(b))) for a,b,c,d in ((i.split(',')[0].split('-')+i.split(',')[1].split('-')) for i in open('input.txt').read().splitlines())]))

#Part 2
print(sum([(int(a)<=int(c)<=int(b))|(int(c)<=int(a)<=int(d)) for a,b,c,d in ((i.split(',')[0].split('-')+i.split(',')[1].split('-')) for i in open('input.txt').read().splitlines())]))
