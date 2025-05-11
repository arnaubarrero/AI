import mysql.connector

def con_function():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="user",
        database="python"
    )
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT altura, pes, num_peu, edat, genere FROM DadesPersonas")

    myresult = mycursor.fetchall()

    # X = Extreure totes les dades excepte el genere (totes les columnes menys l'ultima)
    X = [list(row[:-1]) for row in myresult]
    # Y = Extreure els generes de cada (l'ultima columna)
    y = [row[-1] for row in myresult]

    return X, y