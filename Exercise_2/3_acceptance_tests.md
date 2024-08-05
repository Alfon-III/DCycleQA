
## Acceptance Test

A continuación se detallan los tres métodos/endpoints que pueden ser llamados por el usuario y cómo deben ser llamados por la API para funcionar como se espera. 

1. Calcular la huella de carbono del usuario

|   |   |
|---|---|
| Descripcion | Calcula la huella de carbono dados unos parámetros |
| Enpoint | /calculate-carbon-footprint |
| Inputs | energy_consumption: `float`<br>transportation: `float`<br>waste: `float` |
| Output | `float` |
| Comentarios | Se deben rellenar todos los parámetros en el formato indicado. Si no se completa un campo no funcionará la llamada. |

2. Obtener huella de carbono

|   |   |
|---|---|
| Descripcion | Obtener diccionario con la huella de carbono calculada en base a la enviada |
| Enpoint | /get-carbon-footprint |
| Inputs | `dict`: <br>{<br>‘energy_consumption’: `float`, <br>‘transportation’: `float`, <br>‘waste’: `float`, <br>} |
| Output | `dict`  |
| Comentarios | El diccionario enviado de tener todos los parámetros indicados.  |

3. Comparar huella de carbono con el promedio
   
|   |   |
|---|---|
| Descripcion | Calcula la diferencia entre la huella de un usuario y otro (averge) |
| Enpoint | /get-comparison |
| Inputs | dict: <br>{<br>`user_footprint`: dict<br>`averge_footprint`: dict<br>} |
| Output | dict |
| Comentarios | El diccionario debe contener los dos diccionarios con el mismo formato comentado en el apartado de arriba. El valor del `averge_footprint` debe proveerlo de entrada, la función no calculará el promedio, limitándose a compararlo con `ùser_footprint`. |
