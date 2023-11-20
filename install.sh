#!/bin/bash

echo "Instalando dependências..."

# Tentar instalar o pacote GeoIP2 para Python diretamente do GitHub
pip install git+https://github.com/maxmind/GeoIP2-python.git

# Verificar se a instalação foi bem-sucedida ou se há um erro
if [ $? -ne 0 ]; then
    echo "Erro ao instalar GeoIP2. Certifique-se de ter o pip e o python3 instalados e tente novamente."
    # Sair do script com código de erro
    exit 1
fi

echo "Baixando o GeoLite2..."

# URL para o arquivo GeoLite2-City.mmdb.gz via GitHub (raw)
download_url="https://github.com/wp-statistics/GeoLite2-City/raw/master/GeoLite2-City.mmdb.gz"

# Nome do arquivo compactado
zip_file="GeoLite2-City.mmdb.gz"

# Baixar o arquivo compactado
wget --output-document=$zip_file $download_url

# Descompactar o arquivo
gunzip $zip_file

echo "GeoLite2 baixado com sucesso!"
