import classes

tf_empty = classes.tf([],[])
tf = classes.tf([1], [3, 2])

def test_tf_to_str():
    assert tf.tf_to_str() == "1/3s^1 + 2s^0"

def test_str_to_tf():
    assert classes.tf.str_to_tf("s") == tf([1, 0])