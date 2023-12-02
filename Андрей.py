import functools, sys, math

sys.setrecursionlimit(999_999_999)

def task_11948():
    @functools.lru_cache(maxsize=999_999_999)
    def function_g(n):
        if n < 10:
            return n
        
        else:
            return function_g(n - 2) + 1
        
    @functools.lru_cache(maxsize=999_999_999)
    def function_f(n):
        return function_g(n - 1)
    
    count = 0
    for n in range(1, 101):
        if function_f(n) > 0:
            if int(math.sqrt(function_f(n))) ** 2 == function_f(n):
                count += 1

    print(count)

def task_10718():
    @functools.lru_cache(maxsize=999_999_999)
    def function_f(n):
        if n < 3:
            return 2
        
        elif n > 2 and n % 2 == 0:
            return 2 * function_f(n - 2) - function_f(n - 1) + 2

        elif n > 2 and n % 2 != 0:
            return 2 * function_f(n - 1) + function_f(n - 2) - 2
        
    print(function_f(170))

def task_10659():
    def function_f(n):
        if n == 1:
            return 1
        
        elif n > 1:
            return n + function_f(n - 1)
        
        
    count = 0
    for n in range(1,101):
        if (function_f(2023)//function_f(n)) % 2 == 0:
            count += 1
    
    print(count)

def task_8426():
    @functools.lru_cache(maxsize=999_999_999)
    def function_f(n):
        if n > 1_000_000:
            return n
        
        else:
            return n + function_f(2 * n)
        
    @functools.lru_cache(maxsize=999_999_999)
    def function_g(n):
        return function_f(n) / n
    
    count = 0
    for n in range(1, 1_000_000):
        if function_g(n) == function_g(2000):
            count += 1

    print(count)

def task_8685():
    @functools.lru_cache(maxsize=999_999_999)
    def function(x, y):
        if x > y:
            return 0
        
        elif x == y:
            return 1
        
        else:
            return function(x + 3, y) + function(x + 5, y) + function(x * 2, y)
        
    print(function(4, 16) * function(16, 68) + function(4, 32) * function(32, 68) - 2 * function(4, 16) * function(16, 32) * function(32, 68))    

def task_7687():
    @functools.lru_cache(maxsize=999_999_999)
    def function(x, y = 20):
        if x < y:
            return 0
        
        elif x == y:
            return 1
        
        s = function(x - 3, y)

        if x % 2 == 0:
            s += function(x // 3, y)

        else:
            pass

        if x > 9:
            s += function(x // 10, y)

        else:
            pass

        return s

    print(function(1250))

if __name__ == "__main__":
    task_11948()
    task_10718()
    task_10659()
    task_8426()
    task_8685()
    task_7687()

"""
    f(range) = [1, 100) -> 1 - 99

    math.sqrt(number: int | float) -> float:
        return x ** 0.5

    @typing.final
    def function() -> None:
        
"""