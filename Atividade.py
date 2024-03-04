import Util

vali = Util.Validador

class Atividade:

    # Construtor
    def __init__(self, data, titulo, descricao):
        if (
            vali.validarString(titulo) and
            vali.validarString(descricao)
        ):
            self.set_data(data)
            self.set_titulo(titulo)
            self.set_descricao(descricao)

    # Adicione aqui sua lógica de validação para a data
    def set_data(self, data):
        self.data = data

    # Adicione aqui sua lógica de validação para o título
    def set_titulo(self, titulo):
        if (vali.validarString(titulo)):
            self.titulo = titulo

    # Adicione aqui sua lógica de validação para a descrição
    def set_descricao(self, descricao):
        if (vali.validarString(descricao)):
            self.descricao = descricao

    def __str__(self):
        return f"Título: {self.titulo}\nData: {self.data}\n Descrição: {self.descricao}"

    def atualizar(self, data, titulo, descricao):
        if (
            vali.validarString(titulo) and
            vali.validarString(descricao)
        ):
            self.set_data(data)
            self.set_titulo(titulo)
            self.set_descricao(descricao)

    def validarString(string):
        if(vali.validarString(string)): raise ValueError("Texto inválido")

# Exemplo de uso:
atividade = Atividade("2024-03-10", "Exemplo", "Uma descrição qualquer")
print(atividade)
atividade.atualizar("2024-03-12", "Novo título", "Nova descrição")
print(atividade)
