#Bibliotecas
import numpy as np
import sympy as sp
import pandas as pd
from sympy import symbols, sympify

#notas para o próximo dev:

#a ser feito:
#lógica de cálculo de integral com loop de somatória
#todas as saídas especificadas
#erro de truncamento (se der tempo)

#Niikira: 
#Entendi que as entradas podem ser:
#função com String (nome da String como "expr")
#intervalo como Array de tamanho 2 (outro jeito pode ser pedir para o usuário colocar primeiro o início e depois o final)
#numero de trapezios e numero de casas decimais podem ser int

# PedroBZR1:
# Feito a entrada de dados
# Refatoração do código para melhor legibilidade (clean code)

#Niikira:
#descarte da função "area_trapezio" pois não será mais necessária (comentada)
#construção da tabela (x  f(x))
#calculo aproximado da integral


# Entrada de dados
expressao = input("Qual é a função? ")
intervalo = [input("Qual o começo do intervalo? "), input("Qual o fim do intervalo? ")]
numeroDeTrapezios = int(input("Quantos trapézios você gostaria? "))
numeroDeCasasDecimais = int(input("Quantas casas decimais você gostaria? "))
#passo = input("Qual a altura dos trapezios? ") -> o passo não é recebido como entrada
print(expressao)
print (intervalo)
print(numeroDeTrapezios)
print(numeroDeCasasDecimais)
#print(passo)
# Definições de métodos

"""
    Precisa: Calcular a base menor, calcular a base maior, a altura antes de chamar esse método

def area_trapezio(baseMenor, baseMaior, altura):
    areaTrapezio = ((baseMaior + baseMenor)*altura)/2 
    
    return areaTrapezio
"""

def erro_arredondamento(numeroDeTrapezios, numeroDeCasasDecimais, passo): 
    ErroArredondamento = numeroDeTrapezios * ((10 ** (-numeroDeCasasDecimais))/2) * passo 
    print(ErroArredondamento)
    return ErroArredondamento

#cálculo da integral
x = symbols('x') #define x como variavel
func = sympify(expressao) #conversão da string de entrada para função matemática
print(func)
inicio = int(intervalo[0])
fim = int(intervalo[1])
passo = (fim-inicio)/numeroDeTrapezios
dados = {"x": [], "f(x)": []}

#loop de preenchimento da tabela "x  f(x)"
for i in range(inicio, fim+1, passo):
    dados["x"].append(i)
    dados["f(x)"].append(func.subs(x, i))
#criacao da tabela
tabela = pd.DataFrame(dados)
#cópia da coluna "f(x)" para calculo da integral
colunafx = tabela["f(x)"].copy()
#divisão do primeiro e do ultimo valor por 2 para a somatoria das areas do trapezio
colunafx.iloc[0] = colunafx.iloc[0]/2
colunafx.iloc[-1] = colunafx.iloc[-1]/2
#somatória das areas
integral = colunafx.sum()

