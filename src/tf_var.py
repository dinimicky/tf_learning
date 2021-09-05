# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 3:26 下午
# @Author  : kaiji@xiaohongshu.com
# @File    : tf_var.py
# @Software: IntelliJ IDEA


import tensorflow as tf

var1 = tf.Variable(1.0, name='firstvar')
print("var1:", var1.name)

var1 = tf.Variable(2.0, name='firstvar')
print("var1:", var1.name)
var2 = tf.Variable(3.0, )
print("var2:", var2.name)
var2 = tf.Variable(4.0, )
print("var2:", var2.name)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("var1:", var1.eval())
    print("var2:", var2.eval())

get_var1 = tf.get_variable("firstvar", [1], initializer=tf.constant_initializer(0.3))
print("get_var1:", get_var1.name)
'''
再次运行会报错, get_variable 只能定义一次指定名称的变量, 
get_var1 = tf.get_variable("firstvar", [1], initializer=tf.constant_initializer(0.4))
print("get_var1:", get_var1.name)

'''

with tf.variable_scope("test1"):
    var1 = tf.get_variable("firstvar", shape=[2], dtype=tf.float32)

with tf.variable_scope("test2"):
    var2 = tf.get_variable("firstvar", shape=[2], dtype=tf.float32)

print("var1:", var1.name)
print("var2:", var2.name)

with tf.variable_scope("test1"):
    var1 = tf.get_variable("secondvar", shape=[2], dtype=tf.float32)

    with tf.variable_scope("test2"):
        var2 = tf.get_variable("secondvar", shape=[2], dtype=tf.float32)

print("var1:", var1.name)
print("var2:", var2.name)

with tf.variable_scope("test1", reuse=True):
    var3 = tf.get_variable("secondvar", shape=[2], dtype=tf.float32)

    with tf.variable_scope("test2"):
        var4 = tf.get_variable("secondvar", shape=[2], dtype=tf.float32)

print("var3:", var1.name)
print("var4:", var2.name)

with tf.variable_scope("test1", initializer=tf.constant_initializer(0.4)):
    var1 = tf.get_variable("thirdvar", shape=[2], dtype=tf.float32)

    with tf.variable_scope("test2"):
        var2 = tf.get_variable("thirdvar", shape=[2], dtype=tf.float32)
        var3 = tf.get_variable("var3", shape=[2], initializer=tf.constant_initializer(0.3))

print("var1:", var1.name)
print("var2:", var2.name)
print('var3:', var3.name)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("var1:", var1.eval())
    print("var2:", var2.eval())
    print("var3:", var3.eval())

with tf.variable_scope("scope1") as sp:
    var1 = tf.get_variable("v", [1])

print('var1:', var1.name)
print("sp:", sp.name)

with tf.variable_scope("scope2"):
    var2 = tf.get_variable("v", [1])

    with tf.variable_scope(sp) as sp1:
        var3 = tf.get_variable("v3", [1])

print("sp1:", sp1.name)
print("var2:", var2.name)
print("var3:", var3.name)

with tf.variable_scope("scope"):
    with tf.name_scope("bar"):
        v = tf.get_variable("v", [1])
        x = 1.0 + v

print("v:", v.name)
print("x.op", x.op.name)

with tf.variable_scope("scope"):
    var2 = tf.get_variable("v2", [1])
    with tf.variable_scope(sp) as sp1:
        var4 = tf.get_variable("v4", [1])
        with tf.variable_scope(""):
            var5 = tf.get_variable("v5", [1])
print("var2:", var2.name)
print("var4:", var4.name)
print("var5:", var5.name)

with tf.variable_scope("scope4"):
    v7 = tf.get_variable("v7", [1])
    z = 1.0 + v7
    with tf.name_scope("bar"):
        v6 = tf.get_variable("v6", [1])
        x = 1.0 + v6
        with tf.name_scope(""):
            y = 1.0 + v7

print("v7:", v7.name)
print("z.op", z.op.name)
print("v6:", v6.name)
print("x.op:", x.op.name)
print("y.op:", y.op.name)
