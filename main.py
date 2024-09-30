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