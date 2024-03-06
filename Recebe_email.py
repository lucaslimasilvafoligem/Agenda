# USE pip install imap_tools

from imap_tools import MailBox, AND
import Gerencia_compromissos

gC = Gerencia_compromissos.instancia()

def ler_emails():
    meu_email = MailBox("imap.gmail.com").login("SUA SENHA", "SEU EMAIL")
    
    # Busque os emails com o assunto "ADD TAREFA"
    emails_add_tarefa = meu_email.fetch(AND(from_="EMAIL DE QUEM MANDA", subject="ADD TAREFA", seen=False))

    # Busque os emails com o assunto "RM TAREFA"
    emails_excluir_tarefa = meu_email.fetch(AND(from_="EMAIL DE QUEM MANDA", subject="RM TAREFA", seen=False))

    add_tarefas(emails_add_tarefa)
    rm_tarefas(emails_excluir_tarefa)
    meu_email.logout()

def add_tarefas(emails):
    for email in emails:
        tarefas = email.text.split("|")
        for tarefa_str in tarefas:
            tarefa = tuple(tarefa_str.strip().split("`"))
            if len(tarefa) == 3:
                titulo, descricao, data = tarefa
                gC.adicionar_atividade(titulo.strip(), descricao.strip(), data.strip())

def rm_tarefas(emails):
    for email in emails:
        ids = email.text.split("|")
        for id in ids:
            gC.deletar_atividade_id(int(id))

ler_emails()
