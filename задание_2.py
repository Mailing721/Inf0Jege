def main() -> None:
    print(f"x y z w")
    x: int
    y: int
    z: int
    w: int
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((x or (not(y))) and (not(x == z)) and w):
                        print(f"{x} {y} {z} {w}")

if __name__ == f"__main__":
    main()