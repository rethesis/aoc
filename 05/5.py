#Part 1
print([f:=open('input.txt').readlines(),s:=[[*''.join(i[j].strip() for i in f[:8])][::-1] for j in range(1,35,4)],[[s[int(c)-1].append(s[int(b)-1].pop()) for _ in range(int(a))] for a,b,c in ((i[5:7].strip(),i[12:14].strip(),i[-3:-1].strip()) for i in f[10:])],''.join(s[q][-1] for q in range(0,9))][3])

#Part 2
print([f:=open('input.txt').readlines(),s:=[[*''.join(i[j].strip() for i in f[:8])][::-1] for j in range(1,35,4)],[[s[int(c)-1].append(s[int(b)-1].pop(l-int(a))) for l in range(int(a))] for a,b,c in ((i[5:7].strip(),i[12:14].strip(),i[-3:-1].strip()) for i in f[10:])],''.join(s[q][-1] for q in range(0,9))][3])
