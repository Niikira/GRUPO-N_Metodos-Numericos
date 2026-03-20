#Bibliotecas
import numpy as np
import sympy as sp
import pandas as pd

def area_trapezio(bmenor, bmaior, h): #bmenor = base menor bmaior = base maior h = altura
    at = ((bmaior + bmenor)*h)/2 #at = area do trapezio
    return at

def erro_arredondamento(ntrap, ncd, passo): #ntrap = numero de trapézios ncd = numero de casas decimais
    Ea = ntrap * ((10 ** (-ncd))/2) * passo #Ea = erro de arredondamento
    return Ea

