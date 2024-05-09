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

