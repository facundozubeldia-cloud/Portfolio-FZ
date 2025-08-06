## 🧮 Transformaciones y Lógica

### 📦 Preparación de datos

- Se generó un conjunto de datos bidimensionales sintéticos para facilitar la visualización de los clusters.
- Se estandarizaron las variables con `StandardScaler` para evitar sesgos por escala.
- Se aplicó una validación visual previa para detectar posibles agrupamientos naturales.

---

### 📊 Algoritmos de clustering aplicados

#### 🔹 K-Means
- Se entrenó el modelo con distintos valores de `k` (número de clusters).
- Se utilizó el método del codo (`KElbowVisualizer`) para determinar el valor óptimo de `k`.
- Se evaluó la cohesión de los clusters con el coeficiente de silueta (`SilhouetteVisualizer`).
- Se graficaron los clusters resultantes con colores diferenciados y centroides marcados.

#### 🔸 DBSCAN
- Se aplicó el algoritmo con distintos valores de `eps` y `min_samples`.
- Se identificaron clusters de forma arbitraria y puntos considerados ruido.
- Se comparó la sensibilidad del modelo frente a densidades variables.

---

### 📐 Métricas y visualizaciones

- **Coeficiente de silueta**: se utilizó para evaluar la separación entre clusters.
- **Gráficos de dispersión**: se emplearon para visualizar los agrupamientos y comparar resultados entre algoritmos.
- **Visualizadores de Yellowbrick**: facilitaron la interpretación de métricas y la elección de parámetros óptimos.

---

### 🧠 Conclusiones

- K-Means funciona bien en datos con forma esférica y distribución homogénea.
- DBSCAN es más robusto frente a ruido y formas arbitrarias, pero sensible a la elección de `eps`.
- La combinación de visualización + métricas permite tomar decisiones más informadas sobre el modelo a aplicar.