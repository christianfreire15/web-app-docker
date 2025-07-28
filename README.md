# Comandos para levantar el servicio

1. Colocar las credenciales de IMAGGA en el archivo app.py
  
2. Crear la imagen con el comando
  `docker build -t web-app-docker .`
  
3. Habilitar el servicio con el comando
  `docker run -d -p 5000:5000 --name web-app-docker web-app-docker`
  
4. URL accesible
  `http://localhost:5000/`
  
5. Descripción
  
  * Existe una página principal donde se encuentran cargadas 3 imágenes con una url pública
    
  * Mediante el botón "Analizar" se realizará la consulta mediante API al servicio de IMAGGA donde se obtendrá las etiquetas de cada imagen

  * Mediante el botón "Historial" se podrá visualizar el historial de resultados obtenidos
