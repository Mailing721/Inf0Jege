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

        d.sort(key=min)
        p = []
        for i in range(len(d) - 1):
            last_year_len = 0
            inapplicable_count = 0
            max_last_year = 0
            for i, (km, rep) in enumerate(d):
                if rep == 1:
                    inapplicable_count += (km - last_year_len > 0)
                    if km - last_year_len >= max_last_year:
                        max_last_year = km - last_year_len

                    last_year_len = km
                else:
                    last_year_len += rep
   
    print(inapplicable_count, max_last_year)

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
    """
if __name__ == f"__main__":
    task_4()