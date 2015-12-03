# coding=utf-8
import decimal as dec # imports the decimal package and name it dec

#Bayes rule:
#P(A|B)=P(B|A)*P(A)/P(B)

#For Disease/Test
#P(D|T)=P(T|D)*P(D)/P(T)

Disease = dec.Decimal ('0.0001')#P(D)
N_Disease = 1 - Disease #P(¬D)

t_d = dec.Decimal ('0.99')  # P(T|D)
nt_d = dec.Decimal ('0.01')  # P(¬T|D)
nt_nd = dec.Decimal ('0.95')  # P(¬T|¬D)
t_nd = dec.Decimal ('0.05')  # P(T|¬D)


print 'Finding the Value of P(T)'
print 'P(T)=P(T|D)*P(D)+P(T|¬D)*P(¬D)'

test = t_d * Disease + t_nd * N_Disease
print 'The Value of P(T) = ', round(test,3)

n_Test = 1 - test

Results = t_d * Disease / test
print "\nP(D|T)=P(T|D)*P(D)/P(T) \nP(D|T) = ", round(Results,6)
