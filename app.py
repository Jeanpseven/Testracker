from flask import Flask, render_template, request
from urllib.request import urlretrieve
import gzip
import shutil
import os
from geolite2 import geolite2

app = Flask(__name__)

# Função para baixar e descompactar o GeoLite2
def download_geolite2():
    download_url = "https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz"
    local_path = "GeoLite2-City.mmdb.gz"
    geoip_path = "GeoLite2-City.mmdb"

    # Baixar o arquivo compactado
    urlretrieve(download_url, local_path)

    # Descompactar o arquivo
    with gzip.open(local_path, 'rb') as f_in, open(geoip_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

    # Remover o arquivo compactado
    os.remove(local_path)

# Verificar se o arquivo GeoLite2 existe, se não, fazer o download
if not os.path.exists("GeoLite2-City.mmdb"):
    print("Baixando GeoLite2...")
    download_geolite2()

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
    download_geolite2()
    app.run(host='0.0.0.0', port=80)
