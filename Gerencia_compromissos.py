import sqlite3
import Util
import datetime
from datetime import datetime


vali = Util.Validador

# Conectar ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect('atividade.db')
cursor = conn.cursor()

class Agenda():

    def __init__(self):
        # Conectar ao banco de dados (se não existir, ele será criado)
        self.conn = sqlite3.connect('atividade.db')
        self.cursor = self.conn.cursor()    
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS atividade (
                id INTEGER PRIMARY KEY,
                titulo CHAR(255) NOT NULL,
                descricao TEXT NOT NULL,
                data DATE NOT NULL
            )
        ''')

    # Criar tabela para armazenar as atividades


    def adicionar_atividade(self, titulo, descricao, data):
        if (
            vali.validarString(titulo) and
            vali.validarString(descricao)
        ):
            self.cursor.execute('INSERT INTO atividade (titulo, descricao, data) VALUES (?, ?, ?)', (titulo, descricao, data))
            print("Criado")
            self.conn.commit()
        elif (
            vali.validarString(titulo) and
            vali.validarString(descricao)
        ):
            data = data.today()
            self.cursor.execute('INSERT INTO atividade (titulo, descricao, data) VALUES (?, ?, ?)', (titulo, descricao, data.strftime("%Y-%m-%d")))
            print("Criado")
            self.conn.commit()
        else: raise ValueError("parametro inválido na criação da atividade") 

    def atualizar_atividade(self, id, novoTitulo, novaDescricao, novaData):
        if (
            isinstance(novaData, datetime.date) and
            vali.validarId(id) and
            vali.validarString(novoTitulo) and
            vali.validarString(novaDescricao)
        ):
            self.cursor.execute("UPDATE atividades SET titulo = ?, descricao = ?, data = ? WHERE id = ?", (novoTitulo, novaDescricao, novaData.strftime("%Y-%m-%d"), id))
            print("Atualizado")
            self.conn.commit()
        elif (
            vali.validarId(id) and
            vali.validarString(novoTitulo) and
            vali.validarString(novaDescricao)
        ):
            self.cursor.execute("UPDATE atividades SET titulo = ?, descricao = ?, data = ? WHERE id = ?", (novoTitulo, novaDescricao, novaData, id))
            print("Atualizado")
            self.conn.commit()
        else: raise ValueError("parametro inválido na atualização da atividade")

    def deletar_atividade_id(self, id):
        if (vali.validarId(id)):
            self.cursor.execute("DELETE FROM atividade WHERE id = ?", (id,))
            print("Deletado")
            self.conn.commit()
        else: raise ValueError("Id inválido")

    def deletar_atividade_data(self, data):
            print(datetime.strptime(data, "%Y-%m-%d").replace(hour=0, minute=0, second=0,))
            self.cursor.execute("DELETE FROM atividade a WHERE a.data = ?", (datetime.strptime(data, "%Y-%m-%d").replace(hour=0, minute=0, second=0,)))
            print("Deletado")
            self.conn.commit()

    def deletar_atividade_titulo_data(self, titulo, data):
        if (vali.validarString(titulo) and isinstance(data, datetime.date)):
            self.cursor.execute("DELETE FROM atividade a WHERE a.data = ? and a.titulo = ?", (data.strftime("%Y-%m-%d"), titulo))
            print("Deletado")
            self.conn.commit()
        elif (
            vali.validarString(titulo)
        ):
            self.cursor.execute("DELETE FROM atividade a WHERE a.data = ? and a.titulo = ?", (data, titulo))
            print("Deletado")
            self.conn.commit()
        else: raise ValueError("Parametro nválido para a exclusão")

    def exibir_atividades_data(self, data):
            data = datetime.strptime(str(data), "%Y-%m-%d").replace(hour=0, minute=0, second=0,)
            self.cursor.execute("SELECT * FROM atividade WHERE data = ?", (data,))
            return self.cursor.fetchall()

    def exibir_atividades(self):
        self.cursor.execute('SELECT * FROM atividade')
        return self.cursor.fetchall()
    
    def menu(self):
        while True:
            print("\n===== Menu de Opções =====")
            print("1. Adicionar Atividade")
            print("2. Atualizar Atividade")
            print("3. Listar Todas As Atividades")
            print("4. Listar Atividades Por Data")
            print("5. Deletar Uma Atividade Por Id")
            print("6. Deletar Uma Atividade Por Titulo E Data")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                titulo = input("Digite o título da atividade: ")
                descricao = input("Digite a descrição da atividade: ")
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                self.adicionar_atividade(titulo, descricao, datetime.strptime(data, '%Y-%m-%d'))
            elif opcao == '2':
                titulo = input("Digite o título da atividade: ")
                descricao = input("Digite a descrição da atividade: ")
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                self.adicionar_atividade(titulo, descricao, datetime.strptime(data, '%Y-%m-%d'))
            elif opcao == '3':
                atividades = self.exibir_atividades()
                if atividades:
                    print("\n===== Atividades =====")
                    for atividade in atividades:
                        print("ID:", atividade[0])
                        print("Título:", atividade[1])
                        print("Descrição:", atividade[2])
                        print("Data:", atividade[3])
                        print("--------------------------")
                else:
                    print("Nenhuma atividade encontrada.")
            elif opcao == '4':
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                atividades = self.exibir_atividades_data(data)
                if atividades:
                    print("\n===== Atividades =====")
                    for atividade in atividades:
                        print("ID:", atividade[0])
                        print("Título:", atividade[1])
                        print("Descrição:", atividade[2])
                        print("Data:", atividade[3])
                        print("--------------------------")
                else:
                    print("Nenhuma atividade encontrada.")
            elif opcao == '5':
                id = int(input("Digite o Id: "))
                self.deletar_atividade_id(id)
            elif opcao == '6':
                titulo = input("Digite o título da atividade: ")
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                self.deletar_atividade_titulo_data(titulo, data)
            elif opcao == '7':
                conn.close() # fechar a conexão
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    
    # Adicione funções semelhantes para atualizar e excluir atividades
    # Exemplo de uso:
    """
    adicionar_atividade('Estudar Python', 'Ler capítulo 5 do livro', '2024-03-02')
    adicionar_atividade('Fazer exercícios', 'Resolver exercícios de listas', '2024-03-03')

    print(exibir_atividades())
    """
def instancia():
    return Agenda()

