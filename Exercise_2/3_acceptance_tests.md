
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

Pseudocode implementation
```python
Input (user_data )

# Check the input is a dictionary
if not isinstance(user_data, dict):
   return False

# Check the keys are correctly submitted
if set(user_data.keys()) != {'energy_consumption', 'waste', 'transportation'}:
   return False

# Chek if all keyy values are the correct type
for v in user_data.values():
   if not issinstance(v, (int, float)):
      return False

#Send validated dict
respuesta = request.get('/get-carbon-footprint', json=user_data )

if respuesta.status_code  != 200:
   return False

return True
```

3. Comparar huella de carbono con el promedio
   
|   |   |
|---|---|
| Descripcion | Calcula la diferencia entre la huella de un usuario y otro (averge) |
| Enpoint | /get-comparison |
| Inputs | dict: <br>{<br>`user_footprint`: dict<br>`averge_footprint`: dict<br>} |
| Output | dict |
| Comentarios | El diccionario debe contener los dos diccionarios con el mismo formato comentado en el apartado de arriba. El valor del `averge_footprint` debe proveerlo de entrada, la función no calculará el promedio, limitándose a compararlo con `ùser_footprint`. |

```python
Input (compare_data )

# Check the input is a dictionary
if not isinstance(compare_data , dict):
   return False

# Check if dictionary has the user, and compared dictionary
if set(compare_data.keys()) != {'energy_consumption', 'averge_footprint'}:
   return False

# Iter dictionaries to check both are correctly formatted 
for dict_name, dict_detail in compare_data.items():
   # Check detail is a dict
   if not isinstance(dict_detail, dict):
      return False

   # Check if the detail is a dictionary
   if set(dict_detail.keys()) != {'user_footprint', 'waste', 'transportation'}:
      return False

   # Check if all key values are the correct type
   for v in dict_detail.values():
      if not issinstance(v, (int, float)):
         return False

#Send validated dict
respuesta = request.get('/get-comparison', json=compare_data )

if respuesta.status_code  != 200:
   return False

return True
```
