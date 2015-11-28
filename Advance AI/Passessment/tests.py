# coding=utf-8
import numpy

Disease = 1 / 10000
N_Disease = 1 - Disease

t_d = 0.99  # P(T|D)
nt_d = 0.01  # P(¬T|D)
nt_nd = 0.95  # P(¬T|¬D)
t_nd = 0.05  # P(T|¬D)
# Test; #P(T)
# n_Test; #P(¬T)


# Finding the Value of test
# P(T)=P(T|D)*P(D)+P(T|¬D)*(¬D)
Test = t_d * Disease + t_nd * N_Disease

print(Test)

