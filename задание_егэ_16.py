import sys, functools, math

sys.setrecursionlimit(1_000_000)

def task_1() -> None:
    @functools.lru_cache(maxsize=1_000_000)
    def function_g(n: int) -> int:
        if n < 10:
            return n
        
        else:
            return function_g(n - 2) + 1
        
    @functools.lru_cache(maxsize=1_000_000)
    def function_f(n: int) -> int:
        return function_g(n - 1)
    
    print(f"###11948###")    
    n: int
    count: int = 0
    for n in range(1, 101):
        if function_f(n) > 0:
            if int(math.sqrt(function_f(n))) ** 2 == function_f(n):
                count += 1

    print(f"{count}")
    print(f"#" * 11)

def task_2() -> None:
    @functools.lru_cache(maxsize=1_000_000)
    def function_f(n: int) -> int:
        if n < 3:
            return 2
        
        elif n > 2 and n % 2 == 0:
            return 2 * function_f(n - 2) - function_f(n - 1) + 2
        
        elif n > 2 and n % 2 != 0:
            return 2 * function_f(n - 1) + function_f(n - 2) - 2
        
    print(f"###10718###")
    print(f"{function_f(170)}")
    print(f"#" * 11)

def task_3() -> None:
    def function_f(n: int) -> None:
        if n == 1:
            return 1
        
        else:
            return n + function_f(n - 1)
        
    print(f"###10659###")
    n: int
    our_list: list[int] = []
    for n in range(1, 101):
        if (function_f(2023) // function_f(n)) % 2 == 0:
            our_list.append(n)

    print(f"{len(our_list)}")
    print(f"#" * 11)

def task_4() -> None:
    def function_f(n: int) -> int:
        if n < 2025:
            return function_f(n + 1) - function_f(n + 2) + 7
        
        else:
            return n

    print(f"###9163###")
    print(f"{function_f(15) - function_f(24)}")
    print(f"#" * 11)

def task_5() -> None:
    @functools.lru_cache(1_000_000)
    def function_f(n: int) -> int:
        if n > 1_000_000:
            return n
        
        else:
            return n + function_f(2 * n)

    @functools.lru_cache(1_000_000)    
    def function_g(n: int) -> int:
        return function_f(n) / n

    print(f"###8426###")
    n: int
    our_list: list[int] = []
    for n in range(1, 1_000_000):
        if function_g(n) == function_g(2000):
            our_list.append(n)

    print(f"{len(our_list)}")
    print(f"#" * 11)

def task_6() -> None:
    def function_f(n: int) -> int:
        if n > 3000:
            return 2
        
        elif n <= 3000 and n % 2 == 0:
            return n + function_f(n + 1) + 1
        
        elif n <= 3000 and n % 2 != 0:
            return function_f(n + 2) + 2
        
    print(f"###8160###")
    print(f"{function_f(40) - function_f(43)}")
    print(f"#" * 11)

def task_7() -> None:
    @functools.lru_cache(1_000_000)
    def function_f(n: int) -> int:
        if n < 2:
            return n 
        
        else:
            return function_f(n // 2) * 10 + n % 2

    print(f"###8372###")
    n: int
    our_list: list[int] = []
    for n in range(1, 20000000000000000000000000000000000000000000000):
        if function_f(n) == 100000100001000100101:
            our_list.append(n)

    print(f"{len(our_list)}")

def task_8() -> None:
    @functools.lru_cache(1_000_000)
    def function_f(n: int) -> int:
        if n < 9:
            return n // 3 + n % 3
        
        else:
            return function_f(n // 9) + function_f(n % 9)

    print(f"###9069###")
    n: int
    our_list: list[int] = []
    for n in range(1, 9**9):
        if function_f(n) == 33:
            our_list.append(n)

    print(f"{len(our_list)}")

def task_9() -> None:
    @functools.lru_cache(1_000_000)
    def function_g(n: int) -> int:
        if n < 10:
            return n
        
        else:
            return function_g(n - 3) + 5
        
    @functools.lru_cache(1_000_000)    
    def function_f(n: int) -> int:
        if n < 3210:
            return function_f(n + 3) + 7
        
        else:
            return 1

    print(f"###9371###")
    print(f"{function_f(15 - function_g(3000))}")
    print(f"#" * 10)

def task_10() -> None:
    @functools.lru_cache(1_000_000)
    def function_f(n: int) -> int:
        if n < 2:
            return n
        
        else:
            return function_f(n // 2) + function_f(n % 2)

    print(f"###9703###")
    n: int
    our_list: list[int] = []
    for n in range(1, 2**30):
        if function_f(n) == 27:
            our_list.append(n)

    print(f"{len(our_list)}")

if __name__ == f"__main__":
    task_1()
    task_2()
    task_3()
#    task_4()
    task_5()
    task_6()
"""
task_7()
task_8()
task_9()
task_10()
"""