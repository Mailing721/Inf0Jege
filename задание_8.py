import itertools

def task_1():
    k = 0
    c = 0
    for i in itertools.product("ьрплеа", repeat=5):
        s="".join(i)
        k += 1
        if s[-1] == "ь":
            c += 1

        if k == 387:
            print(c)

def task_2():
    k = 0
    c = []
    for i in itertools.product("ангмсту", repeat=6):
        s = "".join(i)
        k += 1
        if s[0] != "у" and s.count("м") == 2 and s.count("г") <= 1:
            c.append(k)

    print(f"{max(c)}")

def task_3():
    a = "0123456789abcdef"
    b = "02468ace"
    k = 0
    for i in itertools.permutations(a, r = 3):
        s = "".join(i)
        if s[0] != "0":
            for j in s:
                if j in b:
                    s = s.replace(j, "2")

                else:
                    s = s.replace(j, "3")

            if "22" not in s and "33" not in s:
                k += 1

    print(k)

if __name__ == f"__main__":
    task_1()
    task_2()
    task_3()