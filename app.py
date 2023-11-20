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

def run_app():
    port = 80
    while True:
        try:
            app.run(host='0.0.0.0', port=port, debug=False)
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"A porta {port} já está em uso. Tentando outra porta.")
                port += 1
            else:
                print(f"Erro ao iniciar o aplicativo: {e}")
                break

if __name__ == '__main__':
    run_app()
