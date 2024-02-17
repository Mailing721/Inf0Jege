a=open('09_9156.csv').readlines()
k=0
for i in a:
    s=[int(x) for x in i.strip().split(';')]
    if (min(s)+max(s))%3==0 and (abs(s[0]-s[1])==abs(s[2]-s[3]) or abs(s[0]-s[2])==abs(s[1]-s[3])):
        k+=1

print(k)
