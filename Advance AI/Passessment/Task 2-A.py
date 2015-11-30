# coding=utf-8

import numpy as np


def HMM(Seq, T, count, s):
    # print Seq[count], "\n print ", count
    s = Seq[count] * T * s
    if count < 3:
        count += 1
        # print count
        HMM(Seq, T, count, s)
    else:
        print "\n sum = \n ", (s[0] + s[1])


np.set_printoptions(precision=4)  # set the display pre
# T = np.transpose(np.matrix('0.5 0.5; 0.8 0.2'))
t = np.transpose(np.matrix('0.75, 0.25; 0.25, 0.75'))

# print "T = \n", T

S = np.matrix('0.45 0; 0 0.05')

T = np.matrix('0.05 0; 0 0.45')

O = np.matrix('0 0.05; 0.45 0')

P = np.matrix('0 0.45; 0.05 0')

# Omama = np.matrix('0.4 0; 0 0.1')
# print "Omama = \n", Omama

# Opapa = Omama
# print "Opapa = \n", Opapa

# Opee = np.matrix('0.1 0; 0 0.4')
# print "Opee = \n", Opee

# Opoo = Opee
# print "Opoo = \n", Opoo

Seq = np.array([S, T, O, P])
# Seq = np.array([Omama, Opapa, Opee, Opoo])
# print Seq[0], "test"
# print Seq

s0 = np.transpose(np.matrix('0.75 0.25'))
# s0 = np.transpose(np.matrix('0.5 0.5'))

# print "s0 = \n", s0

# s1 = Omama * T * s0
# print "s1 = \n", s1

# s2 = Opapa * T * s1
# print "s2 = \n", s2

# s3 = Opee * T * s2
# print "s3 = \n", s3

# s4 = Opoo * T * s3
# print "s4 = \n", s4

# sum1 = (s4[0] + s4[1])

# print "\n sum = \n ", (s4[0] + s4[1])
HMM(Seq, t, 0, s0)
