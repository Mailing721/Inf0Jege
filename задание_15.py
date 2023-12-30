def f(x,a,b):
    return ((x in b)<=(not(x%7==0))) or (a>2*x)

b=[x for x in range(120,131)]
for a in range(1,1000):
    if all(f(x,a,b) for x in range(1,1000)):
        print(a)