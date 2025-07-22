## 📘 Dashboard Estratégico de Capital Humano

Este dashboard brinda a la dirección una visión integral del ciclo de vida del empleado, permitiendo identificar riesgos, oportunidades y tomar decisiones informadas en torno a la gestión del talento.

---

### 🧱 Estructura del modelo

El tablero se divide en 5 secciones temáticas, cada una basada en datasets específicos:

### 1. 👥 Visión General de la Fuerza Laboral
- Headcount total y por área, ubicación, tipo de contrato y estado laboral
- Distribución por antigüedad, edad, género y desempeño
- Indicadores: antigüedad promedio, % por rango etario, desempeño laboral

🔎 **Objetivo**: conocer la composición actual, detectar desequilibrios y planificar necesidades futuras.

---

### 2. 🎯 Adquisición de Talento
- Vacantes abiertas/cubiertas, candidatos por vacante, fuentes de reclutamiento
- KPIs: tasa de cobertura, efectividad por fuente, costo por contratación

🔎 **Objetivo**: medir eficiencia en atracción de talento y optimizar recursos en reclutamiento.

---

### 3. 📚 Desarrollo y Capacitación
- Participación en capacitaciones, horas invertidas, calificaciones y correlación con desempeño
- KPIs: participación, tasa de completación, inversión y mejora post-capacitación

🔎 **Objetivo**: evaluar el impacto de la formación en el rendimiento y retención del personal.

---

### 4. 🌟 Compromiso y Clima Laboral
- Puntuación general y segmentada del compromiso, drivers clave, evolución temporal
- KPIs: nivel de compromiso, participación en encuestas, tendencias históricas

🔎 **Objetivo**: detectar señales de desconexión y orientar acciones de mejora en la experiencia laboral.

---

### 5. 🔄 Retención y Rotación
- Tasa de rotación total, voluntaria/involuntaria, por departamento y antigüedad
- Posibles correlaciones con compromiso, razones de salida y costo asociado

🔎 **Objetivo**: entender por qué se van los empleados, cuantificar el impacto y prevenir futuras pérdidas.

---

## 🧮 Transformaciones y Limpieza en Power Query

### 👥 Tabla Empleados

- Combinación de nombre y apellido en `Empleado`.
- Renombrado de campos (e.g., `Title` → `Puesto`, `ADEmail` → `Email`).
- Conversión de fechas (`StartDate`, `ExitDate`, `DOB`) y numéricos.
- Cálculo de `Edad`, `Antigüedad` y estado (`Estatus`: activo/inactivo).
- Clasificación de desempeño (`Interpretación de resultado`: mala, regular, buena).

---

### 📊 Tabla Encuesta de Compromiso

- Renombrado de campos (e.g., `Engagement Score` → `Compromiso`).
- Cálculo de promedio entre compromiso, satisfacción y balance → `Resultado`.
- Segmentación del resultado (`Interpretación`: atención, oportunidad, satisfecho).

---

### 📋 Tabla Reclutamiento

- Combinación de nombre en `Postulante`.
- Renombrado de campos (género, teléfono, dirección, estudios, experiencia).
- Corrección en campo `Telefono` para eliminar caracteres inválidos.
- Unificación de formatos numéricos y categóricos para análisis.

---

### 🎓 Tabla Capacitación

- Renombrado de campos (programa, fecha, tipo, duración, costo).
- Conversión de duración y costo a formato numérico.
- Reemplazo de caracteres para corrección regional (punto → coma).

---

## 📊 Resultado del Análisis de Recursos Humanos

### 🧾 Conclusión General

La empresa presenta una **alta fuga de talentos**, evidenciada por una **rotación histórica del 51%** — es decir, **1 de cada 2 empleados abandona la organización**.

Esta rotación sostenida afecta negativamente:
- La **productividad** general del equipo
- La **rentabilidad** de los procesos
- La **especialización** en funciones clave
- La **calidad** de los entregables y servicios

---

### 🔍 Principales causas de la alta rotación

1. **Calificación laboral deficiente**
   - Promedio **inferior a 3 puntos** sobre 5
   - Indica posibles niveles bajos de calidad y genera **desmotivación**

2. **Compromiso laboral bajo**
   - Valor promedio de **2.9**, por debajo del nivel considerado "bueno" (≥ 4)
   - Impacta de forma directa en la **productividad** y el rendimiento

3. **Ambiente laboral regular**
   - Promedio de **3/5**, no percibido como satisfactorio por la mayoría
   - Puede generar **malestar, conflictos internos** y predisposición negativa

4. **Satisfacción laboral insuficiente**
   - Clasificada como **"Mala"**, al no alcanzar el valor de 3 en la escala
   - Se vincula directamente con la intención de abandono

5. **Problemas en la capacitación**
   - El **75% de los empleados no completó** la capacitación asignada
   - Representa una pérdida presupuestaria superior a **1 millón de dólares**
   - Implica una **pérdida del 75% de la inversión total** en capacitación

---

### 📌 Recomendaciones sugeridas

- Revisar los contenidos y formatos de capacitación
- Diseñar estrategias para mejorar el compromiso y satisfacción del personal
- Implementar acciones correctivas sobre el ambiente laboral
- Establecer métricas de seguimiento y mejora continua

## 🎯 Impacto en el Negocio

---

La combinación de rotación elevada y baja satisfacción afecta:
- ⏳ Continuidad operativa
- 📉 Margen de rentabilidad
- 🔄 Agilidad ante cambios
- 🧠 Conservación del conocimiento crítico