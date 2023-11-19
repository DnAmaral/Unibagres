class Cabeça:
    def __init__(self):
        pass  # Sem atributos específicos para a cabeça

class Boneco:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.cabeça = Cabeça()  # Composição: o Boneco é composto por uma Cabeça

    def acao_do_botao(self):
        print(f"Botão pressionado para destruir o boneco {self.nome}.")
        self.destruir()

    def __del__(self):
        print(f"O boneco {self.nome} foi destruído.")

boneco1 = Boneco("Pedrito", "Amarelo")

# Ação de botão para destruir o boneco
boneco1.acao_do_botao()

# Acessar a Cabeça do boneco não é mais possivel pois ela se destruiu junto com o corpo do boneco
# Comentario para evitar o erro
# print(boneco1.cabeça)  # Isso resultará em um erro, pois o boneco foi destruído