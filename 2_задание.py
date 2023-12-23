from itertools import *
def f(x,y,w,z):
	return y and (x or z) or (not(y or z)) or w

for i1,i2,i3,i4 in product([0,1],repeat=4):
	t=[(1,i1,0,1),(i2,1,0,i3),(0,0,i4,1)]
	if len(t)==len(set(t)):
		for p in permutations('xywz'):
			if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:	
				print(p)