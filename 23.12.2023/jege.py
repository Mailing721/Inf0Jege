import functools, itertools, sys
from tkinter import filedialog

sys.setrecursionlimit(999_999_999)

@functools.cache
def task_2() -> None:
    print(f"задание 2")
    print(f"x y z w")
    x: int
    y: int
    z: int
    w: int
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not(y and (x or z) or (not(y or z)) or w):
                        print(f"{x} {y} {z} {w}")

@functools.cache
def task_5() -> None:
    print(f"задание 5")
    d: list[int] = []
    n: int
    for n in range(2, 1_000):
        s: str = bin(n)[2:]
        if n % 2 == 0:
            s += s[-2:]

        else:
            s = f"1" + s + f"0"

        r: int = int(s, 2)
        if r < 100:
            d.append(n)

    print(f"{max(d)}")

@functools.cache
def task_7() -> None:
    print(f"задание 7")
    print(result := (((1280 * 1024 * 10) / 8) * 220) / 12_582_912)

@functools.cache
def task_11() -> None:
    print(f"задание 11")
    print(result := (((110 * 11) / (8 * 1024)) * 32_768))

@functools.cache
def task_12() -> None:
    print(f"задание 12")
    n: int
    d: list[int] = []
    for n in range(4, 1001):
        s: str = f"3" + f"5" * n
        while f"333" in s or f"555" in s:
            if f"555" in s:
                s = s.replace(f"555", f"3" ,1)

            else:
                s = s.replace(f"333", f"5", 1)

            r: int = int(s)

        d.append(r)

    print(f"{max(d)}")

def task_16() -> None:
    print(f"задание 16")
    def function(n: int = 0) -> int:
        if n <= 3:
            return 1

        else:
            return (n + 3) * function(n - 2)

    print(f"задание 16")
    print(f"{function(2028) / function(2024)}")

@functools.cache
def task_17() -> None:
    print(f"задание 17")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = max(x for x in a if len(str(abs(x))) == 5 and str(abs(x))[-1] == f"3")
        d: list[int] = []
        k: int = 0
        i: int
        for i in range(len(a) - 2):
            if ((abs(a[i]) % 10 == 3) + (abs(a[i + 1]) % 10 == 3) + (abs(a[i + 2]) % 10 == 3)) == 1:
                if abs(a[i]) + abs(a[i + 1]) + abs(a[i + 2]) < m:
                    k += 1
                    d.append( abs(a[i]) + abs(a[i]) + abs(a[i]))

    print(f"{k, max(d)}")

def task_19_20_21() -> None:
    def main_1() -> None:
        @functools.cache
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 301 or y > 3:
                return y == 3

            return function(x + 3, y + 1) or function(x * 5, y + 1)

        s: int
        for s in range(1, 301):
            if function(s, 1):
                print(f"task 19: {s}")
                break

    def main_2() -> None:
        @functools.cache
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 301 or y > 4:
                return y == 4

            else:
                if y % 2 != 0:
                    return function(x + 3, y + 1) or function(x * 5, y + 1)

                else:
                    return function(x + 3, y + 1) and function(x * 5, y + 1)

        s: int
        for s in range(1, 301):
            if function(s, 1):
                print(f"task 20: {s}")

    def main_3() -> None:
        @functools.cache
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 301 or y > 5:
                return y == 3 or y == 5

            else:
                if y % 2 == 0:
                    return function(x + 3, y + 1) or function(x * 5, y + 1)

                else:
                    return function(x + 3, y + 1) and function(x * 5, y + 1)

        s: int
        for s in range(1, 301):
            if function(s, 1):
                print(f"task 21: {s}")

    main_1()
    main_2()
    main_3()

if __name__ == f"__main__":
    task_2()
    task_5()
    task_7()
    task_11()
    task_12()
    task_16()
    task_17()
    task_19_20_21()