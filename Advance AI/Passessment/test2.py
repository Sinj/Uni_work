# coding=utf-8

import numpy as np


def recurse(seq, count, t, m):
    clean = np.max(seq[count][:1])*np.max([t[0,0]*m[0], t[0,1]*m[1]])
    dirty = np.max(seq[count][1:])*np.max([t[1,0]*m[0], t[1,1]*m[1]])
    #print clean
    #print dirty
    if count < 1:
        a = clean/ (clean + dirty)#do once- first form nomral
        dirty = dirty/ (clean + dirty)#do once
        clean = a
    #print clean
    #print dirty
    s0 = np.array([clean, dirty])# needs transpose ? trying with oust
    print s0
    print "\n count = ", count
    count += 1
    if count < 4:
        recurse(Seq, count, t, s0)
    else:
        print round(s0[0],3),round(s0[1],3)


np.set_printoptions(precision=4)  # set the display pre

t = np.transpose(np.matrix('0.5, 0.5; 0.8, 0.2'))


omama = np.matrix('0.4 0; 0 0.1')

opapa = omama

opee = np.matrix('0.1 0; 0 0.4')

opoo = opee
print np.max(opee[:1]), "\n4444bb"
# print np.max(opee[0:1]), "\nbb"
# print np.max(opee[1:]),"ww"

Seq = np.array([omama, omama, opee, opee])
# print np.max(Seq[3][0:1]),"muwa"
# print np.max(Seq[3][1:])

s0 = np.transpose(np.matrix('0.5 0.5'))

recurse(Seq, 0, t, s0)








