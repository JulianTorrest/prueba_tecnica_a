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

# URL cruda del archivo CSV en GitHub
file_url3 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/testing/covid-testing-all-observations.csv'

# Cargar los datos desde la URL
locations_vaccines_df = pd.read_csv(file_url3)

# URL cruda del archivo CSV en GitHub
file_url4 = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/testing/covid-testing-latest-data-source-details.csv'

# Cargar los datos desde la URL
locations_vaccines_df = pd.read_csv(file_url4)

# Función para leer y concatenar archivos CSV
def read_and_concat_csv_files(base_url, file_names):
    dfs = []
    for file_name in file_names:
        file_url = base_url + file_name
        try:
            df = pd.read_csv(file_url)
            dfs.append(df)
        except Exception as e:
            print(f"Error al leer el archivo {file_name}: {e}")
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# URL base de la carpeta en GitHub
base_url = 'https://raw.githubusercontent.com/JulianTorrest/prueba_tecnica_a/main/vaccines_country_data/'

# Lista de nombres de los archivos CSV en la carpeta
file_names = [
    "Andorra.csv", "Anguilla.csv", "Algeria.csv", "Angola.csv", "Albania.csv", "Afghanistan.csv", "Antigua and Barbuda.csv", "Armenia.csv", "Botswana.csv", "Azerbaijan.csv", "Cambodia.csv", "Cameroon.csv", "Aruba.csv", "Bahamas.csv", "Bermuda.csv", "Argentina.csv", "Austria.csv", "Belgium.csv", "Bahrain.csv", "Belize.csv", "Canada.csv", "Barbados.csv", "Brazil.csv", "Belarus.csv", "Bolivia.csv", "Bhutan.csv", "Bulgaria.csv", "Bangladesh.csv", "Bosnia and Herzegovina.csv", "Brunei.csv", "Australia.csv", "Cayman Islands.csv", "Chile.csv", "Cote d'Ivoire.csv", "China.csv", "England.csv", "Denmark.csv", "Democratic Republic of Congo.csv", "Djibouti.csv", "Croatia.csv", "El Salvador.csv", "Egypt.csv", "Dominican Republic.csv", "Dominica.csv", "Cape Verde.csv", "Equatorial Guinea.csv", "Colombia.csv", "Estonia.csv", "Czechia.csv", "Congo.csv", "Costa Rica.csv", "Ecuador.csv", "Cyprus.csv", "Curacao.csv", "Guernsey.csv", "Guatemala.csv", "Guyana.csv", "Fiji.csv", "Greece.csv", "Gabon.csv", "Grenada.csv", "Georgia.csv", "Honduras.csv", "Falkland Islands.csv", "Hungary.csv", "Iceland.csv", "Faeroe Islands.csv", "Ethiopia.csv", "Guinea.csv", "Gambia.csv", "Ghana.csv", "Gibraltar.csv", "France.csv", "Eswatini.csv", "Germany.csv", "Hong Kong.csv", "Greenland.csv", "Finland.csv", "Laos.csv", "Latvia.csv", "Jamaica.csv", "Kosovo.csv", "Lesotho.csv", "Iraq.csv", "Kenya.csv", "Israel.csv", "Jordan.csv", "Jersey.csv", "Kyrgyzstan.csv", "Ireland.csv", "India.csv", "Isle of Man.csv", "Italy.csv", "Indonesia.csv", "Libya.csv", "Liechtenstein.csv", "Japan.csv", "Iran.csv", "Kazakhstan.csv", "Lebanon.csv", "Luxembourg.csv", "Lithuania.csv", "Kuwait.csv", "Mauritania.csv", "Montenegro.csv", "Moldova.csv", "Mali.csv", "Malawi.csv", "Malaysia.csv", "Mexico.csv", "Mauritius.csv", "Maldives.csv", "Monaco.csv", "Malta.csv", "Macao.csv", "Mongolia.csv", "Morocco.csv", "Montserrat.csv", "Northern Cyprus.csv", "Nepal.csv", "Niger.csv", "Poland.csv", "Netherlands.csv", "Oman.csv", "Norway.csv", "Panama.csv", "Nicaragua.csv", "Portugal.csv", "Peru.csv", "Nauru.csv", "Philippines.csv", "Paraguay.csv", "Palau.csv", "Palestine.csv", "Myanmar.csv", "North Macedonia.csv", "Papua New Guinea.csv", "Northern Ireland.csv", "New Zealand.csv", "Mozambique.csv", "Nigeria.csv", "Namibia.csv", "Pakistan.csv", "Saint Lucia.csv", "Singapore.csv", "Scotland.csv", "Sierra Leone.csv", "Seychelles.csv", "Samoa.csv", "Saint Vincent and the Grenadines.csv", "San Marino.csv", "Slovakia.csv", "Qatar.csv", "Saint Helena.csv", "Serbia.csv", "South Korea.csv", "Slovenia.csv", "Sao Tome and Principe.csv", "Russia.csv", "Saudi Arabia.csv", "Senegal.csv", "Somalia.csv", "Solomon Islands.csv", "Rwanda.csv", "Saint Kitts and Nevis.csv", "Romania.csv", "South Sudan.csv", "South Africa.csv", "Togo.csv", "Syria.csv", "Spain.csv", "Tonga.csv", "Thailand.csv", "Sweden.csv", "Suriname.csv", "Turkey.csv", "Uruguay.csv", "Ukraine.csv", "United States.csv", "Timor.csv", "Trinidad and Tobago.csv", "Uganda.csv", "Uzbekistan.csv", "Sudan.csv", "Turks and Caicos Islands.csv", "Switzerland.csv", "Sri Lanka.csv", "Tunisia.csv", "Vietnam.csv", "Taiwan.csv", "Venezuela.csv", "United Kingdom.csv", "United Arab Emirates.csv", "Zambia.csv", "Wales.csv", "Zimbabwe.csv"
]

# Leer y concatenar los archivos CSV
combined_df = read_and_concat_csv_files(base_url, file_names)

# Mostrar el resultado en Streamlit
st.write("### Datos combinados de los archivos CSV:")
st.write(combined_df)
