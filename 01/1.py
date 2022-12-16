#Part 1
print(max([sum(map(int,i.splitlines())) for i in open("input.txt").read().split('\n\n')]))
#Part 2
print(sum(sorted([sum(map(int,i.splitlines())) for i in open("input.txt").read().split('\n\n')])[-3:]))
