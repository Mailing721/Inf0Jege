import functools, typing
from tkinter import filedialog

def memorise(function_param: str) -> functools.wraps:

    cache: dict = {}

    @functools.wraps(function_param)
    def wrapper(*args: tuple, **kwargs: dict[str, typing.Any]) -> str:
        key: str = str(args) + str(kwargs)
        if key not in cache:
            cache[key]: function = function_param(*args, **kwargs)

        return cache[key]
    
    return wrapper

@memorise
def task_12254() -> None:
    print(f"task 12254")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: str = file.read()
        k: int
        m: int
        k = m = 1
        i: int
        for i in range(1, len(a)):
            if a[i - 1] + a[i] in (f"RS", f"SQ", f"QR"):
                k += 1
                m = max(k, m)

            else:
                k = 1
    
    print(m)

@memorise
def task_11241() -> None:
    print(f"task 11241")
    words: str = f"ABCD"
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: str = file.read()
        a = a.strip()
        i: str
        for i in words:
            a = a.replace(i, f" ")

        print(f"{max(len(c) for c in a.split())}")

@memorise
def task_9850() -> None:
    print(f"task 9850")
    words: str = f"LISENOK"
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: str = file.read()
        a = a.strip()
        i: str
        for i in words:
            a = a.replace(i, f" ")

        print(f"{max(len(c) for c in a.split())}")

@memorise
def task_9075() -> None:
    print(f"task 9075")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: str = file.read()
        a = a.strip()
        k: int
        m: int
        k = m = 0
        numbers: str = f"02468"
        i: str
        for i in range(len(a) - 1):
            x: str = a[i]
            y: str = a[i + 1]
            if not((x in numbers) != (y in numbers)):
                k += 1
                m = max(m, k)

            else:
                k = 0

        print(f"{m + 1}")

@memorise
def task_8615() -> None:
    print(f"task 8615")
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a = file.read()
        m: int
        back: int 
        m = back = 0
        i: int
        for i in range(len(a) - 2):
            m = max(m, i + 1 - back + 1)
            if a[i] in f"ABCDEF" and a[i + 1] in f"ABCDEF" and a[i + 2] in f"ABCDEF": 
                back = i + 1
    
    print(f"{m}")

if __name__ == f"__main__":
    task_12254()
    task_11241()
    #task_10724
    task_9850()
    #task_9845
    task_9075()
    #task_8959
    task_8615()