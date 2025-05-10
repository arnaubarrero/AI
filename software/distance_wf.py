import tkinter as tk
from tkinter import messagebox
from geopy.distance import geodesic

def calcular_distancia():
    try:
        lat1 = float(entry_lat_origen.get())
        lon1 = float(entry_lon_origen.get())
        lat2 = float(entry_lat_dest.get())
        lon2 = float(entry_lon_dest.get())

        origen = (lat1, lon1)
        destino = (lat2, lon2)
        distancia = geodesic(origen, destino).meters

        resultado.set(f"Distancia: {distancia:.2f} metros.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce solo números válidos en todas las coordenadas.")

# Crear ventana
ventana = tk.Tk()

# Coordenadas de origen
tk.Label(ventana, text="Latitud de origen:").grid(row=0, column=0, padx=5, pady=5)
entry_lat_origen = tk.Entry(ventana)
entry_lat_origen.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Longitud de origen:").grid(row=1, column=0, padx=5, pady=5)
entry_lon_origen = tk.Entry(ventana)
entry_lon_origen.grid(row=1, column=1, padx=5, pady=5)

# Coordenadas de destino
tk.Label(ventana, text="Latitud del destino:").grid(row=2, column=0, padx=5, pady=5)
entry_lat_dest = tk.Entry(ventana)
entry_lat_dest.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Longitud del destino:").grid(row=3, column=0, padx=5, pady=5)
entry_lon_dest = tk.Entry(ventana)
entry_lon_dest.grid(row=3, column=1, padx=5, pady=5)

# Botón para calcular
tk.Button(ventana, text="Calcular distancia", command=calcular_distancia).grid(row=4, column=0, columnspan=2, pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).grid(row=5, column=0, columnspan=2, pady=5)

ventana.mainloop()