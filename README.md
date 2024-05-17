# AppMovil-LSM
![lsm](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZdidhZ_EIwN-vuqvXyyCqloHIJcjfazFrmQ&usqp=CAU)

Aplicación Móvil que da un acercamiento a la interpretación de lengua de señas mexicana en un contexto de una consulta medica.
Para elegir las señas que serían utilizadas para entrenar los modelos de aprendizaje automático, se optó por el enfoque de la mnemotecnia Alicia. En este contexto, se seleccionaron gestos de la lengua de señas mexicana que representaran aspectos como la antigüedad, localización, intensidad y características de un dolor, considerados todos ellos elementos cruciales en la evaluación y diagnóstico del dolor en el ámbito médico.


## Features

- Detectar señas de la lengua de señas mexicana desde la cámara del móvil en tiempo real
- Interpretar señas a texto
-
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
Hecho con mucha pasión [RosaSainz](https://github.com/rosaainz) 💜

   [MediaPipe]: <https://ai.google.dev/edge/mediapipe/solutions/guide?hl=es-419>
   [Scikit-learn]: <https://scikit-learn.org/stable/>
   [Python]: <https://www.python.org/>
