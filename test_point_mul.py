#!/usr/bin/env python
from sympy import geometry as ge
import sympy

def test_point_multiplication():
    print("Testing point multiplication...")
    point1 = ge.Point(0, 0)
    point2 = ge.Point(1, 1)
    
    # This worked before the fix
    result1 = point1 + point2 * sympy.sympify(2.0)
    print(f"point1 + point2 * sympy.sympify(2.0) = {result1}")
    
    # This should now work with our fix
    result2 = point1 + sympy.sympify(2.0) * point2
    print(f"point1 + sympy.sympify(2.0) * point2 = {result2}")
    
    # Verify results are equal
    print(f"Results are equal: {result1 == result2}")
    
    # Verify with integers too
    result3 = point1 + point2 * 3
    result4 = point1 + 3 * point2
    print(f"point1 + point2 * 3 = {result3}")
    print(f"point1 + 3 * point2 = {result4}")
    print(f"Results are equal: {result3 == result4}")

if __name__ == "__main__":
    test_point_multiplication()