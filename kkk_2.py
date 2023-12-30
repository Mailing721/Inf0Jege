import functools

def memorise(function_param: str) -> str:

    cache: dict = {}

    @functools.wraps(function_param)
    def wrapper(*args, **kwargs) -> str:
        key: str = str(args) + str(kwargs)
        if key not in cache:
            cache[key]: function = function_param(*args, **kwargs)

        return cache[key]
    
    return wrapper

@memorise
def main() -> None:
    def triangle(x, y, z):
        return x + y > z

    def max(x, y):
        if x > y:
            return x

        else:
            return y

    def f(x,a):
        return not((triangle(x, 11, 18) == (not(max(x, 5) > 68))) and triangle(x, a, 5))

    for a in range(1,1000000):
        if all(f(x,a) for x in range(1,1000000)):
            print(a)

if __name__ == f"__main__":
    main()