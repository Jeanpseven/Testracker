from flask import Flask, render_template, request
from urllib.request import urlretrieve
import gzip
import shutil
import os
from geolite2 import geolite2
from datetime import datetime

# Função para baixar e descompactar o GeoLite2
def download_geolite2():
    download_url = "https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"
    local_path = "GeoLite2-City.mmdb.gz"
    geoip_path = "GeoLite2-City.mmdb"

    try:
        # Baixar o arquivo compactado
        urlretrieve(download_url, local_path)

        # Descompactar o arquivo
        with gzip.open(local_path, 'rb') as f_in, open(geoip_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

        # Remover o arquivo compactado
        os.remove(local_path)

        print("GeoLite2 baixado com sucesso!")

    except Exception as e:
        print(f"Erro durante o download/descompactação do GeoLite2: {e}")

# Verificar se o arquivo GeoLite2 existe e se está desatualizado
def is_geoip_outdated():
    geoip_path = "GeoLite2-City.mmdb"

    if not os.path.exists(geoip_path):
        return True

    # Comparar datas de modificação
    current_time = datetime.now()
    modified_time = datetime.fromtimestamp(os.path.getmtime(geoip_path))
    days_difference = (current_time - modified_time).days

    # Se o arquivo tem mais de 7 dias, considerar desatualizado
    return days_difference > 7

# Instalar o pacote GeoIP2 para Python diretamente do GitHub
try:
    os.system("pip install git+https://github.com/maxmind/GeoIP2-python.git")
    print("Pacote GeoIP2-python instalado com sucesso!")
except Exception as e:
    print(f"Erro durante a instalação do pacote GeoIP2-python: {e}")

if is_geoip_outdated():
    print("Baixando GeoLite2...")
    download_geolite2()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.remote_addr
        geo_data = geolite2.lookup(ip_address)
        if geo_data is not None:
            latitude = geo_data.latitude
            longitude = geo_data.longitude
            location = geolite2.get_name_by_ip(ip_address)
            return render_template('index.html', latitude=latitude, longitude=longitude, location=location)
        else:
            return render_template('index.html', error='IP address not found.')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
