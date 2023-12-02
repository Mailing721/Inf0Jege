def f(x,y,c1,c2,c3,c4):
	if c1+c2+c3+c4=='BACA':
		return 0
	if x>y or x==28:
		return 0
	if x==y:
		return 1
	if x<y:
		return f(x+2,y,c2,c3,c4,'A')+f(x+3,y,c2,c3,c4,'B')+f(x*2,y,c2,c3,c4,'C')
print(f(2,40,'','','',''))
