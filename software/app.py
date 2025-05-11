from sklearn import tree
from db_con import con_function

con_function()

altura    = int(input("Inserta l'altura: "))
pes       = int(input("Inserta el pes: "))
talla     = int(input("Inserta el numero de peu: "))
edat      = int(input("Inserta l'edat: "))

# Dades d'entrenamet (altura,pes,num. peu,edat)
# X = Dades de la persona 
# Y = Genere de la persona
X = [[163, 70, 37, 52], [172, 72, 41, 21], [168, 70, 41, 24], [180, 67, 43, 22]]

# 0 = Mujer && 1 = hombre
y = [0, 1, 1, 1]

# Entrenament tenint amb conte les dades
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Fer una predicció segons les dades adjuntades
prediction = clf.predict([[altura, pes, talla, edat]])

print("Predicció (0=dona, 1=home):", prediction)