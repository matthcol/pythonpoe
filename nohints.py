import numpy as np

def compute(x):
    return 2*x**2 + 1

r1 = compute(12)
print(r1)

r2 = compute(12.2)
print(r2)

# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# r3 = compute("toto")
# r3

x = np.random.normal(10.0, 3.5, 10_000)
r4 = compute(x)
print(r4)