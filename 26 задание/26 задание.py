from tkinter.filedialog import askopenfilename

def task_13087():
    with open(askopenfilename()) as file:
        d = []
        for line in file.readlines()[1:]:
            s = [int(x) for x in line.strip().split(f" ")]
            d.append(s)
    
        d.sort(key=lambda x: (x[0], x[1]))
        p = []
        for i in range(len(d) - 1):
                if d[i][0] < d[i + 1][0] and d[i][1] - 20 >= d[i + 1][0]:
                   p.append(d[i])
        
        print(f"{max(p[-1])} {p[-1][1] + 1}")

def task_12256():
    f = open(askopenfilename())
    s, n = map(int, f.readline().split())
    weights = sorted(int(x) for x in f) 
    for i in range(n):
        if s - weights[i] >= 0:
            s -= weights [i]
    	
        else:
            for j in range(i, n):
                if s + weights[i-1] - weights[j] >= 0: 
                    m = weights[j]
        
            break
    
    print(i, m)

def task_12113():
    a=sorted([int(x) for x in open(askopenfilename()).readlines()[1:]])[::-1]
    for i in range(a.count(9998)):
        a.remove(9998)
    
    a.remove(9996)
    d=[a[0]]
    c=a[0]
    for i in a:
        if c - i >= 7 and c % 2 != i % 2:
            d.append(i)
            c = i

    print(len(d), min(d))

def task_11940():
    with open(askopenfilename()) as file:
        d = []
        for line in file.readlines()[1:]:
            s = [int(x) for x in line.strip().split(" ")]
            d.append(s)

        d.sort(key=lambda x: (x[0], x[1]))
        c = d[0]   
        p = [d[0]]
        for i in range(len(d) - 1):
            if d[i + 1][0] / c[1] == 2 and  d[i + 1][1] / c[1] == 2:
                p.append(c)
                c = d[i + 1]

        p.append(c)

    print(len(p), min(x[1] - x[0] for x in p))

    """
    f = open('26.txt')
    n = int(f.readline())
    seq = []
    for i in range(n):
        a, b = map(int, f.readline().split())
        seq.append((a - b, a + b))

    seq = sorted(seq, key=lambda x: (x[0], x[1]))[::-1]
    mx = 0
    ans = 10 ** 20
    for j in range(n):
        c = seq[j]
        count = 1
        res = [c]
        for i in range(n):
            if j != i and abs(c[0]) == abs(seq[i][1]):
                c = seq[i]
                count += 1
                res.append(c)
        
        if count > mx:
            mx = count
            ans = res[0][1]
        
        elif count == mx:
            mx = count
            ans = min(res[0][1], ans)

            print(mx, ans)
    """

def task_11921():
    with open(askopenfilename()) as file:
        d = []
        for line in file.readlines()[102:]:
            s = [int(x) for x in line.strip().split(" ")]
            d.append(s)

        d.sort(key=lambda x: (x[0], x[1]))
        c = d[0]
        p = [d[0]]
        for i in range(len(d) - 1):
            if d[i + 1][1] > c[1] and d[i + 1][0] > c[0]:
                p.append(c)
                c = d[i + 1]

        p.append(c)

    print(min(x[1]-x[0] for x in p), max(x[1]-x[0] for x in p))

    """
    f = open('26.txt')
    n = int(f.readline())
    powers = []
    for i in range(n):
        powers.append(int(f.readline()))
    
    powers.sort(reverse=True)
    m = int(f.readline())
    dems = []
    for _ in range(m):
        b, c = map(int, f.readline().split())
        dems.append((b, c))
    
    dems.sort()
    first, second = 0, m - 1
    amount = 0
    optimal = 10e20
    max_price = 0
    toggle = True
    for first in range(n):
        while second >= 0 and powers[first] <= dems[second][0]:
            if dems[second][1] < optimal:
                optimal = dems[second][1]
            
            second -= 1
        if toggle:
            max_price = optimal
            toggle = False
        
        amount += optimal
    # print(powers)
    # print(dems)
    print(amount, max_price)
    """

def task_6096():
    a = sorted([int(x) for x in open(askopenfilename()).readlines()[1:]])[::-1]
    d = [a[0]]
    c = a[0]
    for i in a:
        if c - i >= 3:
            d.append(i)
            c = i

    print(min(d), len(d))

def task_6031():
    a = sorted([int(x) for x in open(askopenfilename()).readlines()[1:]])[::-1]
    d = [a[0]]
    c = a[0]
    for i in a:
        if c - i >= 6:
            d.append(i)
            c = i

    print(len(d), min(d))

def task_5228():
    a = sorted([int(x) for x in open(askopenfilename()).readlines()[1:]])[::-1]
    d = [a[0]]
    c = a[0]
    for i in a:
        if c - i >= 8:
            d.append(i)
            c = i

    print(len(d), min(d))

def task_5066():
    a = sorted([int(x) for x in open(askopenfilename()).readlines()[1:]])[::-1]
    d = [a[0]]
    c = a[0]
    for i in a:
        if c - i >= 7:
            d.append(i)
            c = i

    print(min(d), len(d))

def task_4965():
    with open(askopenfilename()) as file:
        n, m = map(int, file.readline().split())
        a = [[int(y) for y in line.split()] for line in file]
        a.sort()
        exp_max = 0
        exp_total = 0
        exp_left = 0
        inexp_max = 0
        inexp_total = 0
        inexp_left = 0
        sales = 0
        left = 0
        last = 0
        for i in range(n):
            if i == 0 or a[i][0] == a[i - 1][0]:
                last = a[i][0]
                if a[i][1] == 0:
                    left += 1
                
                else:
                    sales += 1
            
            if i == n - 1 or i != 0 and a[i][0] != a[i - 1][0]:
                if last > m:
                    if sales > exp_max:
                        exp_max = sales
                        exp_total = sales * last
                        exp_left = left
                
                else:
                    if sales > inexp_max:
                        inexp_max = sales
                        inexp_total = sales * last
                        inexp_left = left
                
                if a[i][1] == 0:
                    left = 1
                    sales = 0
                
                else:
                    left = 0
                    sales = 1
        
    
    print(exp_total + inexp_total, exp_left + inexp_left)

if __name__ == f"__main__":
    #task_12256()
    #task_12113()
    #task_11921()
    #task_6096()
    task_6031()
    task_5228()
    task_5066()
    task_4965()