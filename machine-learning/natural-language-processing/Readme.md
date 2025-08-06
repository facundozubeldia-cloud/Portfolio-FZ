## 🧮 Transformaciones y Lógica del Proyecto

### 😏 Detección de Sarcasmo en Titulares

#### 📦 Preparación de texto

- Se extrajeron hashtags usando expresiones regulares para identificar contexto implícito.
- Se construyó un corpus inicial a partir de los titulares, y se aplicó una vectorización con `CountVectorizer`.
- Se exploró el dataset `Sarcasm_Headlines_Dataset` para entender distribución de clases.

#### 🧹 Limpieza y preprocesamiento

- Se aplicó tokenización a nivel oración y palabra.
- Se eliminaron stopwords usando NLTK para mejorar señal textual.
- Se aplicó `PorterStemmer` para reducir palabras a su raíz.
- Se realizó lematización con `WordNetLemmatizer`, ajustando etiquetas POS para mayor precisión.

#### 📊 Ingeniería de características

- Se limitó el vocabulario a 1 000 características con `CountVectorizer(max_features=1000)`.
- Se separó el corpus en `X` e `y`, utilizando `stratify` para preservar proporción de clases en el split.

#### 🌲 Entrenamiento del modelo

- Se entrenó un `RandomForestClassifier` con 50 árboles (`n_estimators=50`).
- Se evaluó el modelo sobre el 20% de datos reservados para test.

#### 📈 Resultados clave

- Gráficos de frecuencia comparativa entre titulares sarcásticos y no sarcásticos.
- Accuracy del modelo mostrado sobre conjunto de evaluación.
- Pipeline completo de NLP + modelo listo para integrar en aplicación real.

---

### 🧠 Reducción de Dimensionalidad con PCA

#### 📦 Preparación de datos

- Se utilizó el dataset `Iris` de `sklearn.datasets`.
- Se separaron las características (`X`) y etiquetas (`y`).
- Se escalaron las variables con `StandardScaler` para evitar distorsión por magnitud.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)