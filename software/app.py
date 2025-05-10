import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user",
  database="python"
)

mycursor = mydb.cursor()

print("1. Show data \n2. Insert data")
opcio = int(input("Choose an option: "))

if (opcio == 1):
    mycursor.execute("SELECT * FROM categorias")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
elif (opcio == 2):
    insertWord = input("Write the name of the new category: ")