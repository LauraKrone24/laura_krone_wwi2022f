'''
    Autor: Laura Krone
    Version: 1 
    Beschreibung:   Diese unter /artists bereitgestellte Microservice - Methode
                    stellt eine Verbindung zu Datenbank her und gibt ihren Inhalt sortiert
                    im JSON Format aus
     
'''

import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, jsonify, request 
import mysql.connector
from mysql.connector import errorcode
  
app = Flask(__name__) 

#Set up Logging File
logging.basicConfig(filename="../var/log/app.log", level=logging.INFO, format="'%(asctime)s - %(levelname)s %(name)s :  %(message)s'")

#Umgebungsvariablen 
user = os.environ.get("USER")
mysql_password = os.environ.get("MYSQL_PASSWORD")
mysql_container_name = os.environ.get("MYSQL_CONTAINER_NAME")
database = os.environ.get("MYSQL_DATABASE")
database_port =os.environ.get("DATABASE_PORT")
microservice_port =os.environ.get("MICROSERVICE_PORT")

@app.route('/artists') 
def show_artists(): 


    #Verbindung wird erstellt 
    my_sql_db_connection = mysql.connector.connect(
        user=user,
        password=mysql_password,
        host=mysql_container_name,
        port=database_port,
        database=database,
        auth_plugin='mysql_native_password'
    )

    # Daten werden abgefragt
    curser=my_sql_db_connection.cursor()
    curser.execute("SELECT * FROM artists ORDER BY times_played DESC;")
    list_of_artist_tupel = curser.fetchall()

    # Umformatieren für besseres JSON
    keys = ("Artist_ID","Artist_Name", "Times_Played")
    list_of_artist_dict = [dict(zip(keys, values)) for values in list_of_artist_tupel]


    # Verbindung wird geschlossen 
    my_sql_db_connection.close()

    # Ergebniss wird zurückgegeben
    return jsonify(list_of_artist_dict) 
    
    
  
'''
    Dies ist der Einstiegspunkt des Programms
    Der Port auf welchem dre Microservice läuft wird aus den Enviroment Variablen entnommen.
'''  
if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0',port=microservice_port) 