
sair = "sair"

num01 = input("Digite o primeiro número:")
num02 = input("Digite o segundo número:")
operador = input ("Digite o operador ( +, -, /, *):")

num01_float = 0
num02_float = 0

num01_float = float(num01)
num02_float = float(num02)

if operador == "+":
    print(f" {num01_float} + {num02_float} ="  , num01_float + num02_float )
