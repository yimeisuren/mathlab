import numpy as np


def l_n(x: np.ndarray, newX: np.ndarray):
    return np.max(np.abs(newX - x))


def l_2(x: np.ndarray, newX: np.ndarray):
    return np.sqrt(np.sum(np.square(newX - x)))


def jacobi(A, x, b, distance, e, k=1e4):
    # 规范化, 否则溢出
    # maxA = np.max(A, axis=1).reshape(-1, 1)
    # maxB = np.max(b)
    # A = A / maxA
    #
    # b = b / maxB

    a = []
    for i in range(len(A)):
        a.append(A[i][i])
    a = np.array(a)

    result = []
    i = 0
    while True:
        newX = (b - np.dot(x, A.T) - a * x) / a
        d = distance(x, newX)
        if d < e or i > k:
            break
        x = newX
        result.append(x)
        i += 1
    return result


A = np.array([[5, 2, 3], [-1, 4, 2], [2, -3, 10]])
b = np.array([[-12], [20],[3]])
x0 = np.array([0.0, 0.0, 0.0])
distance = l_n
e = 1e-4

xlist = jacobi(A, x0, b, distance, e)
print(xlist)
