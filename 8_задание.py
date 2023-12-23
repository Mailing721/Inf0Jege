from itertools import *
k=0
for i in product('012345678',repeat=5):
	s=''.join(i)
	c=0
	for j in s:
		if j+j in s:
			c+=1
	if c==0 and s[0]!='0' and s.count('5')==1:
		k+=1
print(k)

