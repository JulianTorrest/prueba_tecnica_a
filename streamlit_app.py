import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

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
vaccines_country_data_df = read_and_concat_csv_files(base_url, file_names)

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

# Eliminar valores faltantes
vaccines_country_data_df.dropna(inplace=True)
locations_vaccines_df.dropna(inplace=True)
vaccinations_by_manufacturer_df.dropna(inplace=True)
covid_testing_all_observations_df.dropna(inplace=True)
covid_testing_latest_data_source_details_df.dropna(inplace=True)

# Mostrar el resultado en Streamlit
st.write("### Dataframe: vaccines_country_data_df")
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

# Análisis exploratorio del DataFrame vaccines_country_data_df
st.write("## Análisis exploratorio del DataFrame vaccines_country_data_df")

# Descripción del DataFrame
st.write("### Descripción del DataFrame")
st.write(vaccines_country_data_df.describe())

# Tipos de columnas
st.write("### Tipos de columnas")
st.write(vaccines_country_data_df.dtypes)

# Valores faltantes
st.write("### Valores faltantes")
st.write(vaccines_country_data_df.isnull().sum())

# Verificar si hay columnas numéricas
numeric_cols = vaccines_country_data_df.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_cols) > 0:
    # Estadísticas básicas para columnas numéricas
    st.write("### Estadísticas básicas para columnas numéricas")
    st.write(vaccines_country_data_df[numeric_cols].describe())
else:
    st.write("No hay columnas numéricas en este DataFrame.")

# Visualización de algunas columnas relevantes (por ejemplo, las primeras 5 filas)
st.write("### Visualización de algunas columnas relevantes")
st.write(vaccines_country_data_df.head())

# Matriz de correlación y mapa de calor
if len(numeric_cols) > 1:
    st.write("### Matriz de correlación")
    st.write(vaccines_country_data_df[numeric_cols].corr())

    # Graficar el mapa de calor
    st.write("### Mapa de calor de la matriz de correlación")
    correlation_matrix = vaccines_country_data_df[numeric_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot(plt)  # Mostrar el mapa de calor en Streamlit
else:
    st.write("No hay suficientes columnas numéricas para calcular la matriz de correlación.")
    
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

# Verificar si hay columnas numéricas
numeric_cols = locations_vaccines_df.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_cols) > 0:
    # Estadísticas básicas para columnas numéricas
    st.write("### Estadísticas básicas para columnas numéricas")
    st.write(locations_vaccines_df[numeric_cols].describe())
else:
    st.write("No hay columnas numéricas en este DataFrame.")

# Análisis exploratorio del DataFrame vaccinations_by_manufacturer_df
st.write("## Análisis exploratorio del DataFrame vaccinations_by_manufacturer_df")

# Descripción del DataFrame
st.write("### Descripción del DataFrame")
st.write(vaccinations_by_manufacturer_df.describe())

# Tipos de columnas
st.write("### Tipos de columnas")
st.write(vaccinations_by_manufacturer_df.dtypes)

# Valores faltantes
st.write("### Valores faltantes")
st.write(vaccinations_by_manufacturer_df.isnull().sum())

# Matriz de correlación
st.write("### Matriz de correlación")
st.write(vaccinations_by_manufacturer_df[['total_vaccinations']].corr())

# Obtener la matriz de correlación
correlation_matrix = vaccinations_by_manufacturer_df[['total_vaccinations']].corr()

# Graficar el mapa de calor
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matriz de correlación')
plt.xlabel('Columnas')
plt.ylabel('Columnas')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()

# Mostrar el mapa de calor en Streamlit
st.pyplot(plt)


# Análisis exploratorio del DataFrame covid_testing_all_observations_df
st.write("## Análisis exploratorio del DataFrame covid_testing_all_observations_df")

# Descripción del DataFrame
st.write("### Descripción del DataFrame")
st.write(covid_testing_all_observations_df.describe())

# Tipos de columnas
st.write("### Tipos de columnas")
st.write(covid_testing_all_observations_df.dtypes)

# Valores faltantes
st.write("### Valores faltantes")
st.write(covid_testing_all_observations_df.isnull().sum())

# Estadísticas básicas para columnas numéricas
st.write("### Estadísticas básicas para columnas numéricas")
st.write(covid_testing_all_observations_df.select_dtypes(include=['float64', 'int64']).describe())

# Visualización de algunas columnas relevantes (por ejemplo, las primeras 5 filas)
st.write("### Visualización de algunas columnas relevantes")
st.write(covid_testing_all_observations_df.head())

# Seleccionar solo las columnas numéricas
numeric_cols = covid_testing_all_observations_df.select_dtypes(include=['float64', 'int64'])

# Obtener la matriz de correlación
correlation_matrix = numeric_cols.corr()

# Graficar el mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matriz de correlación para columnas numéricas')
plt.xlabel('Columnas')
plt.ylabel('Columnas')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()

# Mostrar el mapa de calor en Streamlit
st.pyplot(plt)

