import tkinter.filedialog

with open(tkinter.filedialog.askopenfilename()) as file:
    k = 0
    for line in file.readlines():
        s = [int(x) for x in line.split()]
        if len([x for x in s if str(x)[-1] == "3"]) == 3 and sum(x for x in s if x > 0) ** 2 < sum(x for x in s if x < 0) ** 2:
            k += 1

    print(k)

"""
a=open('9_8554.csv').readlines()
k=0
for i in a:
    s=[int(x) for x in i[:-14].strip().split(';')]
    if len([x for x in s if str(x)[-1]=='3'])==3 and sum(x for x in s if x>0)**2<sum(x for x in s if x<0)**2:
        k+=1

print(k)
"""