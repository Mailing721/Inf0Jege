from tkinter import filedialog
import functools

@functools.cache
def main() -> None:
    with open(filedialog.askopenfilename(), f"r+", encoding=f"UTF-8") as file:
        a: str = file.read()
        c: str = f""
        k: list[str] = []
        i: str
        for i in a:
            if c.count(f"y") <= 150:
                c = c + i

            else:
                k.append(len(c))
                c = f""
        
        print(f"{max(k)}")

if __name__ == f"__main__":
    main()