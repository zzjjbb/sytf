import tensorflow as tf
import numpy as np

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(np.array([1, 1, 2]))
print(sess.run(hello))
