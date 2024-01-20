import functools, itertools

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
def task_12234() -> None:
    def function(x: int = 0, y: int = 0, z: int = 0, w: int = 0) -> int:
        return y and (x or z) or not(y or z) or w

    print(f"task 12234")
    i_1: int
    i_2: int
    i_3: int
    i_4: int
    for i_1, i_2, i_3, i_4 in itertools.product([0, 1], repeat=4):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(1, i_1, 0, 1), (i_2, 1, 0, i_3), (0, 0, i_4, 1)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in itertools.permutations(f"xyzw"):
                if [function(**dict(zip(p, r))) for r in our_list] == [0, 0, 0]:
                    print(f"{p}")

@memorise
def task_11650() -> None:
    def function(x: int = 0, y: int = 0, z: int = 0, w: int = 0) -> int:
        return ((y and (x == (not z))) <= w) and (z <= y)

    print(f"task 11650")
    cell_1: int
    cell_2: int
    cell_3: int
    cell_4: int
    cell_5: int
    for cell_1, cell_2, cell_3, cell_4, cell_5 in itertools.product([0, 1], repeat=5):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(0, 0, cell_1, cell_2), (0, cell_3, 0, 0), (1, cell_4, cell_5, 1)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in itertools.permutations(f"xyzw"):
                if [function(**dict(zip(p, r))) for r in our_list] == [0, 0, 0]:
                    print(f"{p}")

@memorise
def task_8547() -> None:
    def function(a: int = 0, b: int = 0, c: int = 0, t: int = 0) -> int:
        return ((not a) or (not b)) and (c <= (not a)) and (t and (not a) or c and (not b))

    print(f"task 8547")
    our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(1, 0, 0, 1), (1, 1, 0, 1), (0, 0, 0, 1), (1, 0, 0, 0)]
    if len(our_list) == len(set(our_list)):
        p: str
        for p in itertools.permutations(f"abct"):
            if [function(**dict(zip(p, r))) for r in our_list] == [0, 1, 0, 1]:
                print(f"{p}")

@memorise
def task_8489() -> None:
    def function(x: int = 0, y: int = 0, z: int = 0, w: int = 0) -> int:
        return ((w <= y) <= (x == y)) or (not z)

    print(f"task 8489")
    cell_1: int
    cell_2: int
    cell_3: int
    cell_4: int
    cell_5: int
    for cell_1, cell_2, cell_3, cell_4, cell_5 in itertools.product([0, 1], repeat=5):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(cell_1, 0, 1, 0), (0, cell_2, cell_3, 0), (cell_4, 1, 1, cell_5)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in itertools.permutations(f"xyzw"):
                if [function(**dict(zip(p, r))) for r in our_list] == [0, 0, 0]:
                    print(f"{p}")

@memorise
def task_8460() -> None:
    def function(x: int = 0, y: int = 0, z: int = 0, w: int = 0) -> int:
        return ((x == z) or not(x == w)) and ((y <= x) or (not z))

    print(f"task 8460")
    cell_1: int
    cell_2: int
    cell_3: int
    cell_4: int
    cell_5: int
    cell_6: int
    cell_7: int
    cell_8: int
    cell_9: int
    for cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9 in itertools.product([0, 1], repeat=9):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(1, cell_1, 1, 1), (cell_2, 1, cell_3, 1), (cell_4, 1, 1, 1), (1, cell_5, 1, cell_6), (cell_7, 1, cell_8, cell_9)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in itertools.permutations(f"xyzw"):
                if [function(**dict(zip(p, r))) for r in our_list] == [0, 0, 0, 0, 0]:
                    print(f"{p}")

if __name__ == f"__main__":
    task_12234()
    task_11650()
    task_8547()
    task_8489()
    task_8460()