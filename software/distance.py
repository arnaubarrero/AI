# Import de necesaries dependencias
from geopy.distance import geodesic

# Ask for the coordenades
lat1 = float(input("Tu latitud actual: "))
lon1 = float(input("Tu longitud actual: "))
lat2 = float(input("Latitud del destino: "))
lon2 = float(input("Longitud del destino: "))

# Calculate de distance
origen  = (lat1, lon1)
destino = (lat2, lon2)
distance = geodesic(origen,destino).meters

# Resoult
print(f"{distance:.2f} metros.")