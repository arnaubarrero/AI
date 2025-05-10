from flask import Flask, render_template, request
from geopy.distance import geodesic

# Crea instancia de la aplicación Flask
app = Flask(__name__)

# Función que calcula la distancia entre dos coordenadas geográficas
def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula la distancia entre dos puntos geográficos."""
    origen = (lat1, lon1)
    destino = (lat2, lon2)
    distance_meters = geodesic(origen, destino).meters
    distance_km = distance_meters / 1000
    return distance_meters, distance_km

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Toma los datos del formulario HTML y los convierte a tipo float
            lat1 = float(request.form["lat1"])
            lon1 = float(request.form["lon1"])
            lat2 = float(request.form["lat2"])
            lon2 = float(request.form["lon2"])
            
            distancia_meters, distancia_km = calcular_distancia(lat1, lon1, lat2, lon2)
            return render_template("index.html", distancia_meters=distancia_meters, distancia_km=distancia_km)
        except ValueError:
            return render_template("index.html", error="Put valid coordinates")
    
    return render_template("index.html")

# Ejecuta la aplicación en modo debug, accesible desde cualquier IP local
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
