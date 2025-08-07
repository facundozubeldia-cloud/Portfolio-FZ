## Formula 1 - Escuderias

**Descripción**  
Este script en Python procesa los datos de una carrera de Fórmula 1 de 52 vueltas (hasta 20 pilotos), estructurando la información en un diccionario anidado, calculando posiciones y puntos, obteniendo estadísticas y generando distintos informes.

## Funcionalidades principales

- **Transformación de datos**  
  Convierte un diccionario de listas en un diccionario anidado con claves:
  - `tiempo total en pista`  
  - `vuelta más rápida`  
  - `total de vueltas`  
  - `Escuderia`  
  - `Numero`  
  - `Puntos`

- **Determinación de finalistas**  
  Separa e imprime las listas de pilotos que terminaron la carrera y los que abandonaron.

- **Cálculo del ganador**  
  Identifica al piloto con el menor tiempo total entre quienes completaron las 52 vueltas.

- **Generación de pódium**  
  Extrae los tres primeros puestos según el tiempo total en pista y muestra sus datos.

- **Asignación de puntos**  
  Reparte puntos reglamentarios (25 – 18 – 15 – 12 – 10 – 8 – 6 – 4 – 2 – 1) a los 10 primeros finalistas y otorga un punto extra al autor de la vuelta más rápida (aunque no termine).

- **Reporte de vuelta más rápida**  
  Encuentra al piloto con la vuelta más rápida dentro del top 10 y muestra su tiempo y posición.

- **Estadísticas de tiempos**  
  Calcula e imprime medidas descriptivas de los tiempos de carrera (count, mean, median, min, max, std).

- **Puntos por escudería**  
  Suma los puntos obtenidos por cada equipo, ordena las escuderías por total de puntos y extrae el top 3.

- **Exportación de resultados**  
  - JSON (`podio_escuderias.json`)  
  - Excel (`podio_escuderias.xlsx`)  
  - SQLite (`podio_escuderias.db`)

# Resultados:

Lista de pilotos: ['Alexander Albon', 'Carlos Sainz', …, 'Yuki Tsunoda']
Lista de tiempos: [[1417,13,86], …, [5824,52,92]]
Lista de aux: ('tiempo total en pista', 'total de vueltas', 'vuelta mas rapida')

… (detalle por piloto) …

Finishers: ['Charles Leclerc', 'Isack Hadjar', …, 'Yuki Tsunoda']
Abandonos: ['Alexander Albon', 'Carlos Sainz', …, 'Lance Stroll']

Ganador: Max Verstappen  
    Vueltas: 52  
    V. rápida: 85 s  
    Tiempo total: 5200 s

PÓDIUM FÓRMULA 1 2025
1. Max Verstappen   – 5200 s (vuelta rápida 85 s)  
2. Lando Norris    – 5304 s (vuelta rápida 90 s)  
3. Oscar Piastri   – 5356 s (vuelta rápida 87 s)

Estadísticas (finishers):  
  • Count : 13  
  • Mean  : 5652.00 s  
  • Median: 5616.00 s  
  • Min   : 5200 s  
  • Max   : 6084 s  
  • Std   : 280.68 s  

TOP 3 ESCUDERÍAS
1. McLaren  – 33 ptos  
2. Red Bull – 27 ptos  
3. Ferrari  – 20 ptos