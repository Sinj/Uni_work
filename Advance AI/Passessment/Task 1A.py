import numpy as np
np.set_printoptions(precision=4)
T = np.matrix('0.5 0.5; 0.8 0.2')
print "T = \n", T

Omama = np.matrix('0.4 0; 0 0.1')
print "Omama = \n", Omama

Opapa = Omama
print "Opapa = \n", Opapa

Opee = np.matrix('0.1 0; 0 0.4')
print "Opee = \n", Opee

Opoo = Opee
print "Opoo = \n", Opoo

s0 = np.transpose(np.matrix('0.5 0.5'))
print "s0 = \n", s0

s1 = Omama * np.transpose(T) * s0
print "s1 = \n", s1

s2 = Opapa * np.transpose(T) * s1
print "s2 = \n", s2

s3 = Opee * np.transpose(T) * s2
print "s3 = \n", s3

s4 = Opoo * np.transpose(T) * s3
print "s4 = \n", s4


sum1 = (s4[0] + s4[1])

print "\n sum = \n ", (s4[0] + s4[1])
