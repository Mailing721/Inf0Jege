import functools

def memorise(function_param: str) -> str:

    cache: dict = {}

    @functools.wraps(function_param)
    def wrapper(*args, **kwargs) -> str:
        key: str = str(args) + str(kwargs)
        if key not in cache:
            cache[key]: function = function_param(*args, **kwargs)

        return cache[key]
    
    return wrapper

@memorise
def task_12247() -> None:
    def function(x: int = 0, a: int = 0) -> int: return (x & a == 0) or not(x & 37 == 0) or not(x & 12 == 0)
    
    print(f"task 12247")
    list_our: list[int] = []
    for a in range(1, 1_000):
        if all(function(x, a) for x in range(1, 1_000)):
            list_our.append(a)

    print(f"{max(list_our)}")

@memorise
def task_11665() -> None:
    def function(x: int = 0, a: int = 0) -> int: return (a + x > 700 - a) and (a % 100 + 100 % x > 50)
    
    print(f"task 11665")
    list_our: list[int] = []
    for a in range(1, 1_000):
        if all(function(x, a) for x in range(1, 1_000)):
            list_our.append(a)

    print(f"{min(list_our)}")

@memorise
def task_11607() -> None:
    def function(x: int = 0, a: int = 0) -> int: return (not((x % 263 == 0) <= (x % a == 0)) and (x % 71 == 0))
    
    print(f"task 11607")
    list_our: list[int] = []
    for a in range(1, 1_000_000):
        if all(function(x, a) for x in range(1, 1_000_000)):
            print(f"{a}")

@memorise
def task_10098() -> None:
    def function(x: int = 0, y: int = 0, a: int = 0) -> int: return (x + 2 * y < a) or (y > x) or (x > 60)
    
    print(f"task 10098")
    for a in range(1, 1_000):
        if all(function(x, y, a) for x in range(1, 1_000) for y in range(1, 1_000)):
            print(f"{a}")
            break

@memorise
def task_9838() -> None:
    def function(x: int = 0, y: int = 0, a: int = 0) -> int: return (x + 2 * y > a) or (y < x) or (x < 30)
    
    print(f"task 9838")
    for a in range(1, 1_000):
        if all(function(x, y, a) for x in range(1, 1_000) for y in range(1, 1_000)):
            print(f"{a}")

if __name__ == f"__main__":
    task_12247()
    task_11665()
#    task_11607()
    task_10098()
    task_9838()