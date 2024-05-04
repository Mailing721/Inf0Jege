
def f(x,p):
    if x>=512 or p>3:
        return p==3
    
    if p%2==0:
        return f(x+2,p+1) or f(x+3,p+1) or f(x+4,p+1) or f(x+5,p+1) or f(x*2,p+1)
    
    else:
        return f(x+2,p+1) and f(x+3,p+1) and f(x+4,p+1) and f(x+5,p+1) and f(x*2,p+1)

for s in range(1,512):
    if f(s,1):
        print(s)
        
from tkinter.filedialog import askopenfilename

a=[int(x) for x in open(askopenfilename()).readlines()]
mk=min(x for x in a if str(x)[-2:]=='25')**2
d=[]
for i in range(len(a)-2):
    c=0
    for j in range(i,i+3):
        if len(str(abs(a[j])))==4:
            c+=1
        
        if c>=2 and a[i]*a[i+1]*a[i+2]<=mk:
            d.append(a[i]*a[i+1]*a[i+2])

print(len(d),max(d))