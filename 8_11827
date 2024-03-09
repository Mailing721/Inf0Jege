from itertools import *
k=0
a='01234567'
b='0246'
c='135'
for i in product(a,repeat=7):
  s=''.join(i)
  if s[0]!='0':
    for j in s:
      if j in b:
        s=s.replace(j,'ч')
      elif j in c:
        s=s.replace(j,'н')
    if s.count('ч')==2 and 'н7' not in s and '7н' not in s and '77' not in s:
      k+=1
print(k)
