# 📍 Project: **D.E.D.E.**

**D** → *Donde*  
**E** → *Estoy*  
**D** → *Donde*  
**E** → *Estás*

---

## 🧠 Overview

This is a Python-based project designed to help determine location-based information. The acronym **D.E.D.E.** stands for "Where am I?" and "Where are you?" in Spanish — emphasizing a location-awareness context.

---

## 🗂️ Project Structure

/  
├── README.md # Main project overview (this file)  
├── new-start.md # Instructions to restart or reinitialize the project  
└── software/  
    └── distance.py # Logic for calculating distances  

---

## 🔄 Restart Instructions

To restart the project, please follow the steps detailed in [`new-start.md`](./new-start.md).

---

## 🐍 Technologies Used

- Python 3.13.3

---

## Components Used

### 1. **Raspberry Pi**
The **Raspberry Pi 7" Touchscreen** will be used to create a user interface to input the drone's destination coordinates.

- **Product**: [Raspberry Pi 7" LCD Touchscreen](https://www.pccomponentes.com/raspberry-pantalla-tactil-7-lcd-para-pi)
- **Features**:
  - Capacitive 10-point touchscreen.
  - 800 x 480 pixel resolution at 60 fps.
  - Connected via the DSI connector of the Raspberry Pi.
  - Compatible with various operating systems like **Kivy** for touchscreen interface development.

### 2. **Dron**
The **Klack F169 WiFi Quadcopters with Dual 4K Camera** will be used as the autonomous aerial vehicle. This drone includes basic features for stable flight and a camera for potential surveillance or monitoring missions.

- **Product**: [Klack F169 WiFi Quadcopters with Dual 4K Camera](https://www.pccomponentes.com/klack-f169-dron-cuadricoptero-wifi-con-camara-dual-4k)
- **Features**:
  - Dual 4K camera with stabilization.
  - WiFi connectivity for remote control.
  - Basic autonomous flight functionality.
  - Good performance for short to medium-range flights.

---

## Objective of the Project

The main objective is to integrate these components so that by inputting the destination coordinates via the Raspberry Pi touchscreen, the drone will lift off, fly to those coordinates autonomously, and perform the flight with minimal human intervention.
