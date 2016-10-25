import numpy
import decimal
import math

golden = decimal.Decimal((1 + 5 ** 0.5) / 2)


g2 = decimal.Decimal(1.0)
iteracao2 = 1

while (abs((decimal.Decimal(g2) - decimal.Decimal(golden))) > 0.00000000000000000009):
    g2 = math.sqrt(1+g2)
    iteracao2 = iteracao2+1
    #print 'rai i: ' + str(iteracao2)

print 'raizes: '+ str(iteracao2)


g1 = decimal.Decimal(1.0)
iteracao1 = 1

while (abs((decimal.Decimal(g1) - decimal.Decimal(golden))) > 0.00000000000000000009) and iteracao1 <= 1000000:
    g1 = decimal.Decimal(decimal.Decimal(1.0) + decimal.Decimal(1.0)/decimal.Decimal(g1))
    # print decimal.Decimal(decimal.Decimal(golden) - decimal.Decimal(g1))
    #print "g1: " + str(g1)
    #print "golden: " + str(golden)
    #print "golden - g1: " + str(decimal.Decimal(golden) - decimal.Decimal(g1))
    #print decimal.Decimal(g1)
    iteracao1 = iteracao1+1
    #print 'frac i: ' + str(iteracao1)

print 'fracoes: ' + str(iteracao1)

# g1 = decimal.Decimal(1.0)
# g2 = decimal.Decimal(1.0)

# while (abs((decimal.Decimal(g1) - decimal.Decimal(golden))) > 0.000001):
#     g2 = g1
#     g1 = decimal.Decimal(decimal.Decimal(g)1 + decimal.Decimal(g2))
#     # print decimal.Decimal(decimal.Decimal(golden) - decimal.Decimal(g1))
#     #print "g1: " + str(g1)
#     #print "golden: " + str(golden)
#     #print "golden - g1: " + str(decimal.Decimal(golden) - decimal.Decimal(g1))
#     print decimal.Decimal(g1)

