lista1 = ("Danilo", "Silva", "Amaral", "É", "Maneiro")
print(type(lista1))
print(len(lista1))
print(lista1[2])

lista2 = lista1 *2

print(lista2)

lista1.remove("Silva")
print(lista1)

lista1.pop(3)
print(lista1)

for listageral in lista1:
    print(listageral)

#É adicionado no final da lista!

lista1.append("SouEu")
print(lista1)