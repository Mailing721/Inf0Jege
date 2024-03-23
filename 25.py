x=10
d=[]
for j in range(1,int(x**0.5)+1):
    if x%j==0:
        d.append(j)
        d.append(x//j)

print(sorted(d))