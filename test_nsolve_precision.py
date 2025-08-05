#!/usr/bin/env python3

from sympy import symbols, Eq, S, rf, Float, nsolve
import mpmath

x = symbols('x')

# Original example from the issue
eqn = Eq(rf(18, x), 77 + S(1)/3)

# Solve with nsolve at high precision
x0 = Float('1.5', 64)  # Initial guess
result = nsolve(eqn, x, x0, prec=64)

# Check the result precision
rf_result = rf(18, result).evalf(64)
expected = (77 + S(1)/3).evalf(64)

print(f"rf(18, x) = {rf_result}")
print(f"77 + 1/3 = {expected}")
print(f"Difference: {abs(rf_result - expected).evalf(64)}")