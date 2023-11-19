#!/bin/bash

echo "Baixando o GeoLite2..."

# URL para o arquivo GeoLite2-City.mmdb.gz
download_url="https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"

# Nome do arquivo compactado
zip_file="GeoLite2-City.mmdb.gz"

# Nome do arquivo descompactado
geoip_file="GeoLite2-City.mmdb"

# Baixar o arquivo compactado
wget $download_url

# Descompactar o arquivo
gunzip $zip_file

echo "GeoLite2 baixado com sucesso!"
