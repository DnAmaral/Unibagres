#atividade 1:
def saudacao():
    print("Bem-vindo ao nosso programa!")

saudacao()

#atividade 2:

def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} e {b} é igual a {resultado}")

soma(5, 3)

#atividade 3:

def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print(f"A média dos números na lista é: {media}")