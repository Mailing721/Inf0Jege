def task_13853():
    n = {}
    k = [0, 1]
    
    def вправо():
        k[0], k[1] = k[1], -k[0]

    def влево():
        k[0], k[1] = -k[1], k[0]

    def вперед(x):
        p[0] += k[0]*x
        p[1] += k[1]*x

    def закрасить():
        res.add(tuple(p))

    res = set()
    p = [0, 0]
    for _ in range(10):
        вперед(5)
        закрасить()
        вправо()
        вперед(3)
        закрасить()
        вправо()
        вперед(2)
        закрасить()
        вправо()
    
    print(len(res))

def task_13851():
    n = {}
    k = [0, 1]
    
    def вперед(x):
        p[0] += k[0]*x
        p[1] += k[1]*x

    def назад(x):
        p[0] -= k[0]*x
        p[1] -= k[1]*x

    def закрасить():
        res.add(tuple(p))

    res = set()
    p = [0, 0]
    for _ in range(11):
        вперед(2)
        закрасить()
        назад(4)
        закрасить()
        вперед(2)
        вперед(2)
    
    print(len(res))

def task_13850():
    colbes = {'A': 0, 'B': 0, 'C': 0}
    mx = {'A': 3, 'B': 5, 'C': 11}
    a, b, c = 'ABC'
    
    def наполни(n):
      colbes[n] = mx[n]

    def вылей(n):
      colbes[n] = 0

    def перелей(a, b):
      if colbes[b] + colbes[a] <= mx[b]:
        colbes[b] += colbes[a]
        colbes[a] = 0
      
      else:
        v = mx[b] - colbes[b]
        colbes[b] = mx[b]
        colbes[a] -= v


    for _ in range(10):
      наполни(a)
      перелей(a, b)
      перелей(a, c)
      наполни(a)
      перелей(a, b)
      перелей(a, c)
      вылей(b)
      перелей(c, b)
    
    print(colbes[c])

def task_13838():
    n = {}
    k = [0, 1]
    
    def вправо():
        k[0], k[1] = k[1], -k[0]

    def влево():
        k[0], k[1] = -k[1], k[0]

    def вперед(x):
        p[0] += k[0]*x
        p[1] += k[1]*x

    def закрасить():
        res.add(tuple(p))

    res = set()
    p = [0, 0]
    for _ in range(10):
        вперед(2)
        закрасить()
        вперед(3)
        вправо()
        вперед(3)
        влево()
        вперед(1)
        закрасить()
        влево()
        вперед(3)
        влево()
    
    print(len(res))

def task_13837():
    n = {}
    k = 0
    for _ in range(7):
      for _ in range(2):
        k += 3
      
      n[k] = not n.get(k, 0)
      k -= 4
      n[k] = not n.get(k, 0)
    
    print(sum(n.values()))

def task_13836():
    n = {}
    k = [0, 1]
    
    def вперед(x):
        p[0] += k[0]*x
        p[1] += k[1]*x

    def назад(x):
        p[0] -= k[0]*x
        p[1] -= k[1]*x

    def закрасить():
        res.add(tuple(p))

    res = set()
    p = [0, 0]
    for _ in range(7):
        for _ in range(2):
            вперед(3)
        
        закрасить()
        назад(4)
        закрасить()
    
    print(len(res))

if __name__ == f"__main__":
    task_13853()
    task_13851()
    task_13850()
    #13847
    #13846
    task_13838()
    task_13837()
    task_13836()