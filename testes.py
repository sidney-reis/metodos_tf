from decimal import *
import math

# configura precisao para 100
getcontext().prec = 100

# define valor de comparacao
proporcaoAurea = \
    (Decimal(1) + Decimal(5) ** Decimal(0.5)) / Decimal(2)

# valor aproximado inicial
valorAproximado = Decimal(1.0)

iteracao = 1

print 'iteracao 1: 1'

# compara se os 21 primeiros caracteres sao
# iguais (o "." tambem conta) e se iteracao
# nao atingiu 1.000.000
while str(Decimal(valorAproximado))[0:21] != \
    str(Decimal(proporcaoAurea))[0:21] and \
    iteracao <= 1000000:

# realiza calculo da iteracao
    valorAproximado = \
        (Decimal(1)+Decimal(valorAproximado)).sqrt()

    iteracao = iteracao + 1

    print 'iteracao ' + str(iteracao) + ': ' \
        + str(Decimal(valorAproximado))

print 'iteracoes necessarias: '+ str(iteracao)

#1.618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862


# g1 = Decimal(1.0)
# iteracao1 = 1

# while (abs((Decimal(g1) - Decimal(proporcaoAurea))) > 0.00000000000000000009) and iteracao1 <= 1000000:
#     g1 = Decimal(Decimal(1.0) + Decimal(1.0)/Decimal(g1))
#     iteracao1 = iteracao1+1

# print 'fracoes: ' + str(iteracao1)
