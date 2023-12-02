def f(n,k):
    if k>12:
        return set()
    return {n} | f(n+1,k+1) | f(n-1,k+1)
print(len(f(1,0)))