# Análisis exploratorio del DataFrame covid_testing_latest_data_source_details_df
st.write("## Análisis exploratorio del DataFrame covid_testing_latest_data_source_details_df")

# Descripción del DataFrame
st.write("### Descripción del DataFrame")
st.write(covid_testing_latest_data_source_details_df.describe())

# Tipos de columnas
st.write("### Tipos de columnas")
st.write(covid_testing_latest_data_source_details_df.dtypes)

# Valores faltantes
st.write("### Valores faltantes")
st.write(covid_testing_latest_data_source_details_df.isnull().sum())

# Estadísticas básicas para columnas numéricas
st.write("### Estadísticas básicas para columnas numéricas")
st.write(covid_testing_latest_data_source_details_df.select_dtypes(include=['float64', 'int64']).describe())

# Visualización de algunas columnas relevantes (por ejemplo, las primeras 5 filas)
st.write("### Visualización de algunas columnas relevantes")
st.write(covid_testing_latest_data_source_details_df.head())

# Seleccionar solo las columnas numéricas
numeric_cols_latest = covid_testing_latest_data_source_details_df.select_dtypes(include=['float64', 'int64'])

# Matriz de correlación para las columnas numéricas
st.write("### Matriz de correlación para columnas numéricas")
st.write(numeric_cols_latest.corr())

# Obtener la matriz de correlación
correlation_matrix = numeric_cols_latest.corr()

# Graficar el mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matriz de correlación para columnas numéricas')
plt.xlabel('Columnas')
plt.ylabel('Columnas')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()

# Mostrar el mapa de calor en Streamlit
st.pyplot(plt)

def explore_dataframe(df):
    """
    Muestra los valores únicos de las columnas categóricas y calcula estadísticas básicas para las numéricas.

    Parámetros:
    - df (DataFrame): El DataFrame que se desea explorar.
    """
    st.write("### Valores únicos de las columnas categóricas:")
    for column in df.select_dtypes(include=['object']).columns:
        st.write(f"#### {column}")
        st.write(df[column].unique())

    st.write("### Estadísticas básicas de las columnas numéricas:")
    st.write(df.describe())

# Mostrar las opciones para el DataFrame vaccines_country_data_df
st.write("### Opciones para el DataFrame vaccines_country_data_df")
# Aquí debes cargar y asignar a vaccines_country_data_df el DataFrame que desees analizar
explore_dataframe(vaccines_country_data_df)

# Mostrar las opciones para el DataFrame locations_vaccines_df
st.write("### Opciones para el DataFrame locations_vaccines_df")
# Aquí debes cargar y asignar a locations_vaccines_df el DataFrame que desees analizar
explore_dataframe(locations_vaccines_df)

# Mostrar las opciones para el DataFrame vaccinations_by_manufacturer_df
st.write("### Opciones para el DataFrame vaccinations_by_manufacturer_df")
# Aquí debes cargar y asignar a vaccinations_by_manufacturer_df el DataFrame que desees analizar
explore_dataframe(vaccinations_by_manufacturer_df)

# Mostrar las opciones para el DataFrame covid_testing_all_observations_df
st.write("### Opciones para el DataFrame covid_testing_all_observations_df")
# Aquí debes cargar y asignar a covid_testing_all_observations_df el DataFrame que desees analizar
explore_dataframe(covid_testing_all_observations_df)

# Mostrar las opciones para el DataFrame covid_testing_latest_data_source_details_df
st.write("### Opciones para el DataFrame covid_testing_latest_data_source_details_df")
# Aquí debes cargar y asignar a covid_testing_latest_data_source_details_df el DataFrame que desees analizar
explore_dataframe(covid_testing_latest_data_source_details_df)

# Eliminación de columnas irrelevantes
vaccines_country_data_df.drop(['source_url'], axis=1, inplace=True)

# Eliminación de columnas irrelevantes
locations_vaccines_df.drop(['iso_code'], axis=1, inplace=True)

# Eliminación de columnas irrelevantes
covid_testing_all_observations_df.drop(['ISO code', 'Source URL'], axis=1, inplace=True)

# Eliminación de columnas irrelevantes
covid_testing_latest_data_source_details_df.drop(['ISO code', 'Source URL', 'General source label'], axis=1, inplace=True)

# Función para mostrar gráficos EDA en Streamlit
def plot_eda_streamlit(df, name):
    st.write(f"## Análisis exploratorio de {name}")

    # Gráfico de barras para columnas categóricas
    st.write("### Gráfico de barras para columnas categóricas")
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        st.write(f"#### {column}")
        st.bar_chart(df[column].value_counts())

    # Histograma para columnas numéricas
    st.write("### Histograma para columnas numéricas")
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_columns) >= 2:
        for column in numeric_columns:
            st.write(f"#### {column}")
            st.line_chart(df[column].value_counts())

        # Diagrama de dispersión para pares de columnas numéricas
        st.write("### Diagrama de dispersión para pares de columnas numéricas")
        st.write("#### Pairplot")
        sns.pairplot(df[numeric_columns])
        st.pyplot(plt)  # Mostrar el pairplot en Streamlit
    else:
        st.write("No hay suficientes columnas numéricas para generar el pairplot.")

