import pytest
import sympy
from  utf.tf import tf, s

tf_empty = tf([],[])
t_num_empty = tf([],[1])
t_num_zero = tf([0],[1])
t_den_empty = tf([1],[])
t_den_empty2 = tf([2, 1], [])
t_den_empty0 = tf([2, 0], [])
t11 = tf([1], [3])
t12 = tf([1],[2,3])
t22 = tf([2,3],[3,4])
t23 = tf([1,2],[2,3,4])
t13 = tf([1],[2,3,4])
t102 = tf([1],[2,0])
t202 = tf([2,3],[3,0])
t0202 = tf([2,0],[3,0])
t103 = tf([1],[2,0,4])
tneg = tf([-1],[1])
#test negative numbers

def test_constructor():
    assert 1 == 1

def test_get_tf():
    assert tf_empty.get_tf() == 0
    assert t_num_empty.get_tf() == 0
    assert t_num_zero.get_tf() == 0

    assert t_den_empty.get_tf() == 1
    assert t_den_empty2.get_tf() == 2*s + 1
    assert t_den_empty0.get_tf() == 2*s
    assert t11.get_tf() == sympy.Rational(1,3)
    assert t12.get_tf() == 1/(2*s + 3)
    assert t22.get_tf() == (2*s + 3)/(3*s + 4)
    assert t23.get_tf() == (s + 2)/(2*s**2 + 3*s + 4)
    assert t13.get_tf() == 1/(2*s**2 + 3*s + 4)
    assert t102.get_tf() == 1/(2*s)
    assert t202.get_tf() == (2*s + 3)/(3*s)
    assert t0202.get_tf() == (2*s)/(3*s)
    assert t103.get_tf() == 1/(2*s**2 + 4)

    assert tneg.get_tf() == -1

def test_str_to_tf():
    assert t11.str_to_tf("s") == tf([1, 0])