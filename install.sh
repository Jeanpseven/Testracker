#!/bin/bash

echo "Instalando dependências e criando ambiente virtual..."

# Nome do ambiente virtual
venv_name="myenv"

# Criar e ativar o ambiente virtual
python -m venv $venv_name
source ./$venv_name/bin/activate

# Tentar instalar o pacote GeoIP2 para Python diretamente do GitHub dentro do ambiente virtual
pip install git+https://github.com/maxmind/GeoIP2-python.git

# Verificar se a instalação foi bem-sucedida ou se há um erro
if [ $? -ne 0 ]; then
    echo "Erro ao instalar GeoIP2. Tentando instalar geolite2..."
    
    # Tentar instalar o pacote geolite2 para Python diretamente do GitHub dentro do ambiente virtual
    pip install git+https://github.com/lelit/geolite2.git

    # Verificar se a instalação foi bem-sucedida ou se há outro erro
    if [ $? -ne 0 ]; then
        echo "Erro ao instalar geolite2. Certifique-se de ter o python3-venv instalado e tente novamente."
        # Sair do script com código de erro
        exit 1
    fi
fi

echo "Baixando o GeoLite2..."

# URL para o arquivo GeoLite2-City.mmdb.gz via GitHub
download_url="https://github.com/maxmind/GeoLite2-City/releases/latest/download/GeoLite2-City.mmdb.gz"

# Nome do arquivo compactado
zip_file="GeoLite2-City.mmdb.gz"

# Baixar o arquivo compactado
wget $download_url

# Descompactar o arquivo
gunzip $zip_file

echo "GeoLite2 baixado com sucesso!"

# Desativar o ambiente virtual
deactivate
