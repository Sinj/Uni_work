# coding=utf-8

import numpy as np

Burglary = 0.001
N_Burglary = 1 - Burglary
Earthquake = 0.002
N_Earthquake = 1 - Earthquake

#                   A      ¬A
alarms = np.matrix('0.95 0.05;'  # B  E
                   '0.94 0.06;'  # B  ¬E
                   '0.29 0.71;'  # ¬B E
                   '0.001 0.999')  # ¬B ¬E

#                   J   ¬J
john = np.matrix('0.9 0.1;' #A
                 '0.05 0.95')#¬A

#                   M   ¬M
mary = np.matrix('0.7 0.3;'#A
                 '0.01 0.99')#¬A

BJM = Burglary * john[0,0] * mary[0,0] * Earthquake * alarms[0,0]#not b not e
N_BJM = N_Burglary * john[0,0] * mary[0,0] * Earthquake * alarms[2,0]

print "BJM = ", BJM,"\nN_BJM = ",N_BJM
#a being the B + everthing
#b being ¬b
#alptha = 1/a+b

print "boo"


print BJM + N_BJM
