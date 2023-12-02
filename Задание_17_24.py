import functools, os, sys, tkinter.filedialog

def main() -> None:
    with open(tkinter.filedialog.askopenfilename()) as file:
        a: list[int] = [int(x) for x in file.readlines()]
        mk: list[int] = max([x for x in a if x % 17 == 0])
        i: int
        count: int = 0
        ms: list[int] = []
        for i in range(len(a)-1):
            if a[i] + a[i + 1] > mk:
                count += 1
                ms.append(a[i] + a[i + 1])

    print(count, max(ms))

if __name__ == f"__main__":
    main()