***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

## Instalación y enviroment en Anaconda
Para la realización de esta práctica fue necesario instalar la versión de cuda apropiada para mi tarjeta gráfica, se puede saber mediante el comando nvidia-smi en el cmd.

### CUDA
![image](https://github.com/user-attachments/assets/9e9c030e-a947-4567-865b-70c5270693d3)

Una vez sabes la versión de Cuda que necesitas, basta con instalarla en la web oficial, [CUDA Version 12.6](https://developer.nvidia.com/cuda-downloads).

Tras esto instalé el [cuDNN](https://developer.nvidia.com/cudnn-downloads).

### Anaconda
Una vez la instalación de CUDA es exitosa, solo queda instalarse el enviroment. Instalando los paquetes mencionados en el [repositorio de la prática](https://github.com/otsedom/otsedom.github.io/blob/main/VC/P4/README.md), y el pytorch.


Para el pytorch instalé la última versión disponible, que funciona correctamente para las versiones más recientes de CUDA. 
![image](https://github.com/user-attachments/assets/1390642d-39a8-4431-9f3b-ed84b6a969d1)

En cuanto a los detectores de textos, easyOCR tiene una instalación bastante simple. Pero en el caso de Tesseract, es necesario descargarse un [instalador](https://github.com/UB-Mannheim/tesseract/wiki), 
añadir la variable de entorno con la ruta del tesseract.exe, y finalmente añadir en el código la ruta dl ejecutable que se instalará. 

Cabe destacar que el easyOCR no funciona para las versiones más actuales de python, con lo que hay que usar un enviroment con versión inferior, en mi caso funcionó la versión 3.9.20. No obstante,
esta versión puede acarrear problemas con ciertas funcionalidades de OpenCV como cv2.imshow(), que me dio ciertos problemas a la hora de mostrar videos durante la ejecución. 

Se podría mostrar el video con alternativas, como usar matplotlib para la visualización del video, pero preferí tener dos enviroments. Uno con la versión 3.11.5 de python para la primera parte de la práctica,
en la que me interesa mostrar el video mientras se ejecuta. Y la versión 3.9.20 la utilizo para la detección de textos con easyOCR.

## Anotación de imágenes. 

Para el entrenamiento del modelo yolo, es necesario hacer uso de un dataset de imágenes anotadas. Para ello anoté con [Roboflow](https://roboflow.com/) un total de 96 imágenes de cosecha propia, y además utilicé
un dataset con 404 imágenes que encontré en [Roboflow Universe](https://universe.roboflow.com/projectyolo-qvrgr/license-plate-detection-1v7hv). Dando lugar a un dataset de 500 imágenes, que está actualmente 
disponible para ser utilizado por otros usuarios, [en Roboflow Universe](https://universe.roboflow.com/vc-z7qrx/vc_project_merged_public-own_datasets). 
A este conjunto de imágenes le apliqué varios filtros de data augmentation, dando lugar al siguiente conjunto de entrenamiento, validación y test:

![image](https://github.com/user-attachments/assets/60435af5-7843-4bf0-a4c4-d5e38dabae54)

Finalmente exporté en formato YOLO v11 los datos de las imágenes anotadas.
### IMPORTANTE
**Recomiendo que si alguien utiliza ese Dataset, elimine las imágenes en las que se anotó matrículas parcialmente cubiertas con plantas, o que realice más fotos de esa índole para evitar falsas detecciones.**

## Entrenamiento del Modelo
Como mencioné previamente, hice uso de CUDA para el entrenamiento.
```
model = YOLO('yolo11n.pt') #Contenedores
data_Yaml_path = "ruta"

results = model.train(data= data_Yaml_path, epochs=40, imgsz=640, batch=16, lr0=0.001, patience=5)
```
- data : Se refiere a la ruta del archivo data.yaml que fue obtenido tras exportar los datos de Roboflow en formato YOLO
- epochs=40: Define el número de épocas que el modelo entrenará en el conjunto de datos. Una época es una pasada completa a través de todos los datos de entrenamiento. En este caso, entrenará durante 40 épocas, permitiendo que el modelo aprenda iterativamente a partir de los datos.

- imgsz=640: Establece el tamaño de las imágenes de entrada (640x640 píxeles) que se usarán para entrenar el modelo. El tamaño corresponde al tamaño de las imágenes que fueron exportadas con roboflow en formato yolov11 

- batch=16: El batch size es el número de imágenes que se procesan en paralelo en cada paso de entrenamiento Tamaños de batch más grandes aceleran el entrenamiento y pueden estabilizar el aprendizaje, pero requieren más memoria.

- lr0=0.001: Este es el learning rate inicial, que controla la magnitud de los ajustes de los pesos durante el entrenamiento. Utilicé un valor de 0.001, ya que es comúnmente utlizado por ser una buena tasa de aprendizaje inicial.
  - valores más altos pueden hacer que el modelo converja más rápido, pero también pueden hacer que se salte el mínimo óptimo.
  - Valores más bajos pueden estabilizar el aprendizaje pero requerirán más tiempo de entrenamiento.

- patience=5: Define el Early Stopping, si no hay mejora en 5 épocas, el entrenamiento se detiene. Esto no fue necesario en mi caso, pero si hubiese puesto un número mayor de épocas, podría haber sido útil.

## Aplicaciones

Para la realización de esta práctica, seguí un enfoque modular. Haciendo en primer lugar tareas simples, para luego pasar a detecciones más complejas.
Las tareas realizadas se pueden dividir en lo siguiente:

***Enviromennt con versión 3.11.5 de python:***
- Detección del contorno de la matrícula en una imagen estática.
- Detección del cotnro de la matrícula en video.
- Detectar contornos de matrículas, coches y personas.
- Añadir a lo anterior que la matrícula debe estar en un coche, para evitar falsos positivos. Y encapsularlo en una función para facilitar las ejecuciones con diferentes videos.

Con el objetivo de detectar el texto de las matrículas detectadas, hice uso de dos OCR: Tesseract y easyOCR.


***Enviromennt con versión 3.9.2 de python:***

- Detección de textos con Tesseract en imagen estática (Tesseract funciona con la versión 3.11.5 también).
- Detección de textos con eastOCR en imagen estática.
Tras ejecutar el código con con varias imágenes, noté mejores resultados con easyOCR, con lo que decidí hacer las tareas siguientes con dicho detector.
- Detección de texto de matrículas en video, guardando las detecciones en un csv, junto a sus ocurrencias. 
- 