# Mostrar gráficos EDA para cada DataFrame en Streamlit
plot_eda_streamlit(vaccines_country_data_df, "vaccines_country_data_df")
plot_eda_streamlit(locations_vaccines_df, "locations_vaccines_df")
plot_eda_streamlit(vaccinations_by_manufacturer_df, "vaccinations_by_manufacturer_df")
plot_eda_streamlit(covid_testing_all_observations_df, "covid_testing_all_observations_df")
plot_eda_streamlit(covid_testing_latest_data_source_details_df, "covid_testing_latest_data_source_details_df")
        
# Verificar si hay columnas numéricas
numeric_cols = covid_testing_latest_data_source_details_df.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_cols) > 0:
    # Estadísticas básicas para columnas numéricas
    st.write("### Estadísticas básicas para columnas numéricas")
    st.write(covid_testing_latest_data_source_details_df[numeric_cols].describe())
else:
    st.write("No hay columnas numéricas en este DataFrame.")

def encode_categorical(df, categorical_columns):
    # Eliminar filas con valores faltantes en columnas categóricas
    df.dropna(subset=categorical_columns, inplace=True)
    
    # Verificar si quedan columnas categóricas después de eliminar los valores faltantes
    if len(categorical_columns) == 0:
        st.warning("No hay columnas categóricas después de eliminar los valores faltantes.")
        return None
    
    # Crear el codificador OneHotEncoder
    encoder = OneHotEncoder(sparse=False, drop='first')
    
    # Codificar las columnas categóricas
    encoded_features = encoder.fit_transform(df[categorical_columns])
    
    # Crear un DataFrame con las características codificadas
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names(categorical_columns))
    
    return encoded_df

st.write("### Predicción de vacunaciones por país")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

# Dividir los datos en características (X) y objetivo (y)
X = vaccines_country_data_df.drop(columns=['total_vaccinations'])
y = vaccines_country_data_df['total_vaccinations']

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir transformadores para datos numéricos y categóricos
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinar transformadores
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Definir modelos
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(),
    "ElasticNet": ElasticNet(),
    "Random Forest": RandomForestRegressor(),
    "Gradient Boosting": GradientBoostingRegressor(),
    "AdaBoost": AdaBoostRegressor(),
    "Support Vector Machine": SVR(),
    "Neural Network": MLPRegressor(max_iter=1000),
    "XGBoost": XGBRegressor()
}

# Entrenar y evaluar modelos
results = {}
for name, model in models.items():
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])
    model_pipeline.fit(X_train, y_train)
    train_score = model_pipeline.score(X_train, y_train)
    test_score = model_pipeline.score(X_test, y_test)
    y_pred = model_pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    results[name] = {
        "Training R^2 Score": train_score,
        "Testing R^2 Score": test_score,
        "Mean Squared Error": mse
    }
# Obtener los nombres de los modelos y sus resultados
model_names = list(results.keys())
train_scores = [results[model]["Training R^2 Score"] for model in model_names]
test_scores = [results[model]["Testing R^2 Score"] for model in model_names]
mse_scores = [results[model]["Mean Squared Error"] for model in model_names]

# Crear un gráfico de barras para los puntajes de R^2
plt.figure(figsize=(10, 6))
plt.barh(model_names, test_scores, color='skyblue')
plt.xlabel('R^2 Score')
plt.ylabel('Modelos')
plt.title('Puntajes de R^2 en el conjunto de prueba')
plt.xlim(0, 1)  # Establecer límites para el eje x
plt.gca().invert_yaxis()  # Invertir el eje y para que el modelo con el puntaje más alto esté en la parte superior
plt.show()

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Crear un gráfico de barras para el error cuadrático medio (MSE)
plt.figure(figsize=(10, 6))
plt.barh(model_names, mse_scores, color='salmon')
plt.xlabel('Mean Squared Error')
plt.ylabel('Modelos')
plt.title('Error Cuadrático Medio (MSE)')
plt.gca().invert_yaxis()  # Invertir el eje y para que el modelo con el MSE más bajo esté en la parte superior
plt.show()

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Encontrar el mejor modelo
best_model_name = max(results, key=lambda x: results[x]["Testing R^2 Score"])
best_model_scores = results[best_model_name]

# Mostrar resultados en Streamlit
st.title("Resultados de los Modelos de Predicción")
st.write("Mejor Modelo:", best_model_name)
st.write("R^2 Score (Entrenamiento):", best_model_scores["Training R^2 Score"])
st.write("R^2 Score (Prueba):", best_model_scores["Testing R^2 Score"])
st.write("Error Cuadrático Medio:", best_model_scores["Mean Squared Error"])
