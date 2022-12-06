#Part 1
print([m:=open('input.txt').read().strip(),list(set([j*(len(set(m[j-4:j]))==4) for j in range(4,len(m))]))[1]][1])

#Part 2
print([m:=open('input.txt').read().strip(),list(set([j*(len(set(m[j-14:j]))==14) for j in range(14,len(m))]))[1]][1])
