#Part 1
print(sum([cycle:=0,X:=1,[[cycle:=cycle+1,((cycle-20)%40==0)*cycle*X,X:=X+int(k*k.strip('-').isnumeric() or 0)][1] for j in [i.split() for i in open('input.txt').read().splitlines()] for k in j]][2]))
#Part 2
print(''.join([c:=0,X:=1,[['\n'*((c)==0)+('#' if(X-1)<=c<=(X+1) else '.'),X:=X+int(k.strip('-').isnumeric()*k or 0),c:=(c+1)%40][0] for j in [i.split() for i in open('input.txt').read().splitlines()] for k in j]][2]))
