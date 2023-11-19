class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def exibir_info(self):
        print(f"Monitor {self.marca}, Tamanho: {self.tamanho} polegadas")


class Computador:
    def __init__(self, nome, marca, monitor=None):
        self.nome = nome
        self.marca = marca
        self.monitor = monitor

    def conectar_monitor(self, monitor):
        self.monitor = monitor
        print(f"Computador {self.nome} conectado ao monitor {monitor.marca}.")

    def desconectar_monitor(self):
        if self.monitor:
            print(f"Computador {self.nome} desconectado do monitor {self.monitor.marca}.")
            self.monitor = None
        else:
            print("Computador não está conectado a nenhum monitor.")

    def exibir_info(self):
        print(f"Computador {self.nome}, Marca: {self.marca}")
        if self.monitor:
            self.monitor.exibir_info()
        else:
            print("Sem monitor conectado.")

monitor1 = Monitor("Dell", 24)
computador1 = Computador("Desktop1", "HP", monitor1)

# Exibir informações do computador (incluindo o monitor)
computador1.exibir_info()

# Desconectar o computador do monitor
computador1.desconectar_monitor()

# Exibir informações novamente (sem monitor)
computador1.exibir_info()
