dieimes_matriz = [
    [3, 4, 1],
    [3, 2, 1]
]

soma_total = 0

for linha in dieimes_matriz:
    for elemento in linha:
        soma_total += elemento

print("Matriz:")
for linha in dieimes_matriz:
    print(linha)
print("Soma total dos elementos:", soma_total)