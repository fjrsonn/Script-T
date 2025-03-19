import http.client
import threading
import time
import pyfiglet
import rich
from rich.console import Console
from collections import defaultdict, deque


esp = ' '
banner1 = pyfiglet.figlet_format(f'{esp*4}S c a n', font='slant')
banner2 = pyfiglet.figlet_format(f'{esp*5}F l a r e', font='slant')
banner3 = pyfiglet.figlet_format(f'{esp*5}F r o n t', font='slant')
rich.print(f'[magenta]{banner1}[/magenta]')
rich.print(f'[magenta]{banner2}[/magenta]')
rich.print(f'[magenta]{banner3}[/magenta]')
time.sleep(2)


with open("allhosts.txt", "r") as allhosts:
    linhas = [line.strip() for line in allhosts if line.strip()]


server_host = str(input('Digite seu Dominio: '))


results_lock = threading.Lock()
print_lock = threading.Lock()
print_queue = deque()


proxy_order = {proxy: {'HEAD': None, 'PATCH': None, 'PUT': None, 'DELETE': None, 'OPTIONS': None} for proxy in linhas}

console = Console()

def scan_proxy(proxy):
    proxy_host = proxy.split(':')[0]
    proxy_port = int(proxy.split(':')[1]) if ':' in proxy else 80

    local_results = []
    success_methods = []
    failed_methods = []

    for method in ['HEAD', 'PATCH', 'PUT', 'DELETE', 'OPTIONS']:
        try:
            conn = http.client.HTTPConnection(proxy_host, proxy_port, timeout=3)
            conn.request(method, "/", headers={"Host": server_host})

            response = conn.getresponse()
            status = response.status
            status_message = f"Status {status}"
            
            result_line = f"Escaneando {method} {proxy} {status_message} Host Salvo"
            
            if status == 101 or status == 200:
                with results_lock:
                    if method in proxy_order[proxy]:
                        proxy_order[proxy][method] = status_message
                        with print_lock:
                            print(f"\033[1;33m{result_line}\033[m")  
                success_methods.append(method)
            else:
                failed_methods.append(method)
                local_results.append(f"{method} - Status {status}")
        except Exception as e:
            failed_methods.append(method)
            local_results.append(f"{method} - Error: {e}")

    if success_methods or failed_methods:
        success_str = ', '.join(success_methods) if success_methods else 'Nenhum'
        failed_str = ', '.join(failed_methods) if failed_methods else 'Nenhum'
        with results_lock:
            with print_lock:
                print()  
                console.print(f"[grey60]Métodos que funcionaram para o Proxy {proxy}: {success_str}[/grey60]")
                print()  
                console.print(f"[red]Métodos que falharam: {failed_str}[/red]")
                print()  

def worker(proxy):
    scan_proxy(proxy)

def organize_hosts():
    with open("hosts_ordenados.txt", "w") as file:
        for proxy in linhas:  
            if proxy in proxy_order:
                for method in ['HEAD', 'PATCH', 'PUT', 'DELETE', 'OPTIONS']:
                    status_message = proxy_order[proxy][method]
                    if status_message:
                        file.write(f"{method} {proxy} {status_message}\n")

    print("Arquivo hosts_ordenados.txt criado.")

def main():
    threads = []

    for proxy in linhas:
        thread = threading.Thread(target=worker, args=(proxy,))
        thread.start()
        threads.append(thread)
        
        
        if len(threads) >= 10:
            for thread in threads:
                thread.join()
            threads = []

    
    for thread in threads:
        thread.join()

    organize_hosts()

if __name__ == "__main__":
    main()
