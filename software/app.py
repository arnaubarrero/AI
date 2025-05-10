import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user",
  database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM categorias")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)