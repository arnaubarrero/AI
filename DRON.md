# 🛠 Proyecto: Dron Autónomo Casero

Este documento enumera los componentes necesarios para construir un dron casero con capacidad de navegación autónoma, donde se le asignan coordenadas de salida y destino previamente al vuelo.

---

## 🎯 Objetivo

Configurar un dron que pueda volar de forma **autónoma**, con una ruta preestablecida entre coordenadas GPS, sin necesidad de intervención durante el vuelo.

---

## 📦 Componentes Necesarios

### 🔌 Distribución y Alimentación

- 🔋 **Batería LiPo** – Fuente de energía principal.
- 🔌 **Tarjeta de distribución de energía (PDB)** – Distribuye corriente del pack de baterías a los ESCs y otros componentes.
- ⚡ **Regulador de voltaje (BEC o integrado en la PDB)** – Proporciona voltajes estables a los componentes sensibles como el controlador de vuelo o receptor.

### 🧠 Control y Navegación

- 🧭 **Controlador de vuelo (Flight Controller, FC)** – El "cerebro" del dron. Ej: Pixhawk, Matek, AIO FC compatibles con Ardupilot o INAV.
- 📡 **Receptor RC** – Permite control manual (útil para pruebas o emergencias).
- 🛰 **Módulo GPS + brújula (magnetómetro)** – Para navegación autónoma basada en coordenadas.
- 🔌 **Cable de servo** – Para conectar componentes como GPS o receptor al FC.

### 🌀 Propulsión

- ⚙️ **Motores brushless para drones**
- ⚙️ **ESC (Electronic Speed Controller)** – Uno por motor, regula la velocidad del motor.
- ⚙️ **Hélices adecuadas** – Según el tamaño y potencia de tu dron.

### 🛠 Otros componentes clave

- 🪛 **Chasis o frame** – Estructura para montar los componentes.
- 📶 **Telemetría (opcional pero recomendada)** – Permite monitorear el dron en tiempo real desde el suelo.
- 🧰 **Software de planificación de misiones** – Ej: Mission Planner (ArduPilot), QGroundControl (PX4).
- 🖥️ **Puerto USB o conexión para cargar firmware y configurar rutas desde la PC.**

---

## 🎬 Video de referencia

[YouTube: Construcción de dron paso a paso](https://www.youtube.com/watch?v=3mJWsnT1gRE&list=LL&index=1&t=228s)

---

## ✅ Siguientes pasos

1. Montar componentes en el frame.
2. Configurar el controlador de vuelo con el firmware adecuado (ArduPilot o INAV recomendado).
3. Calibrar sensores y motores.
4. Planificar ruta de vuelo desde software de misión.
5. Realizar pruebas en entorno controlado.