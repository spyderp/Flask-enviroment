# Ambiente de desarrollo para Flask

Este ambiente de desarrollo esta listo para empezar a trabajar, cuenta con base de datos y e instalado flask. Si crees que le hace falta algo por favor aportar. 

## Configuración

Luego de clonar el proyecto  y tener instalado docker solo debe hacer 2 pasos. 

 1. Crear un volumen para que nuestra base de datos no se pierda al reiniciar nuestra imagen.
```bash
sudo docker volume create --name dbdata
```
 2. Construir nuestra imagen si es la primera vez y subir nuestros servicios.
 ```bash
 sudo docker-compose up --build # si es tu primera vez o a realizado un cambio en dockerfile
 sudo docker-compose up # Para el resto de ocaciones.
 ```
 3. Acceder a tu navegador y colocar localhost y nuestro primer hola mundo en flask

**Nota:** El ambiente de desarrollo permite trabajar y ver cambios en vivo. No es necesario reiniciar la imagen de docker para ver los cambios. 

## Ambiente de desarrollo.

El entorno de desarrollo se encuentra en la carpeta ***flask/app*** se pueden agregar nuevas carpeta de ser necesario para su proyecto.


## Agregar nuevas librerías

Si deseas agregar nuevas librerías necesitas modificar el archivo **requirements.txt** el cual se encuentra dentro de la carpeta *flask* y ejecutar el siguiente comando.

 ```bash
 sudo docker-compose up --build 
 ```

## Connectarse a la base de datos.

Debe remplazar en los datos de conexión de su aplicación **localhost** por **db**
*Ejemplo:*
 ```python
 import mysql.connector as mysql
 db = mysql.connect(host='db', user='root', password='password', database='flask')
 ```


## Agradecimiento

Este entorno  de desarrollo es gracias  el tutorial de [Building a Flask app with Docker](https://pythonise.com/feed/flask/building-a-flask-app-with-docker-compose)