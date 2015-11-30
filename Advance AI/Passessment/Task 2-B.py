# coding=utf-8

import numpy as np


def HMM(Seq, T, count, s):

    s = Seq[count] * T * s
    if count < 3:
        count += 1
        HMM(Seq, T, count, s)
    else:
        print "\n sum = \n ", (s[0] + s[1])


np.set_printoptions(precision=4)  # set the display pre

t = np.transpose(np.matrix('0.75, 0.25; 0.25, 0.75'))



S = np.matrix('0.45 0; 0 0.05')

T = np.matrix('0.05 0; 0 0.45')

O = np.matrix('0 0.05; 0.45 0')

P = np.matrix('0 0.45; 0.05 0')



Seq = np.array([S, T, O, P])


s0 = np.transpose(np.matrix('0.75 0.25'))

HMM(Seq, t, 0, s0)
