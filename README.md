# Cloud_Forecasting_CNN_LSTM

En este proyecto se encuentra el codigo necesario para la descarga del producto ACMF del satelite GOES-16. Este producto se usa para determinar las caracteristicas de las nubes en una localizacion geoespacial.

### Archivos .ipynb
1. download - Descarga de archivos .nc del producto ACMF.
2. viewer - Procesamiento de archivos .nc para convertirlos en imagenes .png.
3. lstm_cnn - Red neuronal convolucional que se encarga de tomar como muestra las imagenes generadas en `viewer.ipynb` y generar 6 predicciones adelante.
