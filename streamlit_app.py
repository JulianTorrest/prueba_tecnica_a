import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configura el directorio de trabajo
os.chdir('prueba_tecnica_a')

# Cargar los datos
file_path = 'vaccines/locations.csv'
locations_vaccines_df = pd.read_csv(file_path)

# Limpieza de datos
locations_vaccines_df['location'] = locations_vaccines_df['location'].str.strip()
locations_vaccines_df['vaccines'] = locations_vaccines_df['vaccines'].str.strip()
locations_vaccines_df['last_observation_date'] = pd.to_datetime(locations_vaccines_df['last_observation_date'], errors='coerce')
locations_vaccines_df['iso_code'] = locations_vaccines_df['iso_code'].astype(str)

# Definir el diccionario de países a continentes
country_to_continent = {
    # Tu diccionario completo aquí...
    'Afghanistan': 'Asia', 'Albania': 'Europe', # Continúa...
}

# Asignar los continentes al DataFrame
locations_vaccines_df['continent'] = locations_vaccines_df['location'].map(country_to_continent)

# Configurar Streamlit para el filtro interactivo
st.title("Análisis de Vacunas por Continente")
selected_continent = st.selectbox('Selecciona un continente:', options=sorted(locations_vaccines_df['continent'].unique()))

# Filtrar el DataFrame por el continente seleccionado
filtered_data = locations_vaccines_df[locations_vaccines_df['continent'] == selected_continent]

# Crear el gráfico
plt.figure(figsize=(10, 7))
sns.barplot(x='vaccines', y='location', data=filtered_data, palette='viridis')
plt.title(f'Cantidad de Vacunas Utilizadas en {selected_continent}')
plt.xlabel('Cantidad de Vacunas')
plt.ylabel('País')
st.pyplot(plt)
