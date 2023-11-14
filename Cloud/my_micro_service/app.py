from flask import Flask, jsonify, request 
import mysql.connector
from mysql.connector import errorcode
  
app = Flask(__name__) 
  
@app.route('/') 
def helloworld(): 


    print("Es beginnt")
    
    my_sql_db_connection = mysql.connector.connect(
        user="root",
        password="root_password",
        host="my_sql_database",
        port="3306",
        database="my_database",
        auth_plugin='mysql_native_password'
    )
    print(my_sql_db_connection)
    curser=my_sql_db_connection.cursor()
    print(curser)
    curser.execute("SELECT * FROM artists")
    artists = curser.fetchall()
    print(artists)
    my_sql_db_connection.close()
    print(artists)
    return jsonify(artists) 
    
    
  
  
if __name__ == '__main__': 
    print("Container up")
    app.run(host='0.0.0.0',port=3000) 