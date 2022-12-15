#Part 1
print([h:=(0,0),t:=(0,0),p:=[],len(set([(t:=(h[0]-x,h[1]-y)) for r,n in [i.split() for i in open('input.txt').read().splitlines()] for _ in range(int(n)) for x,y in [[-(((ord(r)&14)-3)>>3),(ord(r)-69)>>4]] if (abs([h:=(h[0]+x,h[1]+y),h[0]][1]-t[0])|abs(h[1]-t[1]))>1]))][3]+1)
#Part 2
print([[p:=[(0,0)]*10,s:=[]],[[[p:=[((p[0][0]+(r=='R')-(r=='L'),p[0][1]+((ord(r)-69)>>4)))]+p[1:]],[[[p:=(p[:t]+[(p[t][0]+(X>0)-(X<0),p[t][1]+(Y>0)-(Y<0))]+p[t+1:])],s.append(p[9])][1] for t in range(1,10) if [X:=p[t-1][0]-p[t][0],Y:=p[t-1][1]-p[t][1],(abs(X)|abs(Y))>1][2]]] for r,n in [i.split() for i in open('input.txt').read().splitlines()] for _ in range(int(n))],len(set(s))][2])
