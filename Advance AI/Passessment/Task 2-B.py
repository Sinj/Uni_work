# coding=utf-8

import numpy as np


def recurs (seq, count, t, m, path):
    zero = np.max(seq[count][:1]) * np.max([t[0, 0] * m[0], t[0, 1] * m[1]])
    one = np.max(seq[count][1:]) * np.max([t[1, 0] * m[0], t[1, 1] * m[1]])
    if count < 1:
        a = zero / (zero + one)  # do once- first normal form
        one = one / (zero + one)
        zero = a
    m = np.array([zero, one])# store the values to m
    print "m",count+1," \n",m
    #save the path
    if zero ==  one:
        path += ["both"]
    elif zero > one:
        path +=[0]
    else:
        path +=[1]
    if count < 3:
        count += 1
        recurs(Seq, count, t, m, path)
    else:
        print "sequence of hidden states: ",path
        if zero ==  one:
            print round(m[0], 6), round(m[1], 6)
        else:
            print "probability: ", round(np.max(m), 6)


np.set_printoptions(precision=4)  # set the display pre

t = np.transpose(np.matrix('0.75, 0.25;'  # transition
                           '0.25, 0.75'))
# emission
S = np.matrix('0.45 0; '
              '0 0.05')

T = np.matrix('0.05 0; '
              '0 0.45')

O = np.matrix('0 0.05;'
              '0.45 0')

P = np.matrix('0 0.45; '
              '0.05 0')

Seq = np.array([S, T, O, P])#seqance of instreast

s0 = np.transpose(np.matrix('0.75 0.25'))#starting matrix
path = []
recurs(Seq, 0, t, s0, path)
