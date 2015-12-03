# coding=utf-8

import numpy as np


def HMM(Seq, T, count, s):
    s = Seq[count] * T * s
    print "s", count + 1, " =\n", s
    if count < 3:
        count += 1
        HMM(Seq, T, count, s)
    else:
        print "\ns4(0) + s4(1) = \n ", (s[0] + s[1])
        os = (s[0] + s[1])
        print "The probability of observing the sequence S-T-O-P is", os


np.set_printoptions(precision=4)  # set the printing of floats to 4 decimal places

t = np.transpose(np.matrix('0.75, 0.25;'  # transition
                           '0.25, 0.75'))
# emission
S = np.matrix('0.45 0;'
              '0 0.05')

P = np.matrix('0 0.45;'
              '0.05 0')

O = np.matrix('0 0.05;'
              '0.45 0')

T = np.matrix('0.05 0;'
              '0 0.45')

s0 = np.transpose(np.matrix('0.75 0.25'))  # starting matrix

Seq = np.array([S, T, O, P])  # seqance of intreast

HMM(Seq, t, 0, s0)
