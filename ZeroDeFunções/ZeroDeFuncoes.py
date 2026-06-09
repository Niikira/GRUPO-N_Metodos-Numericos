from sympy import symbols, sympify



a = int(input("Digite o mínimo do intervalo: "))
b = int(input("Digite o máximo do intervalo: "))
erro_max = float(input("Digite o erro máximo: "))
expressao = input("Digite a função: ")

x = symbols('x')
f = sympify(expressao)

erro = (b-a)/2
i = 1
print("")
while(erro > erro_max):
    x0 = (a+b)/2
    print(f"{i} estimativa")
    print(f"A média do intervalo [{a}, {b}] é {x0}")
    print(f"A erro é {erro}")
    print(f"Vamos dividir o intervalo [{a}, {b}] em dois subintervalos:")
    print(f"Consideremos: [{a}, {x0}] e [{x0}, {b}]")
    fa = f.subs(x, a) # calcula f(a)
    fx0 = f.subs(x, x0) # calcula f(x0)
    fb = f.subs(x, b) # calcula f(b)

    if fa * fx0 < 0: # ou seja, um numero negativo multiplicado por um positivo (sempre resulta <0)
        b = x0
    else: # ou seja, quando dois numeros negativos sao multiplicados e viram positivo (significa que só muda no intervalo [x0, b])
        a = x0

    print("")
    amplitude = (b-a)/2


print(f"A raiz aproximada é {x0} com erro máximo {amplitude}")

