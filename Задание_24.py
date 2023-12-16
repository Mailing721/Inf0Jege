from tkinter import filedialog

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
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: str = file.read()
        a = a.split(f"Y")
        i: int
        d: list[str] = []
        for i in range(len(a) - 151):
            c: str = f"Y".join(a[i:i+151])
            d.append(len(c))

        print(f"{max(d)}")
        
if __name__ == f"__main__":
    main()
