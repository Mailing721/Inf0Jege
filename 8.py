import itertools

def task_13298():
    n = 0
    for word in itertools.product(sorted('ПРИВЫЧКА'), repeat = 5):
        n += 1
        if n % 5 != 0 and len(set(word)) == 5 and all(x not in word for x in 'ИЫА'):
            print(n - n // 5)
            break


def task_13253():
    k = 0
    word_one = "КОНЕЦ"
    word_two = "ДРАКОН"
    for i in itertools.product(word_one, repeat=5):
        s = "".join(i)
        
        for j in itertools.product(word_two, repeat=5):
            h = "".join(j)

            if "ДРАКОНКОНЕЦ" in s and "ДРАКОНКОНЕЦ" not in h or "ДРАКОНКОНЕЦ" not in s and "ДРАКОНКОНЕЦ" in h:
                k += 1

    print(k)

def task_13094():
    a_0 = "2468"
    a_1 = "1357"
    k = 0
    for x in itertools.product(a_0, a_1, a_0, a_1, a_0, a_1, a_0, a_1, a_0):
        s = "".join(x)
        if all(s.count(x) <= 3 for x in s):
            k += 1 
 
    print(k * 2)

if __name__ == f"__main__":
    task_13298()
#   task_13253()
    task_13094()