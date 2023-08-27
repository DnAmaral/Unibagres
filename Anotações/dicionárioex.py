dados_cliente = {
    "Nome": "Danilo",
    "Endereço": "Rua ABC, 123",
    "Telefone": "948696918"
}

print (dados_cliente['Nome'])

dados_cliente["Cidade"] = "Ivaiporã"
print (dados_cliente)

dados_cliente.pop ("Telefone")

for indice, valor in dados_cliente.items():
    print(f"Índice: {indice}, valor: {valor}")
    print("-------------------------------------------------")