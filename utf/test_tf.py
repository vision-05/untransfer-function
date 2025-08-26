import pytest
import utf.tf as tf

tf_empty = tf.tf([],[])
t_num_empty = tf.tf([],[1])
t_num_zero = tf.tf([0],[1])
t_den_empty = tf.tf([1],[])
t_den_zero = tf.tf([1],[0])
t_ints = tf.tf(1,3)
t_str = tf.tf("1","3")
t_str_list = tf.tf(["1"],["3"])
t11 = tf.tf([1], [3])
t12 = tf.tf([1],[2,3])
t22 = tf.tf([2,3],[3,4])
t23 = tf.tf([1,2],[2,3,4])
t13 = tf.tf([1],[2,3,4])
t102 = tf.tf([1],[2,0])
t202 = tf.tf([2,3],[3,0])
t0202 = tf.tf([2,0],[3,0])
t103 = tf.tf([1],[2,0,4])
#test zeros in num + denominator

def test_tf_to_str():
    assert tf_empty.tf_to_str() == "0"
    assert t_num_empty.tf_to_str() == "0"
    assert t_num_zero.tf_to_str() == "0"
    with pytest.raises(ZeroDivisionError):
        assert t_den_empty.tf_to_str()
        assert t_den_zero.tf_to_str()
        assert t_str.tf_to_str()
        assert t_str_list.tf_to_str()

    assert t_ints.tf_to_str() == "1\n-------\n3"
    assert t11.tf_to_str() == "1\n-------\n3"
    assert t12.tf_to_str() == "1\n-------\n2s + 3"
    assert t22.tf_to_str() == "2s + 3\n-------\n3s + 4"
    assert t23.tf_to_str() == "s + 2\n-------\n2s^2 + 3s + 4"
    assert t13.tf_to_str() == "1\n-------\n2s^2 + 3s + 4"
    assert t102.tf_to_str() == "1\n-------\n2s"
    assert t202.tf_to_str() == "2s + 3\n-------\n3s"
    assert t0202.tf_to_str() == "2s\n-------\n3s"

def test_str_to_tf():
    assert t11.str_to_tf("s") == tf([1, 0])