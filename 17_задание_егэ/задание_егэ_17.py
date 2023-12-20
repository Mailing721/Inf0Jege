import functools, typing
from tkinter import filedialog

def memorise(function_param: str) -> str:

    cache: dict = {}

    @functools.wraps(function_param)
    def wrapper(*args: tuple, **kwargs: dict[str, typing.Any]) -> str:
        key: str = str(args) + str(kwargs)
        if key not in cache:
            cache[key]: function = function_param(*args, **kwargs)

        return cache[key]
    
    return wrapper

@memorise
def task_11949() -> None:
    print(f"task 11949")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = max(x for x in a if str(abs(x))[-2:] == f"68")
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 3):
            c: int = 0
            j: int
            for j in range(i, i + 4):
                if len(str(abs(a[j]))) == 2:
                    c += 1

            if (c == 1 or c == 4) and (a[i] + a[i + 1] + a[i + 2] + a[i + 3]) >= m:
                k += 1
                d.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])

    print(f"{k, max(d)}")

@memorise
def task_11236() -> None:
    print(f"task 11236")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = min(x for x in a if 9 < x < 100)
        mk: int = max(x for x in a if 999 < x < 10_000 and str(abs(x))[-1] == f"1")
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 2):
            if (a[i] > m ** 2) + (a[i + 1] > m ** 2) + (a[i + 2] > m ** 2) == 2:
                if (abs(a[i]) * abs(a[i + 1]) * abs(a[i + 2])) % mk == 0:
                    k += 1
                    d.append(abs(a[i]) + abs(a[i + 1]) + abs(a[i + 2]))

    print(f"{k, max(d)}")

@memorise
def task_10771() -> None:
    @memorise
    def function(x: int = 0) -> int:
        n: int
        for n in range(2, x):
            if x % n == 0:
                return 0
            
        return 1

    print(f"task 10771")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 2):
            c: int = 0
            j: int
            for j in range(i, i + 3):
                if str(abs(a[j])).count(f"3") > 0:
                    c += 1

            if c == 3 and function(abs(a[i]) + abs(a[i + 1]) + abs(a[i + 2])):
                k += 1
                d.append(abs(a[i]) + abs(a[i + 1]) + abs(a[i + 2]))

        print(f"{k, min(d)}")

@memorise
def task_10100() -> None:
    print(f"task 10100")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = max(x for x in a if str(abs(x))[-2:] == f"13")
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 2):
            result: int = (99 < a[i] < 1_000) + (99 < a[i + 1] < 1_000) + (99 < a[i + 2] < 1_000)
            if result == 2 and a[i] + a[i + 1] + a[i + 2] <= m:
                k += 1
                d.append(a[i] + a[i + 1] + a[i + 2])

        print(f"{k, max(d)}")

@memorise
def task_9840() -> None:
    print(f"task 9840")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = max(x for x in a if len(str(abs(x))) == 4 and str(abs(x))[-2:] == f"39")
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 1):
            result: int = (len(str(abs(a[i]))) == 4) + (len(str(abs(a[i + 1]))) == 4)
            if result == 1 and (a[i] + a[i + 1]) ** 2 <= m ** 2:
                k += 1
                d.append(a[i] + a[i + 1])

        print(f"{k, max(d)}")           

if __name__ == f"__main__":
    task_11949()
    task_11236()
    task_10771()
    task_10100()
    task_9840()