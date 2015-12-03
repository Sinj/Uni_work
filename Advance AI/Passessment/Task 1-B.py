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
#       P(b)        P(J|A)      P(M|A)        P(E)     P(A|B,E)     +    P(B)     P(J|A)      P(M|A)      P(¬E)         P(A|B,¬E)     +  P(B)        P(J|¬A)     P(M|¬A)        P(E)      P(¬A|B,E)   +  P(b)        P(J|¬A)    P(M|¬A)     P(¬E)           P(¬A|B,¬E)
BJM = (Burglary * john[0,0] * mary[0,0] * Earthquake * alarms[0,0]) + (Burglary * john[0,0] * mary[0,0] * N_Earthquake * alarms[1,0]) + (Burglary * john[1,0] * mary[1,0] * Earthquake * alarms[0,1]) + (Burglary * john[1,0] * mary[1,0] * N_Earthquake * alarms[1,1])

#       P(¬b)        P(J|A)      P(M|A)        P(E)        P(A|¬B,E)    |    P(¬B)      P(J|A)      P(M|A)      P(¬E)         P(A|¬B,¬E)    |  P(¬B)        P(J|¬A)     P(M|¬A)        P(E)      P(¬A|¬B,E)   |  P(¬b)        P(J|¬A)    P(M|¬A)     P(¬E)           P(¬A|¬B,¬E)
N_BJM = (N_Burglary * john[0,0] * mary[0,0] * Earthquake * alarms[2,0]) + (N_Burglary * john[0,0] * mary[0,0] * N_Earthquake * alarms[3,0]) + (N_Burglary * john[1,0] * mary[1,0] * Earthquake * alarms[2,1]) + (N_Burglary * john[1,0] * mary[1,0] * N_Earthquake * alarms[3,1])

print "BJM = ",BJM, "\nN_BJM = ",N_BJM
alpha = 1 / (BJM + N_BJM)
print "alpha = ",alpha

BJM = alpha * BJM
N_BJM = alpha * N_BJM
print "P(B|J,M) = ",round(BJM,3) ,"\nP(¬B|J,M) = ",round(N_BJM,3) , "\nprove that both are correct by adding P(B|J,M) and P(¬B|J,M) should make 1 \nP(B|J,M) + P(¬B|J,M) = ",BJM + N_BJM


