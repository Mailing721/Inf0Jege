import functools

@functools.cache
def task_one() -> None:
    print(f"задание 9543")
    n: int
    for n in range(101, 200):
        s: str =f"5" * n
        while f"555" in s or f"11" in s or f"2" in s:
            if f"555" in s:
                s = s.replace(f"555", f"1", 1)

            if f"11" in s:
                s = s.replace(f"11", f"25", 1)

            if f"2" in s:
                s = s.replace(f"2", f"5", 1)

        if s == f"15":
            print(f"{n}")
            break


@functools.cache
def task_two() -> None:
    print(f"задание 9159")
    n: int
    for n in range(108, 250, 9):
        s: str =f"5" * n
        while f"555" in s or f"11" in s or f"2" in s:
            if f"555" in s:
                s = s.replace(f"555", f"1", 1)

            if f"11" in s:
                s = s.replace(f"11", f"25", 1)

            if f"2" in s:
                s = s.replace(f"2", f"5", 1)

        print(f"{s, n}")


@functools.cache
def task_three() -> None:
    print(f"задание 9065")
    n: int
    d: list[int] = []
    for n in range(4, 200):
        s: str = f">" + f"0" * 21 + n * f"1" + 11 * f"2"
        while s[-1] != f">":
            s = s.replace(f">1", f"22>", 1)
            s = s.replace(f">2", f"2>", 1)
            s = s.replace(f">0", f"1>", 1)

        z: int = sum(map(int, s[:-1]))
        if z % n == 0:
            print(n)


@functools.cache
def task_four() -> None:
    our_list: list[int] = []
    p: int
    for p in range(1000, 2001):
        s: str = f"7" + f"8" * p
        while f"78" in s or f"888" in s:
            if f"78" in s:
                s = s.replace(f"78", f"8", 1)

            if f"888" in s:
                s = s.replace(f"888", f"7", 1)

        if sum([int(x) for x in s]) == 16:
            our_list.append(p)

    print(f"{len(our_list)}")


@functools.cache
def task_five() -> None:
    print(f"задание 8557")
    n: int
    for n in range(10, 100):
        s: str = n * f"13"
        while f"13" in s or f"31" in s or f"11" in s:
            if f"13" in s:
                s = s.replace(f"13", f"4", 1)

            if f"31" in s:
                s = s.replace(f"31", f"1", 1)

            if f"11" in s:
                s = s.replace(f"11", f"2", 1)

            if f"44" in s:
                s = s.replace(f"44", f"1", 1)

        new_s: int = sum([int(x) for x in s])
        print(f"{new_s, n}")


"""
@functools.cache
def task_six() -> None:
    print(f"задание 8500")
    n: int
    for n in range(4, 100):
        s: str = f"2" + f"5" * n
        while f"25" in s or f"25" in s or f"25" in s:
            if f"25" in s:
                s = s.replace(f"25", f"5", 1)

            if f"355" in s:
                s = s.replace(f"355", f"52", 1)

            if f"555" in s:
                s = s.replace(f"555", f"3", 1)

        if s.count("3") == 2:
            print(f"{n}")
            break
"""

@functools.cache
def task_seven() -> None:
    print(f"задание 8470")
    n: int
    for n in range(6, 2000):
        s: str = f"1" + f"5" * n + f"2" + f"5" * n
        while f"15" in s or f"355" in s or f"555" in s:
            if f"15" in s:
                s = s.replace(f"15", f"2", 1)

            if f"255" in s:
                s = s.replace(f"255", f"1", 1)

            if f"555" in s:
                s = s.replace(f"555", f"12", 1)

        new_s: int = sum([int(x) for x in s])
        print(f"{new_s, n}")


@functools.cache
def task_eight() -> None:

    @functools.cache
    def function(number: int) -> int:
        p: int
        for p in range(2, z):
            if number % p == 0:
                return 0

        return 1

    print(f"задание 7417")
    n: int
    for n in range(2, 100):
        s: str = f">" + f"0" * 37 + f"1" * n + f"2" * 37
        while f">1" in s or f">2" in s or f">0" in s:
            if f">1" in s:
                s = s.replace(f">1", f"22>", 1)

            if f">2" in s:
                s = s.replace(f">2", f"2>", 1)

            if f">0" in s:
                s = s.replace(f">0", f"1>", 1)

        s = s[:-1]
        z: int = sum([int(x) for x in s])
        if function(z):
            print(f"{n}")
            break

"""
7351
7033
"""

if __name__ == f"__main__":
    task_one()
    task_two()
    task_three()
    task_four()
    task_five()
#   task_six()
    task_seven()
    task_eight()
