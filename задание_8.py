import itertools, math

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

def task_4():
    d = []
    g = "ae"
    for i in itertools.product("abcdef", repeat = 6):
        s = "".join(i)
        if s[0] not in g and s[-1] not in g:
            d.append(s)

    print(f"{len(list(set(d)))}")

def task_5():
    word = "джаваскрипт"
    g = "аи"
    k = 0 
    for i in set(itertools.permutations(word, r = 11)):
        s = "".join(i)
        d = []
        for j in range(len(s)):
            if s[j] in g:
                d.append(j + 1)

        if sum(d) == 11:
            k += 1

    print(f"{k}")

if __name__ == f"__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()