## **E27-R Python Error - Understanding Multiplication and Addition Order with SymPy Points**

Bug - [Unexpected exception when multiplying geometry.Point and number #17116](https://github.com/sympy/sympy/issues/17116)

PR - [Implement Point.__rmul__ #17655](https://github.com/sympy/sympy/pull/17655)

---

### **[1] First Pair of Completions**

- **Completion A**
    
    ```diff
    (
      cd "$(git rev-parse --show-toplevel)"
      git apply --3way <<'EOF'
    diff --git a/sympy/geometry/point.py b/sympy/geometry/point.py
    index 7c978c47be..bb06536fdf 100644
    --- a/sympy/geometry/point.py
    +++ b/sympy/geometry/point.py
    @@ -105,6 +105,8 @@ class Point(GeometryEntity):
     
         is_Point = True
     
    +    _op_priority = 11.0
    +
         def __new__(cls, *args, **kwargs):
             evaluate = kwargs.get('evaluate', global_evaluate[0])
             on_morph = kwargs.get('on_morph', 'ignore')
    @@ -278,6 +280,9 @@ def __mul__(self, factor):
             coords = [simplify(x*factor) for x in self.args]
             return Point(coords, evaluate=False)
     
    +    def __rmul__(self, factor):
    +        return self*factor
    +
         def __neg__(self):
             """Negate the point."""
             coords = [-x for x in self.args]
    diff --git a/sympy/geometry/tests/test_point.py b/sympy/geometry/tests/test_point.py
    index 475d1d403f..8f43b053f7 100644
    --- a/sympy/geometry/tests/test_point.py
    +++ b/sympy/geometry/tests/test_point.py
    @@ -27,6 +27,8 @@ def test_point():
         assert (p3 + p4) == p4
         assert (p2 - p1) == Point(y1 - x1, y2 - x2)
         assert p4*5 == Point(5, 5)
    +    assert S(2.0)*p4 == Point(2.0, 2.0)
    +    assert p3 + S(2.0)*p4 == Point(2.0, 2.0)
         assert -p2 == Point(-y1, -y2)
         raises(ValueError, lambda: Point(3, I))
         raises(ValueError, lambda: Point(2*I, I))
    EOF
    )
    ```
    
- **Completion B**
    
    ```diff
    (
      cd "$(git rev-parse --show-toplevel)"
      git apply --3way <<'EOF'
    diff --git a/sympy/geometry/point.py b/sympy/geometry/point.py
    index 7c978c47be..e504568da4 100644
    --- a/sympy/geometry/point.py
    +++ b/sympy/geometry/point.py
    @@ -216,6 +216,15 @@ def __add__(self, other):
             try:
                 s, o = Point._normalize_dimension(self, Point(other, evaluate=False))
             except TypeError:
    +            from sympy.core.mul import Mul
    +            if isinstance(other, Mul) and len(other.args) == 2:
    +                # Try to handle the case where other is a Mul like 2*Point(1, 1)
    +                if isinstance(other.args[1], Point):
    +                    factor, point = other.args
    +                    return self + point * factor
    +                elif isinstance(other.args[0], Point):
    +                    point, factor = other.args
    +                    return self + point * factor
                 raise GeometryError("Don't know how to add {} and a Point object".format(other))
     
             coords = [simplify(a + b) for a, b in zip(s, o)]
    @@ -283,6 +292,26 @@ def __neg__(self):
             coords = [-x for x in self.args]
             return Point(coords, evaluate=False)
     
    +    def __rmul__(self, factor):
    +        """Multiply a factor by this point.
    +
    +        This method is called when a number (or other object) is multiplied
    +        by a Point, as in 2 * Point(1, 2).
    +
    +        Examples
    +        ========
    +
    +        >>> from sympy.geometry import Point
    +        >>> 2 * Point(1, 2)
    +        Point2D(2, 4)
    +
    +        See Also
    +        ========
    +
    +        sympy.geometry.point.Point.__mul__
    +        """
    +        return self.__mul__(factor)
    +
         def __sub__(self, other):
             """Subtract two points, or subtract a factor from this point's
             coordinates."""
    diff --git a/test_point_mul.py b/test_point_mul.py
    new file mode 100644
    index 0000000000..f5263af6ca
    --- /dev/null
    +++ b/test_point_mul.py
    @@ -0,0 +1,29 @@
    +#!/usr/bin/env python
    +from sympy import geometry as ge
    +import sympy
    +
    +def test_point_multiplication():
    +    print("Testing point multiplication...")
    +    point1 = ge.Point(0, 0)
    +    point2 = ge.Point(1, 1)
    +    
    +    # This worked before the fix
    +    result1 = point1 + point2 * sympy.sympify(2.0)
    +    print(f"point1 + point2 * sympy.sympify(2.0) = {result1}")
    +    
    +    # This should now work with our fix
    +    result2 = point1 + sympy.sympify(2.0) * point2
    +    print(f"point1 + sympy.sympify(2.0) * point2 = {result2}")
    +    
    +    # Verify results are equal
    +    print(f"Results are equal: {result1 == result2}")
    +    
    +    # Verify with integers too
    +    result3 = point1 + point2 * 3
    +    result4 = point1 + 3 * point2
    +    print(f"point1 + point2 * 3 = {result3}")
    +    print(f"point1 + 3 * point2 = {result4}")
    +    print(f"Results are equal: {result3 == result4}")
    +
    +if __name__ == "__main__":
    +    test_point_multiplication()
    \ No newline at end of file
    EOF
    )
    ```
    

---

### **[2] Second Pair of Completions**

- **Completion A**
    
    ```diff
    (
      cd "$(git rev-parse --show-toplevel)"
      git apply --3way <<'EOF'
    diff --git a/sympy/geometry/point.py b/sympy/geometry/point.py
    index 7c978c47be..bb06536fdf 100644
    --- a/sympy/geometry/point.py
    +++ b/sympy/geometry/point.py
    @@ -105,6 +105,8 @@ class Point(GeometryEntity):
     
         is_Point = True
     
    +    _op_priority = 11.0
    +
         def __new__(cls, *args, **kwargs):
             evaluate = kwargs.get('evaluate', global_evaluate[0])
             on_morph = kwargs.get('on_morph', 'ignore')
    @@ -278,6 +280,9 @@ def __mul__(self, factor):
             coords = [simplify(x*factor) for x in self.args]
             return Point(coords, evaluate=False)
     
    +    def __rmul__(self, factor):
    +        return self*factor
    +
         def __neg__(self):
             """Negate the point."""
             coords = [-x for x in self.args]
    diff --git a/sympy/geometry/tests/test_point.py b/sympy/geometry/tests/test_point.py
    index 475d1d403f..8f43b053f7 100644
    --- a/sympy/geometry/tests/test_point.py
    +++ b/sympy/geometry/tests/test_point.py
    @@ -27,6 +27,8 @@ def test_point():
         assert (p3 + p4) == p4
         assert (p2 - p1) == Point(y1 - x1, y2 - x2)
         assert p4*5 == Point(5, 5)
    +    assert S(2.0)*p4 == Point(2.0, 2.0)
    +    assert p3 + S(2.0)*p4 == Point(2.0, 2.0)
         assert -p2 == Point(-y1, -y2)
         raises(ValueError, lambda: Point(3, I))
         raises(ValueError, lambda: Point(2*I, I))
    EOF
    )
    ```
    
- **Completion B**
    
    ```diff
    (
      cd "$(git rev-parse --show-toplevel)"
      git apply --3way <<'EOF'
    diff --git a/sympy/geometry/point.py b/sympy/geometry/point.py
    index 7c978c47be..231820a2a9 100644
    --- a/sympy/geometry/point.py
    +++ b/sympy/geometry/point.py
    @@ -278,6 +278,8 @@ def __mul__(self, factor):
             coords = [simplify(x*factor) for x in self.args]
             return Point(coords, evaluate=False)
     
    +    __rmul__ = __mul__
    +
         def __neg__(self):
             """Negate the point."""
             coords = [-x for x in self.args]
    diff --git a/sympy/geometry/tests/test_point.py b/sympy/geometry/tests/test_point.py
    index 475d1d403f..b1bfd66728 100644
    --- a/sympy/geometry/tests/test_point.py
    +++ b/sympy/geometry/tests/test_point.py
    @@ -352,6 +352,12 @@ def test_arguments():
         assert a/10.0 == Point(0, 0.1, evaluate=False)
         a = Point(0, 1)
         assert a*10.0 == Point(0.0, 10.0, evaluate=False)
    +    # reversed multiplication should behave the same
    +    assert 10.0*a == a*10.0
    +    # test addition with reversed multiplication yields same result as forward multiplication
    +    p1 = Point(0, 0)
    +    p2 = Point(1, 1)
    +    assert p1 + p2*2.0 == p1 + 2.0*p2
     
         # test evaluate=False when changing dimensions
         u = Point(.1, .2, evaluate=False)
    EOF
    )
    ```