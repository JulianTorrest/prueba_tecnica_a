import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL cruda del archivo CSV en GitHub
file_url1 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines/locations.csv'

# Cargar los datos desde la URL
locations_vaccines_df = pd.read_csv(file_url1)

# URL cruda del archivo CSV en GitHub
file_url2 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines/vaccinations-by-manufacturer.csv'

# Cargar los datos desde la URL
vaccinations_by_manufacturer_df = pd.read_csv(file_url2)

# Función para leer y concatenar archivos CSV desde una carpeta en GitHub
def read_and_concat_csv_files(base_url, file_names):
    dfs = []
    for file_name in file_names:
        file_url = base_url + file_name
        response = requests.head(file_url)
        if response.status_code == 200:
            try:
                df = pd.read_csv(file_url)
                dfs.append(df)
            except Exception as e:
                st.error(f"Error al leer el archivo {file_name}: {e}")
        else:
            st.error(f"El archivo {file_name} no existe o no se pudo acceder.")
            continue

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        return combined_df
    else:
        return None

# URL base de la carpeta en GitHub
base_url = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines_country_data/'

# Lista de nombres de los archivos CSV en la carpeta
file_names = [
    "Andorra.csv", "Anguilla.csv", "Algeria.csv", # Lista completa de nombres de archivo aquí
]

# Leer y concatenar los archivos CSV
combined_df = read_and_concat_csv_files(base_url, file_names)

# Mostrar el resultado en Streamlit
st.write("### Datos combinados de los archivos CSV:")
if combined_df is not None:
    st.write(combined_df)
else:
    st.error("No se encontraron datos para mostrar.")
# Leer y concatenar los archivos CSV
dfs = []
for file_name in file_names:
    file_url = base_url + file_name
    df = pd.read_csv(file_url)
    dfs.append(df)

# Concatenar todos los DataFrames en uno solo
combined_df = pd.concat(dfs, ignore_index=True)
