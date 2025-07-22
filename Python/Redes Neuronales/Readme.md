## 🧮 Transformaciones y Lógica del Proyecto

### 🖼️ Proyecto: Clasificación de Imágenes con CIFAR-10

Este notebook implementa un pipeline completo para la clasificación de imágenes utilizando el conjunto de datos **CIFAR-10** (60 000 imágenes de 32x32 píxeles, distribuidas en 10 clases). Se comparan dos enfoques: una red neuronal densa y una red convolucional (CNN).

---

### 📦 Carga y visualización de datos

- Se importó el dataset `CIFAR-10` desde `Keras.datasets`.
- Se dividió el conjunto en **entrenamiento** y **testeo**.
- Se visualizaron 10 imágenes de muestra con sus respectivas etiquetas usando `Matplotlib`.

---

### 🧹 Preprocesamiento

- Se normalizaron los valores de píxeles al rango `[0,1]`.
- Las etiquetas fueron transformadas a formato **one-hot encoding** con `to_categorical`.

---

### 🔣 Modelo Denso (Fully Connected)

#### 🔧 Arquitectura

```python
Input(shape=(32,32,3)) → Flatten()
→ Dense(128, activation='relu')
→ Dense(64, activation='relu')
→ Dense(10, activation='softmax')

## 📊 Comparación de Modelos sobre CIFAR-10

### 🧪 Resultados del Modelo Denso

**Accuracy final:** `49.0 %`  
**Loss final:** `1.4302`  
**Accuracy de validación:** `47.0 %`  
**Loss de validación:** `1.4814`

📉 Evolución por época:

| Época | Accuracy | Loss   | Val_Accuracy | Val_Loss |
|-------|----------|--------|--------------|----------|
| 1     | 26.7%    | 2.0106 | 35.0%        | 1.7896   |
| 2     | 37.4%    | 1.7423 | 38.1%        | 1.7113   |
| 3     | 40.8%    | 1.6566 | 43.2%        | 1.5992   |
| 4     | 42.9%    | 1.6039 | 43.5%        | 1.5803   |
| 5     | 44.6%    | 1.5506 | 44.8%        | 1.5486   |
| 6     | 46.1%    | 1.5224 | 45.5%        | 1.5188   |
| 7     | 46.8%    | 1.4897 | 46.5%        | 1.5211   |
| 8     | 47.7%    | 1.4774 | 45.9%        | 1.5204   |
| 9     | 48.4%    | 1.4491 | 46.4%        | 1.5067   |
| 10    | 49.0%    | 1.4302 | 47.0%        | 1.4814   |

---

### 🧠 Resultados del Modelo CNN

**Accuracy final:** `76.6 %`  
**Loss final:** `0.6780`  
**Accuracy de validación:** `69.1 %`  
**Loss de validación:** `0.9159`

📉 Evolución por época:

| Época | Accuracy | Loss   | Val_Accuracy | Val_Loss |
|-------|----------|--------|--------------|----------|
| 1     | 34.7%    | 1.8141 | 52.3%        | 1.3418   |
| 2     | 55.7%    | 1.2589 | 59.3%        | 1.1660   |
| 3     | 62.2%    | 1.0839 | 62.4%        | 1.0843   |
| 4     | 65.3%    | 1.0031 | 63.7%        | 1.0535   |
| 5     | 67.9%    | 0.9306 | 66.1%        | 0.9963   |
| 6     | 69.4%    | 0.8807 | 66.6%        | 0.9798   |
| 7     | 71.9%    | 0.8153 | 66.8%        | 0.9755   |
| 8     | 72.9%    | 0.7803 | 66.6%        | 0.9877   |
| 9     | 75.0%    | 0.7286 | 68.6%        | 0.9191   |
| 10    | 76.6%    | 0.6780 | 69.1%        | 0.9159   |

---

### 🔍 Comparativa

| Métrica           | Modelo Denso | CNN        |
|-------------------|--------------|------------|
| Accuracy Final    | 49.0%        | 76.6%      |
| Validación Final  | 47.0%        | 69.1%      |
| Mejora Relativa   | —            | +27.6%     |
| Interpretación    | 🌿 Básico     | 🚀 Optimizado para imágenes |

---

### 🎯 Visualización (Confusion Matrix)

El modelo CNN muestra mayor precisión en clases complejas como **perro**, **gato** y **camión**, según la matriz de confusión visualizada. Las categorías menos diferenciadas en el modelo denso tienen errores más dispersos fuera de la diagonal.

---

## 📊 Evaluación Final – Modelo CNN (CIFAR-10)

### 🧮 Matriz de Confusión

Este gráfico resume cómo se desempeñó el modelo CNN sobre el conjunto de test. Cada fila representa la categoría real, y cada columna la predicción del modelo.

| Índice | Etiqueta         |
|--------|------------------|
| 0      | ✈️ Avión          |
| 1      | 🚗 Automóvil      |
| 2      | 🐦 Pájaro         |
| 3      | 😺 Gato           |
| 4      | 🦌 Ciervo         |
| 5      | 🐶 Perro          |
| 6      | 🐸 Rana           |
| 7      | 🐴 Caballo        |
| 8      | 🚢 Barco          |
| 9      | 🚚 Camión         |

### ✅ Rendimiento destacado

- **Automóvil (Clase 1):** 869 clasificaciones correctas
- **Rana (Clase 6):** 780 clasificaciones correctas
- **Barco (Clase 8):** 783 clasificaciones correctas
- **Camión (Clase 9):** 725 clasificaciones correctas

### ⚠️ Áreas de mejora

- Alta confusión entre animales: Gato, Perro, Ciervo y Caballo.
- El modelo confundió al Gato con Perro en 177 ocasiones y con Ciervo en 61.
- Algunas imágenes de Avión se confundieron con Barco y Automóvil, probablemente por fondo visual similar.

### 📌 ¿Por qué importa?

La matriz ayuda a:
- Identificar clases que necesitan mejor definición o más datos.
- Guiar ajustes en arquitectura o estrategia de entrenamiento.
- Evaluar si conviene aplicar técnicas como **data augmentation**, regularización o balanceo de clases.