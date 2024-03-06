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
        
        # Criar tabela para armazenar as atividades, caso não exista
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS atividade (
                id INTEGER PRIMARY KEY,
                titulo CHAR(255) NOT NULL,
                descricao TEXT NOT NULL,
                data DATE NOT NULL
            )
        ''')

    def adicionar_atividade(self, titulo, descricao, data):
        if (
            vali.validarString(titulo) and
            vali.validarString(descricao) and
            vali.validarData(data)
        ):
            data = datetime.strptime(str(data), '%Y-%m-%d').date()
            self.cursor.execute('INSERT INTO atividade (titulo, descricao, data) VALUES (?, ?, ?)', (titulo, descricao, data))
            print("Criado")
            self.conn.commit()
        else: raise ValueError("parametro inválido na criação da atividade") 

    def atualizar_atividade(self, id, novoTitulo, novaDescricao, novaData):
        if (
            vali.validarId(id) and
            vali.validarString(novoTitulo) and
            vali.validarString(novaDescricao) and
            vali.validarData(novaData)
        ):
            novaData = datetime.strptime(str(novaData), '%Y-%m-%d').date()
            self.cursor.execute('UPDATE atividade SET titulo = ?, descricao = ?, data = ? WHERE id = ?', (novoTitulo, novaDescricao, novaData, id))
            print("Atualizado")
            self.conn.commit()
        else: raise ValueError("parametro inválido na atualização da atividade")

    def deletar_atividade_id(self, id):
        if (vali.validarId(id)):
            self.cursor.execute('DELETE FROM atividade WHERE id = ?', (id,))
            print("Deletado")
            self.conn.commit()
        else: raise ValueError("Id inválido")

    def deletar_atividade_data(self, data):
        if(vali.validarData(data)):
            self.cursor.execute('DELETE FROM atividade a WHERE a.data = ?', (datetime.strptime(data, "%Y-%m-%d")))
            print("Deletado")
            self.conn.commit()

    def deletar_atividade_titulo_data(self, titulo, data):
        if (vali.validarString(titulo and vali.validarData(data))):
            self.cursor.execute('DELETE FROM atividade a WHERE a.data = ? and a.titulo = ?', (data, titulo))
            print("Deletado")
            self.conn.commit()
        else: raise ValueError("Parametro nválido para a exclusão")

    def deletar_todas_as_atividades(self):
            self.cursor.execute("DELETE FROM atividade")
            self.conn.commit()

    def exibir_atividades_data(self, data):
        data = datetime.strptime(str(data), "%Y-%m-%d")
        self.cursor.execute('SELECT * FROM atividade WHERE data = ?', (data,))
        return self.cursor.fetchall()

    def exibir_atividades_anteriores(self, data):
        data = datetime.strptime(str(data), "%Y-%m-%d")
        self.cursor.execute('SELECT * FROM atividade WHERE data < ?;', (data,))
        return self.cursor.fetchall()

    def exibir_atividades(self):
        self.cursor.execute('SELECT * FROM atividade')
        return self.cursor.fetchall()
    
    def menu(self):
        while True:
            print("\n======== Menu de Opções ========")
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
                self.adicionar_atividade(titulo, descricao, data)
                self.conn.close()
            elif opcao == '2':
                id = int(input("Digite o id: "))
                titulo = input("Digite o título da atividade: ")
                descricao = input("Digite a descrição da atividade: ")
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                self.atualizar_atividade(id, titulo, descricao, data)
            elif opcao == '3':
                atividades = self.exibir_atividades()
                if (len(atividades) > 0):
                    print(self.formatar_saida(atividades))
            elif opcao == '4':
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                atividades = self.exibir_atividades_data(data)
                if (len(atividades) > 1):
                    print(self.formatar_saida(atividades))
            elif opcao == '5':
                id = int(input("Digite o Id: "))
                self.deletar_atividade_id(id)
            elif opcao == '6':
                titulo = input("Digite o título da atividade: ")
                data = input("Digite a data da atividade (YYYY-MM-DD): ")
                self.deletar_atividade_titulo_data(titulo, data)
            elif opcao == '7':
                self.conn.close() # fechar a conexão
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                
    def formatar_saida(self, compromissos):
        if (len(compromissos) > 0):
            saida ="\n======== Atividades ========"
            for atividade in compromissos:
                saida+= "\n Id:" + str(atividade[0]) + "\nTítulo: " + atividade[1] + "\nDescrição: " + atividade[2] + "\nData: " + str(atividade[3]) + "\n---------------------------------------"
        else: saida ="Não há Atividades"
        return saida
    
def instancia():
    return Agenda()
