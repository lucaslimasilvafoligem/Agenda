#!/usr/bin/env bash

ultimaData=""

# Obtém o dia da semana (0 é domingo, 6 é sábado)
dia_semana=$(date +%w)

# Verifica se o dia da semana é sexta-feira (5), sábado (6) ou domingo (0)
if [[ $dia_semana -eq 5 || $dia_semana -eq 6 || $dia_semana -eq 0 ]]; then
    python3 Recebe_email.py && echo "Recebeu as mensagens" > status.txt || { echo "Erro ao ler" > status.txt; exit 1; }
    python3 Compromissos_semanais.py && echo "Enviou as Tarefas" >> status.txt || { echo "Erro ao enviar" >> status.txt; exit 1; }
fi

exit 0
