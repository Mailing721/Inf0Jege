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