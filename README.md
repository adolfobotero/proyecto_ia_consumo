
# Predicción de Consumo Energético

Este proyecto utiliza un modelo de aprendizaje automático basado en **Random Forest** para predecir el consumo energético de una comunidad a partir de datos históricos y factores climáticos.

## Contenido del Repositorio
- `modelo_consumo_energetico.pkl`: Modelo entrenado para realizar predicciones.
- `escalador_consumo_energetico.pkl`: Escalador para normalizar los datos de entrada.
- `prediccion_consumo.py`: Script para cargar el modelo, procesar datos y realizar predicciones.
- `Granja_Solar_2023_2024.xlsx`: Datos de ejemplo utilizados para entrenar y evaluar el modelo.

## Requisitos Previos
1. **Python 3.7 o superior**.
2. Instalar las bibliotecas necesarias:
   ```bash
   pip install pandas scikit-learn joblib
   ```

## Cómo Usar
1. Descarga o clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Coloca los archivos de modelo (`.pkl`) y los datos en el mismo directorio que el script.

3. Ejecuta el script de predicción:
   ```bash
   python prediccion_consumo.py
   ```

4. Modifica los datos de entrada en el script `prediccion_consumo.py` para adaptarlos a tus necesidades. Por ejemplo:
   ```python
   datos_ejemplo = [25.0, 70.0, 300.0, 1, 1, 15]  # Cambia estos valores con tus datos reales
   ```

## Estructura de los Datos
El modelo requiere las siguientes columnas como entrada:
- **Temperatura**: Temperatura promedio diaria (°C).
- **Humedad**: Humedad promedio diaria (%).
- **Consumo_Previo**: Consumo energético del día anterior (kWh).
- **Uso_Renovable**: Indicador binario (0: No, 1: Sí) para el uso de energía renovable.
- **Mes**: Mes del año (1-12).
- **Día**: Día del mes (1-31).

## Notas Técnicas
- El modelo se entrenó con datos simulados de una granja solar en Colombia, correspondientes a los años 2023 y 2024.
- El rendimiento del modelo se evaluó utilizando el Error Cuadrático Medio (MSE).

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras un error o deseas mejorar el proyecto, envía un pull request.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.
