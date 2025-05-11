import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user",
  database="python"
)
mycursor = mydb.cursor()

def show_menu():
    print("\n----------\n1. Show data\n2. Insert data\n3. Delete category\n0. Exit\n----------")

while True:
    show_menu()
    opcio = int(input("Choose an option: "))

    if opcio == 0:
        print("Good bye :)")
        break

    elif opcio == 1:
        mycursor.execute("SELECT * FROM categorias")
        myresult = mycursor.fetchall()
        for x in myresult:
          print(x)

    elif opcio == 2:
        insertWord = input("Write the name of the new category: ")
        mycursor.execute("INSERT INTO categorias (nombre_categoria) VALUES (%s)", (insertWord,))
        mydb.commit()
        print("Categoría insertada correctamente.")

    elif opcio == 3:
        DeleteCategory = int(input("Enter the ID of the category you want to delete: "))
        mycursor.execute("DELETE FROM categorias WHERE id_categoria = %s", (DeleteCategory,))
        mydb.commit()
        print("Categoría eliminada correctamente.")

mycursor.close()
mydb.close()