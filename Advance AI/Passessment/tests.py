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

clean = 0.4*np.max([0.5*0.5, 0.8*0.5])
dirty = 0.1*np.max([0.5*0.5, 0.2*0.5])
print clean
print dirty
normalization1 = clean/ (clean + dirty)#do once- first form nomral
normalization2 = dirty/ (clean + dirty)#do once
print normalization1
print  normalization2
m1 = np.array([normalization1, normalization2])# needs transpose ? trying with out
print m1
#recusion from here
clean = 0.4*np.max([0.5*m1[0], 0.8*m1[1]])
dirty = 0.1*np.max([0.5*0.5, 0.2*0.5])
print clean
print dirty


#HMM(Seq, t, 0, s0)
