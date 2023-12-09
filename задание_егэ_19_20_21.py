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


def task_11282() -> None:
    print(f"task 11282")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 273 or y > 3:
                return y == 3
            
            return function(x + 2, y + 1) or function(x + 5, y + 1) or function(x * 4, y + 1)
        
        s : int
        for s in range(1, 273):
            if function(s, 1):
                print(f"task 19: {s}")
                break

    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 273 or y > 4:
                return y == 4
            
            if y % 2 != 0:
                return function(x + 2, y + 1) or function(x + 5, y + 1) or function(x * 4, y + 1)
            
            else:
                return function(x + 2, y + 1) and function(x + 5, y + 1) and function(x * 4, y + 1)
        
        s : int
        for s in range(1, 273):
            if function(s, 1):
                print(f"task 20: {s}")
                      

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 273 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0:
                return function(x + 2, y + 1) or function(x + 5, y + 1) or function(x * 4, y + 1)
            
            else:
                return function(x + 2, y + 1) and function(x + 5, y + 1) and function(x * 4, y + 1)
        
        s : int
        for s in range(1, 273):
            if function(s, 1):
                print(f"task 21: {s}")
                break

    task_19()
    task_20()
    task_21()

def task_11281() -> None:
    print(f"task 11281")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 429:
                return y % 2 == 0
            
            if y == 0:
                return 0
            
            our_function_list: list[int] = [function(x + 5, y - 1), function(x * 5, y - 1)]
            return any(our_function_list) if y % 2 != 0 else all(our_function_list)
      
    
        print(f"task 19: {min(s for s in range(1, 429) if function(s, 2))}")

    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 429 or y > 4:
                return y == 4
            
            if y % 2 != 0: 
                return function(x + 5, y + 1) or function(x * 5, y + 1)
            
            else: 
                return function(x + 5, y + 1) and function(x * 5, y + 1)
      
        s: int
        for s in range(1, 429):
            if function(s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 429 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0: 
                return function(x + 5, y + 1) or function(x * 5, y + 1)
            
            else: 
                return function(x + 5, y + 1) and function(x * 5, y + 1)
      
        s: int
        for s in range(1, 429):
            if function(s, 1):
                print(f"task 21: {s}")
                break

    task_19()
    task_20()
    task_21()

def task_11280() -> None:
    print(f"task 11280")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 199 or y > 3:
                return y == 3
            
            return function(x + 1, y + 1) or function(x + 5, y + 1) or function(x * 3, y + 1)
      
        s: int
        for s in range(1, 199):
            if function(s, 1):
                print(f"task 19: {s}")
                break
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 199 or y > 4:
                return y == 4
            
            if y % 2 != 0: 
                return function(x + 1, y + 1) or function(x + 5, y + 1) or function(x * 3, y + 1)
            
            else: 
                return function(x + 1, y + 1) and function(x + 5, y + 1) and function(x * 3, y + 1)
      
        s: int
        for s in range(1, 199):
            if function(s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 199 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0: 
                return function(x + 1, y + 1) or function(x + 5, y + 1) or function(x * 3, y + 1)
            
            else: 
                return function(x + 1, y + 1) and function(x + 5, y + 1) and function(x * 3, y + 1)
      
        s: int
        for s in range(1, 199):
            if function(s, 1):
                print(f"task 21: {s}")
                break

    task_19()
    task_20()
    task_21()

def task_11279() -> None:
    print(f"task 11279")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 281:
                return y % 2 == 0
            
            if y == 0:
                return 0 
            
            our_function_list: list[int] = [function(x + 4, y - 1), function(x * 2, y - 1)]
            return any(our_function_list) if y % 2 != 0 else all(our_function_list)
      
        print(f"task 19: {min(s for s in range(1, 281) if function(s, 2))}")
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 281 or y > 4:
                return y == 4
            
            if y % 2 != 0: 
                return function(x + 4, y + 1) or function(x * 2, y + 1)
            
            else: 
                return function(x + 4, y + 1) and function(x * 2, y + 1)
      
        s: int
        for s in range(1, 281):
            if function(s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 281 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0: 
                return function(x + 4, y + 1) or function(x * 2, y + 1)
            
            else: 
                return function(x + 4, y + 1) and function(x * 2, y + 1)
      
        s: int
        for s in range(1, 281):
            if function(s, 1):
                print(f"task 21: {s}")
                break

    task_19()
    task_20()
    task_21()

def task_11278() -> None:
    print(f"task 11278")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 449 or z > 3:
                return z == 3
            
            return function(x + 1, y, z + 1) or function(x, y + 1, z + 1) or function(x * 2, y, z + 1) or function(x, y * 2, z + 1)
      
        s: int
        for s in range(1, 436):
            if function(11, s, 1):
                print(f"task 19: {s}")
                break
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 449 or z > 4:
                return z == 4
            
            if z % 2 != 0:
                return function(x + 1, y, z + 1) or function(x, y + 1, z + 1) or function(x * 2, y, z + 1) or function(x, y * 2, z + 1)
            
            else:
                return function(x + 1, y, z + 1) and function(x, y + 1, z + 1) and function(x * 2, y, z + 1) and function(x, y * 2, z + 1)

        s: int
        for s in range(1, 436):
            if function(11, s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 449 or z > 5:
                return z == 3 or z == 5
            
            if z % 2 == 0:
                return function(x + 1, y, z + 1) or function(x, y + 1, z + 1) or function(x * 2, y, z + 1) or function(x, y * 2, z + 1)
            
            else:
                return function(x + 1, y, z + 1) and function(x, y + 1, z + 1) and function(x * 2, y, z + 1) and function(x, y * 2, z + 1)

        s: int
        for s in range(1, 436):
            if function(11, s, 1):
                print(f"task 21: {s}")
                break
    
    task_19()
    task_20()
    task_21()

def task_11275() -> None:
    print(f"task 11275")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 131 or z > 3:
                return z == 3
            
            return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 2, y, z + 1) or function(x, y * 2, z + 1)
      
        s: int
        for s in range(1, 123):
            if function(11, s, 1):
                print(f"task 19: {s}")
                break
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 131 or z > 4:
                return z == 4
            
            if z % 2 != 0:
                return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 2, y, z + 1) or function(x, y * 2, z + 1)
            
            else:
                return function(x + 2, y, z + 1) and function(x, y + 2, z + 1) and function(x * 2, y, z + 1) and function(x, y * 2, z + 1)

        s: int
        for s in range(1, 123):
            if function(11, s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 131 or z > 5:
                return z == 3 or z == 5
            
            if z % 2 == 0:
                return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 2, y, z + 1) or function(x, y * 2, z + 1)
            
            else:
                return function(x + 2, y, z + 1) and function(x, y + 2, z + 1) and function(x * 2, y, z + 1) and function(x, y * 2, z + 1)

        s: int
        for s in range(1, 123):
            if function(11, s, 1):
                print(f"task 21: {s}")
                break
    
    task_19()
    task_20()
    task_21()

def task_11238() -> None:
    print(f"task 11238")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 464:
                return z % 2 == 0
            
            if z == 0:
                return 0
            
            our_function_list: list[int] = [function(x + 2, y, z - 1), function(x, y + 2, z - 1), function(x * 3, y, z - 1), function(x, y * 3, z - 1)]
            return any(our_function_list) if z % 2 != 0 else all(our_function_list)
      
        print(f"task 19: {min(s for s in range(1, 451) if function(s, 13, 2))}")
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 464 or z > 4:
                return z == 4
            
            if z % 2 != 0:
                return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 3, y, z + 1) or function(x, y * 3, z + 1)
            
            else:
                return function(x + 2, y, z + 1) and function(x, y + 2, z + 1) and function(x * 3, y, z + 1) and function(x, y * 3, z + 1)

        s: int
        for s in range(1, 451):
            if function(13, s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x + y >= 464 or z > 5:
                return z == 3 or z == 5
            
            if z % 2 == 0:
                return function(x + 2, y, z + 1) or function(x, y + 2, z + 1) or function(x * 3, y, z + 1) or function(x, y * 3, z + 1)
            
            else:
                return function(x + 2, y, z + 1) and function(x, y + 2, z + 1) and function(x * 3, y, z + 1) and function(x, y * 3, z + 1)

        s: int
        for s in range(1, 451):
            if function(13, s, 1):
                print(f"task 21: {s}")
                break
    
    task_19()
    task_20()
    task_21()

def task_10102() -> None:
    print(f"task 10102")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 129:
                return y % 2 == 0
            
            if y == 0:
                return 0 
            
            our_function_list: list[int] = [function(x + 1, y - 1), function(x * 2, y - 1)]
            return any(our_function_list) if y % 2 != 0 else all(our_function_list)
      
        print(f"task 19: {min(s for s in range(1, 129) if function(s, 2))}")
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 129 or y > 4:
                return y == 4
            
            if y % 2 != 0:
                return function(x + 1, y + 1) or function(x * 2, y + 1)
            
            else:
                return function(x + 1, y + 1) and function(x * 2, y + 1)
      
        s: int
        for s in range(1, 129):
            if function(s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0, z: int = 0) -> int:
            if x >= 129 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0:
                return function(x + 1, y + 1) or function(x * 2, y + 1)
            
            else:
                return function(x + 1, y + 1) and function(x * 2, y + 1)

        s: int
        for s in range(1, 129):
            if function(s, 1):
                print(f"task 21: {s}")
                break
    
    task_19()
    task_20()
    task_21()

def task_9842() -> None:
    print(f"task 9842")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 111:
                return y % 2 == 0
            
            if y == 0:
                return 0 
            
            our_function_list: list[int] = [function(x + 1, y - 1), function(x + 3, y - 1), function(x * 4, y - 1)]
            return any(our_function_list) if y % 2 != 0 else all(our_function_list)
      
        print(f"task 19: {min(s for s in range(1, 111) if function(s, 2))}")
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 111 or y > 4:
                return y == 4
            
            if y % 2 != 0:
                return function(x + 1, y + 1) or function(x + 3, y + 1) or function(x * 4, y + 1)
            
            else:
                return function(x + 1, y + 1) and function(x + 3, y + 1) and function(x * 4, y + 1)
      
        s: int
        for s in range(1, 111):
            if function(s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 111 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0:
                return function(x + 1, y + 1) or function(x + 3, y + 1) or function(x * 4, y + 1)
            
            else:
                return function(x + 1, y + 1) and function(x + 3, y + 1) and function(x * 4, y + 1)
      
        s: int
        for s in range(1, 111):
            if function(s, 1):
                print(f"task 21: {s}")
                break
    
    task_19()
    task_20()
    task_21()

def task_9788() -> None:
    print(f"task 9788")
    def task_19() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 59:
                return y % 2 == 0
            
            if y == 0:
                return 0 
            
            our_function_list: list[int] = [function(x + 1, y - 1), function(x + 3, y - 1), function(x * 4, y - 1)]
            return any(our_function_list) if y % 2 != 0 else all(our_function_list)
      
        print(f"task 19: {min(s for s in range(1, 59) if function(s, 2))}")
    
    def task_20() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 59 or y > 4:
                return y == 4
            
            if y % 2 != 0:
                return function(x + 1, y + 1) or function(x + 3, y + 1) or function(x * 4, y + 1)
            
            else:
                return function(x + 1, y + 1) and function(x + 3, y + 1) and function(x * 4, y + 1)
      
        s: int
        for s in range(1, 59):
            if function(s, 1):
                print(f"task 20: {s}")

    def task_21() -> None:
        @memorise
        def function(x: int = 0, y: int = 0) -> int:
            if x >= 59 or y > 5:
                return y == 3 or y == 5
            
            if y % 2 == 0:
                return function(x + 1, y + 1) or function(x + 3, y + 1) or function(x * 4, y + 1)
            
            else:
                return function(x + 1, y + 1) and function(x + 3, y + 1) and function(x * 4, y + 1)
      
        s: int
        for s in range(1, 59):
            if function(s, 1):
                print(f"task 21: {s}")
                break
    
    task_19()
    task_20()
    task_21()

if __name__ == f"__main__":
    task_11282()
    task_11281()
    task_11280()
    task_11279()
    task_11278()
    task_11275()
    task_11238()
    task_10102()
    task_9842()
    task_9788()