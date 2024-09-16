# Cloud_Forecasting_CNN_LSTM

Este proyecto contiene el código necesario para la descarga del producto ACMF del satélite GOES-16. 

### Introducción

El satélite GOES-16 es parte de la serie de satélites GOES-R de la NOAA, diseñado para proporcionar datos meteorológicos en tiempo real. Uno de los productos clave que ofrece es el **Advanced Baseline Imager Cloud Mask (ACMF)**, que se utiliza para determinar las características de las nubes, como la cobertura, altura y fase, en una ubicación geoespacial específica.

### Archivos .ipynb

1. **`download.ipynb`** - Descarga de archivos .nc del producto ACMF.  
   Este cuaderno permite descargar las imágenes necesarias parametrizando las fechas de interés. Para ello, es necesario definir los valores de:
   - `fecha_hora_inicio`
   - `fecha_hora_fin`
   
   Estos valores deben estar en el formato `YYYYmmdd-HHMMSS`.

   ![image](https://github.com/user-attachments/assets/b44f6e40-ac9f-4229-a558-801db34bdb26)

2. **`viewer.ipynb`** - Procesamiento de archivos .nc para convertirlos en imágenes .png. También permite visualizar la metadata e información relevante sobre los archivos .nc.  
   
   Imagen generada por el producto ACMF:
   
   ![image](https://github.com/user-attachments/assets/c0859a12-a8cf-43c1-8d5d-ab7203e44039)
   
   ![image](https://github.com/user-attachments/assets/0f702f48-2374-4804-856e-8bc04a8a8472)

3. **`lstm_cnn.ipynb`** - Red neuronal convolucional que toma como entrada las imágenes generadas en `viewer.ipynb` y genera predicciones para 6 intervalos de tiempo futuros (periodos diezminutales).

   ![forecast_clouds](https://github.com/user-attachments/assets/b3d906db-a76c-40b3-abbb-a7431fdf98cd)

