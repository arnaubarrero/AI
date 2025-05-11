from sklearn import tree
from db_con import con_function


X, y = con_function()

# Inputs de l'usuari
altura = int(input("Inserta l'altura: "))
pes    = int(input("Inserta el pes: "))
talla  = int(input("Inserta el numero de peu: "))
edat   = int(input("Inserta l'edat: "))

# Entrenament tenint en compte les dades
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Un cop entrenat, es treu una conclusio 
prediction = clf.predict([[altura, pes, talla, edat]])

if (prediction == 1):
    print("Ets un home")
else:
    print("Ets una dona")