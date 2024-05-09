# -*- coding: utf-8 -*-
"""Prueba Tecnica Avianca Pagina Web.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rLrpPSmaLr9TDa2lMbKOPGj1HFEQKB5w
"""

!pip install pandas
import pandas as pd

pip install pandas streamlit
git clone https://github.com/JulianTorrest/prueba_tecnica_a.git

import os
os.chdir('prueba_tecnica_a')

# Ruta al archivo CSV
file_path = '/content/prueba_tecnica_a/vaccines/locations.csv'

# Cargar los datos
locations_vaccines_df = pd.read_csv(file_path)

# Mostrar las primeras filas para inspección
print(locations_vaccines_df.head())

# Verificar valores faltantes
print(locations_vaccines_df.isnull().sum())

# Limpiar strings: eliminar espacios al principio y al final, y otros caracteres no deseados
locations_vaccines_df['location'] = locations_vaccines_df['location'].str.strip()
locations_vaccines_df['vaccines'] = locations_vaccines_df['vaccines'].str.strip()

# Convertir fechas
locations_vaccines_df['last_observation_date'] = pd.to_datetime(locations_vaccines_df['last_observation_date'], errors='coerce')

# Asegurar que los códigos de país sean tratados como strings en caso de que pandas los haya interpretado incorrectamente
locations_vaccines_df['iso_code'] = locations_vaccines_df['iso_code'].astype(str)

