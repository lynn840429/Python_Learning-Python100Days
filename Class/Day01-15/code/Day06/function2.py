"""
函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""

### gcd M1
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1

print(gcd(15, 27))

### gcd M2
import math

print(math.gcd(15, 27))

### gcd M3
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

print(computeGCD(15, 27))

### lcm
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(15, 27))
