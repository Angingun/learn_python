# 打印杨辉三角


def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]


def main():
    layers = int(input("input layers"))
    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == layers:
            break


if __name__ == "__main__":
    main()
