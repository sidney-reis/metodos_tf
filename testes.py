import decimal
import math

proporcaoAurea = decimal.Decimal((1 + 5 ** 0.5) / 2)
valorAproximado = decimal.Decimal(1.0)
iteracao = 1

while (abs((decimal.Decimal(valorAproximado) - \
    decimal.Decimal(proporcaoAurea))) \
    > 0.00000000000000009) and (iteracao <= 1000000):

    valorAproximado = math.sqrt(1+valorAproximado)
    iteracao = iteracao+1

print 'iteracoes necessarias: '+ str(iteracao)





# g1 = decimal.Decimal(1.0)
# iteracao1 = 1

# while (abs((decimal.Decimal(g1) - decimal.Decimal(proporcaoAurea))) > 0.00000000000000000009) and iteracao1 <= 1000000:
#     g1 = decimal.Decimal(decimal.Decimal(1.0) + decimal.Decimal(1.0)/decimal.Decimal(g1))
#     iteracao1 = iteracao1+1

# print 'fracoes: ' + str(iteracao1)
