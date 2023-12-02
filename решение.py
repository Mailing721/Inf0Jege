def f(x,y):
	if x>y:
		return 0
	if x==y:
		return 1
	if x<y:
		return f(x+1,y)+f(x*2,y)+f(x*3,y)
k=0
for i in range(2,15,2):
	k+=f(i,15)
		print(k)
