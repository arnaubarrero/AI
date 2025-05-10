from dronekit import VehicleMode
import time

def dar_potencia_maxima(vehicle, tiempo=2):
    """
    Da potencia máxima a todos los motores durante el tiempo especificado.
    
    :param vehicle: Instancia del vehículo (dron).
    :param tiempo: Tiempo (en segundos) durante el cual se dará potencia máxima a los motores.
    """
    # Aseguramos que el vehículo esté en modo GUIDED y armado
    if vehicle.mode != VehicleMode("GUIDED"):
        print("Cambiando a modo 'GUIDED'")
        vehicle.mode = VehicleMode("GUIDED")
    
    if not vehicle.armed:
        print("Arming the vehicle")
        vehicle.armed = True
        while not vehicle.armed:
            print("Esperando a que el vehículo esté armado...")
            time.sleep(1)
    
    # Aplicar potencia máxima a los motores
    print(f"Aplicando potencia máxima a los motores durante {tiempo} segundos...")
    
    # El control de potencia máxima puede implicar un ajuste del throttle o directamente enviando el comando para dar potencia completa
    vehicle.channels.overwrite(3, 2000)  # Canal 3 generalmente es el throttle, valor 2000 es potencia máxima (puede variar)
    
    # Mantener la potencia máxima durante el tiempo indicado
    time.sleep(tiempo)
    
    # Luego restablecemos el throttle a 1000 para detener los motores (esto es opcional según tus necesidades)
    vehicle.channels.overwrite(3, 1000)  # Restablecer el throttle a un valor neutro (idle)
    
    print("Potencia máxima aplicada durante el tiempo especificado.")