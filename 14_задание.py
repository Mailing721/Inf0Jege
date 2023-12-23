def f(x):
	s=''
	while x!=0:
		s=s+str(x%9)
		x=x//9
	return s[::-1]

a=2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
print(len(f(a))-f(a).count('0'))