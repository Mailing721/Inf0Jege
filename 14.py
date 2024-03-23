def task_13246():
    def f(x: list[int], n = 10):
        c = len(x) - 1
        s = 0
        for i in x:
            s = s + i * n ** c
            c -= 1

        return s
    
    for p in range(10, 50):
        for x in range(0, p):
            for y in range(0, p):
                s = f([2,4,x,9], p) + f([y,x,y,3], p)
                if s == f([x,4,y,0], p):
                    print(f([x,y,y], p))
                

def task_12923():
    def f(x, n = 10):
        s = ""
        while x > 0:
            s = str(x % n) + s
            x = x // n

        return s
    
    s = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
    print(f(s, 25).count('0'))

def task_12731():
    def f(x: list[int], n = 10):
        c = len(x) - 1
        s = 0
        for i in x:
            s = s + i * n ** c
            c -= 1

        return s
    
    for x in range(0, 10):
        s = f([9,x,"a","b"], 13) + f([x,4,6,"c"], 16) - f(["b",7,x], 15)
        if s % 14 == 0:
            print(x // 14)
            break

if __name__ == f"__main__":
    task_13246()
    task_12923()
    task_12731()