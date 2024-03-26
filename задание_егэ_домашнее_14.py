import string

def task_13246():
    def f(x: list[int], n=10):
        c = len(x) - 1
        s = 0
        for i in x:
            s = s + i * n ** c
            c -= 1

        return s

    for p in range(10, 50):
        for x in range(0, p):
            for y in range(0, p):
                s = f([2, 4, x, 9], p) + f([y, x, y, 3], p)
                if s == f([x, 4, y, 0], p):
                    print(f([x, y, y], p))

def task_12923():
    def f(x, n=10):
        s = ""
        while x > 0:
            s = str(x % n) + s
            x = x // n

        return s

    s = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
    print(f(s, 25).count('0'))

def task_12731():
    for x in f"0123456789abc":
        s = int(f"9{x}ab", 13) + int(f"{x}46c", 16) - int(f"b7{x}", 15)
        if s % 14 == 0:
            print(x, s // 14)

def task_12484():
    def f(x, n=10):
        s = ""
        while x > 0:
            s = str(x % n) + s
            x = x // n

        return s

    for x in range(0, 1000):
        for y in range(0, 1000):
            s = 5 ** 50 + 5 ** 30 - 5 ** x - x - y - 5 ** y - x
            s = f(s, 5)
            if s.count("0") == 10:
                print(x * y)

def task_12468():
    for x in "0123456789abcdefghi":
        s = int(f"78{x}79643", 19) + int(f"25{x}43", 19) + int(f"63{x}5", 19)
        if s % 18 == 0:
            print(s // 18)
            break

def task_12246():
    def f(x, n=10):
        s = ""
        while x > 0:
            s = str(x % n) + s
            x = x // n

        return s

    s = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
    print(len(f(x=s, n=9)) - f(x=s, n=9).count("0"))

def task_12103():
    def f(x, n=10):
        s = ""
        while x > 0:
            s = str(x % n) + s
            x = x // n

        return s

    s = 361 * 2349 ** 84 - 89 ** 192 + 1953 ** 481 * 4843 ** 151
    print(f(x=s, n=9).count("5"))

def task_11663():
    for x in "0123456789abcdefghijklmnopq":
        s = int(f"17{x}35", 27) + int(f"{x}742M", 27) + int(x, 27) ** 3
        if s % 23 == 0:
            print(s // 23)

def task_11836():
    for x in (string.digits + string.ascii_uppercase)[:32]:
        s = int(f"931{x}964", 32) + int(f"4{x}51{x}1", 32) + int(f"2861{x}637", 32)
        if s % 31 == 0:
            print(s // 31)
            break

if __name__ == f"__main__":
    task_13246()
    task_12923()
    task_12731()
    task_12484()
    task_12468()
    task_12246()
    task_12103()
    task_11663()
    task_11836()