# Listar solo las ubicaciones únicas
print(locations_vaccines_df['location'].unique())

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Definir el diccionario de países a continentes
country_to_continent = {
    'Afghanistan': 'Asia', 'Albania': 'Europe', 'Algeria': 'Africa',
    'Andorra': 'Europe', 'Angola': 'Africa', 'Anguilla': 'North America',
    'Antigua and Barbuda': 'North America', 'Argentina': 'South America',
    'Armenia': 'Asia', 'Aruba': 'North America', 'Australia': 'Oceania',
    'Austria': 'Europe', 'Azerbaijan': 'Asia', 'Bahamas': 'North America',
    'Bahrain': 'Asia', 'Bangladesh': 'Asia', 'Barbados': 'North America',
    'Belarus': 'Europe', 'Belgium': 'Europe', 'Belize': 'North America',
    'Bermuda': 'North America', 'Bhutan': 'Asia', 'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe', 'Botswana': 'Africa', 'Brazil': 'South America',
    'Brunei': 'Asia', 'Bulgaria': 'Europe', 'Cambodia': 'Asia', 'Cameroon': 'Africa',
    'Canada': 'North America', 'Cape Verde': 'Africa', 'Cayman Islands': 'North America',
    'Chile': 'South America', 'China': 'Asia', 'Colombia': 'South America',
    'Congo': 'Africa', 'Costa Rica': 'North America', "Cote d'Ivoire": 'Africa',
    'Croatia': 'Europe', 'Curacao': 'North America', 'Cyprus': 'Europe',
    'Czechia': 'Europe', 'Democratic Republic of Congo': 'Africa',
    'Denmark': 'Europe', 'Djibouti': 'Africa', 'Dominica': 'North America',
    'Dominican Republic': 'North America', 'Ecuador': 'South America',
    'Egypt': 'Africa', 'El Salvador': 'North America', 'England': 'Europe',
    'Equatorial Guinea': 'Africa', 'Estonia': 'Europe', 'Eswatini': 'Africa',
    'Ethiopia': 'Africa', 'Faeroe Islands': 'Europe', 'Falkland Islands': 'South America',
    'Fiji': 'Oceania', 'Finland': 'Europe', 'France': 'Europe', 'Gabon': 'Africa',
    'Gambia': 'Africa', 'Georgia': 'Asia', 'Germany': 'Europe', 'Ghana': 'Africa',
    'Gibraltar': 'Europe', 'Greece': 'Europe', 'Greenland': 'North America',
    'Grenada': 'North America', 'Guatemala': 'North America', 'Guernsey': 'Europe',
    'Guinea': 'Africa', 'Guyana': 'South America', 'Honduras': 'North America',
    'Hong Kong': 'Asia', 'Hungary': 'Europe', 'Iceland': 'Europe',
    'India': 'Asia', 'Indonesia': 'Asia', 'Iran': 'Asia', 'Iraq': 'Asia',
    'Ireland': 'Europe', 'Isle of Man': 'Europe', 'Israel': 'Asia',
    'Italy': 'Europe', 'Jamaica': 'North America', 'Japan': 'Asia',
    'Jersey': 'Europe', 'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kenya': 'Africa',
    'Kosovo': 'Europe', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia', 'Laos': 'Asia',
    'Latvia': 'Europe', 'Lebanon': 'Asia', 'Lesotho': 'Africa', 'Libya': 'Africa',
    'Liechtenstein': 'Europe', 'Lithuania': 'Europe', 'Luxembourg': 'Europe',
    'Macao': 'Asia', 'Malawi': 'Africa', 'Malaysia': 'Asia', 'Maldives': 'Asia',
    'Mali': 'Africa', 'Malta': 'Europe', 'Mauritania': 'Africa', 'Mauritius': 'Africa',
    'Mexico': 'North America', 'Moldova': 'Europe', 'Monaco': 'Europe',
    'Mongolia': 'Asia', 'Montenegro': 'Europe', 'Montserrat': 'North America',
    'Morocco': 'Africa', 'Mozambique': 'Africa', 'Myanmar': 'Asia',
    'Namibia': 'Africa', 'Nauru': 'Oceania', 'Nepal': 'Asia', 'Netherlands': 'Europe',
    'New Zealand': 'Oceania', 'Nicaragua': 'North America', 'Niger': 'Africa',
    'Nigeria': 'Africa', 'North Macedonia': 'Europe', 'Northern Cyprus': 'Europe',
    'Northern Ireland': 'Europe', 'Norway': 'Europe', 'Oman': 'Asia',
    'Pakistan': 'Asia', 'Palestine': 'Asia', 'Panama': 'North America',
    'Papua New Guinea': 'Oceania', 'Paraguay': 'South America', 'Peru': 'South America',
    'Philippines': 'Asia', 'Poland': 'Europe', 'Portugal': 'Europe',
    'Qatar': 'Asia', 'Romania': 'Europe', 'Russia': 'Europe', 'Rwanda': 'Africa',
    'Saint Helena': 'Africa', 'Saint Kitts and Nevis': 'North America',
    'Saint Lucia': 'North America', 'Saint Vincent and the Grenadines': 'North America',
    'Samoa': 'Oceania', 'San Marino': 'Europe', 'Sao Tome and Principe': 'Africa',
    'Saudi Arabia': 'Asia', 'Scotland': 'Europe', 'Senegal': 'Africa',
    'Serbia': 'Europe', 'Seychelles': 'Africa', 'Sierra Leone': 'Africa',
    'Singapore': 'Asia', 'Slovakia': 'Europe', 'Slovenia': 'Europe',
    'Solomon Islands': 'Oceania', 'Somalia': 'Africa', 'South Africa': 'Africa',
    'South Korea': 'Asia', 'South Sudan': 'Africa', 'Spain': 'Europe',
    'Sri Lanka': 'Asia', 'Sudan': 'Africa', 'Suriname': 'South America',
    'Sweden': 'Europe', 'Switzerland': 'Europe', 'Syria': 'Asia', 'Taiwan': 'Asia',
    'Thailand': 'Asia', 'Timor': 'Asia', 'Togo': 'Africa', 'Tonga': 'Oceania',
    'Trinidad and Tobago': 'North America', 'Tunisia': 'Africa', 'Turkey': 'Europe',
    'Turks and Caicos Islands': 'North America', 'Uganda': 'Africa',
    'Ukraine': 'Europe', 'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe',
    'United States': 'North America', 'Uruguay': 'South America', 'Uzbekistan': 'Asia',
    'Venezuela': 'South America', 'Vietnam': 'Asia', 'Wales': 'Europe',
    'Zambia': 'Africa', 'Zimbabwe': 'Africa'
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
sns.barplot(x='vaccine_count', y='location', data=filtered_data, errorbar=None, palette='viridis')
plt.title(f'Cantidad de Vacunas Utilizadas en {selected_continent}')
plt.xlabel('Cantidad de Vacunas')
plt.ylabel('País')
st.pyplot(plt.gcf())

# Ruta al archivo CSV
file_path = '/content/prueba_tecnica_a/vaccines/vaccinations-by-manufacturer.csv'

# Cargar los datos
vaccinations_by_manufacturer = pd.read_csv(file_path)

# Mostrar las primeras filas para inspección
print(vaccinations_by_manufacturer.head())

# Ruta al archivo CSV
file_path = '/content/prueba_tecnica_a/testing/covid-testing-all-observations.csv'

# Cargar los datos
covid_testing_all_observations = pd.read_csv(file_path)

# Mostrar las primeras filas para inspección
print(covid_testing_all_observations.head())

# Ruta al archivo CSV
file_path = '/content/prueba_tecnica_a/testing/covid-testing-latest-data-source-details.csv'

# Cargar los datos
covid_testing_latest_data_source_details = pd.read_csv(file_path)

# Mostrar las primeras filas para inspección
print(covid_testing_latest_data_source_details.head())

import os
import pandas as pd

# Crear una lista para almacenar los datos de todos los archivos Excel
all_data = []

# Asegúrate de definir 'folder_path' correctamente
folder_path = '/content/prueba_tecnica_a/vaccines_country_data'  # Ajusta esta ruta según la ubicación de tus archivos

# Iterar sobre los nombres de los archivos
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):  # Verificar si el archivo es un archivo CSV
        # Crear la ruta completa del archivo
        file_path = os.path.join(folder_path, file_name)
        try:
            # Leer el archivo CSV y almacenar los datos en un DataFrame
            data = pd.read_csv(file_path)
            # Agregar los datos del archivo a la lista
            all_data.append(data)
        except pd.errors.EmptyDataError:
            print(f'El archivo {file_name} está vacío y no se ha cargado.')

# Combinar todos los DataFrames en uno solo, asegurándose de que 'all_data' no esté vacío
if all_data:
    combined_data_vaccines_country = pd.concat(all_data, ignore_index=True)
else:
    print("No se encontraron datos para combinar.")

streamlit run app.py
