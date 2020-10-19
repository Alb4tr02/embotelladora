#  Sistema de información y control para una embotelladora de bajo costo
Este es un servicio creado en Python mediante el framework Django para administrar y controlar una embotelladora de bajo costo. Algunas de sus funcionalidades son.
  - Registro y login de usuarios.
  - Registro de fabricantes.
  - Creación de pedidos para la embotelladora.
  - Control de la embotelladora por parte del fabricante.

La aplicación se encuentra alojada en Heroku y puede ser accedida mediante https://embotelladora.herokuapp.com/  
  Para ejecutar la aplicación en un entorno local siga las siguientes instrucciones:
# Antes de comenzar
  - Clone el repositorio mediante git clone
  - Asegúrese de crear y activar un entorno virtual mediante ```$python3 -m venv venv```
  - Instalar los requerimientos mediante ```$pip install -r requirements.txt```
  - Asegúrese de crear una base de datos en postgres.
  - Declare el nombre, el usuario y la contraseña de la base de datos como variables de entorno mediante:
  ```shell script                                                                                                                                                                                                              
$ export DB_NAME=<nombre base de datos>                                                                                                                                                                                    
$ export USER=<nombre usuario postgres>
$ export PASSWORD=<password de USER para acceder a la base de datos>                                                                                                                                                                                         
``` 
- Genere y aplique las migraciones necesarias en la base de datos mediante:
```shell script
$ python manage.py makemigrations
$ python manage.py migrate
```                       
- Lance el servicio mediante
```shell script
$ python manage.py runserver
```                                                                                                                                                                                          
# Endpoints                                                                                                                                                                                                          
## · Creación de usuarios                                                                                                                                                                     
- URL: **/user/create**                                                                                                                                                                                              
- Métodos: POST                                                                                                                                                                                                      
- Descripción: mediante este endpoint y el método **POST** se pueden crear nuevos usuarios en la plataforma                                                                                  
##### Entrada                                                                                                                                                                                                        
Mediante el método POST un Json con el siguiente formato:                                                                                                                                                   
                                                                                                                                                                                                                     
| Nombre | Méteodo | Descripción |                                                                                                                                                                                             
| ------ | ----------|------ |                                                                                                                                                                                                  
| username | POST | Nombre del nuevo usuario |                                                                                                                                                                   
| password | POST | Contraseña del nuevo usuario |
| email | POST | Correo de registro del nuevo usuario |
| nombres | POST | Nombres completos del nuevo usuario |
| apellidos | POST | Apellidos completos del nuevo usuario |
                                                                                                 
##### Respuesta                                                                                                                                                                                                      
En caso de que la petición sea exitosa se envía un json con el siguiente formato:
                                                                                                                                                  
| Nombre | Descripción |                                                                                                                                                                                             
| ------ | ------ |                                                                                                                                                                                                  
| username | username del nuevo usuario |                                          
| email | Email del nuevo usuario |                                 

En caso contrario se envía un json con el siguiente formato:  

| Nombre | Descripción |
| ------ | ------ |
| error | Mensaje explicativo del error ocurrido |

##### Códigos de respuesta
A continuación se incluye la lista de de los posibles códigos que se pueden obtener al realizar una petición y su significado

|Código | Significado |
| ------ | ------ |
| 201 | El usuario fue creado con exito |
| 400 |  Error de formato, puede producirse porque faltan parámetros en el json |
| 403 |  El username o correo ya se encuentran registrados |
| 500 | Error en la base de datos, puede producirse por fallos en la conexión a la base de datos |


##### Ejemplos curl
.
```shell script
# usuario creado sin problemas
$ curl -X POST -H 'Content-Type: application/json' -d '{"username": "pepito", "password": "pepito", "email": "pepito@gmail.com", "rol": "C", "nombres": "pepito", "apellidos": "perez", "genero": "M"}' https://embotelladora.herokuapp.com/user/create/
{"username": "pepito", "email": "pepito@gmail.com"}

# username ya registrado
$ curl -X POST -H 'Content-Type: application/json' -d '{"username": "pepito", "password": "pepito", "email": "pepito@gmail.com", "rol": "C", "nombres": "pepito", "apellidos": "perez", "genero": "M"}' https://embotelladora.herokuapp.com/user/create/
{"error":"username o email ya registrado"}
