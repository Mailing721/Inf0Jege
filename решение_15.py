def tr(n,m,k):
	return max(n,m,k)<sum([n,m,k])-max(n,m,k)

def f(x,a):
	return not((tr(x,11,18)==(not(max(x,5)>68))) and (tr(x,a,5)))

for a in range(1,100):
	fl=True
	for x in range(1,100):
		if not(f(x,a)):
			fl=False
			break
		if fl:
			print(a)