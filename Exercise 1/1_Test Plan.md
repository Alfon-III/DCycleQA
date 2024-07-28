# Test Plan for EcoTrack Dashboard

## Test Objectives
Los objetivos del plan serán comprobar el correcto funcionamiento de funcionalidades individuales y la interacción entre todos los componentes.

## Test Scope
- El software y la interfaz de uso, así como la infraestructura del despliegue de la aplicación.
- Se testearán cada una de las funcionalidades descritas del dashboard y su interacción.
- Se revisará el correcto funcionamiento de la interfaz web/app móvil para que cada botón/pantalla haga lo requerido.
- Se testearán los endpoints para asegurar que los usuarios tienen únicamente acceso a la información que les corresponde.
- Se harán pruebas para comprobar el correcto funcionamiento del dashboard cuando sea utilizado por múltiples usuarios.
- Pruebas en distintos dispositivos (telefono/tablet/ordenador) de distintas resoluciones y prestaciones.

## Test Approach
- **Unit Test:** Comprobar las funcionalidades de cada uno de los componentes.
- **API Testing:** Probar los distintos endpoints llamados desde el frontend para asegurar que no permiten acceder a datos de otros usuarios.

## Test Environment
- Se creará un docker con las especificaciones de la máquina donde se vaya a subir a la nube en el cual se realizarán los tests.
- Una vez completados los tests, se podrán lanzar en un entorno de pruebas en la nube, más semejante a lo que se hará en producción.
- Testear funcionalidades en distintos dispositivos (esto es más de frontend).

## Test Schedule
1. Recibo de la tarea, documentación y conocimiento de la funcionalidad.
2. Planteamiento de este documento.
3. Desarrollo de los tests:
   1. Unit Test
   2. API Test
4. Ejecución de los tests y notificación de posibles errores.
5. Ejecución en entorno de preproducción.

## Deliverables
- Plan de pruebas.
- Casos de prueba.
- Scripts de prueba automatizados.
- Informes de resultados de las pruebas.
- Registro de fallos y seguimiento.
