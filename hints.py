import numpy as np

def compute(x: float) -> float:
    return 2*x**2 + 1

r1 = compute(12)
print(r1)

r2 = compute(12.2)
print(r2)

# Execution (duck typing)
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#
# Mypy checker: 
#hints.py:13: error: Argument 1 to "compute" has incompatible type "str"; expected "float"  [arg-type]
# r3 = compute("toto")
# r3

# Mypy checker: 
#hints.py:17: error: Argument 1 to "compute" has incompatible type "ndarray[Any, dtype[floating[_64Bit]]]"; expected "float"  [arg-type]
# x = np.random.normal(10.0, 3.5, 10_000)
# r4 = compute(x)
# print(r4)