from imap_tools import MailBox, AND
import Gerencia_compromissos

gC = Gerencia_compromissos.instancia()

def ler_emails():
    meu_email = MailBox("imap.gmail.com").login("bazinga2112br@gmail.com", "sua senha")
    # Busque os emails com o assunto "ADD TAREFA"
    emails_add_tarefa = meu_email.fetch(AND(from_="lucas.lima.silva@ccc.ufcg.edu.br", subject="ADD TAREFA"))

    # Busque os emails com o assunto "EXCLUIR TAREFA"
    emails_excluir_tarefa = meu_email.fetch(AND(from_="lucas.lima.silva@ccc.ufcg.edu.br", subject="EXCLUIR TAREFA"))

    add_tarefa(list(emails_add_tarefa))
    rm__tarefa(list(emails_excluir_tarefa))
    meu_email.logout()

def add_tarefa(tarefas):
    if (len(tarefas) > 0):
        print("oi")
        tarefas = tarefas.text.split("|")
        for tarefa in tarefas:
            if tarefa.startswith("(") and tarefa.endswith(")"):
                tarefa = tuple(tarefa[1:-1].split(","))
                gC.adicionar_atividade(tarefa[0], tarefa[1], tarefa[2])

def rm__tarefa(idTarefas):
    if (len(idTarefas) > 0):
        ids = idTarefas.split(",")
        for id in ids:
            gC.deletar_atividade_id(int(id))

ler_emails()
