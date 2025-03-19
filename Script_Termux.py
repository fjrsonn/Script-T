#!/usr/bin/python3
import os
import time
import sys

# Subprocessos
def executar_script(script, args=""):
    try:
        os.system(f"python3 {script} {args}")
    except Exception as e:
        print(f"Erro ao executar o script {script}: {e}")

# Comandos do sistema operacional.
def executar_comando(comando, args=""):
    try:
        os.system(f"{comando} {args}")
    except Exception as e:
        print(f"Erro ao executar o comando {comando}: {e}")

# Acesso inicial.
def acesso():
    senha = input("Senha: ")
    if senha != "123456":
        print("Acesso não liberado")
        exit()
    elif senha == "123456":
        print("Acesso liberado")
        time.sleep(3)
        os.system("clear")
    else:
        print("Senha inválida")

# Loading.
def imprimir_cabecalho():
    print("Olá FjrSon")
    time.sleep(1)
    print("LOADING...")
    time.sleep(2)
    os.system("clear")
    os.system("neofetch")  # O comando neofetch pode falhar se não estiver instalado
    time.sleep(2)
    os.system("clear")

# Banner + menu.
def exibir_menu():
    print('\033[0;37m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print("\033[0;31m         ..............")
    print("               ..,;:ccc,.")
    print("             ......''';lxO.")
    print("   .....''''..........,:ld;")
    print("              .';;;:::;,,.x,")
    print("         ..'''.            0Xxoc:,.  ...")
    print("     ....                ,ONkc;,;cokOdc',.")           
    print("             .          OMo           ':ddo.")
    print("                     dMc               :OO;")
    print("                      0M. \033[0;37m  ➤ FjrSon\033[0;31m     .:o.")
    print("                     ;Wd")
    print("                        ;XO,")
    print("                         ,d0Odlc;,..")
    print("                              ..',;:cdOOd::,.")
    print("                                       .:d;.':;.")
    print("                                          'd,  .'")
    print("                                            ;l   ..")
    print("                                             .o")
    print("                                               c")
    print("                                               .")
    print("                                               .")
    print("                    t3rmux n3thunt3r kal1 l1nux")
    print('\033[0;37m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print("[1] \033[0;31m➤ \033[0;37m Update and Upgrade")
    print("[2] \033[0;31m➤ \033[0;37m Nmap")
    print("[3] \033[0;31m➤ \033[0;37m SQLmap")
    print("[4] \033[0;31m➤ \033[0;37m Sherlock")
    print("[5] \033[0;31m➤ \033[0;37m MrHolmes")
    print("[6] \033[0;31m➤ \033[0;37m Scan Subdomínios")
    print("[7] \033[0;31m➤ \033[0;37m Scan Hosts Proxys")
    print("[8] \033[0;31m➤ \033[0;37m Executar Outro Script")
    print("[9] \033[0;31m➤ \033[0;37m Sair")
    print("[10] \033[0;31m➤ \033[0;37m Reiniciar Menu")

# Reset.
def reiniciar():
    print("Reiniciando o menu...")
    time.sleep(1)
    os.system("clear")
    imprimir_cabecalho()

# Função principal.
def main():
    acesso()
    imprimir_cabecalho()  
    escolha = False

    while not escolha:
        exibir_menu()
        try:
            nivel = int(input("PROMPT ➤ "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        # Primeiro Nivel - Update e Upgrade
        if nivel == 1:
            executar_comando("pkg", "update && pkg upgrade")

        # Segundo Nivel - Nmap
        elif nivel == 2:
            while True:         
                argumento = input("NMAP: ").strip()
                if argumento:
                    os.system("clear")
                    executar_comando("nmap", argumento)

                voltar = input("'v' para voltar ao menu ou 'ENTER' para continuar com NMAP: ")
                if voltar.lower() == 'v':
                    break

        # Terceiro Nivel - SQLmap
        elif nivel == 3:
            while True:
                # Alterando para a execução correta do comando
                requerimento = input("requerimento: ").strip()
                if requerimento:
                    os.system(f"cd $HOME/sqlmap && python3 sqlmap.py {requerimento}")

                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SQLmap: ")
                if continuar.lower() == 'v':
                    break

        # Sherlock
        elif nivel == 4:
            while True:
                username = input("USERNAME: ").strip()
                if username:
                    os.system(f"cd $HOME/sherlock && ./sherlock {username}")

                voltar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SHERLOCK: ")
                if voltar.lower() == 'v':
                    break

        # MrHolmes
        elif nivel == 5:
            while True:
                # Alterando para a execução correta do comando
                print("Iniciando o MrHolmes...")
                os.system("cd $HOME/Mr.Holmes && python3 MrHolmes.py")

                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com MR.HOLMES: ")
                if continuar.lower() == 'v':
                    break

        # Scan Subdomínios
        elif nivel == 6:
            while True:
                if os.path.isfile("subf.py"):
                    executar_script("subf.py")
                else:
                    print("subf.py não encontrado!")

                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SCAN SUBDOMÍNIOS: ")
                if continuar.lower() == 'v':
                    break

        # Scan Hosts Proxys
        elif nivel == 7:
            while True:
                if os.path.isfile("scanfast.py"):
                    executar_script("scanfast.py")
                else:
                    print("scanfast.py não encontrado!")

                continuar = input("'v' para voltar ao menu ou 'ENTER' para continuar com SCAN HOSTS PROXYS: ")
                if continuar.lower() == 'v':
                    break

        # Execução de outro script
        elif nivel == 8:
            while True:
                script = input("Scripts.py: ").strip()
                if script.lower() == 'sair':
                    break
                if os.path.isfile(script):
                    executar_script(script)
                    input("Pressione Enter para voltar ao menu...")
                else:
                    print("Script não encontrado!")

        # Sair
        elif nivel == 9:
            print("Saindo do Script...")
            escolha = True

        # Reiniciar o Menu
        elif nivel == 10:
            reiniciar()

if __name__ == "__main__":
    main()