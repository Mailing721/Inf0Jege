def f(x,p):
	if x>=301 or p>3:
		return p==3
	if p%2==0:
		return f(x+3,p+1) or f(x*5,p+1)
	else:
		return f(x+3,p+1) and f(x*5,p+1)
for s in range(1,301):
	if f(s,1):
		print(s)