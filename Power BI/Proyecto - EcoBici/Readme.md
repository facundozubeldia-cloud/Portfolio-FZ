# 📊 Análisis de Ventas - Power BI

Este proyecto analiza las ventas de una cadena de retail entre 2021 y 2023. Se construyó un dashboard interactivo en Power BI con KPIs clave, segmentación por región y análisis temporal.

## 🧼 Limpieza y transformación de datos

- Se importaron archivos CSV desde una carpeta.
- Se eliminaron valores nulos y se unificaron formatos de fecha.
- Se crearon columnas calculadas en Power Query para categorizar productos.
- Se aplicaron relaciones entre tablas de hechos y dimensiones.

## 🧠 Métricas DAX destacadas

- `Total Ventas = SUM(Ventas[Monto])`
- `Crecimiento Anual = (Ventas Año Actual - Año Anterior) / Año Anterior`

## 📷 Capturas del dashboard

### Vista general
![Dashboard general](img/dashboard_general.png)

### Segmentación por región
![Segmentación](img/segmentacion_region.png)

## 📌 Conclusiones

- Las ventas crecieron un 18% interanual.
- La región norte mostró mayor rentabilidad por unidad vendida.
- El 80% de las ventas provienen del 20% de los productos (ley de Pareto).

## 📁 Archivos

- `ventas.pbix`: archivo de Power BI.
- `datos/`: carpeta con los CSV originales.
- `README.md`: documentación del proyecto.

## 📬 Contacto

[Tu LinkedIn] | [Tu email]