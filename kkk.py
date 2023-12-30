from itertools import *
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
def task_12234() -> None:
    def function(x: int = 0, y: int = 0, w: int = 0, z: int = 0) -> int: return y and (x or z) or not(y or z) or w

    print(f"task 12234")
    cell_one: int
    cell_two: int
    cell_three: int
    cell_four: int
    for cell_one, cell_two, cell_three, cell_four in product([0,1], repeat=4):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(1, cell_one, 0, 1), (cell_two, 1, 0, cell_three), (0, 0, cell_four, 1)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in permutations(f"xywz"):
                if [function(**dict(zip(p,r))) for r in our_list] == [0, 0, 0]:
                    print(p)
                    i: int
                    for i in our_list:
                        print(f"{i}")

@memorise
def task_11650() -> None:
    def function(x: int = 0, y: int = 0, w: int = 0, z: int = 0) -> int: return ((y and (x == (not(z)))) <= w) and (z <= y)

    print(f"task 11650")
    cell_one: int
    cell_two: int
    cell_three: int
    cell_four: int
    cell_five: int
    for cell_one, cell_two, cell_three, cell_four, cell_five in product([0,1], repeat=5):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(0, 0, cell_one, cell_two), (0, cell_three, 0, 0), (0, cell_four, cell_five, 1)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in permutations(f"xywz"):
                if [function(**dict(zip(p,r))) for r in our_list] == [0, 0, 0]:
                    print(p)
                    i: int
                    for i in our_list:
                        print(f"{i}")

@memorise
def task_11606() -> None:
    def function(x: int = 0, y: int = 0, w: int = 0, z: int = 0) -> int: return (x <= y) and ((not(y)) <= z) and w 

    print(f"task 11650")
    cell_one: int
    cell_two: int
    cell_three: int
    cell_four: int
    cell_five: int
    cell_six: int
    for cell_one, cell_two, cell_three, cell_four, cell_five, cell_six in product([0,1], repeat=6):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(cell_one, cell_two, 0, 0), (0, 1, 0, cell_three), (0, cell_four, cell_five, cell_six)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in permutations(f"xywz"):
                if [function(**dict(zip(p,r))) for r in our_list] == [1, 1, 1]:
                    print(p)
                    i: int
                    for i in our_list:
                        print(f"{i}")

@memorise
def task_9357() -> None:
    def function_1(x: int = 0, y: int = 0, w: int = 0, z: int = 0) -> int: return (x <= y) or ((not(w)) == z) 
    def function_2(x: int = 0, y: int = 0, w: int = 0, z: int = 0) -> int: return (x <= y) == (w and (not(z))) 

    print(f"task 9357")
    cell_one: int
    cell_two: int
    cell_three: int
    cell_four: int
    cell_five: int
    cell_six: int
    for cell_one, cell_two, cell_three, cell_four, cell_five, cell_six in product([0,1], repeat=6):
        our_list: list[tuple(int, int, int), tuple(int, int, int), tuple(int, int, int)] = [(cell_one, cell_two, cell_three), (cell_four, cell_five, 0), (cell_six, 0, 0)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in permutations(f"xywz"):
                if [function_1(**dict(zip(p,r))) for r in our_list] == [function_2(**dict(zip(p,r))) for r in our_list] == [1, 1, 1]:
                    print(p)
                    i: int
                    for i in our_list:
                        print(f"{i}")

@memorise
def task_7302() -> None:
    def function(x: int = 0, y: int = 0, w: int = 0, z: int = 0) -> int: return z or not(w <= x) or ((not(z)) <= (not(y))) 
    print(f"task 7302")
    cell_one: int
    cell_two: int
    cell_three: int
    cell_four: int
    cell_five: int
    cell_six: int
    for cell_one, cell_two, cell_three, cell_four, cell_five, cell_six in product([0,1], repeat=6):
        our_list: list[tuple(int, int, int, int), tuple(int, int, int, int), tuple(int, int, int, int)] = [(cell_one, 0, 1, 1), (1, cell_two, 1, cell_three), (cell_four, cell_five, cell_six, 1)]
        if len(our_list) == len(set(our_list)):
            p: str
            for p in permutations(f"xywz"):
                if [function(**dict(zip(p,r))) for r in our_list] == [0, 0, 0]:
                    print(p)
                    i: int
                    for i in our_list:
                        print(f"{i}")

if __name__ == f"__main__":
    task_12234()
    task_11650()
    task_11606()
    task_9357()
    task_7302()