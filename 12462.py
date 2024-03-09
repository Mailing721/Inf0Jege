from itertools import *
k=0
a='0123456789abcdef'
for i in product(a,repeat=3):
    s=''.join(i)
    if s[0]!='0' and len(i)==len(set(i)) and s==''.join(sorted(s)[::-1]):
        k+=1

for i in product(a,repeat=5):
    s=''.join(i)
    if s[0]!='0' and len(i)==len(set(i)) and s==''.join(sorted(s)[::-1]):
        k+=1

print(k)
