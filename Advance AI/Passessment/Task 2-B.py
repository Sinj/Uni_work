# coding=utf-8

import numpy as np


def recurse(seq, count, t, m, path):
    zero = np.max(seq[count][:1]) * np.max([t[0, 0] * m[0], t[0, 1] * m[1]])
    one = np.max(seq[count][1:]) * np.max([t[1, 0] * m[0], t[1, 1] * m[1]])
    if count < 1:
        a = zero / (zero + one)  # do once- first form nomral
        one = one / (zero + one)
        zero = a
    m = np.array([zero, one])
    print m
    if zero ==  one:
        path += ["both"]
        print
    elif zero > one:
        path +=[0]
    else:
        path +=[1]
    print "\n count = ", count
    count += 1
    if count < 4:
        recurse(Seq, count, t, m, path)
    else:
        print round(m[0], 6), round(m[1], 6)
        print "path taken: ",path

np.set_printoptions(precision=4)  # set the display pre

t = np.transpose(np.matrix('0.75, 0.25;'
                           '0.25, 0.75'))

S = np.matrix('0.45 0; '
              '0 0.05')

T = np.matrix('0.05 0; '
              '0 0.45')

O = np.matrix('0 0.05;'
              '0.45 0')

P = np.matrix('0 0.45; '
              '0.05 0')

Seq = np.array([S, T, O, P])

s0 = np.transpose(np.matrix('0.75 0.25'))
path = []
recurse(Seq, 0, t, s0, path)
