def f(x):
	s=''
	while x!=0:
		s=str(x%5)+s
		x=x//5
	return s
for i in range(1,1000000):
	r=f(i)
	if i%25==0:
		r=r[-3:]+r
	else:
		r=r+f(i%25)
	r=int(r,5)
	if r>10000:
		print(i)
		break