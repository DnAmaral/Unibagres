#Professor explicou sobre o elif, siga o código de explicação adiante

nota = int (input('Digite a nota do aluno:'))

if nota >= 90:
    print ('A - Excelente')
elif nota >= 80:
    print('B - Muito Bom')
elif nota >= 70:
    print('C - Bom')
elif nota >= 60:
    print('D - Regular')
else:
    print('F - Reprovado')


#Lembrete! Todos os códigos que estão aqui não irão funcionar tudo junto!

opcao = int(input('Escolha uma opção:\n1 - Maçã, Banana, Laranja:'))

if opcao == 1:
    print ('Você escolheu Maçã.')
elif opcao == 2:
    print('Você escolheu Banana.')
elif opcao == 3:
    print('Você escolheu Laranja.')
else:
    print('Opção inválida!')

#Estruturas de Repetição!

contador = 1

while contador <= 5:
    print('Contador', contador)
    contador = contador + 1