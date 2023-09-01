def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"A chave é {chave} e o valor é {valor}")
    print(type(kwargs))

minha_funcao(nome="João", idade=25, país="Brasil")