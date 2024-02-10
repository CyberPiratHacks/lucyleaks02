#!/bin/bash

# Definindo cores
GREEN='\033[0;32m'
RED='\033[0;31m'
VIOLET='\033[0;35m'
BROWN='\033[0;33m'
NC='\033[0m'  # Sem cor

# Arte ASCII
echo -e "\033[96m"
cat << "EOF"
██▓     █    ██  ▄████▄  ▓██   ██▓ ██▓    ▓█████  ▄▄▄       ██ ▄█▀  ██████ 
▓██▒     ██  ▓██▒▒██▀ ▀█   ▒██  ██▒▓██▒    ▓█   ▀ ▒████▄     ██▄█▒ ▒██    ▒ 
▒██░    ▓██  ▒██░▒▓█    ▄   ▒██ ██░▒██░    ▒███   ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   
▒██░    ▓▓█  ░██░▒▓▓▄ ▄██▒  ░ ▐██▓░▒██░    ▒▓█  ▄ ░██▄▄▄▄██ ▓██ █▄   ▒   ██▒
░██████▒▒▒█████▓ ▒ ▓███▀ ░  ░ ██▒▓░░██████▒░▒████▒ ▓█   ▓██▒▒██▒ █▄▒██████▒▒
░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░   ██▒▒▒ ░ ▒░▓  ░░░ ▒░ ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
░ ░ ▒  ░░░▒░ ░ ░   ░  ▒    ▓██ ░▒░ ░ ░ ▒  ░ ░ ░  ░  ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░
  ░ ░    ░░░ ░ ░ ░         ▒ ▒ ░░    ░ ░      ░     ░   ▒   ░ ░░ ░ ░  ░  ░  
    ░  ░   ░     ░ ░       ░ ░         ░  ░   ░  ░      ░  ░░  ░         ░  
                 ░         ░ ░                                              
EOF
echo -e "\033[0m"
echo -e "${VIOLET}SCRIPT LUCYLEAKS DESENVOLVIDO POR DAVID A. MASCARO${NC}"

# Pergunta se deseja baixar e atualizar os pacotes APT do Kernel
echo -e "${GREEN}Deseja baixar e atualizar os pacotes completos APT do Kernel?${NC} ${RED}(s/n)${NC}"
read -r resposta01

# Lendo resposta
if [ "$resposta01" = "s" ]; then
    echo -e "${RED}Realizando instalação e atualização dos pacotes, por favor aguarde...${NC}"
    # Executando ação
    sudo apt update && sudo apt full-upgrade -y && clear

elif [ "$resposta01" = "n" ]; then
    echo -e "${VIOLET}Instalação dos pacotes negada!${NC}"
    # Executando ação
    clear

else
    echo -e "${BROWN}Comando Inválido!${NC}"
    # Executando ação
    clear
fi

# Pergunta se deseja instalar e executar o LucyLeaks imediatamente
echo -e "${GREEN}DESEJA INSTALAR E EXECUTAR O LUCYLEAKS IMEDIATAMENTE?${NC} ${RED}(s/n)${NC}"
read -r resposta02

# Lendo resposta
if [ "$resposta02" = "s" ]; then
    echo -e "${RED}Realizando instalação do LucyLeaks, por favor aguarde...${NC}"
    # Clonando repositório
    git clone https://github.com/CyberPiratHacks/lucyleaks02.git
    clear
    # Navegando até a pasta
    cd lucyleaks02
    # Instalando os requisitos
    pip3 install http.client
    pip3 install argparse
    pip3 install requests
    pip3 install colorama
    clear
    # Executando o programa
    python3 lucyleaks.py

elif [ "$resposta02" = "n" ]; then
    echo -e "${PURPLE}Tudo bem! Até mais... ;)${NC}"

else
    echo -e "${BROWN}Comando Inválido!${NC}"
    # Executando ação
    clear
fi
