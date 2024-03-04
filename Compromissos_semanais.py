import Util
import Gerencia_compromissos
import Envia_email
from datetime import datetime

gC = Gerencia_compromissos.instancia()
dataUtil = Util.DataUtil()
email = Envia_email

def compromissos(data):
    return gC.exibir_atividades_data(data)

def enviar_compromissos(dia, data):
    if (dia == 6):
        email.enviar_email(
            "lucas.lima.silva@ccc.ufcg.edu.br",
            "COMPROMISSOS DA SEMANA",
            formatar_saida(compromissos_semanais(dia, data))
            )
    else: enviar_compromissos(dia + 1, dataUtil.proximo_dia(data))

def compromissos_semanais(dia, data):
    if (dia < 0): return []
    else: return compromissos(data) + compromissos_semanais(dia - 1, dataUtil.proximo_dia(data))

def formatar_saida(compromissos):
    if (len(compromissos) > 0):
        saida ="\n===== Atividades ====="
        for atividade in compromissos:
            saida+= "\n Id:" + str(atividade[0]) + "\nTítulo: " + atividade[1] + "\nDescrição: " + atividade[2] + "\nData:" + str(atividade[3]) + "\n--------------------------"
    else: saida ="Não há Atividades"
    return saida

enviar_compromissos(dataUtil.dia_semana(), dataUtil.data_hoje())
