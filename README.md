
# PREDICCIÓN DE CONSUMO ENERGÉTICO

Este proyecto implementa un sistema de predicción del consumo energético utilizando modelos de aprendizaje automático integrados en una aplicación web desarrollada con **Flask**. La solución permite cargar datos históricos, realizar predicciones basadas en entradas del usuario, y visualizar resultados en gráficos interactivos.

---

## 🚀 Características principales

- **Predicción basada en IA**: Utiliza un modelo de aprendizaje automático entrenado para prever el consumo energético diario.
- **Visualización de datos históricos y predicciones**: Genera gráficos estilizados para interpretar fácilmente los resultados.
- **Interfaz web intuitiva**: Facilita la interacción del usuario mediante formularios y visualizaciones.
- **Personalización**: El sistema puede adaptarse a diferentes tipos de datos energéticos según las necesidades.

---

## 🛠️ Instrucciones de instalación

Sigue los pasos a continuación para configurar y ejecutar el proyecto en tu entorno local:

### 1️⃣ Requisitos previos
- **Python 3.7 o superior**: Asegúrate de tener Python instalado. Verifica tu versión con:
  ```bash
  python --version
  ```
- **Pip**: Instalador de paquetes incluido con Python.
- **Visual Studio Code (VSC)** u otro editor de texto: Para abrir y trabajar con el proyecto.

### 2️⃣ Pasos para configurar el entorno

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/adolfobotero/proyecto_ia_consumo.git
   cd proyecto_ia_consumo
   ```
2. **Abrir proyecto**
   Abrir el proyecto con visual studio code.

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Verificar los archivos necesarios**:
   Asegúrate de que los siguientes archivos estén en el directorio raíz:
   - `modelo_consumo_energetico.pkl`: Modelo entrenado.
   - `escalador_consumo_energetico.pkl`: Escalador de datos.

5. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

6. **Abrir en el navegador**:
   Visita [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para usar la aplicación.

---

## ⚙️ Funcionalidades del sistema

### **Cargar datos históricos**
- **Formato esperado**: Archivo Excel con las siguientes columnas:
  - `Fecha`: En formato `YYYY-MM-DD`.
  - `Consumo`: Consumo energético diario en kWh.
- Una vez cargados, se generará un gráfico con el historial de consumo.

### **Predicción del consumo**
- Ingresa los siguientes datos en el formulario:
  - **Temperatura**: Promedio diario en grados Celsius (ejemplo: 25).
  - **Humedad**: Promedio diario en porcentaje (ejemplo: 70).
  - **Consumo Previo**: Consumo energético del día anterior en kWh (ejemplo: 300).
  - **Uso Renovable**: `0` (sin renovables) o `1` (con renovables).
  - **Mes**: Número del mes (1 a 12).
  - **Día**: Día del mes (1 a 31).
- La predicción se mostrará junto con un gráfico que incluye los datos históricos y el valor predicho.

---

## 🧩 Integrantes del proyecto

- [Luis Adolfo Botero López]

---

## 🎓 Talento TECH
Este proyecto fue desarrollado como parte del programa de **Talento Tech**.
