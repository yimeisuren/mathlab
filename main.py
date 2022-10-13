def simple_iteration(x, e, func):
    i = 0
    while True:
        i += 1
        newX = func(x)
        if abs(newX - x) < e:
            return i, newX
        x = newX


def f2(x):
    return 1 / (x ** 2 - 1)


i, x = simple_iteration(2, 1e-10, f2)
print(f"迭代次数:{i}, 结果:{x}")
