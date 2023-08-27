lista_de_compras = []

while True:
    print("Escolha uma opção:")
    print("1. Mostrar Lista")
    print("2. Adicionar Item")
    print("3. Remover Item")
    print("4. Editar Item")
    print("5. Sair")

    escolha = input()

    if escolha == "1":
        print("Lista de Compras:")
        for i, item in enumerate(lista_de_compras, start=1):
            print(f"{i}. {item}")
    elif escolha == "2":
        item = input("Digite o novo item: ")
        lista_de_compras.append(item)
        print(f"{item} foi adicionado à lista.")
    elif escolha == "3":
        indice = int(input("Digite o índice do item a ser removido: ")) - 1
        if 0 <= indice < len(lista_de_compras):
            item_removido = lista_de_compras.pop(indice)
            print(f"{item_removido} foi removido da lista.")
        else:
            print("Índice inválido.")
    elif escolha == "4":
        indice = int(input("Digite o índice do item a ser editado: ")) - 1
        if 0 <= indice < len(lista_de_compras):
            novo_item = input("Digite o novo valor: ")
            lista_de_compras[indice] = novo_item
            print(f"Item editado para: {novo_item}")
        else:
            print("Índice inválido.")
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")