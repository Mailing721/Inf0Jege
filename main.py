import functools, sys

sys.setrecursionlimit(999_999_999)

@functools.lru_cache(maxsize=999_999_999)
def function_f(n):
    if n >= 2025:
        return n
        
    else:
        return function_f(n + 1) - function_f(n + 2) + 7


print(function_f(15) - function_f(24))