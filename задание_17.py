f"""
from tkinter import filedialog

def main() -> None: 
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: tuple(int, int, int) = max(x for x in a if len(str(abs(x))) == 4 and str(abs(x))[-2:] == f"39")
        i: int
        k: int = 0
        d: list[int] = []
        for i in range(len(a) - 1):
            c: int = 0
            j: int
            for j in range(i, i + 2):
                if len(str(abs(a[j]))) == 4:
                    c += 1

            if c == 1 and (a[i] + a[i + 1]) ** 2 <= m ** 2:
                k += 1
                d.append(a[i] + a[i + 1])

        print(f'...')

if __name__ == f"__main__":
    main()
"""

from tkinter import filedialog

def task_11481() -> None:
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: tuple(int, int, int) = max(x for x in a if str(abs(x))[0] == f"8")
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 2):
            c: int = 0
            j: int
            for j in range(i, i + 3):
                if str(abs(a[j]))[0] == f"6":
                    c += 1

            if c <= 1 and a[i] + a[i + 1] + a[i + 2] >= m:
                k += 1
                d.append(a[i] + a[i + 1] + a[i + 2])

        print(f"{k, min(d)}")

def task_10719() -> None:
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 3):
            if (str(a[i])[-2:] == f"13" and str(a[i + 3])[-2:] != f"13") or (str(a[i])[-2:] != f"13" and str(a[i + 3])[-2:] == f"13"):
                k += 1
                d.append(a[i] + a[i + 3])

    print(f"{k, max(d)}")

def task_9164() -> None:
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = max(x for x in a if x % 17 == 0)
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 1):
            if a[i] + a[i + 1] > m:
                k += 1
                d.append(a[i] + a[i + 1])

    print(f"{k, max(d)}")

def task_11949() -> None:
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

def task_11236() -> None:
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: list[int] = [int(x) for x in file.readlines()]
        m: int = min(x for x in a if 9 < x < 100)
        mk: int = min(x for x in a if 999 < x < 10_000 and str(abs(x))[-1] == f"1")
        k: int = 0
        d: list[int] = []
        i: int
        for i in range(len(a) - 2):
            c: int = 0
            j: int
            for j in range(i, i + 3):
                pass                

    print(f"{k, max(d)}")

if __name__ == f"__main__":
    task_11236()