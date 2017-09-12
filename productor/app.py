# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
import random
import time

app = Flask(__name__)

def productor():

    cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='estacion')
    cursor = cnx.cursor()
    cursor = cnx.cursor(buffered=True)
    cursor.autocommit = True
    query = ("SELECT valor FROM frecuencia_muestreo WHERE id=1")
    cursor.execute(query)
    frecuencia = cursor.fetchone()[0]
    print(frecuencia)

    valor_temp = random.uniform(0, 100)
    valor_vient = random.uniform(0, 80)
    valor_hum = random.uniform(0, 20)
    valor_pres = random.uniform(0, 50)
    valor_temp = round(valor_temp, 2)
    valor_vient = round(valor_vient, 2)
    valor_hum = round(valor_hum, 2)
    valor_pres = round(valor_pres, 2)
    id = 'NULL'


    cursor.execute('''INSERT into temperatura (id, valor)
                  values (%s, %s)''',
                  (id, valor_temp))
    cursor.execute('''INSERT into humedad (id, valor)
                  values (%s, %s)''',
                  (id, valor_hum))
    cursor.execute('''INSERT into presion (id, valor)
                  values (%s, %s)''',
                  (id, valor_pres))
    cursor.execute('''INSERT into velocidad_viento (id, valor)
                  values (%s, %s)''',
                  (id, valor_vient))

    # Commit cambios en la BD
    cnx.commit()
    # Cierro la conexion
    cnx.close()
    time.sleep(frecuencia)

if __name__ == "__main__":
    # Set up productor
    while True:
        productor()
