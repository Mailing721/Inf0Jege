import itertools

def task_13243():
    a = "0123456789abcdefgh"
    print(f"{len(a)}")
    for x in a:
        s = int(f"1{x}253", 18) + int(f"32{x}8", 18)
        if s % 7 == 0:
            print(x, s//7)
            break

def task_12243():
    for x in range(0,18):
        s=1*18**4+x*18**3+2*18**2+5*18**1+3+3*18**3+2*18**2+x*18+8
        if s%7==0:
            print(x,s//7)

def task_11243():
    def f(x: list[int], n = 10):
        c = len(x) - 1
        s = 0
        for i in x:
            s = s + i * n ** c
            c -= 1

        return s
    
    for x in range(0,39):
        for y in range(0, 39):
            s = f([5,8,x,7,2,3,y,4,9], 39)
            if s%38==0 and (f([y,x], 39) ** 0.5) == int(f([y,x], 39) ** 0.5):
                print(f([y, x], 39))

if __name__ == f"__main__":
    task_13243()
    task_12243()
    task_11243()