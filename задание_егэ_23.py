import functools, sys

sys.setrecursionlimit(999_999_999)

def task_1() -> None:
    @functools.lru_cache(maxsize=999_999_999)
    def function(x: int, y: int) -> None:
        if x > y or x == 100:
            return 0
        
        elif x == y:
            return 1
        
        s: int = 0
        if x % 10 != 0:
            s += function(x + x % 10, y)

        if x % 68 != 0:
            s += function(x + x % 68, y)

        s += function(x ** 2, y)
        return s

    print(f"11953")    
    print(f"{function(2, 68) * function(68, 680)}")

def task_2() -> None:
    @functools.lru_cache(999_999_999)
    def function(x: int, y: int, z: int) -> int:
        count: int = 0
        if x == y:
            count += 1
            return 1
        
        elif x > y:
            count += 1
            return 0
        
        if z == 2:
            return function(x + 2, y, 1) + function(x * 3, y, 3)
        
        return function(x + 2, y, 1) + function(x ** 2, y, 2) + function(x * 3, y, 3)
        
    print(f"11240")
    print(f"{function(2, 64, 0)}")

def task_3() -> None:
    @functools.lru_cache(maxsize=999_999_999)
    def function(x: int, y: int) -> int:
        if x > y:
            return 0
        
        elif x == y:
            return 1
        
        else:
            return function(x + 1, y) + function(x + 2, y) + function(x * 3, y)
        
    print(f"9376")
    print(f"{function(6, 15) * function(15, 25) + function(6, 21) * function(21, 25) - 2 * function(6, 15) * function(15, 21) * function(21, 25)}")

def task_5() -> None:
    @functools.lru_cache(maxsize=999_999_999)
    def function(x: int, y: int) -> int:
        if x > y:
            return 0
        
        elif x == y:
            return 1
        
        else:
            return function(x + 3, y) + function(x + 5, y) + function(x * 2, y)
        
    print(f"8685")
    print(f"{function(4, 16) * function(16, 68) + function(4, 32) * function(32, 68) - 2 * function(4, 16) * function(16, 32) * function(32, 68)}")

def task_7() -> None:
    @functools.lru_cache(maxsize=999_999_999)
    def function(x: int, y: int = 20) -> int:
        if x < y:
            return 0
        
        elif x == y:
            return 1
        
        s: int = function(x - 3, y)
        if x % 2 == 0:
            s += function(x // 3, y)

        if x > 9:
            s += function(x // 10, y)

        return s            
        
    print(f"7687")
    print(f"{function(1250)}")

def task_10() -> None:
    @functools.lru_cache(maxsize=999_999_999)
    def function(x: int, y: int) -> int:
        if x > y or x == 58:
            return 0
        
        elif x == y:
            return 1
        
        else:
            return function(x + 1, y) + function(x + 2, y) + function(x + 3, y) + function(x * 4, y)
        
    print(f"6797")
    print(f"{function(38, 45) * function(45, 68)}")

if __name__ == f"__main__":
    task_1()
    task_2()
    task_3()
    #9168
    task_5()
    #8165
    task_7()
    #7074
    #7011
    task_10()