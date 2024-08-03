


The EcoTrack dashboard

1. Carbon Footprint Summary
   - 🗓️ Carbon footprint by Time Interval: (Day/Week/Month)
   - 🔎 Breakdown of CF by category:
     - ⚡ Energy Consumption 
     - 🚚 Transportation 
     - 🗑️ Waste 

2. Trends Graph
   - 📈 Line Chart CF last month
   - 🎛️ Filter by category

3. Comparison Char
   - 📊  Bar Chart to compare: User CF with Avg. User in Region
   - 🎯% Difference by each category

4. Tips and Recommendations:
   - 💡 List of tips based on user's activity
   - 📰 Link to detailed articles and resources

5. Achievements and Badges:
   - 🏅 Badges earned based on eco-friendly actions
   - 🔥 Progress Towards next badge


---

https://www.guru99.com/test-planning.html


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




----

Test Case Design


TODO Detallar uno de estos ejemplos

Detalle de ejemplos a testear:

Carbon Footprint Summary
1. Consultar por los datos de un usuario para distintas fechas (tenga datos o no)
2. Obtener detalle de Huella de carbono para cada una de dichas fechas

Trends Graph
1. Obtener gráfico/valores de cada día 
2. Varios test con distintas permutaciones de filtros

Comparison Char
1. Obtener el valor de la grafica del promediio en distintas regiones
2. Comprobar que Los datos del Usuario coinciden con los del 1.1 


Tips and Recommendations
1. Comprobar  que los consejos son acordes a la actividad: 
   1. Ej: Si el usuario tiene grandes valores de gasto energético, que le recomiende cosas como desconectar los enchufes o que se compre una placa solar.
   2. Si Tiene un gasto grande de Transporte y energía, pues que no pida comida a domicilio de manera habitual.
   3. HAcer permutaciones con distintos casos y ver los resultados

2. Los artículos deben ser testeados y acordes al test anterior, aunque su criterio puede ser más laxo

Archievements and badges

1. Obtener los umblaes o características bajo los que se consiguen dichos logros y comprobar si se han alcanzado los umbrales y obtenido el logro. 
2. Calcular la diferencia entre el umbral del usuario y el umbral para el siguiente objetivo y comprobar si coincide con el % o diferencia esperada. 

Combinación de tests

Perfiles a Testear
Añadiir tabla con permutaciones de Gasto en categorías Alto, medio y bajo en distintos países y  
