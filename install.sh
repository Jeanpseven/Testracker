#!/bin/bash

echo "Instalando dependências..."

# Instalar o pacote GeoIP2 para Python diretamente do GitHub
pip install git+https://github.com/maxmind/GeoIP2-python.git

echo "Baixando o GeoLite2..."

# URL para o arquivo GeoLite2-City.mmdb.gz via GitHub
download_url="https://github.com/maxmind/GeoLite2-City/releases/latest/download/GeoLite2-City.mmdb.gz"

# Nome do arquivo compactado
zip_file="GeoLite2-City.mmdb.gz"

# Nome do arquivo descompactado
geoip_file="GeoLite2-City.mmdb"

# Baixar o arquivo compactado
wget $download_url

# Descompactar o arquivo
gunzip $zip_file

echo "GeoLite2 baixado com sucesso!"
