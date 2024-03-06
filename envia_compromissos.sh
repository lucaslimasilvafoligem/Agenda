#!/usr/bin/env bash

# Obter a data da última sexta-feira e do próximo domingo
domingo=$(date "+%Y-%m-%d" -d "next Sunday")
sexta_antes_domingo=$(date "+%Y-%m-%d" -d "$domingo - 3 days")

# Ler a última linha do arquivo
ultima_linha=$(tail -n 1 .status.txt)

# Função para converter a data para um timestamp Unix
converter_para_timestamp() {
    local data="$1"
    date -d "$data" "+%s"
}

# Verificar se a última linha do arquivo não está vazia e se é uma data válida
if [[ -n "$ultima_linha" && "$ultima_linha" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then

    # Converter as datas para timestamps Unix
    echo $ultima_linha "oi"
    timestamp_ultima_linha=$(converter_para_timestamp "$ultima_linha")
    timestamp_sexta_antes_domingo=$(converter_para_timestamp "$sexta_antes_domingo")
    timestamp_domingo=$(converter_para_timestamp "$domingo")
    
    # Verificar se a última linha corresponde à última sexta-feira que antecede o próximo domingo; se for verdade, o código já rodou no fim de semana
    if (( timestamp_ultima_linha >= timestamp_sexta_antes_domingo && timestamp_ultima_linha <= timestamp_domingo )); then
        exit 0
    fi
fi

# Obtém o dia da semana (0 é domingo, 6 é sábado)
dia=$(date +%w)

# Verifica se o dia da semana é sexta-feira (5), sábado (6) ou domingo (0)
if [[ $dia -eq 5 || $dia -eq 6 || $dia -eq 0 ]]; then
    python3 Recebe_email.py && echo "Recebeu as mensagens" > .status.txt || { echo "Erro ao ler" > .status.txt; exit 1; }
    python3 Compromissos_semanais.py && echo "Enviou as Tarefas" >> .status.txt || { echo "Erro ao enviar" >> .status.txt; exit 1; }
    echo "$(date +"%Y-%m-%d")" >> .status.txt
fi

exit 0
