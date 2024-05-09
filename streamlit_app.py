import streamlit as st
import pandas as pd

# Función para leer y concatenar archivos CSV
def read_and_concat_csv_files(base_url, file_names):
    dfs = []
    for file_name in file_names:
        file_url = base_url + file_name.replace(" ", "%20")  # Reemplazar espacios en blanco con "%20"
        try:
            df = pd.read_csv(file_url)
            dfs.append(df)
        except Exception as e:
            st.error(f"Error al leer el archivo {file_name}: {e}")
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# URL base de la carpeta en GitHub
base_url = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines_country_data/'

# Lista de nombres de los archivos CSV en la carpeta
file_names = [
    "Andorra.csv", "Anguilla.csv", "Algeria.csv", "Angola.csv", "Albania.csv", "Afghanistan.csv", "Antigua%20and%20Barbuda.csv", "Armenia.csv", "Botswana.csv", "Azerbaijan.csv", "Cambodia.csv", "Cameroon.csv", "Aruba.csv", "Bahamas.csv", "Bermuda.csv", "Argentina.csv", "Austria.csv", "Belgium.csv", "Bahrain.csv", "Belize.csv", "Canada.csv", "Barbados.csv", "Brazil.csv", "Belarus.csv", "Bolivia.csv", "Bhutan.csv", "Bulgaria.csv", "Bangladesh.csv", "Bosnia%20and%20Herzegovina.csv", "Brunei.csv", "Australia.csv", "Cayman%20Islands.csv", "Chile.csv", "Cote%20d'Ivoire.csv", "China.csv", "England.csv", "Denmark.csv", "Democratic%20Republic%20of%20Congo.csv", "Djibouti.csv", "Croatia.csv", "El%20Salvador.csv", "Egypt.csv", "Dominican%20Republic.csv", "Dominica.csv", "Cape%20Verde.csv", "Equatorial%20Guinea.csv", "Colombia.csv", "Estonia.csv", "Czechia.csv", "Congo.csv", "Costa%20Rica.csv", "Ecuador.csv", "Cyprus.csv", "Curacao.csv", "Guernsey.csv", "Guatemala.csv", "Guyana.csv", "Fiji.csv", "Greece.csv", "Gabon.csv", "Grenada.csv", "Georgia.csv", "Honduras.csv", "Falkland%20Islands.csv", "Hungary.csv", "Iceland.csv", "Faeroe%20Islands.csv", "Ethiopia.csv", "Guinea.csv", "Gambia.csv", "Ghana.csv", "Gibraltar.csv", "France.csv", "Eswatini.csv", "Germany.csv", "Hong%20Kong.csv", "Greenland.csv", "Finland.csv", "Laos.csv", "Latvia.csv", "Jamaica.csv", "Kosovo.csv", "Lesotho.csv", "Iraq.csv", "Kenya.csv", "Israel.csv", "Jordan.csv", "Jersey.csv", "Kyrgyzstan.csv", "Ireland.csv", "India.csv", "Isle%20of%20Man.csv", "Italy.csv", "Indonesia.csv", "Libya.csv", "Liechtenstein.csv", "Japan.csv", "Iran.csv", "Kazakhstan.csv", "Lebanon.csv", "Luxembourg.csv", "Lithuania.csv", "Kuwait.csv", "Mauritania.csv", "Montenegro.csv", "Moldova.csv", "Mali.csv", "Malawi.csv", "Malaysia.csv", "Mexico.csv", "Mauritius.csv", "Maldives.csv", "Monaco.csv", "Malta.csv", "Macao.csv", "Mongolia.csv", "Morocco.csv", "Montserrat.csv", "Northern%20Cyprus.csv", "Nepal.csv", "Niger.csv", "Poland.csv", "Netherlands.csv", "Oman.csv", "Norway.csv", "Panama.csv", "Nicaragua.csv", "Portugal.csv", "Peru.csv", "Nauru.csv", "Philippines.csv", "Paraguay.csv", "Palau.csv", "Palestine.csv", "Myanmar.csv", "North%20Macedonia.csv", "Papua%20New%20Guinea.csv", "Northern%20Ireland.csv", "New%20Zealand.csv", "Mozambique.csv", "Nigeria.csv", "Namibia.csv", "Pakistan.csv", "Saint%20Lucia.csv", "Singapore.csv", "Scotland.csv", "Sierra%20Leone.csv", "Seychelles.csv", "Samoa.csv", "Saint%20Vincent%20and%20the%20Grenadines.csv", "San%20Marino.csv", "Slovakia.csv", "Qatar.csv", "Saint%20Helena.csv", "Serbia.csv", "South%20Korea.csv", "Slovenia.csv", "Sao%20Tome%20and%20Principe.csv", "Russia.csv", "Saudi%20Arabia.csv", "Senegal.csv", "Somalia.csv", "Solomon%20Islands.csv", "Rwanda.csv", "Saint%20Kitts%20and%20Nevis.csv", "Romania.csv", "South%20Sudan.csv", "South%20Africa.csv", "Togo.csv", "Syria.csv", "Spain.csv", "Tonga.csv", "Thailand.csv", "Sweden.csv", "Suriname.csv", "Turkey.csv", "Uruguay.csv", "Ukraine.csv", "United%20States.csv", "Timor.csv", "Trinidad%20and%20Tobago.csv", "Uganda.csv", "Uzbekistan.csv", "Sudan.csv", "Turks%20and%20Caicos%20Islands.csv", "Switzerland.csv", "Sri%20Lanka.csv", "Tunisia.csv", "Vietnam.csv", "Taiwan.csv", "Venezuela.csv", "United%20Kingdom.csv", "United%20Arab%20Emirates.csv", "Zambia.csv", "Wales.csv", "Zimbabwe.csv"
]

