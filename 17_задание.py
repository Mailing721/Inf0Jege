a=[int(x) for x in open('17_12249.txt').readlines()]
mk=max([x for x in a if len(str(abs(x)))==5 and str(abs(x))[-1]=='3'])
d=[]
for i in range(len(a)-2):
	c=0
	for j in range(i,i+3):
		if str(abs(a[j]))[-1]=='3':
			c+=1
	if c>=1 and a[i]+a[i+1]+a[i+2]<=mk:
		d.append(a[i]+a[i+1]+a[i+2])
print(len(d),max(d))