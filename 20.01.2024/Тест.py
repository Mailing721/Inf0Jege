import functools, itertools, math, sys

sys.setrecursionlimit(999_999_999)

def task_2():
    f = lambda a, b, c, d: (a <= b) and (b <= c) and (c <= d)
    for i1, i2 in itertools.product([0, 1], repeat=2):
        l = [(0, i1, 1, 0), (0, i2, 1, 0), (0, 1, 1, 1)]
        if len(l) == len(set(l)):
            for p in itertools.permutations("abcd"):
                if [f(**dict(zip(p, r))) for r in l] == [1, 1, 1]:
                    print(p)

def task_5():
    def f(x):
        s = ""
        while x > 0:
            reminder = x % 5
            s = str(reminder) + s
            x = x // 5
        
        return s

    for n in range(1, 100000):
        s = f(n)
        if n % 25 == 0:
            s = s[-3:-1] + s

        else:
            s += f(n % 25)

        r = int(s, 5)
        if r > 10000:
            print(n)
            break

task_7 = lambda: print(s := math.log(((8*1024*1024*1024) / 200) / (2560*1440), 2))
task_11 = lambda: print(s := ((10 * 8 * 1024) / 1000) / 6)

def task_12():
    for n in range(3, 10001):
        s = "5" + "2" * n
        while "52" in s or "2222" in s or "1112" in s:
            if "52" in s:
                s = s.replace("52", "11", 1)
                s = s.replace("2222", "5", 1)

            else:
                s = s.replace("1112", "2", 1)

        l = [int(x) for x in s]
        if sum(l) == 1685:
            print(n)

def task_15():
    f = lambda x, y, a: not((3*x + y > a) and (y < x) and (x < 30))
    for a in range(1, 1000):
        if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
            print(a)
            break

def task_16():
    @functools.lru_cache(maxsize=999_999_999)
    def f(n):
        if n > 10_000:
            return 42

        elif n <= 10_000 and n % 2 == 0:
            return 2 * n + f(n + 3) + f(n + 4) + f(n + 6)

        elif n <= 10_000 and n % 2 != 0:
            return -(n + f(n+1) + f(n+3))

    print(f(9996) - f(9994))

def task_19_20_21():
    def task_19():
        def f(x, y, z):
            if x + y >= 231 or z > 3:
                return z == 3
            
            else:
                if z % 2 == 0:
                    return f(x + 4, y, z + 1) or f(x, y + 4, z + 1) or f(x * 3, y, z + 1) or f(x, y * 3, z + 1) 

                else: 
                    return f(x + 4, y, z + 1) and f(x, y + 4, z + 1) and f(x * 3, y, z + 1) and f(x, y * 3, z + 1) 

        for s in range(1, 218):
            if f(10, s, 1):
                print(s)
                break

    def task_20():
        def f(x, y, z):
            if x + y >= 231 or z > 4:
                return z == 4
            
            else:
                if z % 2 != 0:
                    return f(x + 4, y, z + 1) or f(x, y + 4, z + 1) or f(x * 3, y, z + 1) or f(x, y * 3, z + 1) 

                else:
                    return f(x + 4, y, z + 1) and f(x, y + 4, z + 1) and f(x * 3, y, z + 1) and f(x, y * 3, z + 1) 

        for s in range(1, 218):
            if f(10, s, 1):
                print(s)

    def task_21():
        def f(x, y, z):
            if x + y >= 231 or z > 5:
                return z == 3 or z == 5
            
            else:
                if z % 2 == 0:
                    return f(x + 4, y, z + 1) or f(x, y + 4, z + 1) or f(x * 3, y, z + 1) or f(x, y * 3, z + 1) 

                else:
                    return f(x + 4, y, z + 1) and f(x, y + 4, z + 1) and f(x * 3, y, z + 1) and f(x, y * 3, z + 1) 

        for s in range(1, 218):
            if f(10, s, 1):
                print(s)

    print("task 19")
    task_19()
    print("task 20")
    task_20()
    print("task 21")
    task_21()

def task_23():
    def g(x):
        if x % 2 != 0:
            return x
  
        else:
            while x % 2 == 0:
                x += 1

                if x % 2 != 0:
                    return x

    def h(x):
        x = str(x)
        return int(x[0]) + 1

         
    def f(x, y):
        if x > y or x == 81:
            return 0

        elif x == y:
            return 1

        else:
            return f(h(x), y) + f(x + 3, y) + f(g(x), y)

    print(f(42, 73) * f(73, 89))

if __name__ == "__main__":
    task_2()
    task_5()
    task_7()
    task_11()
#    task_12()
    task_15()
    task_16()
    task_19_20_21()
#    task_23()