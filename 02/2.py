#Part 1
print(sum([(3*(a&b)+6*(((b>>1)|(b<<2))&a)>>(a>>1))+b-(b>>2) for a,b in ((1<<((ord(i.split(' ')[0])&7)-1),1<<(ord(i.split(' ')[1])&7)) for i in open('input.txt').read().split('\n'))]))

#Part 2
print(sum([3*(b>>1)+((b&4)>>2)*(((a<<1)|(a>>2))&7)+(b&1)*(((a>>1)|(a<<2))&7)+(((b&2)>>1)*a)-(((a>>1)&(b>>2)^(a>>2)&(b>>1)^(a&b))&1) for a,b in ((1<<((ord(i.split(' ')[0])&7)-1),1<<(ord(i.split(' ')[1])&7)) for i in open('input.txt').read().split('\n'))]))
