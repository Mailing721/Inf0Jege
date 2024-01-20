import functools, sys

sys.setrecursionlimit(10_000_000)

@functools.lru_cache(10_000_000)
def function_f(n: int) -> None:
    if n == 1:
        return 1
        
    else:
        return n + function_f(n - 1)

print(f"###10659###")
n: int
our_list: list[int] = []
for n in range(1, 101):
    if (function_f(2023) // function_f(n)) % 2 == 0:
        our_list.append(n)

print(f"{len(our_list)}")
print(f"#" * 12)