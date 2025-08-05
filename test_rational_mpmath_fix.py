#!/usr/bin/env python3

from sympy import symbols, Eq, S, rf, Float
from sympy.utilities.lambdify import lambdify
import inspect
import mpmath

def test_rational_mpmath():
    x = symbols('x')
    # Original example from the issue
    eqn = Eq(rf(18, x), 77 + S(1)/3)
    
    # Print the generated lambda source before the fix
    print("Before fix:")
    f = lambdify(x, eqn.lhs - eqn.rhs, 'mpmath')
    print(inspect.getsource(f))
    
    # Solve the equation with nsolve and check precision
    mpmath.mp.dps = 64  # Set high precision
    x0 = 1.5  # Initial guess
    result = mpmath.findroot(f, x0)
    print(f"Solution: {result}")
    
    # Check the result precision
    rf_result = mpmath.rf(18, result)
    expected = mpmath.mpf(77) + mpmath.mpf(1)/mpmath.mpf(3)
    print(f"rf(18, x) = {rf_result}")
    print(f"77 + 1/3 = {expected}")
    print(f"Difference: {abs(rf_result - expected)}")
    
    return rf_result, expected, abs(rf_result - expected)

if __name__ == "__main__":
    rf_result, expected, diff = test_rational_mpmath()
    if diff < 1e-30:
        print("TEST PASSED: High precision maintained")
    else:
        print("TEST FAILED: Precision issue remains")