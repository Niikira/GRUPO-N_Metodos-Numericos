#Bibliotecas
import numpy as np
import sympy as sp
import pandas as pd
from sympy import symbols, sympify

#notas para o próximo dev:

#a ser feito:
#lógica de cálculo de integral com loop de somatória
#construção da tabela com x e f(x) dentro do loop
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


# Entrada de dados
numeroDeTrapezios = input("Quantos trapézios você gostaria? ")
numeroDeCasasDecimais = input("Quantas casas decimais você gostaria? ")
passo = input("Qual a altura dos trapezios? ")
expressao = input("Qual é a função? ")
intervalo = [input("Qual o começo do intervalo? "), input("Qual o fim do intervalo? ")]
print(numeroDeTrapezios)
print(numeroDeCasasDecimais)
print(passo)
print(expressao)
print (intervalo)
# Definições de métodos

"""
    Precisa: Calcular a base menor, calcular a base maior, a altura antes de chamar esse método
"""
def area_trapezio(baseMenor, baseMaior, altura):
    areaTrapezio = ((baseMaior + baseMenor)*altura)/2 
    
    return areaTrapezio

def erro_arredondamento(numeroDeTrapezios, numeroDeCasasDecimais, passo): 
    ErroArredondamento = numeroDeTrapezios * ((10 ** (-numeroDeCasasDecimais))/2) * passo 
    print(ErroArredondamento)
    return ErroArredondamento

#cálculo da integral
x = symbols('x') #define x como variavel
func = sympify(expressao) #conversão da string de entrada para função matemática
print(func)
inicio = intervalo[0]
fim = intervalo[1]
# altura = (fim-inicio)/numeroDeTrapezios -> não é necessário pois o passo já é a altura.
# Se quiser mesmo calcular a altura precisa fazer um parse pois o input recebe string.
