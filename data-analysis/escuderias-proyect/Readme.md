# Proyecto Escuderías

**Descripción**  
Este proyecto en Python procesa datos de una carrera de Fórmula 1 de 52 vueltas para un máximo de 20 pilotos, organizando la información en estructuras anidadas, calculando clasificaciones, asignando puntos y generando distintos informes y salidas.

## Funcionalidades principales

- **Transformación de datos**  
  Convierte un diccionario de listas en un diccionario anidado con claves claras (`tiempo total en pista`, `vuelta más rápida`, `total de vueltas`, `Escuderia`, `Numero`, `Puntos`).

- **Determinación de finalistas**  
  Separa a los pilotos que terminaron la carrera de los que abandonaron e imprime ambas listas.

- **Cálculo del ganador**  
  Identifica al piloto con menor tiempo total (entre quienes completaron las 52 vueltas).

- **Generación de podio**  
  Extrae los tres primeros puestos según el tiempo total en pista y los presenta con sus datos detallados.

- **Asignación de puntos**  
  Reparte puntos (25, 18, 15, 12, 10, 8, 6, 4, 2, 1) a los 10 primeros finalistas y otorga un punto extra al autor de la vuelta más rápida (aunque no haya terminado).

- **Reporte de vuelta más rápida**  
  Encuentra al piloto con la vuelta más rápida entre los 10 primeros y muestra su tiempo y posición.

- **Estadísticas por escudería**  
  Suma los puntos de sus pilotos, ordena las escuderías por total de puntos y obtiene el top 3.

- **Exportación de resultados**  
  - JSON (`podio_escuderias.json`)  
  - Excel (`podio_escuderias.xlsx`)  
  - Base de datos SQLite (`podio_escuderias.db`)

## Requisitos

- Python 3.7+  
- Paquetes:
  ```bash
  pip install pandas sqlalchemy openpyxl