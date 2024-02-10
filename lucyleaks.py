import requests
import time
import argparse
import random
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Função para gerar uma cor aleatória do arco-íris
def cor_arco_iris():
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return random.choice(cores)

# Função para exibir a nova ASCII Art colorida com degradê
def exibir_ascii_art():
    linhas_ascii_art = [
        "  _                       _               _        ",
        " | |   _   _  ___ _   _  | |    ___  __ _| | _____ ",
        " | |  | | | |/ __| | | | | |   / _ \/ _` | |/ / __|",
        " | |__| |_| | (__| |_| | | |__|  __| (_| |   <\__ \\",
        " |_____\\__,_|\\___|\\__, | |_____\\___|\\__,_|_|\\_\\___/",
        "                  |___/                            "
    ]

    for linha in linhas_ascii_art:
        cor = cor_arco_iris()
        print(f"{cor}{linha}{Style.RESET_ALL}")

# Função para exibir os detalhes de um resultado
def exibir_detalhes_resultado(resultado):
    print(f"{Fore.RED}[*] Email: {resultado.get('email')}")
    print(f"{Fore.YELLOW}[*] Senha: {resultado.get('password')}")
    print(f"{Fore.GREEN}[*] Hash: {resultado.get('hash')}")
    print(f"{Fore.CYAN}[*] sha1: {resultado.get('sha1')}")
    print(f"{Fore.BLUE}[*] Sources: {', '.join(resultado.get('sources', []))}")

# Função para consultar a API de BreachDirectory
def consultar_brecha(consulta):
    api_key = "SUA-CHAVE-DE-API-AQUI"
    headers = {
        'X-RapidAPI-Key': api_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    resultados_totais = []

    for item in consulta:
        url = f"https://api.breachdirectory.org/rapidapi-IscustemTaingtowItrionne?func=auto&term={item}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            json_data = response.json()
            resultados_totais.extend(json_data.get("result", []))
            exibir_resultados(json_data)
        else:
            print(f"{Fore.RED}[!] Erro na requisição. Código de status: {response.status_code}")
            print(f"{Fore.RED}[!] Continuando com o próximo item...")

        time.sleep(1)

    return resultados_totais

# Função para exibir os resultados formatados
def exibir_resultados(json_data):
    if "result" in json_data and isinstance(json_data["result"], list):
        resultados = json_data["result"]

        for resultado in resultados:
            print(f"{Fore.RED}[*] {'=' * 40}")
            exibir_detalhes_resultado(resultado)

# Função para exibir o menu de ajuda
def exibir_menu_ajuda():
    print("\nModo de Uso:")
    print("-e, --email\t\tConsultar um único endereço de e-mail.")
    print("-l, --lista\t\tConsultar uma lista de endereços de e-mail, senhas ou usuários a partir de um arquivo.")
    print("-h, --help\t\tExibir este menu de ajuda.\n")

# Adicionando os créditos
print(f"{Fore.RED}Desenvolvido por: David A. Mascaro\n{Style.RESET_ALL}")
exibir_ascii_art()

# Configurando o parser de argumentos
parser = argparse.ArgumentParser(description='Consultar a API de BreachDirectory para verificar se um e-mail, senha ou usuário foi comprometido em vazamentos de dados.')
parser.add_argument('-e', '--email', help='Endereço de e-mail para consulta.')
parser.add_argument('-l', '--lista', help='Caminho para arquivo contendo uma lista de e-mails, senhas ou usuários.')
args = parser.parse_args()

# Verificando as opções fornecidas
if args.email:
    consulta = [args.email]
elif args.lista:
    with open(args.lista, 'r') as file:
        consulta = [line.strip() for line in file.readlines()]
else:
    entrada = input(f"{Fore.RED}Escolha uma opção:\n1 - Digitar endereço de e-mail\n2 - Carregar lista de e-mails, senhas ou usuários de um arquivo\n{Style.RESET_ALL}")
    if entrada == "1":
        consulta = [input(f"{Fore.RED}Digite o endereço de e-mail, senha ou usuário: {Style.RESET_ALL}")]
    elif entrada == "2":
        arquivo = input(f"{Fore.RED}Digite o caminho do arquivo contendo a lista: {Style.RESET_ALL}")
        with open(arquivo, 'r') as file:
            consulta = [line.strip() for line in file.readlines()]
    else:
        print(f"{Fore.RED}[!] Opção inválida. Saindo.")
        exit()

# Consultando a API e exibindo resultados
resultados_totais = consultar_brecha(consulta)

# Perguntando se deseja salvar em um arquivo
if input(f"{Fore.RED}[?] Deseja salvar os resultados em um arquivo? (s/n): {Style.RESET_ALL}").lower() == 's':
    arquivo_saida = input(f"{Fore.RED}[?] Digite o nome do arquivo de saída: {Style.RESET_ALL}")
    with open(arquivo_saida, 'w') as file:
        for resultado in resultados_totais:
            file.write(f"{Fore.RED}[*] {'=' * 40}\n")
            for chave, valor in resultado.items():
                file.write(f"{Fore.RED}[*] {chave}: \"{valor}\"\n")
    print(f"{Fore.RED}[+] Resultados salvos em {arquivo_saida}")

# Adicionando os créditos no final da output
print(f"{Fore.RED}Desenvolvido por: David A. Mascaro{Style.RESET_ALL}")
