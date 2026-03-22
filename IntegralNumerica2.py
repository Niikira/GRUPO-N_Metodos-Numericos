

# Entrada de dados
from decimal import ROUND_HALF_UP, getcontext
from sympy import symbols, sympify

getcontext().rounding = ROUND_HALF_UP


# Entrada de dados
expressao = input("Qual é a função? ")
intervalo = [input("Qual o começo do intervalo? "), input("Qual o fim do intervalo? ")]
numeroDeTrapezios = int(input("Quantos trapézios você gostaria? "))
numeroDeCasasDecimais = int(input("Quantas casas decimais você gostaria? "))


# Tratamento de dados
inicio = float(intervalo[0])
fim = float(intervalo[1])
passo = (fim-inicio)/numeroDeTrapezios



x = symbols('x') #define x como variavel
func = sympify(expressao) #conversão da string de entrada para função matemática



firstFX = func.subs(x, inicio)
dadosX = [inicio]
dadosFX = [firstFX]

# variáveis de controle
i = inicio
ii=0
iii=-1

def erro_arredondamento(numeroDeTrapeziosParam, numeroDeCasasDecimaisParam, passoParam): 
    ErroArredondamento = numeroDeTrapeziosParam * ((10 ** (-numeroDeCasasDecimaisParam))/2) * passoParam 
    print(ErroArredondamento)
    return ErroArredondamento

#loop de preenchimento da tabela "x  f(x)"
while i < fim:
    i = i+passo
    ii = ii+1
    value = dadosX[ii-1] + passo
    dadosX.append(value)
    dadosFX.append(func.subs(x, value))


firstPart = dadosFX[0]/2
lastPart = dadosFX[numeroDeTrapezios]/2
anotherParts = 0

# define a somatória que será efetuada ao final
stringGigante = str(passo) + "*(" + str(round(firstPart, numeroDeCasasDecimais)) + " + "


for i in range(1, numeroDeTrapezios, 1):
    anotherParts = anotherParts + dadosFX[i]
    stringGigante = stringGigante + str(round(anotherParts, numeroDeCasasDecimais)) + " + "


totalArea = passo * (firstPart+anotherParts+lastPart)
stringGigante = stringGigante + str(round(lastPart, numeroDeCasasDecimais)) + ")=" + str(round(totalArea, numeroDeCasasDecimais))

print(func)

#criacao da tabela
print("=================")
print("x | f(x)")
for x1, fx in zip(dadosX, dadosFX):
    iii = iii+1
    print(f"{x1} | {round(fx, numeroDeCasasDecimais)}")

print(stringGigante)
erro_arredondamento(numeroDeTrapeziosParam=numeroDeTrapezios, numeroDeCasasDecimaisParam=numeroDeCasasDecimais,passoParam=passo)

