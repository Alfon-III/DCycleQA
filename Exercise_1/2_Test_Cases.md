# Test Case Design

## Caso 1
**Case ID:** ET_DB_Trends_02  
**Descripción:** Comprobar que los valores de la tendencia de los últimos 30 días son correctos aunque haya menos de 30 días de datos (ej. Usuario que lleva usando la aplicación 15 días).  
**Pre-condición:** El usuario existe y no tiene <30 días de datos.

**Test Steps:** 
1. Crear usuario y mockear datos de huella de carbono por N días (1 < N < 30).
2. Consultar a la API por el endpoint de la tendencia para el usuario creado.

**Expected Results:** La tendencia funciona con la muestra de datos menor o muestra un mensaje indicando que aún faltan datos.  
**Post-condición:** Ninguna.

## Caso 2
**Case ID:** ET_DB_TrendsFilter_02  
**Descripción:** Comprobar que los valores de la tendencia filtrada por un campo (ej. Transporte) de los últimos 30 días son correctos aunque solo haya datos para 1 día.  
**Pre-condición:** El usuario existe y solo tiene un día de datos.

**Test Steps:** 
1. Crear usuario y mockear datos de huella de carbono por 1 día.
2. Consultar a la API por el endpoint de la tendencia para el usuario creado.

**Expected Results:** Tendencia N/A o vacía.  
**Post-condición:** Ninguna.

## Caso 3
**Case ID:** ET_DB_ComparisonChart_01  
**Descripción:** Comprobar que el gráfico comparativo muestra los datos correctos para la región del usuario.  
**Pre-condición:** El usuario existe y hay datos para el promedio del país.

**Test Steps:** 
1. Precalcular los datos promedio de una Región X.
2. Crear un usuario con datos para la región X.
3. Llamar a la API de la gráfica promedio de usuarios de una región.

**Expected Results:** Los datos del promedio de la región X coinciden con los datos precalculados (ver que no se usan los de otra región o que el promedio no varía en exceso < 0.05% del precalculado).  
**Post-condición:** Ninguna.

## Caso 4
**Case ID:** ET_DB_Tips_01  
**Descripción:** Comprobar la pertinencia de los consejos en base a los datos del usuario.  
**Pre-condición:** Crear un usuario con un gran consumo de electricidad. (Asumir que los consejos están etiquetados. Ej: `{tip: 'No olvides apagar las regletas y bajar los plomos antes de irte de vacaciones', tags: ['electricity', 'holidays']}`).

**Test Steps:** 
1. Crear usuario con un gran consumo eléctrico.
2. Llamar a la API de consejos personalizados.
3. Analizar los consejos personalizados o ver las posibles etiquetas de los consejos.

**Expected Results:** Los consejos están relacionados con reducir o prevenir el consumo eléctrico. Todos los consejos tienen como mínimo una etiqueta de 'electricity'.  
**Post-condición:** Ninguna.

## Caso 5
**Case ID:** ET_DB_BadgeProgress_01  
**Descripción:** Calcular la diferencia entre el umbral del usuario y el umbral para el siguiente objetivo y comprobar si coincide con la diferencia esperada.  
**Pre-condición:** Crear un usuario con cierto progreso en una insignia. La insignia puede ser: Días sin producir emisiones de carbono. El usuario ya cuenta con 13 días sin haber generado emisiones de carbono. El progreso de la insignia se subdivide en hitos de [1, 7, 15, 30] días.

**Test Steps:** 
1. Consultar a la API del progreso de insignias.

**Expected Results:** Ver que se han alcanzado los primeros 2 hitos y que aún faltan (15 - 13) 2 días más para llegar al tercer hito.  
**Post-condición:** Ninguna.
