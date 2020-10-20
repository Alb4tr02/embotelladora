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
| username | POST | Nombre de usuario |                                                                                                                                                                   
| password | POST | Contraseña del nuevo usuario |
| email | POST | Correo de registro del nuevo usuario |
| nombres | POST | Nombres completos del nuevo usuario |
| apellidos | POST | Apellidos completos del nuevo usuario |
| rol | POST | "C" para cliente, "F" para fabricante |
| genero | POST | "M" para masculino, "F" para femenino, "O" para otros |
                                                                                                 
##### Respuesta                                                                                                                                                                                                      
En caso de que la petición sea exitosa se envía un json con el siguiente formato:
                                                                                                                                                  
| Nombre | Descripción |                                                                                                                                                                                             
| ------ | ------ |                                                                                                                                                                                                  
| username | username del nuevo usuario |                                          
| email | Email del nuevo usuario |                                 

En caso contrario se envía un json con el siguiente formato:  

| Nombre | Descripción |
| ------ | ------ |
| nombre_campo | Mensaje explicativo del error ocurrido con el campo |

##### Códigos de respuesta
A continuación se incluye la lista de de los posibles códigos que se pueden obtener al realizar una petición y su significado

|Código | Significado |
| ------ | ------ |
| 200 | El usuario fue creado con exito |
| 400 |  Error de formato, puede producirse porque faltan parámetros en el json o porque username o correo ya se encuentran registrados |
| 500 | Error en la base de datos, puede producirse por fallos en la conexión a la base de datos |


##### Ejemplos curl
.
```shell script
# usuario creado sin problemas
$ curl -X POST -H 'Content-Type: application/json' -d '{"username": "pepito", "password": "pepito", "email": "pepito@gmail.com", "rol": "C", "nombres": "pepito", "apellidos": "perez", "genero": "M"}' https://embotelladora.herokuapp.com/user/create/
{"username": "pepito", "email": "pepito@gmail.com"}

# username ya registrado
$ curl -X POST -H 'Content-Type: application/json' -d '{"username": "pepito", "password": "pepito", "email": "pepito@gmail.com", "rol": "C", "nombres": "pepito", "apellidos": "perez", "genero": "M"}' https://embotelladora.herokuapp.com/user/create/
{"username": ["username o email ya registrado"]}
```

## · Login de usuarios                                                                                                                                                                     
- URL: **/user/login/**                                                                                                                                                                                              
- Métodos: POST                                                                                                                                                                                                      
- Descripción: mediante este endpoint y el método **POST** se pueden loguear usuarios en la plataforma                                                                                  
##### Entrada                                                                                                                                                                                                        
Mediante el método POST se envía un Json con el siguiente formato:                                                                                                                                                   
                                                                                                                                                                                                                     
| Nombre | Méteodo | Descripción |                                                                                                                                                                                             
| ------ | ----------|------ |                                                                                                                                                                                                  
| username | POST | Nombre de usuario |                                                                                                                                                                   
| password | POST | Contraseña del usuario |
                                                                                                 
##### Respuesta                                                                                                                                                                                                      
En caso de que la petición sea exitosa se envía un json con el siguiente formato:
                                                                                                                                                  
| Nombre | Descripción |                                                                                                                                                                                             
| ------ | ------ |                                                                                                                                                                                                  
| token | token necesario para autentificarse en la plataforma |                                          
| email | Email del usuario |
| user_id | id único que identifica al usuario |
                                 

En caso contrario se envía un json con el siguiente formato:  

| Nombre | Descripción |
| ------ | ------ |
| error | Mensaje explicativo del error ocurrido |

##### Códigos de respuesta
A continuación se incluye la lista de de los posibles códigos que se pueden obtener al realizar una petición y su significado

|Código | Significado |
| ------ | ------ |
| 200 | El usuario fue autenticado con exito |
| 400 |  Error de formato, puede producirse porque faltan parámetros en el json o porque no se encuentra el usuario |
| 500 | Error en la base de datos, puede producirse por fallos en la conexión a la base de datos |


##### Ejemplos curl
.
```shell script
# usuario autenticado con exito
$ curl -X POST -H 'Content-Type: application/json' -d '{"username": "pepito23", "password": "pepito"}' https://embotelladora.herokuapp.com/user/login/
{"token":"495818faa9648a144b28436baa259729041a5696","user_id":8,"email":"pepito@gmail.com"}

# usuario no encontrado
$ curl -X POST -H 'Content-Type: application/json' -d '{"username": "pepito23", "password": "wrong_password"}' https://embotelladora.herokuapp.com/user/login/
{"error":["usuario no encontrado"]}
```


## · Registro de Cervezas                                                                                                                                                                     
- URL: **/cerveza/create/**                                                                                                                                                                                              
- Métodos: POST                                                                                                                                                                                                      
- Descripción: mediante este endpoint y el método **POST** un fabricante puede registrar nuevos tipos de cervezas.                                                                                  
##### Entrada                                                                                                                                                                                                        
Mediante el método POST se envía un Json con el siguiente formato:                                                                                                                                                   
                                                                                                                                                                                                                     
| Nombre | Méteodo | Descripción |                                                                                                                                                                                             
| ------ | ----------|------ |                                                                                                                                                                                                  
| precio | POST | Precio por botella |                                                                                                                                                                   
| color | POST | Color de la cerveza, "M" para rubia, "N" para negra, "A" para ambar y "R" para roja |
| alcohol | POST | Porcentaje de alcohol de la cerveza |
| fermentacion | POST | Tipo de fermentación de la cerveza, "A" para Ale, "L" para Larger y "H" para Híbrida |
| nombre | POST | Nombre de la cerveza |

*Nota: Para registrar cervezas se debe estar logueado como fabricante
                                                                                                 
##### Respuesta                                                                                                                                                                                                      
En caso de que la petición sea exitosa se envía un json con el formato anterior:
                                                                               
                                 

En caso contrario se envía un json con el siguiente formato:  

| Nombre | Descripción |
| ------ | ------ |
| field_name | Mensaje explicativo del error ocurrido |

##### Códigos de respuesta
A continuación se incluye la lista de de los posibles códigos que se pueden obtener al realizar una petición y su significado

|Código | Significado |
| ------ | ------ |
| 201 | La cerveza fue registrada con exito |
| 400 |  Error de formato, puede producirse porque faltan parámetros en el json o porque o porque ya se registró una cerveza con ese nombre |
| 500 | Error en la base de datos, puede producirse por fallos en la conexión a la base de datos |


##### Ejemplos curl
.
```shell script
# cerveza registrada con exito
$ curl -v -X POST -H 'Content-Type: application/json' -H 'Authorization: Token eebc7ce8608dcf3a302b8cc2c76986b36e7d1b0a' -d '{"precio": 5000, "color": "M", "alcohol": 4.5, "fermentacion": "A", "nombre": "Policarpa2"}' https://embotelladora.herokuapp.com/cerveza/create/
{"precio":5000,"color":"M","alcohol":4.5,"fermentacion":"A","nombre":"Policarpa2"}

# registro con nombre de cerveza repetido
$ curl -v -X POST -H 'Content-Type: application/json' -H 'Authorization: Token eebc7ce8608dcf3a302b8cc2c76986b36e7d1b0a' -d '{"precio": 5000, "color": "M", "alcohol": 4.5, "fermentacion": "A", "nombre": "Policarpa2"}' https://embotelladora.herokuapp.com/cerveza/create/
{"nombre":["Ya existe un/a cerveza model con este/a nombre."]}
```


