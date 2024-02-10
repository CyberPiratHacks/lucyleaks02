import requests
import time
import argparse

# Função para exibir a ASCII Art colorida
def exibir_ascii_art():
    print('''
\033[96m██▓     █    ██  ▄████▄  ▓██   ██▓ ██▓    ▓█████  ▄▄▄       ██ ▄█▀  ██████ 
▓██▒     ██  ▓██▒▒██▀ ▀█   ▒██  ██▒▓██▒    ▓█   ▀ ▒████▄     ██▄█▒ ▒██    ▒ 
▒██░    ▓██  ▒██░▒▓█    ▄   ▒██ ██░▒██░    ▒███   ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   
▒██░    ▓▓█  ░██░▒▓▓▄ ▄██▒  ░ ▐██▓░▒██░    ▒▓█  ▄ ░██▄▄▄▄██ ▓██ █▄   ▒   ██▒
░██████▒▒▒█████▓ ▒ ▓███▀ ░  ░ ██▒▓░░██████▒░▒████▒ ▓█   ▓██▒▒██▒ █▄▒██████▒▒
░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░   ██▒▒▒ ░ ▒░▓  ░░░ ▒░ ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
░ ░ ▒  ░░░▒░ ░ ░   ░  ▒    ▓██ ░▒░ ░ ░ ▒  ░ ░ ░  ░  ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░
  ░ ░    ░░░ ░ ░ ░         ▒ ▒ ░░    ░ ░      ░     ░   ▒   ░ ░░ ░ ░  ░  ░  
    ░  ░   ░     ░ ░       ░ ░         ░  ░   ░  ░      ░  ░░  ░         ░  
                 ░         ░ ░                                              
\033[0m''')

# Função para exibir os detalhes de um resultado
def exibir_detalhes_resultado(resultado):
    exibir_item("Email", resultado.get("email"), "\033[91m")
    exibir_item("Senha", resultado.get("password"), "\033[92m")
    exibir_item("Hash", resultado.get("hash"), "\033[93m")
    exibir_item("sha1", resultado.get("sha1"), "\033[94m")
    exibir_item("Sources", ", ".join(resultado.get("sources", [])), "\033[95m")

# Função para exibir um item formatado
def exibir_item(nome, valor, cor):
    if valor is not None:
        print(f"{cor}{nome}: \"{valor}\" \033[0m")

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
            print(f"Erro na requisição. Código de status: {response.status_code}")
            print("Continuando com o próximo item...")

        time.sleep(1)

    return resultados_totais

# Função para exibir os resultados formatados
def exibir_resultados(json_data):
    if "result" in json_data and isinstance(json_data["result"], list):
        resultados = json_data["result"]

        for resultado in resultados:
            print("========================")
            exibir_detalhes_resultado(resultado)

# Função para exibir o menu de ajuda
def exibir_menu_ajuda():
    print("\nModo de Uso:")
    print("-e, --email\t\tConsultar um único endereço de e-mail.")
    print("-l, --lista\t\tConsultar uma lista de endereços de e-mail, senhas ou usuários a partir de um arquivo.")
    print("-h, --help\t\tExibir este menu de ajuda.\n")

# Adicionando a exibição da ASCII Art
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
    entrada = input("Escolha uma opção:\n1 - Digitar endereço de e-mail\n2 - Carregar lista de e-mails, senhas ou usuários de um arquivo\n")
    if entrada == "1":
        consulta = [input("Digite o endereço de e-mail, senha ou usuário: ")]
    elif entrada == "2":
        arquivo = input("Digite o caminho do arquivo contendo a lista: ")
        with open(arquivo, 'r') as file:
            consulta = [line.strip() for line in file.readlines()]
    else:
        print("Opção inválida. Saindo.")
        exit()

# Consultando a API e exibindo resultados
resultados_totais = consultar_brecha(consulta)

# Perguntando se deseja salvar em um arquivo
if input("Deseja salvar os resultados em um arquivo? (s/n): ").lower() == 's':
    arquivo_saida = input("Digite o nome do arquivo de saída: ")
    with open(arquivo_saida, 'w') as file:
        for resultado in resultados_totais:
            file.write(f"========================\n")
            for chave, valor in resultado.items():
                file.write(f"{chave}: \"{valor}\"\n")
    print(f"Resultados salvos em {arquivo_saida}")

print("\nDesenvolvido por David A. Mascaro")
