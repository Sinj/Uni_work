# coding=utf-8
import numpy as np
np.set_printoptions(precision=5)
Disease = 0.0

Disease = np.float(1/10000)#
N_Disease = 1 - Disease

print Disease

Disease = 1 / 10000;  # P(D)
N_Disease = 1 - Disease  # P(¬D)
T_D = 0.99  # P(T|D)
NT_D = 0.01  # P(¬T|D)
NT_ND = 0.95  # P(¬T|¬D)
T_ND = 0.05  # P(T|¬D)
#                    T     ¬T
D_table = np.matrix('0.99 0.01;'   # D
                    ' 0.05 0.95')  # ¬D
print D_table[1, 0]

# Find T
Test = D_table[0, 0] * Disease + D_table[1, 0] * Disease
print Test
Test1 = T_D * Disease + T_ND * Disease
print Test1
# Find T

# Test; //P(T)
# n_Test; //P(¬T)
