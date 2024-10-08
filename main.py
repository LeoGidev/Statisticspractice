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
        password="contraseña", # Contraseña de MySQL
        database="datos"
    )
    return conexion
# Obtener datos de la tabla 
def obtener_datos(conexion):
    query = "SELECT * FROM Stock"
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

# Graficar 
def grafico_stock_bajo(df):
    stock_bajo = df[df['Stock'] < df['Minimo']]
    
    if not stock_bajo.empty:
        plt.figure(figsize=(12, 8))
        sns.barplot(x='producto', y='Stock', data=stock_bajo, palette='viridis')
        plt.axhline(y=0, color='r', linestyle='--', label='Mínimo')
        plt.title('Productos con Stock Bajo')
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("No hay productos con Stock por debajo del mínimo.")

# Obtener estadísticas básicas de los datos
def obtener_estadisticas(df):
    print("Estadísticas básicas de Stock:")
    print(df.describe())
    
    productos_stock_bajo = df[df['Stock'] < df['Minimo']][['producto', 'Stock']]
    print("\nProductos con Stock por debajo del mínimo:")
    print(productos_stock_bajo)

# Función principal
def main():
    # Conectar a la base de datos
    conexion = conectar_db()
    
    try:
        # Obtener datos
        df = obtener_datos(conexion)
        
        # Mostrar estadísticas
        obtener_estadisticas(df)
        
        # Graficar distribución del stock
        grafico_distribucion_stock(df)
        
        # Graficar productos con stock por debajo del mínimo
        grafico_stock_bajo(df)
    
    finally:
        # Cerrar conexión a la base de datos
        conexion.close()


if __name__ == "__main__":
    main() #se llama a la función main