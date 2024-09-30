#Programa principal
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar a la base de datos MySQL en XAMPP
def conectar_db():
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario",        # Usuario de MySQL
        password="ontraseña", # Contraseña de MySQL
        database="datos"
    )
    return conexion
# Obtener datos de la tabla 
def obtener_datos(conexion):
    query = "SELECT * FROM tabla"
    df = pd.read_sql(query, conexion)
    return df

# Graficar la distribución del stock
def grafico_distribucion_stock(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Stock'], kde=True)
    plt.title('Distribución del Stock')
    plt.xlabel('Cantidad de Stock')
    plt.ylabel('Frecuencia')
    plt.show()