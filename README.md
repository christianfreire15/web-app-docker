# Comandos para levantar el servicio

1. Colocar las credenciales de IMAGGA en el archivo app.py

2. Crear la imagen con el comando
   `docker build -t web-app-docker .`

3. Habilitar el servicio con el comando
   `docker run -d -p 5000:5000 --name web-app-docker web-app-docker`




