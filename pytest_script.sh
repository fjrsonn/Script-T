#!/bin/bash

# Exibir uma mensagem de início
echo "🚀 Iniciando os testes com pytest..."

# Verificar se pytest está instalado
if ! command -v pytest &> /dev/null
then
    echo "❌ pytest não encontrado! Instalando..."
    pip install pytest
fi

# Executar os testes
pytest

# Verificar o status dos testes
if [ $? -eq 0 ]; then
    echo "✅ Todos os testes passaram com sucesso!"
else
    echo "❌ Alguns testes falharam. Verifique os erros acima."
fi
