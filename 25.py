from math import *
from fnmatch import *

x=10
d=[]
for j in range(1,int(x**0.5)+1):
    if x%j==0:
        d.append(j)
        d.append(x//j)

print(sorted(d))

def task_1():    
    for i in range(485617,529678+1):
        d=[]
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                d.append(j)
                d.append(i//j)
        
        x=[]
        for l in d:
            p=[]
            for k in range(1,int(l**0.5)+1):
                if l%k==0:
                    p.append(k)
                    p.append(l//k)
        
        if len(set(p))==2:  
            x.append(l)
            
    u=0
    for n in range(len(x)-1):
        if str(x[n])[-1]==str(x[n+1])[-1]:
            u+=1

    if prod(x)==i and len(x)==3 and (max(x)-min(x))<100 and u==2:
        print(i,(max(x)-min(x)),x)

def task_2():
    for i in range(0,10**8,2016):
        if fnmatch(str(i),'*6221*6?') and i%2016==0:
            print(i,i//2016)
            
if __name__ == f"__main__":
    task_1()
