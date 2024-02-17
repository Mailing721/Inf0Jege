a=open('26_11811.txt').readlines()[1:]
d=[]
for i in a:
    s=[int(x) for x in i.strip().split(' ')]
    d.append(s)

d.sort(key=lambda x:(x[0],x[1]))
c=d[0]
p=[d[0]]
for i in range(len(d)-1):
    if d[i+1][0]<c[1] and d[i+1][1]<c[1]:
       d[i+1]=0
  
    elif d[i+1][0]<c[1] and d[i+1][1]>c[1]:
       c[1]=d[i+1][1]
  
    elif d[i+1][0]>c[1] and d[i+1][1]>c[1]:
       p.append(c)
       c=d[i+1]

p.append(c)

print(len(p),max(x[1]-x[0] for x in p))
