a=open('9_12241.csv').readlines()
k=0
for i in a:
	s=[int(x) for x in i.strip().split(';')]
	c=0
	p=[]
	np=[]
	for j in s:
		if s.count(j)==2:
			c+=1
			p.append(j)
		else:
			np.append(j)
	if c==6 and (max(p)+min(p))/2<np[0]:
		k+=1
print(k)