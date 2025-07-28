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

A continuación se muestran las 6 poses del robot junto con sus valores articulares (RAW), vistas desde una vista superior. Además, para simular el salto en baile para cambiar la orientación, tendríamos que sumar 90 grados a cada una de las primeras coordenadas. Para el brazo izquierdo, se cambia la rotación de la primera articulación, para así simular que el codo está hacia el otro lado. En el código se puede apreciar.

| Pose | Imagen | Valores RAW | poses del baile |
|------|--------|-------------| --------------- |
| Pose 1 | <img src="Fotos/pose1.jpg" width="230"/> | `[512, 512, 800, 512, 512]` | palmas hacia abajo |
| Pose 2 | <img src="Fotos/pose2.jpg" width="230"/> | `[512, 512, 800, 512, 0]` | Palmas hacia arriba | 
| Pose 3 | <img src="Fotos/pose3.jpg" width="230"/> | `[300, 300, 800, 250, 512]` | Palmas al hombro contrario | 
| Pose 4 | <img src="Fotos/pose4.jpg" width="230"/> | `[512, 690, 240, 512, 512]` | Palmas a la cabeza | 
| Pose 5 | <img src="Fotos/pose5.jpg" width="230"/> | `[700, 512, 900, 800, 512]` | Palmas a la parte contraria de la cadera |
| Pose 6 | <img src="Fotos/pose6.jpg" width="230"/> | `[512, 512, 900, 700, 512]` | Palmas a la parte correspondiente de la cadera |



---

## 🧾 Código Python

Todo el código está implementado en Python, con módulos comentados para:

- Comunicación serial con los robots (USB) con ayuda de el archivo [`id_dynamixel.py`](codigo/id_dynamixel.py) sin embargo, en este punto se evidenció que, justamente, el segundo robot proporcionado no ejecuta los programas. Se verificó que los puertos utilizados tuvieran habilitado el grupo dialout.
- La imagen que se muestra a continuación fue generada mediante la ejecución del script `pentando.py`, el cual permite enviar una posición angular específica a los servos Dynamixel del robot Phantom X Pincher. En este caso, la pose corresponde a los ángulos `[x°, x°, x°, x°]` para las articulaciones de la base, hombro, codo y muñeca respectivamente. Además de ejecutar físicamente esta pose en el robot real, el script utiliza el modelo cinemático definido en `phantom_dh.py` y la librería `roboticstoolbox` para graficar la configuración del manipulador en pantalla. Esta visualización facilita la validación de la pose deseada antes de realizar la ejecución completa de la coreografía.

<div align="center">
  <img src="Fotos/pose_simulado.jpg" width="350"/>
</div>

- La siguiente imagen muestra la interfaz gráfica desarrollada con la biblioteca `Tkinter` en Python, incluida en el archivo `hmi_coreografia.py`. Esta interfaz permite al usuario controlar de manera intuitiva la ejecución de poses individuales y rutinas completas en el robot Phantom X Pincher. La sección izquierda ("Seleccionar Pose") contiene botones que invocan el método `self.ejecutar_pose_individual(i)` definido en el código, el cual utiliza la función `enviar_pose()` para enviar posiciones individuales a los motores Dynamixel.

- Debajo, se encuentra el botón naranja “Macarena (Ambos Robots)”, el cual ejecuta la rutina sincronizada de ambos robots mediante el método `self.macarena_rutina()`, iterando sobre las listas `poses` y `poses_robot2`. También se incluye un botón adicional que permite ejecutar la rutina del segundo robot en el robot físico (`self.ejecutar_rutina_robot2()`). Esto por la limitación en la cantidad de robots funcionales, para no estar comentando constantemente las lineas de codigo, ni cambiando los puertos. 

- En la parte inferior, se presenta una barra de progreso (`ttk.Progressbar`) que se actualiza en tiempo real con `self.barra["value"] = progreso`, junto con una etiqueta que muestra el tiempo restante por medio de `self.label_tiempo.config(...)`.

- La sección derecha (“Control de Robots”) permite observar el estado actual de cada robot. Por ejemplo, cuando el Robot 1 está en ejecución, el color de fondo cambia a azul con `self.estado_r1.config(bg="blue")`, y vuelve a verde al terminar.

<div align="center">
  <img src="Fotos/interfaz.png" width="500"/>
</div>

---

## 🎥 Video Presentación

(aca va el video de la demostración) 


## ⚙️ Requisitos


