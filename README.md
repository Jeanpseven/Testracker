# Testracker
Teste de script que rastreia por link

# Projeto Flask GeoLocation

Este é um projeto simples usando Flask para rastrear a localização do usuário com base no endereço IP.

## Configuração Inicial

Antes de executar o projeto, certifique-se de ter o Python instalado em seu ambiente. Recomenda-se o uso de um ambiente virtual.

1. Instale as dependências:
   pip install flask geolite2Baixe o arquivo GeoLite2-City.mmdb usando o script fornecido:python app.py
   Executando o Projeto
   Execute o seguinte comando para iniciar o servidor Flask:
   python app.py
   O aplicativo estará disponível em http://127.0.0.1:5000/.
   Para acessá-lo de outras máquinas, substitua 127.0.0.1 pelo endereço IP do seu servidor.
   Estrutura de Diretórios
   app.py: Script principal do Flask.
   templates/: Pasta que contém os arquivos HTML, incluindo index.html.
   Personalização
   Personalize o HTML em templates/index.html conforme necessário para atender aos requisitos do seu projeto.
   Considere ajustar as configurações de segurança, como firewall, ao tornar o aplicativo acessível pela internet.
   Notas Adicionais
   Este projeto usa o GeoLite2 para obter informações de localização com base no endereço IP do usuário.
