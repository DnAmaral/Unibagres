class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente. Saque não permitido.")

    def ver_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo}")

# Criando um objeto da classe ContaBancaria
conta_exemplo = ContaBancaria("João")

# Testando depósitos, saques e verificação de saldo
conta_exemplo.depositar(1000)
conta_exemplo.ver_saldo()

conta_exemplo.sacar(500)
conta_exemplo.ver_saldo()

conta_exemplo.sacar(700)  
conta_exemplo.ver_saldo()