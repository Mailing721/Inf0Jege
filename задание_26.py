import typing, tkinter.filedialog

def task(args: typing.Any = None) -> None:
    a=sorted([int(x) for x in open(tkinter.filedialog.askopenfilename()).readlines()[1:]])[::-1]
    d=[a[0]]
    c=a[0]
    for i in a:
        if c - i>=11:
            d.append(i)
            c = i

    print(len(d), min(d))

def task_2(args: typing.Any = None) -> None:
    with open(tkinter.filedialog.askopenfilename()) as file:
        d = []
        for i in file.readlines()[1:]:
            s = [int(x) for x in i.strip().split(" ")]
            d.append(s)
        
        d.sort(key=lambda x: (x[0], x[1]))
        p = []
        for i in range(len(d) - 1):
            if d[i][0] == d[i + 1][0] and abs(d[i][1] - d[i + 1][1]) == 14:
                p.append(d[i])
    
    print(p[-1][0], p[-1][1] + 1)

def task_3(args: typing.Any = None) -> None:
    file = sorted([int(x) for x in open(tkinter.filedialog.askopenfilename()).readlines()[1:]])[::-1]
    c = 0
    d = []
    for i in file:
        if c != 3:
            d.append(i)
            c += 1

        else:
            c = 0

    print(sum(file[len(file) // 3:]), sum(d))

def task_4():
    with open(tkinter.filedialog.askopenfilename()) as file:
        d = []
        k = 0
        for line in file.readlines()[1:]:
            s = [int(x) for x in line.strip().split(" ")]
            d.append(s)

        d.sort(key=lambda x: (x[0], x[1]))
        p = []
    

    """
    n, r = map(int, input().split())
    events = []
    for _ in range(n):
        start, end = map(int, input().split())
        events.append((start, 1))
        events.append((end, -1))
    
    events.sort()
    last_year_len = 0
    inapplicable_count = 0
    max_last_year = 0
    for i, (km, rep) in enumerate(events):
        if rep == 1:
            inapplicable_count += (km - last_year_len > 0)
            if km - last_year_len >= max_last_year:
                max_last_year = km - last_year_len
            
            last_year_len = km
        else:
            last_year_len += rep
   
    print(inapplicable_count, max_last_year)
    

def task_11940():
    for line in range(0, 2):
        ...
"""
def task_11921():
    with open(tkinter.filedialog.askopenfilename()) as file:
        n = int(file.readline())
        p = []
        for i in range(n):
            p.append(int(file.readline()))

        p.sort(reverse=True)
        m = int(file.readline())
        d = []
        for _ in range(m):
            b, c = map(int, file.readline().split())
            d.append((b, c))

        d.sort()
        f, s = 0, m - 1
        a = 0
        o = 10e20
        m_p = 0
        t = True
        for f in range(n):
            while s >= 0 and p[f] <= d[s][0]: 
                if d[s][1] < o:
                    o = d[s][1]

                s -= 1
            
            if t:
                m_p = o
                t = False
            
            a += o
        
        print(f"{a, m_p}")

def task_8512():
    with open(tkinter.filedialog.askopenfilename()) as file:
        k = int(file.readline())
        n = int(file.readline())
        a = [[int(y) for y in x.split()] for x in file]
        a.sort()
        lockers = [0] * k
        count = 0
        last = 0
        lasttime = 0
        for i in a:
            locker = -1
            for j in range(0, k):
                if lockers[j] < i[0]:
                    locker = j
                    break
            
            if locker != -1:
                if i[0] > lasttime:
                    last = locker + 1
                    lasttime = i[0]

                count += 1
                lockers[locker] = i[1]

    print(count, last)

def task_10726():
    with open(tkinter.filedialog.askopenfile()) as file:
        n = int(file.readline())
        a = [[int(y) for y in x.split()] for x in file]
        a.sort(key=lambda x: x[1], reverse=True) 
        a.sort(key=lambda x: x[0]) 
        start = 0
        last = 0
        total = 0
        mx = 0
        for i in a:
            if i[0] > last:
                start = i[0]
                last = i[0]

            if i[1] > last:
                total += i[1] - last
                last = i[1]
                mx = max(mx, last - start)
    
    print(total, mx)

def task_7826():
    with open(tkinter.filedialog.askopenfilename()) as file:
        k, n = map(int, file.readline().split())
        a = []
        for i in range(n):
            st, end = map(int, file.readline().split())
            a += [[st, end]]
            
        people = [0] * n
        attractions = [0] * n
        a.sort()
        for i in range(n):
            st, end = a[i]
            if st == a[i - 1][0] and people[i - 1] > 0:
                attractions[people[i - 1] - 1] = end
                people[i] = people[i - 1]
                continue

            for nums in range(k):
                if st > attractions[nums]:
                    attractions[nums] = end
                    people[i] = nums + 1
                    break

        print(f"{sum(1 for nums in people if nums > 0)} {[nums for nums in people if nums > 0][-1]}")

def task_6056():
    a=sorted([int(x) for x in open(tkinter.filedialog.askopenfilename()).readlines()[1:]])[::-1]
    d=[a[0]]
    c=a[0]
    for i in a:
        if c - i >= 56:
            d.append(i)
            c = i

    print(len(d), min(d))


if __name__ == f"__main__":
    task_7826()