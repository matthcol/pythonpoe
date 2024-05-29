import numpy as np

class Shаpe:
    pass


if __name__ == '__main__':
    s1 = Shаpe()
    s2 = Shаpe()
    a = np.zeros((1000, 1000))
    for o in s1, s2, a:
        print(o)
        print(str(o))
        print(repr(o))