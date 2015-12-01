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

t = np.transpose(np.matrix('0.5, 0.5; 0.8, 0.2'))



omama = np.matrix('0.4 0; 0 0.1')

opapa = omama

opee = np.matrix('0.1 0; 0 0.4')

opoo = opee



Seq = np.array([omama, omama, opee, opee])


s0 = np.transpose(np.matrix('0.5 0.5'))

HMM(Seq, t, 0, s0)
