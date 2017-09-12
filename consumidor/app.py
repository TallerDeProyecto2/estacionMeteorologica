# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
import random

app = Flask(__name__)

# Define la ruta con la que se ingresara desde el browser
@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        data = request.form
        frecuencia = data["frec"]
        cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='estacion')
        cursor = cnx.cursor()
        query = ("UPDATE frecuencia_muestreo SET valor = %s WHERE id=1")
        cursor.execute(query, (frecuencia,))
        # Commit cambios en la BD
        cnx.commit()
        # Cierro la conexion
        cnx.close()

    cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='estacion')
    cursor = cnx.cursor()
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT valor FROM frecuencia_muestreo WHERE id=1")
    cursor.execute(query)
    frecuencia = cursor.fetchone()[0]

    query = ("SELECT MAX(id) FROM humedad")
    cursor.execute(query)
    max_id = cursor.fetchone()[0]

    humedadProm=0
    if max_id>9:
        query= ("SELECT valor FROM humedad LIMIT %s,%s")
        aux=max_id-10
        cursor.execute(query, (aux,max_id,))


        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm = cursor.fetchone()[0] + humedadProm
        humedadProm=humedadProm/10
    else:
       
        if max_id >=1:
            query= ("SELECT valor FROM humedad LIMIT %s,%s")
            cursor.execute(query, (0,max_id,))

            for i in range(max_id):
                humedadProm = cursor.fetchone()[0] + humedadProm

            humedadProm=humedadProm/max_id

        else:
            humedadProm=0


    if max_id>=1:
        query = ("SELECT valor FROM humedad WHERE id=%s")
        cursor.execute(query, (max_id,))
        humedad = cursor.fetchone()[0]
    else:
        humedad=0

    query = ("SELECT MAX(id) FROM presion")
    cursor.execute(query)
    max_id = cursor.fetchone()[0]

    presionProm=0
    if max_id>9:

        query= ("SELECT valor FROM presion LIMIT %s,%s")
        aux=max_id-10
        cursor.execute(query, (aux,max_id,))
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm = cursor.fetchone()[0] + presionProm
        presionProm=presionProm/10
    else:
       
        if max_id >=1:
            query= ("SELECT valor FROM presion LIMIT %s,%s")
            cursor.execute(query, (0,max_id,))

            for i in range(max_id):
                presionProm = cursor.fetchone()[0] + presionProm

            presionProm=presionProm/max_id

        else:
            presionProm=0


    if max_id>=1:

        query = ("SELECT valor FROM presion WHERE id=%s")
        cursor.execute(query, (max_id,))
        presion = cursor.fetchone()[0]
    else:
        presion=0


    query = ("SELECT MAX(id) FROM temperatura")
    cursor.execute(query)
    max_id = cursor.fetchone()[0]

    temperaturaProm=0
    if max_id>9:

        query= ("SELECT valor FROM temperatura LIMIT %s,%s")
        aux=max_id-10
        cursor.execute(query, (aux,max_id,))
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = cursor.fetchone()[0] + temperaturaProm
        temperaturaProm = temperaturaProm/10
    else:
       
        if max_id >=1:
            query= ("SELECT valor FROM temperatura LIMIT %s,%s")
            cursor.execute(query, (0,max_id,))

            for i in range(max_id):
                temperaturaProm = cursor.fetchone()[0] + temperaturaProm

            temperaturaProm=temperaturaProm/max_id

        else:
            temperaturaProm=0


    if max_id>=1:

        query = ("SELECT valor FROM temperatura WHERE id=%s")
        cursor.execute(query, (max_id,))
        temperatura = cursor.fetchone()[0]
    else:
        temperatura=0


    query = ("SELECT MAX(id) FROM velocidad_viento")
    cursor.execute(query)
    max_id = cursor.fetchone()[0]
    
    velocidad_vientoProm=0
    if max_id>9:
    
        query= ("SELECT valor FROM velocidad_viento LIMIT %s,%s")
        aux=max_id-10
        cursor.execute(query, (aux,max_id,))
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm
        velocidad_vientoProm = velocidad_vientoProm/10
    else:
        if max_id >=1:
            query= ("SELECT valor FROM velocidad_viento LIMIT %s,%s")
            cursor.execute(query, (0,max_id,))

            for i in range(max_id):
                velocidad_vientoProm = cursor.fetchone()[0] + velocidad_vientoProm

            velocidad_vientoProm=velocidad_vientoProm/max_id

        else:
            velocidad_vientoProm=0


    if max_id>=1:
        query = ("SELECT valor FROM velocidad_viento WHERE id=%s")
        cursor.execute(query, (max_id,))
        velocidad_viento = cursor.fetchone()[0]
    else:
        velocidad_viento=0
    cnx.close()
    return render_template('form.html', frecuencia=frecuencia, humedad=humedad, presion=presion, temperatura=temperatura, velocidad_viento=velocidad_viento, humedadProm=humedadProm, temperaturaProm=temperaturaProm, presionProm=presionProm, velocidad_vientoProm=velocidad_vientoProm)


if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=3606)
