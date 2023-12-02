import functools

def main_1() -> None:
    @functools.cache
    def function(x: int, y: int, z: int) -> int:
        if x + y >= 342 or z > 3:
            return z == 3

        return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 5, y, z + 1) or function(x, y * 5, z + 1)

    s: int
    for s in range(1, 326):
        if function(11, s, 1):
            print(f"{s}")
            break

def main_2() -> None:
    @functools.cache
    def function(x: int, y: int, z: int) -> int:
        if x + y >= 342 or z > 4:
            return z == 4

        if z % 2 != 0:
            return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 5, y, z + 1) or function(x, y * 5, z + 1)

        else:
            return function(x + 2, y, z + 1) and function(x, y + 2, z + 1) and function(x * 5, y, z + 1) and function(x, y * 5, z + 1)

    s: int
    for s in range(1, 326):
        if function(11, s, 1):
            print(f"{s}")

def main_3() -> None:
    @functools.cache
    def function(x: int, y: int, z: int) -> int:
        if x + y >= 342 or z > 5:
            return z == 3 or z == 5

        if z % 2 == 0:
            return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 5, y, z + 1) or function(x, y * 5, z + 1)

        else:
            return function(x + 2, y, z + 1) and function(x, y + 2, z + 1) and function(x * 5, y, z + 1) and function(x, y * 5, z + 1)

    s: int
    for s in range(1, 326):
        if function(11, s, 1):
            print(f"{s}")
            break

if __name__ == f"__main__":
    main_1()
    main_2()
    main_3()