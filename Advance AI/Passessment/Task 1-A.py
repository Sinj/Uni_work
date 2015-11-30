# coding=utf-8
import decimal as dec

#Bayes rule:
#P(A|B)=P(B|A)*P(A)/P(B)

#For Disease/Test
#P(D|T)=P(T|D)*P(D)/P(T)

Disease = dec.Decimal ('0.00001')
N_Disease = 1 - Disease

t_d = dec.Decimal ('0.99')  # P(T|D)
nt_d = dec.Decimal ('0.01')  # P(¬T|D)
nt_nd = dec.Decimal ('0.95')  # P(¬T|¬D)
t_nd = dec.Decimal ('0.05')  # P(T|¬D)


print 'Finding the Value of test'
print 'P(T)=P(T|D)*P(D)+P(T|¬D)*(¬D)'

test = t_d * Disease + t_nd * N_Disease
print 'The Value of P(Test) = ', round(test,4)

n_Test = 1 - test
#print "Test + Not_Test = ", test + n_Test
#print "Disease + N_Disease = ", Disease + N_Disease
Results = t_d * Disease / test
print "P(D|T)=P(T|D)*P(D)/P(T) \nP(D|T) = ", round(Results,6)