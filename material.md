# Proyecto Dron Autónomo con Raspberry Pi

Este proyecto tiene como objetivo crear un sistema autónomo para controlar un dron utilizando una **Raspberry Pi**. A través de una interfaz de pantalla táctil, el usuario podrá ingresar las coordenadas de destino y, el dron, realizará el vuelo autónomo hacia ese destino.

## Componentes Utilizados

### 1. **Raspberry Pi**
La **Raspberry Pi 7" Touchscreen** será utilizada para crear una interfaz de usuario para ingresar las coordenadas de destino del dron.

- **Producto**: [Raspberry Pi 7" LCD Touchscreen](https://www.pccomponentes.com/raspberry-pantalla-tactil-7-lcd-para-pi)
- **Características**:
  - Pantalla táctil capacitiva de 10 puntos.
  - Resolución de 800 x 480 píxeles a 60 fps.
  - Conexión a través del conector DSI de la Raspberry Pi.
  - Compatible con diversos sistemas operativos como **Kivy** para el desarrollo de interfaces táctiles.

### 2. **Dron**
El **Klack F169 Cuadricóptero WiFi con Cámara Dual 4K** será utilizado como el vehículo aéreo autónomo. Este dron incluye características básicas para vuelos estables y una cámara para posibles misiones de videovigilancia o monitoreo.

- **Producto**: [Klack F169 Dron Cuadricóptero WiFi con Cámara Dual 4K](https://www.pccomponentes.com/klack-f169-dron-cuadricoptero-wifi-con-camara-dual-4k)
- **Características**:
  - Cámara Dual 4K con estabilización.
  - Conectividad WiFi para control remoto.
  - Funcionalidades para vuelos autónomos básicos.
  - Buen rendimiento en vuelos de corta y media distancia.

## Objetivo del Proyecto

El objetivo principal es integrar estos componentes de forma que, al ingresar las coordenadas de destino a través de la pantalla táctil de la Raspberry Pi, el dron se levante, se dirija hacia esas coordenadas de forma autónoma, y realice el vuelo con la mínima intervención humana.

## Funcionalidad

1. **Interfaz de usuario**:
   - A través de la pantalla táctil, el usuario podrá ingresar las coordenadas de **latitud** y **longitud** de destino.
   - La Raspberry Pi procesará estos datos y enviará las instrucciones al dron para que inicie el vuelo.

2. **Control de vuelo autónomo**:
   - El dron utilizará su sistema de navegación GPS para seguir las instrucciones de vuelo recibidas de la Raspberry Pi.
   - La Raspberry Pi también puede manejar el proceso de elevación (500m de altura) antes de comenzar a desplazarse hacia el destino.

## Requisitos

- **Raspberry Pi** con conexión WiFi.
- **Pantalla táctil 7"** para la entrada de coordenadas.
- **Dron Klack F169** o similar, con capacidad de vuelo autónomo.
- **Conexión WiFi** para enviar datos entre la Raspberry Pi y el dron.
- **Software de control** en la Raspberry Pi para gestionar los vuelos autónomos.

## Instrucciones de Instalación

### 1. **Configurar la Raspberry Pi**
   - Instalar el sistema operativo **Raspberry Pi OS**.
   - Conectar la pantalla táctil LCD 7" a la Raspberry Pi a través del conector DSI.
   - Configurar la red WiFi para asegurar la comunicación con el dron.

### 2. **Integración con el Dron**
   - Configurar el sistema de control de vuelo del dron para recibir comandos de la Raspberry Pi.
   - Usar una API o SDK compatible para el control autónomo, como **MAVLink** o una integración de **DJI SDK** si se utiliza un dron con estas capacidades.

### 3. **Desarrollar la Interfaz Táctil**
   - Crear una interfaz de usuario usando **Kivy** o cualquier otra librería compatible con la Raspberry Pi para permitir la inserción de coordenadas.

### 4. **Vuelos Autónomos**
   - Desarrollar el algoritmo de control autónomo en la Raspberry Pi para gestionar la navegación y asegurar que el dron siga las coordenadas ingresadas.

## Futuras Mejoras

- **Mejora del control de vuelo** para incluir más funcionalidades autónomas.
- **Incorporación de sensores adicionales** (como cámaras o sensores de distancia) para mejorar la seguridad y precisión del vuelo.
- **Optimización del algoritmo de navegación** para realizar vuelos más largos o complejos.

## Contribuciones

Si tienes sugerencias, mejoras o has realizado un proyecto similar, ¡siéntete libre de contribuir al proyecto!

---

**Licencia**: Este proyecto está bajo la licencia MIT.

