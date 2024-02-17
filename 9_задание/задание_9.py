import typing

def task_12463(args: typing.Any = None) -> None:
    with open(f"mYVvuVljQ.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            s: list[int] = [int(x) for x in i.split()]
            s_c: list[int] = [s.count(x) for x in s]
            if s_c.count(4) == 4 and s_c.count(2) == 2 and s_c.count(1) == 3:
                a_p: list[int] = [s[x] for x in range(9) if s_c[x] > 1]
                a_n: list[int] = [s[x] for x in range(9) if s_c[x] == 1]
                if sum(a_n) / 3 >= max(a_p):
                    k += 1

    print(f"{k}")

def task_12241(args: typing.Any = None) -> None:
    with open(f"U6WoKmyVQ.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            s: list[int] = [int(x) for x in i.split()]
            s_c: list[int] = [s.count(x) for x in s]
            if s_c.count(2) == 6 and s_c.count(1) == 1:
                a_p: list[int] = [s[x] for x in range(7) if s_c[x] > 1]
                a_n: list[int] = [s[x] for x in range(7) if s_c[x] == 1]
                if (max(a_p) + min(a_p)) / 2 < a_n[0]:
                    k += 1
    
    print(f"{k}")

def task_12098(args: typing.Any = None) -> None:
    with open(f"h2lSHAMtN.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            s: list[int] = [int(x) for x in i.split()]
            s_c: list[int] = [s.count(x) for x in s]
            if s_c.count(3) == 3 and s_c.count(1) == 1:
                a_p: list[int] = [s[x] for x in range(4) if s_c[x] > 1 and s_c[x] % 2 == 0]
                a_n: list[int] = [s[x] for x in range(4) if s_c[x] == 1 and s_c[x] % 2 != 0]
                k += 1

    print(f"{k}")

def task_11658(args: typing.Any = None) -> None:
    with open(f"JehR964TR.txt") as file:
        k: int = 0
        i: str
        a: list[int] = []
        for i in file.readlines():
            k += 1
            s: list[int] = [int(x) for x in i.split()]
            s_c: list[int] = [s.count(x) for x in s]
            if s_c.count(3) == 3 and s_c.count(1) == 4:
                a_p: list[int] = [s[x] for x in range(7) if s_c[x] > 1]
                a_n: list[int] = [s[x] for x in range(7) if s_c[x] == 1]
                if (sum(a_p) / len(a_p)) > ((sum(a_p) + sum(a_n)) / (len(a_p) + len(a_n))):
                    a.append(k)

    print(f"{max(a)}")

def task_9778(args: typing.Any = None) -> None:
    with open(f"09_9778.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            k += 1
            s: list[int] = [int(x) for x in i.split()]
            s_c: list[int] = [s.count(x) for x in s]
            if s_c.count(2) == 2 and s_c.count(1) == 4:
                a_p: list[int] = [s[x] for x in range(6) if s_c[x] > 1]
                a_n: list[int] = [s[x] for x in range(6) if s_c[x] == 1]
                if a_p[0] > (sum(a_n) / 4):
                    print(f"{k}")
                    break

def task_9062(args: typing.Any = None) -> None:
    with open(f"9_9062.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            s: list[int] = [int(x) for x in i.split()]
            max_value: int = max(s)
            min_value: int = min(s)
            if s[0] != max(s) and s[0] != min(s) and s[-1] != max(s) and s[-1] != min(s):
                s.remove(max_value)
                s.remove(min_value)
                if (max(s) - min(s)) != 0:
                    if (max_value - min_value) % (max(s) - min(s)) == 0:
                        k += 1

    print(f"{k:,}")

def task_9364(args: typing.Any = None) -> None:
    with open(f"AzDLEJQPy.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            s: list[int] = [int(x) for x in i.split()]
            s_c: list[int] = [s.count(x) for x in s]
            if s_c.count(2) == 2 and s_c.count(1) == 3:
                s_count: list[int] = [s[x] for x in range(5) if s_c[x] % 2 == 0]
                s_uncount: list[int] = [s[x] for x in range(5) if s_c[x] % 2 != 0]
                if sum(s_uncount) > sum(s_count):
                    k += 1

    print(f"{k:,}")

def task_8497(args: typing.Any = None) -> None:
    with open(f"zXhQYDHKm.txt") as file:
        k: int = 0
        i: str
        for i in file.readlines():
            s: list[int] = [int(x) for x in i.split()]
            max_value: int = max(s)
            min_value: int = min(s)
            if s[0] != s[1] and s[0] != s[2] and s[0] != s[3] and s[0] != s[4] and s[1] != s[0] and s[1] != s[2] and s[1] != s[3] and s[1] != s[4] and s[2] != s[0] and s[2] != s[1] and s[2] != s[3] and s[2] != s[4] and s[3] != s[0] and s[3] != s[1] and s[3] != s[2] and s[3] != s[4] and s[4] != s[0] and s[4] != s[1] and s[4] != s[2] and s[4] != s[3]:
                s.remove(max_value)
                s.remove(min_value)
                if (max_value + min_value) * 3 >= sum(s) * 2:
                    k += 1

    print(f"{k:,}")

if __name__ == f"__main__":
    task_12463()
    task_12241()
    task_12098()
    task_11658()
    # 9156
    task_9778()
    task_9062()
    task_9364()
    # 8554
    task_8497()