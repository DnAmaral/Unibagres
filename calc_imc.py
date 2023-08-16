# Atividade 2

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o seu peso (kg): "))
altura = float (input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)

print (f"Seu IMC é: {imc:,.1f} " )

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3") 


