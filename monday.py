import numpy as np

class Shape:
    pass


if __name__ == '__main__':
    s1 = Shape()
    s2 = Shape()
    a = np.zeros((1000, 1000))
    for o in s1, s2, a:
        print(o)
        print(str(o))
        print(repr(o))