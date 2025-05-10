from dronekit import VehicleMode
import time
from pymavlink import mavutil

def mover_en_linea_recta(vehicle, tiempo=2, velocidad=2.0):
    """
    Mueve el dron hacia adelante en línea recta durante un tiempo determinado.

    :param vehicle: Instancia del vehículo (dron).
    :param tiempo: Tiempo (en segundos) que el dron debe avanzar.
    :param velocidad: Velocidad en m/s con la que avanzará el dron.
    """

    # Asegurarse de que el vehículo esté en modo GUIDED
    if vehicle.mode != VehicleMode("GUIDED"):
        print("Cambiando a modo 'GUIDED'")
        vehicle.mode = VehicleMode("GUIDED")

    # Función auxiliar para enviar velocidad en NED
    def send_velocity(velocity_x, velocity_y, velocity_z):
        """
        Envía una velocidad al vehículo en el marco NED (North-East-Down).
        +X es hacia el norte, +Y es hacia el este, +Z es hacia abajo.
        """
        msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,       # time_boot_ms
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_FRAME_BODY_NED,  # En el marco del cuerpo del dron
            0b0000111111000111,  # Solo controlamos velocidades
            0, 0, 0,             # Posición (ignoramos)
            velocity_x, velocity_y, velocity_z,  # Velocidades
            0, 0, 0,             # Aceleraciones (ignoramos)
            0, 0                 # Yaw, yaw_rate (ignoramos)
        )
        vehicle.send_mavlink(msg)
        vehicle.flush()

    print(f"Moviendo el dron hacia adelante durante {tiempo} segundos a {velocidad} m/s")

    start_time = time.time()
    while time.time() - start_time < tiempo:
        send_velocity(velocidad, 0, 0)  # Movimiento hacia adelante (eje X positivo en BODY_NED)
        time.sleep(0.1)

    # Detener movimiento tras el tiempo especificado
    send_velocity(0, 0, 0)
    print("Movimiento completado.")

