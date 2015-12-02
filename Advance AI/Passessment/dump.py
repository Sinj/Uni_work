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
count = 0
#def Alg(Seq, count, t, s0):
clean = Seq[count][0][0]*np.max([t[0,0]*s0[0], t[0,1]*s0[1]])
dirty = Seq[count][1][1]*np.max([t[1,0]*s0[0], t[1,1]*s0[1]])
print clean
print dirty
if count < 1:
    a = clean/ (clean + dirty)#do once- first form nomral
    dirty = dirty/ (clean + dirty)#do once
    clean = a
print clean
print dirty
s0 = np.array([clean, dirty])# needs transpose ? trying with oust
print s0
count += 1

#recusion from here
clean = Seq[count][0][0]*np.max([t[0,0]*s0[0], t[0,1]*s0[1]])
dirty = Seq[count][1][1]*np.max([t[1,0]*s0[0], t[1,1]*s0[1]])
print clean
print dirty
s0 = np.array([clean, dirty])
print s0
count += 1
#--
clean = Seq[count][0][0]*np.max([t[0,0]*s0[0], t[0,1]*s0[1]])
dirty = Seq[count][1][1]*np.max([t[1,0]*s0[0], t[1,1]*s0[1]])
print clean
print dirty
s0 = np.array([clean, dirty])
#print s0
count += 1
#---
clean = Seq[count][0][0]*np.max([t[0,0]*s0[0], t[0,1]*s0[1]])
dirty = Seq[count][1][1]*np.max([t[1,0]*s0[0], t[1,1]*s0[1]])
print clean
print dirty
s0 = np.array([clean, dirty])
print round(s0[0],3),round(s0[1],3)


#HMM(Seq, t, 0, s0)
#def Alg(Seq, count, s0 ,t):
