Test Plan
- Test objectives
Los objetivos del plan serán comprobar el correcto funcionamiento de funcionalidades individuales y la interacción entre todos los componentes. 


Test scope:

* El software y la interfaz de uso. Así como la infraestructura del despliegue de la aplicación.
* Se testearán cada una de las funcionalidades descritas del dashboard y la interacción. 
* Se revisará el correcto funcionamiento de la interfaz web/app movil para que cada botón/pantalla haga lo requerido. 
* Se testearán los endpoints para asegurar que los usuarios tienen únicamente acceso a la información que les corresponde. 
* Se harán poruebas para comprobar el correcto funcionamiento del dashboard cuando sea utilizado por múltiples usuarios.
Pruebas en disitintos dispositivos


Test approach

* Unit Test: Comprobar las funcionalidades de cada uno de los componentes
* API Testing de los distintos endpoints que se llamen dedde front y que no permitan acceder a datos de otos usuarios

Test environment
* Se creará un docker con las especificaciones de la máquina donde se vaya a subir a la nube en el cual se realizarán los tests. 

* Una vez completados los test, se podrán lanzar en un entorno de pruebas en la nube, más semejante a lo que se hará en producción

* Testear funcionalidades en distintos dispositivos (esto es má de front no?)

Test Schedule

1. Recibo de la tarea, documentacion y conocimiento de la funcionalidad
2. Planteamiento de este documento
3. Desarrollo de los tests
    1. Unit Test
    2.  API Test
4. Ejecucuion de los tests y notificacion de posibles errores
5. Ejecucion en entorno de preproduccion


Deliverable (Entregables)

* Plan de pruebas
* Casos de prueba
* Scripts de prueba automatizados
* Informes de resultados de las pruebas
* Registro de fallos y seguimiento

