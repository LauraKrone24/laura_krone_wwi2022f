from flask import Flask, jsonify, request 
import mysql.connector
from mysql.connector import errorcode
  
app = Flask(__name__) 


'''
     Diese unter /artists bereitgestellte Microservice - Methode
     stellt eine Verbindung zu Datenbank her und gibt ihren Inhalt
     im JSON Format aus
'''
@app.route('/artists') 
def show_artists(): 


    #Verbindung wird erstellt 
    my_sql_db_connection = mysql.connector.connect(
        user="root",
        password="root_password",
        host="my_sql_database",
        port="3306",
        database="my_database",
        auth_plugin='mysql_native_password'
    )

    # Daten werden abgefragt
    curser=my_sql_db_connection.cursor()
    curser.execute("SELECT * FROM artists ORDER BY times_played DESC;")
    list_of_artist_tupel = curser.fetchall()

    # Umformatieren für besseres JSON Format
    keys = ("Artist_ID","Artist_Name", "Times_Played")
    list_of_artist_dict = [dict(zip(keys, values)) for values in list_of_artist_tupel]


    # Verbindung wird geschlossen 
    my_sql_db_connection.close()

    # Ergebniss wird zurückgegeben
    return jsonify(list_of_artist_dict) 
    
    
  
'''
    Dies ist der Einstiegspunkt des Programms
    Der Micorservice läuft auf Localhost Port 3000
'''  
if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=3000) 