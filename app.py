from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime

# Inicializar Flask
app = Flask(__name__)
app.secret_key = 'some_secret_key'

# Variables globales
df_historico = None

# Cargar modelo y escalador
MODEL_PATH = "modelo_consumo_energetico.pkl"
SCALER_PATH = "escalador_consumo_energetico.pkl"

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
else:
    model = None
    scaler = None
    flash("Modelo o escalador no encontrados. Asegúrate de que los archivos estén en el directorio.")

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Cargar datos y graficar
@app.route("/datos", methods=["GET", "POST"])
def datos():
    global df_historico
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            flash("No se cargó ningún archivo.")
            return redirect(url_for("index"))

        try:
            # Cargar datos históricos
            df_historico = pd.read_excel(file)
            df_historico['Fecha'] = pd.to_datetime(df_historico['Fecha'])

            # Graficar datos
            plt.figure(figsize=(10, 5))
            plt.plot(df_historico["Fecha"], df_historico["Consumo"], label="Consumo Histórico", color="blue")
            plt.title("Consumo Histórico")
            plt.xlabel("Fecha")
            plt.ylabel("Consumo (kWh)")
            plt.legend()
            plt.tight_layout()

            # Convertir gráfica a base64
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

            return render_template("datos.html", plot_url=plot_url)
        except Exception as e:
            flash(f"Error procesando archivo: {e}")
            return redirect(url_for("index"))

    return redirect(url_for("index"))

# Realizar predicción
@app.route("/predecir", methods=["POST"])
def predecir():
    global df_historico
    if not model or not scaler:
        flash("Modelo o escalador no cargados.")
        return redirect(url_for("index"))

    try:
        # Obtener datos del formulario
        temperatura = float(request.form["temperatura"])
        humedad = float(request.form["humedad"])
        consumo_previo = float(request.form["consumo_previo"])
        uso_renovable = int(request.form["uso_renovable"])
        mes = int(request.form["mes"])
        dia = int(request.form["dia"])

        # Preparar datos
        datos = [[temperatura, humedad, consumo_previo, uso_renovable, mes, dia]]
        datos_escalados = scaler.transform(datos)
        prediccion = model.predict(datos_escalados)[0]

        # Validar si hay datos históricos
        if df_historico is not None:
            df_prediccion = df_historico.copy()
            nueva_fecha = datetime.now()
            df_prediccion = pd.concat([
                df_prediccion,
                pd.DataFrame({"Fecha": [nueva_fecha], "Consumo": [prediccion]})
            ])
        else:
            flash("No se cargaron datos históricos para graficar.")
            return render_template("resultado.html", prediccion=prediccion)

        # Graficar datos históricos y predicción
        plt.figure(figsize=(12, 6))

        # Línea para los datos históricos
        plt.plot(
            df_historico["Fecha"], 
            df_historico["Consumo"], 
            label="Consumo Histórico", 
            color="#2ca02c",  # Verde
            linewidth=2, 
            marker="o"
        )

        # Línea para la predicción
        if "df_prediccion" in locals() and nueva_fecha:
            plt.plot(
                [df_historico["Fecha"].iloc[-1], nueva_fecha], 
                [df_historico["Consumo"].iloc[-1], prediccion], 
                label=f"Consumo Predicho ({prediccion:.2f} kWh)", 
                color="#ff7f0e",  # Naranja
                linewidth=2, 
                marker="o", 
                linestyle="--"
            )

        # Configuración del gráfico
        plt.title("Consumo Histórico y Predicción", fontsize=16)
        plt.xlabel("Fecha", fontsize=14)
        plt.ylabel("Consumo (kWh)", fontsize=14)
        plt.legend(fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()

        # Convertir gráfica a base64
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template("resultado.html", prediccion=prediccion, plot_url=plot_url)
    except Exception as e:
        flash(f"Error realizando la predicción: {e}")
        return redirect(url_for("index"))

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
