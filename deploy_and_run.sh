#!/bin/bash

# Instale o Apache2
sudo apt-get update
sudo apt-get install -y apache2

# Crie um diretório para o site
sudo mkdir /var/www/meusite

# Copie o index.html para o diretório do site
cp index.html /var/www/meusite/

# Configure as permissões
sudo chown -R www-data:www-data /var/www/meusite

# Configure o VirtualHost do Apache
cat <<EOL | sudo tee /etc/apache2/sites-available/meusite.conf
<VirtualHost *:80>
    ServerAdmin webmaster@meusite
    DocumentRoot /var/www/meusite

    ErrorLog \${APACHE_LOG_DIR}/error.log
    CustomLog \${APACHE_LOG_DIR}/access.log combined

    <Directory /var/www/meusite>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOL

# Ative o VirtualHost e reinicie o Apache
sudo a2ensite meusite.conf
sudo systemctl restart apache2

# Permita tráfego no firewall
sudo ufw allow 80

# Execute o aplicativo Flask
python3 seu_app.py &

# Obtenha o IP público do servidor
public_ip=$(curl -s ifconfig.me)

# Informe o usuário sobre como acessar o site e o aplicativo
echo "Configuração concluída."
echo "Seu site está agora acessível publicamente em http://${public_ip}/"
echo "Seu aplicativo Flask está em execução no IP interno do servidor."
