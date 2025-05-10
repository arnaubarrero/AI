from flask import Flask, render_template, request
from geopy.distance import geodesic

app = Flask(__name__)

def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula la distancia entre dos puntos geográficos."""
    origen = (lat1, lon1)
    destino = (lat2, lon2)
    distance = geodesic(origen, destino).meters
    return distance

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            lat1 = float(request.form["lat1"])
            lon1 = float(request.form["lon1"])
            lat2 = float(request.form["lat2"])
            lon2 = float(request.form["lon2"])
            
            distancia = calcular_distancia(lat1, lon1, lat2, lon2)
            return render_template("index.html", distancia=distancia)
        except ValueError:
            return render_template("index.html", error="Por favor, ingresa valores válidos para las coordenadas.")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)