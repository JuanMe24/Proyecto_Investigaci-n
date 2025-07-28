# Proyecto_Investigaci-o

**Coreografía programada de robots Phantom X Pincher**  
Facultad de Ingeniería – Universidad Nacional de Colombia  
Grupo: Juan David Meza, Andres Avilan   
Curso: Robótica de Investigación – [2025-I]

---

## 🎯 Descripción del Proyecto

Este repositorio documenta el proceso de diseño, preparación y ejecución de una coreografía colaborativa entre dos robots Phantom X Pincher. Se detallan las fases del proyecto desde la conceptualización, diseño cinemático y programación en Python, hasta la implementación física y visualización mediante interfaz gráfica.

El objetivo es sincronizar dos brazos robóticos para ejecutar una secuencia coreográfica definida, respetando límites articulares y tiempos, controlados desde una HMI desarrollada en Python usando Tkinter.

---

## 📂 Estructura del Repositorio

```
Proyecto_Investigaci-o/
├── Fotos/ # Imágenes de las 6 poses del robot
│ ├── pose1.jpg
│ ├── pose2.jpg
│ ├── pose3.jpg
│ ├── pose4.jpg
│ ├── pose5.jpg
│ └── pose6.jpg
├── codigo/ # Código fuente en Python (control e interfaz)
│ ├── hmi_coreografia.py
│ └── id_dynamixel.py
├── videos/ # Video demostrativo e interfaz gráfica
│ ├── demostración.mp4
│ └── interfaz.webm
└── README.md # Documentación principal del proyecto
```


---

## 🧠 Diagrama de Flujo

Se incluye un diagrama visual que describe el flujo de acciones de los robots, incluyendo activación, selección de poses, sincronización de rutina y visualización.

<div align="center">
  <img src="Fotos/flujo.svg" width="700"/>
</div>


## 🤖 Poses de la Coreografía (Miniaturas)

A continuación se muestran las 6 poses del robot junto con sus valores articulares (RAW):

| Pose | Imagen | Valores RAW | poses del baile |
|------|--------|-------------| --------------- |
| Pose 1 | <img src="Fotos/pose1.jpg" width="250"/> | `[512, 512, 800, 512, 512]` | palmas hacia abajo |
| Pose 2 | <img src="Fotos/pose2.jpg" width="250"/> | `[512, 512, 800, 512, 0]` | Palmas hacia arriba | 
| Pose 3 | <img src="Fotos/pose3.jpg" width="250"/> | `[300, 300, 800, 250, 512]` | Palmas al hombro contrario | 
| Pose 4 | <img src="Fotos/pose4.jpg" width="250"/> | `[512, 690, 240, 512, 512]` | Palmas a la cabeza | 
| Pose 5 | <img src="Fotos/pose5.jpg" width="250"/> | `[700, 512, 900, 800, 512]` | Palmas a la parte contraria de la cadera |
| Pose 6 | <img src="Fotos/pose6.jpg" width="250"/> | `[512, 512, 900, 700, 512]` | Palmas a la parte correspondiente de la cadera |



---

## 🧾 Código Python

Todo el código está implementado en Python, con módulos comentados para:

- Control individual de servos Dynamixel
- Comunicación serial con los robots (USB)
- Representación del modelo cinemático con `roboticstoolbox`
- Interfaz gráfica en `Tkinter` con selección de poses y control de rutina
- Ejecución sincronizada y simulada de 2 robots (1 físico + 1 simulado)

---

## 🔍 Comparación y Validación

Se incluye una discusión técnica entre el modelo simulado (mediante toolbox) y la ejecución real en los robots, evaluando:

- Posición esperada vs. real
- Precisión de los movimientos
- Sincronización entre brazos

---

## 🎥 Video Presentación


## ⚙️ Requisitos


