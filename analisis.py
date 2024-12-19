import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

# Lee el archivo CSV
data_clean = pd.read_csv('/home/kike/Documents/maestria/registro.csv')

# Asegura que la columna 'Fecha de medición' sea de tipo datetime
data_clean['Fecha de medición'] = pd.to_datetime(data_clean['Fecha de medición'])

# Establecer la columna 'Fecha de medición' como índice
data_clean.set_index('Fecha de medición', inplace=True)

# Selecciona solo las columnas numéricas
data_clean_numeric = data_clean.select_dtypes(include='number')

# Crear un diccionario para las predicciones
predictions = {}

# Ajustar el modelo ARIMA y realizar la predicción para cada columna
for column in data_clean_numeric.columns:
    # Ajustar el modelo ARIMA para la columna actual
    model = ARIMA(data_clean_numeric[column], order=(5, 1, 0))  # Orden (p, d, q) que puedes ajustar según sea necesario
    model_fit = model.fit()

    # Realizar la predicción para los próximos 30 días
    forecast = model_fit.forecast(steps=30)

    # Guardar la predicción
    predictions[column] = forecast

# Graficar los resultados
plt.figure(figsize=(10, 6))

# Graficar los datos originales
for column in data_clean_numeric.columns:
    plt.plot(data_clean_numeric.index, data_clean_numeric[column], label=column)

# Graficar las predicciones
for column, forecast in predictions.items():
    # Crear fechas futuras para las predicciones
    future_dates = pd.date_range(start=data_clean_numeric.index[-1] + pd.Timedelta(days=1), periods=30, freq='D')
    plt.plot(future_dates, forecast, label=f'{column} (Predicción)', linestyle='--')

# Agregar título y etiquetas
plt.title('Datos de Mediciones y Predicción ARIMA a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Valor')

# Rotar las fechas en el eje X para mayor legibilidad
plt.xticks(rotation=45)

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.tight_layout()  # Ajusta el diseño para evitar sobreposiciones
plt.show()
