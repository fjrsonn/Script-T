import pytest
import os
import sys
from unittest.mock import patch
from Script_Termux import executar_script, executar_comando, acesso  # Certifique-se de que o nome do arquivo está correto

# Testando a execução de scripts
@patch("os.system")
def test_executar_script(mock_system):
    executar_script("teste.py", "--arg1 valor1")
    mock_system.assert_called_with("python3 teste.py --arg1 valor1")

# Testando a execução de comandos do sistema
@patch("os.system")
def test_executar_comando(mock_system):
    executar_comando("ls", "-la")
    mock_system.assert_called_with("ls -la")

# Testando o acesso com senha correta
@patch("builtins.input", return_value="123456")
@patch("os.system")
@patch("time.sleep")
def test_acesso_sucesso(mock_sleep, mock_system, mock_input):
    acesso()
    mock_input.assert_called_once_with("Senha: ")
    mock_system.assert_called_with("clear")

# Testando o acesso com senha errada (corrigido para capturar SystemExit)
@patch("builtins.input", return_value="000000")
def test_acesso_falha(mock_input):
    with pytest.raises(SystemExit):  # Captura a exceção SystemExit
        acesso()
    mock_input.assert_called_once_with("Senha: ")