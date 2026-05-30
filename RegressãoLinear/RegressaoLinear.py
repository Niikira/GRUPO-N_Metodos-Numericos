import numpy as np
import sys
import matplotlib.pyplot as plt
from decimal import ROUND_HALF_UP, getcontext
from math import sqrt
getcontext().rounding = ROUND_HALF_UP #definição do tipo de arredondamento


X = [] # variaveis independentes
Y = [] # variaveis dependentes

n = int(input('digite o tamanho da tabela: '))

contador = 1

while(contador<=n):
    x_number = float(input(f'Digite a variável independente na posicao {contador}:  '))
    X.append(x_number)
    contador = contador + 1

contador = 1

while(contador<=n):
    y_number = float(input(f'Digite a variável dependente na posicao {contador}:  '))
    Y.append(y_number)
    contador = contador + 1



soma_x = 0
soma_y = 0
soma_produto = 0
contador = 0

for number_x in X:  # somatória dos numeros independentes
    soma_x = soma_x + number_x

for number_y in Y:  # somatória dos numeros dependentes
    soma_y = soma_y + number_y

while(contador < n): #somatória dos produtos das duas variáveis
    soma_produto = soma_produto +(X[contador]*Y[contador])
    contador = contador + 1

print(f'Valor de n:{n}')
print(f'soma da variavel independente: {soma_x}')
print(f'soma da variavel dependente: {soma_y}')
print(f'soma do produto das duas variáveis: {soma_produto}')

#calculo das médias
media_x = soma_x/n
media_y = soma_y/n
media_produto = soma_produto/n

#covariância

Covariancia = (media_produto) - (media_x * media_y) #entre x e y

print(f'média do produto das variáveis: {media_produto}')
print(f'média da variável independente: {media_x}')
print(f'média da variável dependente: {media_y}')
print(f'Covariância: {Covariancia}')

soma_dos_quadrados_x = 0.0
soma_dos_quadrados_y = 0.0

if(Covariancia != 0):
    for number_x_again in X: 
        soma_dos_quadrados_x = soma_dos_quadrados_x + (number_x_again**2)
    for number_y_again in Y: 
        soma_dos_quadrados_y = soma_dos_quadrados_y + (number_y_again**2)

    media_quadrado_x = soma_dos_quadrados_x/n
    media_quadrado_y = soma_dos_quadrados_y/n
    desvio_padrao_x = sqrt((media_quadrado_x)-(media_x**2))
    desvio_padrao_y = sqrt((media_quadrado_y)-(media_y**2))

    print(f'soma dos quadrados de X: {soma_dos_quadrados_x}')
    print(f'média da soma dos quadrados de X: {media_quadrado_x}')
    print(f'desvio padrão de X: {desvio_padrao_x}')
    print(f'soma dos quadrados de Y: {soma_dos_quadrados_y}')
    print(f'média da soma dos quadrados de Y: {media_quadrado_y}')
    print(f'desvio padrão de Y: {desvio_padrao_y}')

    R = float(Covariancia/(desvio_padrao_x*desvio_padrao_y)) # COEFICIENTE DE PEARSON

    det = R**2  # COEFICIENTE DE DETERMINACAO

    print(f'coeficiente de correlação de Pearson: {round(R, 8)}')
    print(f'Coeficiente de determinação: {round(det*100, 2)}%')

#cálculo de 'a', 'b' e construção da reta de regressão
#sistema:
# a*N + b*soma_x = soma_y
# a*soma_x + b*soma_dos_quadrados_x = soma_produto
#estratégia: regra de Cramer (a mesma usada na apresentação)
b = ((n*soma_produto)-(soma_x*soma_y))/((n*soma_dos_quadrados_x)-(soma_x**2))
a = (soma_y - (soma_x*b))/n

print(f'Valor de a: {a}')
print(f'Valor de b: {b}')
print(f'formula da reta: Y = {a} + {b} * X')

#contrução da reta
eixo_X = np.array(X)
eixo_Y = np.array(Y)

x_reta =np.linspace(min(eixo_X)-1, max(eixo_X)+1, 100)
y_reta = a+b*x_reta



print('\nCÁLCULO DA VARIÁVEL DEPENDENTE')
calculo_variavel_independente = float(input('escreva o valor da variável independente: '))

calculo_variavel_dependente = a+b*calculo_variavel_independente

print(f'variável dependente: {calculo_variavel_dependente}')

plt.scatter(eixo_X, eixo_Y, color ='steelblue', zorder = 5, label ='Pares observados')
plt.plot(x_reta, y_reta, color='tomato', label=f'Y = {a} + {b}X')
plt.scatter(calculo_variavel_independente, calculo_variavel_dependente, color='gold', edgecolor='black', s=100, zorder=10, label='Ponto calculado')
plt.xlabel('variável independente (X)')
plt.ylabel('variável dependente (Y)')
plt.title('Regressão Linear')
plt.legend()
plt.grid(True, linestyle ='--', alpha = 0.5)
plt.tight_layout()
plt.show()