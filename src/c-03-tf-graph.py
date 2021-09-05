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
    print(c1.graph)
