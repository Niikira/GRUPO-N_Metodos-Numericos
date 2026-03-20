#Bibliotecas
import numpy as np
import sympy as sp
import pandas as pd
from sympy import symbols, sympify

#notas para o próximo dev:

#a ser feito
#entrada dos dados
#lógica de cálculo de integral com loop de somatória
#construção da tabela com x e f(x) dentro do loop
#todas as saídas especificadas
#erro de truncamento (se der tempo)

#Niikira: 
#Entendi que as entradas podem ser:
#função com String (nome da String como "expr")
#intervalo como Array de tamanho 2 (outro jeito pode ser pedir para o usuário colocar primeiro o início e depois o final)
#numero de trapezios e numero de casas decimais podem ser int

def area_trapezio(bmenor, bmaior, h): #bmenor = base menor bmaior = base maior h = altura
    at = ((bmaior + bmenor)*h)/2 #at = area do trapezio
    return at

def erro_arredondamento(ntrap, ncd, passo): #ntrap = numero de trapézios ncd = numero de casas decimais #passo = altura dos trapezios
    Ea = ntrap * ((10 ** (-ncd))/2) * passo #Ea = erro de arredondamento
    return Ea

#cálculo da integral
x = symbols('x') #define x como variavel
func = sympify(expr) #conversão da string de entrada para função matemática
inicio = intervalo[0]
fim = intervalo[1]
altura = (fim-inicio)/ntrap
