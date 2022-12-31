import taichi as ti
ti.init(arch=ti.cpu,default_ip=ti.i64, default_fp=ti.f64)

@ti.func
def inv_square(x):  # A Taichi function
    a = ti.f64(x)
    return 1.0 / (a * a)

@ti.kernel
def partial_sum(n:int) -> float:  # A kernel
    total = 0.0
    for i in range(1, n+1):
        a = inv_square(i)
        if a < 0:
            print(a)
        total += inv_square(i)
    return total

print(partial_sum(100000000))


import tensorflow as tf
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b) 

@ti.kernel
def taichi_add(a:int, b:int) -> int:
    return tf.add(a, b)

with tf.Session() as sess:
    # Run every operation with variable input
    print ("相加: %i" % sess.run(add, feed_dict={a: 3, b: 4}))
    print ("相乘: %i" % sess.run(mul, feed_dict={a: 3, b: 4}))
    print ("太极相加: %i" % sess.run(taichi_add, feed_dict={a: 3, b: 4}))