# Deteccion de lengua de señas con MediaPipe y Scikit-learn
![lsm](https://ai.google.dev/static/mediapipe/images/solutions/pose_landmarks_index.png?hl=es-419)

Se seleccionaron gestos de la lengua de señas mexicana que representaran aspectos como la antigüedad, localización, intensidad y características de un dolor, considerados todos ellos elementos cruciales en la evaluación y diagnóstico del dolor en el ámbito médico.

## Features

- Detectar señas de la lengua de señas mexicana desde la cámara web en tiempo real
- Entrenamiento del modelo
  
## Tecnologías
La aplicación utiliza una serie de proyectos de código abierto para funcionar correctamente:

- [MediaPipe] - detectar señas
- [Scikit-learn] - aprendizaje automático
- [Python] - 3.10

## Instalacion

```sh
!pip install mediapipe opencv-python pandas scikit-learn
```
```sh
pip install -U scikit-learn scipy matplotlib
```
## Author
[RosaSainz](https://github.com/rosaainz) 💜

   [MediaPipe]: <https://ai.google.dev/edge/mediapipe/solutions/guide?hl=es-419>
   [Scikit-learn]: <https://scikit-learn.org/stable/>
   [Python]: <https://www.python.org/>
