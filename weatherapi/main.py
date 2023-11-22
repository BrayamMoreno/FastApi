# coding=utf-8

#Importar librerías
import decimal
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI

# variables de conexión a base de datos
DB_HOST = "172.190.67.216" # Dirección del servidor
DB_NAME = "estacion"
DB_USER = "postgres"
DB_PASWD = "123456"

#Conectar a la base de datos
cc = psycopg2.connect(database=DB_NAME,user=DB_USER,password=DB_PASWD,host=DB_HOST,port=5432)
#Cursor para ejecutar SQL
cursor_obj = cc.cursor(cursor_factory=RealDictCursor)

#Creación de objeto API
app = FastAPI()

@app.post("/Postlectura")
async def insertar_lectura(temperatura: float, presion: float, altitud: float):
    sql = f"INSERT INTO lecturas (temperatura, presion, altitud) VALUES ({temperatura}, {presion}, {altitud})"
    cursor_obj.execute(sql)
    cc.commit()
    return {"message": "Lectura insertada"}
    

@app.get("/GetLectura")
async def leer_datos():
    sql = f"SELECT * FROM lecturas   ORDER BY id DESC LIMIT 20"
    cursor_obj.execute(sql)
    rows = cursor_obj.fetchall()
    return rows
    
