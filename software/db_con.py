import mysql.connector

def con_function():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="user",
        database="python"
    )
    
    print("Conexió amb la base de dades establerta correctament")