# Leer y concatenar los archivos CSV
combined_df = read_and_concat_csv_files(base_url, file_names)


# URL cruda del archivo CSV en GitHub
file_url1 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines/locations.csv'

# Cargar los datos desde la URL
locations_vaccines_df = pd.read_csv(file_url1)

# URL cruda del archivo CSV en GitHub
file_url2 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines/vaccinations-by-manufacturer.csv'

# Cargar los datos desde la URL
vaccinations_by_manufacturer_df = pd.read_csv(file_url2)

# URL cruda del archivo CSV en GitHub
file_url3 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/testing/covid-testing-all-observations.csv'

# Cargar los datos desde la URL
covid_testing_all_observations_df = pd.read_csv(file_url3)

# URL cruda del archivo CSV en GitHub
file_url4 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/testing/covid-testing-latest-data-source-details.csv'

# Cargar los datos desde la URL
covid_testing_latest_data_source_details_df = pd.read_csv(file_url4)

# Mostrar el resultado en Streamlit
st.write("### Dataframe: combined_df")
st.write(vaccines_country_data_df)

# Ahora mostramos los otros DataFrames con títulos
st.write("### DataFrame: locations_vaccines_df")
st.write(locations_vaccines_df)

st.write("### DataFrame: vaccinations_by_manufacturer_df")
st.write(vaccinations_by_manufacturer_df)

st.write("### DataFrame: covid_testing_all_observations_df")
st.write(covid_testing_all_observations_df)

st.write("### DataFrame: covid_testing_latest_data_source_details_df")
st.write(covid_testing_latest_data_source_details_df)

# Análisis exploratorio del DataFrame locations_vaccines_df
st.write("## Análisis exploratorio del DataFrame locations_vaccines_df")

# Descripción del DataFrame
st.write("### Descripción del DataFrame")
st.write(locations_vaccines_df.describe())

# Tipos de columnas
st.write("### Tipos de columnas")
st.write(locations_vaccines_df.dtypes)

# Valores faltantes
st.write("### Valores faltantes")
st.write(locations_vaccines_df.isnull().sum())

# Estadísticas básicas para columnas numéricas
st.write("### Estadísticas básicas para columnas numéricas")
st.write(locations_vaccines_df.select_dtypes(include=['float64', 'int64']).describe())

# Visualización de algunas columnas relevantes (por ejemplo, las primeras 5 filas)
st.write("### Visualización de algunas columnas relevantes")
st.write(locations_vaccines_df.head())

# Matriz de correlación (si es relevante)
st.write("### Matriz de correlación")
st.write(locations_vaccines_df.corr())
