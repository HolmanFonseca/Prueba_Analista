# Prueba_Analista


Este repositorio muestra el paso a paso para realizar un web service el cual expone un endpoint que retorna los 5 países con mayor densidad demográfica del mundo, de acuerdo a la api https://restcountries.com/v3.1/all

### Comenzando <img src="/imagenes/cohete.jpg" width="30" height="30">
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos <img src="/imagenes/requisitos.jpg" width="30" height="30">

Instalar: <br>
- pandas <br>
- uvicorn <br>
- http3 <br>
- fast api <br>
- mysql-connector-python <br>
- nest-asyncio <br> 
- (opcional) mysql workbench
### Instalación <img src="/imagenes/instalacion.jpg" width="30" height="30">

- pip install pandas == 1.0.5
- pip install uvicorn == 0.14.0
- pip install http3 == 0.6.7
- pip install fastapi == 0.74.0
- pip install mysql-connector-python == 8.0.28
- pip install nest-asyncio == 1.5.4

### Desarrolo de la prueba <img src="/imagenes/portatil.png" width="30" height="30">

1. Crea una cuenta gratuita de AWS y una cuenta gratuita de Azure DevOps. 

Se crearon las cuentas gratuitas en aws y azure devops lo cual se puede comprobar en las siguientes imagenes:

<img src="/imagenes/Cuentaaws.PNG">
<img src="/imagenes/cuentaazuredevops.PNG">

2. Crea una base de datos relacional utilizando el servicio RDS de AWS. La base de datos solo
debe tener una tabla. (Selecciona el motor de base de datos de tu preferencia).

Se decidió utilizar mysql como base de datos RDS en aws, se siguieron los pasos de instalacion y finalmente a continuacion se muestra la instancia de la base de datos creada
llamada db-prueba-analista:

<img src="/imagenes/A.PNG">

Para crear la base de datos dentro de la intancia y la tabla se desarrollo el código CreateTable.py que por medio de la libreria de mysql permite hacer consultas dentro de python.Finalmente a continuacion se muestra la tabla creada la cual se llama logs y sus correspondientes campos.

<img src="/imagenes/Table.PNG">

3.Utilizando el lenguaje de programación de tu preferencia, crea un Web services decualquier naturaleza (REST, SOAP, GraphQL). Dicho Web services debe consumir la siguiente API REST que retorna información de todos los países del mundo:

https://restcountries.com/v3.1/all

El web services que construirás debe exponer un EndPoint que retorne los 5 países con mayor densidad demográfica del mundo (Recuerda que la densidad demográfica es la
división entre el número de habitantes y el área donde viven). Los campos en el API de países para realizar este cálculo son area y population. Cada vez que el Endpoint que construyas sea llamado debes dejar un log de uso en la base de datos que se menciona en el punto 2.





    





