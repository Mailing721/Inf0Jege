import itertools

def task_12917():
    word = "прост"
    init_word = "просто"
    k = 0
    for a in word:
        for b in word:
            for c in word:
                for d in word:
                    for e in word:
                        for f in word:
                            s = a + b + c + d + e + f
                            if sorted(s) == sorted(init_word):
                                if s.count("оо") == 0:
                                    k += 1
    
    print(k) 

"""
def task_12786():
    word = "мак"
    c = 0
    for i in itertools.product(word, repeat=6):
        s = "".join(i)
        for j in s:
            if j in s:
                c += 1
    
    print(c)
"""

def task_12783():
    word = "0123456789"
    a = "02468"
    k = 0
    for i in itertools.permutations(word, r=7):
        s = "".join(i)
        if s[0] != "0":
            for j in s:
                if j in a:
                    s = s.replace(j, "2")

                else:
                    s = s.replace(j, "3")

            if "22" not in s and "33" not in s:
                k += 1

    print(k)

def task_12782():
    word = "ящер"
    k = 0
    for i in itertools.product(word, repeat=5):
        s = "".join(i)
        if s.count("е") <= 3 and s.count("е") > 0:
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

def task_11827():
    word = "01234567"
    k = 0
    for i in itertools.product(word, repeat=7):
        s = "".join(i)
        if i[0] != "0" and sum(y in "0246" for y in i) == 2:
            for j in "135":
                s = s.replace(j, "5")
            
            if "57" not in s and "75" in s and "77" not in s:
                k += 1

    print(k)

def task_11293():
    word = "0123456789abc"
    k = 0
    for i in itertools.product(word, repeat=6):
        s = "".join(i)
        if s[0] != "0" and s.count("5") <= 1:
            for j in "13579b":
                s = s.replace(j, "p")

            if "pp" not in s:
                k += 1

    print(k)

def task_11292():
    word = "0123456789abcdef"
    k = 0
    for i in itertools.product(word, repeat=5):
        s = "".join(i)
        if s[0] != "0" and s.count("6") == 2:
            for j in "0248ace":
                s = s.replace(j, "j")
                
            if "6j" not in s and "j6" not in s and "66" not in s:
                k += 1

    print(k)

def task_11291():
    word = "012345"
    k = 0
    for i in itertools.product(word, repeat=7):
        s = "".join(i)
        if s[0] != "0" and s.count("2") == 1:
            for j in "04":
                s = s.replace(j, "j")
                
            if "2j" not in s and "j2" not in s:
                k += 1

    print(k)

if __name__ == f"__main__":
    task_12917()
#   task_12786()
    task_12783()
    task_12782()
#   task_12462()
    task_13094()
    task_11827()
    task_11293()
    task_11292()
    task_11291()