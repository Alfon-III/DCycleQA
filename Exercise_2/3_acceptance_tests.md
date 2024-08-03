### Acceptance Test EcoChallanges


1. Unirse a un desafío
```python
Input (user, challange)

# Validar usuario existe
if user does not exist:
    return False

# Validar desafío existente
if challange to join does not exist:
    return False

# Validar desafío vigente
if current_date > challenge.deadline:
    return False

participation = join_user_to_challange(user, challange)

# El usuario debe empezar con 0 puntos al ser adscrito
participation.points != 0:
    return False

return True
```

Probar con permutaciones de:
  - Usuario: Existe / No existe
  - Challange: Existe / No existe +  (deadline vencido o no )
  


2. Ver progreso de los desafíos
El test falla si el estado d ela participacón está en un estado indebido. 

```python
# Verificar que el usuario existe
if user does not exist:
    return False

# Verificar que el desafío existe
if challenge does not exist:
    return False

for participation in user.participations:
    # Si el usuario sigue apuntado con participación vigente en una fecha expirada retornar error
    if participation.is_active and current_date > participation.challenge.deadline:
        return False
    # Si la participación es negativa, retornar error
    if participation.points < 0:
        return False
    # No se puede tener una participación activa y con la recompensa reclamada
    if participation.is_reward_claimed and participation.is_active:
        return Flase 

return True

```

3. Aportar/Contribuir al desafío



Asumimos que no podemos sumar puntos negativos al desafío.

``` python
# Verificar datos de entrada para CarbonFootprintCalculator
if not valid_cfc_input(energy, transport, waste)
    return False

cfc = CarbonFootprintCalculator(
    energy_consumption=energy,
    transportation=transport,
    waste=waste
)

points = cfc.total_carbon_footprint()

# Verificar puntos positivos
if points < 0:
    return False 

# Verificar que el usuario existe
if user does not exist:
    return False

# Verificar desafío existente
if challange to join does not exist:
    return False

# Calcular puntuación y añadirla 
participation = get_participation(user, challange)
prev_points = participation.points
participation.contribute(points)
post_points = participation.points

# Verificar que la diferencia coincide con los puntos **sumados**
if post_points - prev_points != points:
    return False

```

4. Comparar puntuación con la región
 
```python
# Verificar que el usuario existe
if user does not exist:
    return False

# Verificar que el desafío existe
if challenge does not exist:
    return False

# Verificar que la región existe
if region does not exist:
    return False

# Calcular la huella de carbono del usuario
user_footprint = get_user_carbon_footprint(user_data)

# Calcular la huella de carbono promedio de la región
region_average_footprint = get_user_carbon_footprint(region_data)

# Comparar la huella de carbono del usuario con la de la región
comparison_result = get_comparison_with_average(user_footprint, region_average_footprint)

# Verificar que la comparación se realizó correctamente
if comparison_result is None: 
    return False


# Verificar que el valor de la diferencia tenga sentido 
if user_footprint['total_footprint'] - average_footprint['total_footprint']
 != comparison_result['total_difference']: 
    return False

return True
```

5. Desapuntarme de un desafío

```python
# Verificar que el usuario existe
if user does not exist:
    return False

# Verificar que el desafío existe
if challenge does not exist:
    return False

# Desapuntarse del desafío
if not leave_challange(user, challange):
    #Si no estaba apuntado, retornar error
    return False

# Verificar que el desafío ha sido removido de la lista de participaciones del usuario
for participations in user.participations:
    if participations.challange.id == challange.id
        return False

return True

```
