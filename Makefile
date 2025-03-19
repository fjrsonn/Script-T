.PHONY: run test install clean

install:
	@echo "Instalando dependências..."
	pip install -r requirements.txt

run:
	@echo "Executando o script..."
	python3 script.py

test:
	@echo "Rodando testes..."
	pytest

clean:
	@echo "Limpando arquivos temporários..."
	rm -rf __pycache__
