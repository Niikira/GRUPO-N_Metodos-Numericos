from sympy import symbols, sympify



a = int(input("Digite um número do intervalo: "))
b = int(input("Digite o outro número do intervalo: "))
erro_max = float(input("Digite o erro máximo: "))
expressao = input("Digite a função: ")

x = symbols('x')
f = sympify(expressao)

amplitude = (b-a)/2

print("")
while(amplitude > erro_max):
    x0 = (a+b)/2
    print(f"A média do intervalo [{a}, {b}] é {x0}")
    print(f"A amplitude desse intervalo é {amplitude}")
    print(f"Vamos quebrar o intervalo [{a}, {b}] em dois subintervalos:")
    print(f"O primeiro é [{a}, {x0}] e o segundo é [{x0}, {b}]")
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

