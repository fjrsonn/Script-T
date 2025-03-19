#!/bin/bash

# Exibir mensagem de início
echo "🚀 Iniciando o Script-Termux..."

# Verificar se o Python3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 não encontrado! Instalando..."
    pkg install python -y  # Para Termux
    # sudo apt install python3 -y  # Para Linux (se necessário)
fi

# Executar o script principal
python3 Script_Termux.py

# Verificar o status da execução
if [ $? -eq 0 ]; then
    echo "✅ Script executado com sucesso!"
else
    echo "❌ Ocorreu um erro na execução do script."
fi
