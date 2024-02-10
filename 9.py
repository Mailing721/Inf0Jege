a=open('9_1.csv').readlines()
k=0
for i in a:
  s=[int(x) for x in i[:-1016].split(';')]
  ch=0
  dv=0
  r=0
  np=[]
  p=[]
  for j in s:
    if s.count(j)==4:
      ch+=1
      p.append(j)
    if s.count(j)==2:
      dv+=1
      p.append(j)
    if s.count(j)==1:
      r+=1
      np.append(j)
if (ch==4 and dv==2 and r==3) and (sum(np)/len(np)>=max(p)):
  k+=1
print(k)
