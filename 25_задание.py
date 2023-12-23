from fnmatch import *
for i in range(98591,10**12,98591):
	if fnmatch(str(i),'12?3*456??9'):
		print(i,i//98591)