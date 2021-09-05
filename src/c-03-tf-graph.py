# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 4:15 下午
# @Author  : kaiji@xiaohongshu.com
# @File    : c-03-tf-graph.py
# @Software: IntelliJ IDEA

import numpy as np
import tensorflow as tf

c = tf.constant(0.0)
g = tf.Graph()

with g.as_default():
    c1 = tf.constant(0.0)
    print("c1 graph:", c1.graph)
    print("g graph:", g)
    print("c graph:", c.graph)
    print("get default graph:", tf.get_default_graph())

g2 = tf.get_default_graph()
print("g2 graph:", g2)

tf.reset_default_graph()
g3 = tf.get_default_graph()
print("g3 graph:", g3)

print('c1 name:', c1.name, c1)
t = g.get_tensor_by_name(name="Const:0")
print('t:', t)

a = tf.constant([[1.0, 2.0]])
b = tf.constant([[1.0], [3.0]])

tensor1 = tf.matmul(a, b, name='exampleop')
print("tensor1:", tensor1.name, tensor1)

test = g3.get_tensor_by_name("exampleop:0")
print("test:", test)
print("tensor1.op:", tensor1.op.name)
testop = g3.get_operation_by_name("exampleop")
print("testop:", testop)
tt2 = g.get_operations()
print("g graph all operations:", tt2)

tt3 = g.as_graph_element(c1)
print('g graph element c1:', tt3)
with tf.Session() as sess:
    test = sess.run(test)
    print("test:", test)
    test = tf.get_default_graph().get_tensor_by_name("exampleop:0")
    print("test:", test)
