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


---

## 🧠 Diagrama de Flujo

Se incluye un diagrama visual que describe el flujo de acciones de los robots, incluyendo activación, selección de poses, sincronización de rutina y visualización.


## 🗺️ Plano y Coreografía

Incluye el diseño del plano de planta y la descripción detallada de la coreografía, indicando los movimientos de cada brazo, su colaboración y tiempos de ejecución sincronizados.


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


