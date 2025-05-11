import mysql.connector

def con_function():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="user",
        database="python"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM DadesPersonas")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        print (x)