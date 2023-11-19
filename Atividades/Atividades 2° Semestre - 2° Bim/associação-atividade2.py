class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

    def designar_professor(self, professor):
        self.professor = professor
        professor.adicionar_curso(self)
        print(f"Professor {professor.nome} designado para o curso {self.nome}.")

    def __str__(self):
        if self.professor:
            return f"Curso: {self.nome}, Professor: {self.professor.nome}"
        else:
            return f"Curso: {self.nome}, Professor não designado"


class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos_lecionados = []

    def adicionar_curso(self, curso):
        self.cursos_lecionados.append(curso)
        print(f"Professor {self.nome} está lecionando o curso {curso.nome}.")

    def listar_cursos_lecionados(self):
        if self.cursos_lecionados:
            print(f"Cursos lecionados por {self.nome}:")
            for curso in self.cursos_lecionados:
                print(f"- {curso.nome}")
        else:
            print(f"Professor {self.nome} não está lecionando nenhum curso no momento.")

curso1 = Curso("Introdução à Programação")
curso2 = Curso("Banco de Dados")
professor1 = Professor("Diemis")
professor2 = Professor("Giulio")

# Designar professores para cursos
curso1.designar_professor(professor1)
curso2.designar_professor(professor2)

# Listar cursos lecionados por um professor
professor1.listar_cursos_lecionados()
professor2.listar_cursos_lecionados()