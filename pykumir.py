n = {}
k = 0
for _ in range(11):
    k += 2
    n[k] = 1
    k -= 4
    n[k] = 1
    k += 2
    k += 2
print(sum(n.values()))

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
