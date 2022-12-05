#Part 1
print(sum([(ord(j)&0b11111)+26*abs(((ord(j)&0b100000)>>5)-1) for j in (''.join(set(i[:len(i)>>1]).intersection(i[len(i)>>1:])) for i in open('input.txt').read().split('\n')[:-1])]))

#Part 2
print(sum([(ord(j)&0b11111)+26*abs(((ord(j)&0b100000)>>5)-1) for j in [''.join(set(i[0]).intersection(i[1]).intersection(i[2])) for i in [(open('input.txt').read().split('\n')[:-1][k:k+3]) for k in range(0,300,3)]]]))
