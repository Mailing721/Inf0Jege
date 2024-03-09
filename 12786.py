from itertools import *

k=0
for i in set(permutations('макака')):
    c=0
    s=''.join(i)
    for j in s:
        if j+j in s:
            c+=1

    if c==0:
        k+=1

print(k)
