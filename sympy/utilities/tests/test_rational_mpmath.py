#!/usr/bin/env python3

from sympy import symbols, Eq, S, rf, Float, Rational
from sympy.utilities.lambdify import lambdify
import inspect
import mpmath
from sympy.utilities.decorator import conserve_mpmath_dps

def test_rational_mpmath_lambdify():
    """Test that rational numbers maintain precision with mpmath lambdify."""
    x = symbols('x')
    
    # Test with the example from the issue
    eqn = Eq(rf(18, x), 77 + S(1)/3)
    f = lambdify(x, eqn.lhs - eqn.rhs, 'mpmath')
    
    # Check that the source code contains mpf wrapped rationals
    source = inspect.getsource(f)
    assert "mpf(" in source
    
    with conserve_mpmath_dps():
        mpmath.mp.dps = 50
        # Test a simple expression with a rational
        expr = Rational(1, 3)
        f = lambdify(x, expr, 'mpmath')
        result = f(0)
        expected = mpmath.mpf(1) / mpmath.mpf(3)
        assert abs(result - expected) < 1e-49
        
        # Test a more complex expression with rationals
        expr = Rational(2, 5) * x + Rational(3, 7)
        f = lambdify(x, expr, 'mpmath')
        result = f(mpmath.mpf(1.5))
        expected = mpmath.mpf(2)/mpmath.mpf(5) * mpmath.mpf(1.5) + mpmath.mpf(3)/mpmath.mpf(7)
        assert abs(result - expected) < 1e-49