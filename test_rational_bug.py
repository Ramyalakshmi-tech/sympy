#!/usr/bin/env python3
from sympy.core.numbers import Rational

# Test case 1: Using strings - reported as bug
r1 = Rational('0.5', '100')
print(f"Rational('0.5', '100') = {r1}")

# Test case 2: Using floats/ints - correct behavior
r2 = Rational(0.5, 100)
print(f"Rational(0.5, 100) = {r2}")

# Test with similar cases
r3 = Rational('0.1', '10')
print(f"Rational('0.1', '10') = {r3}")

r4 = Rational(0.1, 10)
print(f"Rational(0.1, 10) = {r4}")