## 🧮 Transformaciones y Lógica - Iris

### 📦 Preparación de datos

- Se utilizó el dataset clásico **Iris** desde `sklearn.datasets`.
- Se separaron las variables predictoras (`X`) y la variable objetivo (`y`).
- Se dividió el conjunto de datos en entrenamiento y testeo con `train_test_split` (30% test, `random_state=42`).

---

### 🌳 Entrenamiento del modelo

- Se entrenó un `DecisionTreeClassifier` con los siguientes parámetros:
  - `criterion='entropy'`
  - `max_depth=4`
  - `random_state=42`
- El modelo se ajustó sobre el conjunto de entrenamiento (`X_train`, `y_train`).

---

### 📊 Visualización del árbol

- Se generó una visualización gráfica del árbol con `plot_tree`, mostrando:
  - Las reglas de decisión en cada nodo.
  - Las características utilizadas (`sepal length`, `petal width`, etc.).
  - Las clases objetivo (`setosa`, `versicolor`, `virginica`).
- Se utilizó `matplotlib` para renderizar el árbol con estilo redondeado y colores por clase.

---

### ✅ Resultados destacados

- Entrenamiento exitoso del modelo con profundidad máxima de 4.
- Visualización clara de las divisiones jerárquicas del árbol.
- El modelo permite interpretar fácilmente cómo se clasifican las especies según sus atributos.

---

### 📌 Próximos pasos

- Evaluar el rendimiento sobre el conjunto de test:
  - Matriz de confusión
  - Accuracy
  - Precision / Recall
- Ajustar hiperparámetros (`max_depth`, `criterion`) y comparar resultados.
- Explorar otros algoritmos de clasificación:
  - `RandomForestClassifier`
  - `SVM`
  - `KNN`

---
## 🧮 Transformaciones y Lógica RRHH

### 📦 Preparación de datos

- Se cargó un conjunto de datos supervisado desde archivos CSV.
- Se realizó limpieza básica y verificación de tipos con `pandas`.
- Se separaron las variables predictoras (`X`) y la variable objetivo (`y`).
- Se dividió el dataset en entrenamiento (70%) y testeo (30%) usando `train_test_split`.

---

### 🌳 Entrenamiento del modelo

- Se entrenó un `DecisionTreeClassifier` de `scikit-learn` sobre el conjunto de entrenamiento.
- Se ajustaron parámetros básicos como el criterio de división (`gini` o `entropy`) y la profundidad del árbol.
- El modelo se utilizó para predecir sobre el conjunto de test.

---

### 📊 Evaluación del modelo

- Se calculó la **matriz de confusión** para visualizar aciertos y errores por clase.
- Se obtuvieron métricas clave:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1-score**
- Se generó un informe de clasificación completo con `classification_report`.

---

### 🧪 Entorno de ejecución

- Se recomienda crear un entorno virtual para reproducir el proyecto:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows