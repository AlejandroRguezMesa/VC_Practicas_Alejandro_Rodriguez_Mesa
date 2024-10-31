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
  
![image](https://github.com/user-attachments/assets/b93770d6-05c6-48d6-9320-1824776eec35)

El código consiste en darle los pesos obtenidos mediante entrenamiento a ultralytics, obteniendo los recuadros en los que se encuentran las matrículas. Tras obtener las coordenadas de la matrícula, dibujé con opencv los rectángulos correspondientes, y guardé la imagen resultante.

- Detección del cotorno de la matrícula en video.
  
![image](https://github.com/user-attachments/assets/67e89061-09a0-4e91-b556-23b176b89a1a)

Se trata de aplicar lo hecho en el código anterior sobre los frames del video. Con cv2.imshow se puede ver durante la ejecución el video, y con cv2.VideoWriter se puede ir guardando los frames procesados mediante la función write, dando lugar al video procesado.

- Detectar contornos de matrículas, coches y personas.
  
![image](https://github.com/user-attachments/assets/bf6de418-758a-49bd-8595-4fcfa6971bd2)


- Añadir a lo anterior que la matrícula debe estar en un coche, para evitar falsos positivos. Y encapsularlo en una función para facilitar las ejecuciones con diferentes videos.
  Con el código anterior, existe la posibilidad de encontrar falsos positivos, como este:
  
  ![image](https://github.com/user-attachments/assets/721a6e88-45f5-4b8a-9866-d1798aecc92e)
  
  Para evitarlo, se puede aplicar el modelo solo a los coches detectados, o en mi caso, guardé las coordenadas en las que se detectaron matriculas, y posteriormente comprobé si estaban    dentro del cotorno de un coche o no, en caso afirmativo se dibujan las matrículas.
  
![image](https://github.com/user-attachments/assets/1be6b8e1-4ec1-4551-a80d-684bd34c86cb)


***Enviromennt con versión 3.9.2 de python:***

Con el objetivo de detectar el texto de las matrículas detectadas, hice uso de dos OCR: Tesseract y easyOCR.

- Detección de textos con Tesseract en imagen estática (Tesseract funciona con la versión 3.11.5 también).
Se usa la función pytesseract.image_to_string para pasar de una imagen RGB a una string.

  ![image](https://github.com/user-attachments/assets/c271ad80-72a4-4de6-ba1e-bc6a7ed59242)
  
- Detección de textos con easyOCR en imagen estática.
Es posible añadir varios idiomas con este OCR, probé con español e inglés, tanto juntos como de forma separada. Los mejores resultados fueron con el detector inglés, por lo que usaré este aprovechando que no necesito detectar nada que no esté en su diccionario.

```reader = easyocr.Reader(['en'])  # Puedes agregar otros idiomas si es necesario```

Posteriormente se ejecuta la función readtext() sobre la imagen para la obtención de texto.

**Tras ejecutar el código con con varias imágenes, noté mejores resultados con easyOCR, con lo que decidí hacer las tareas siguientes con dicho detector. Es posible que el Tesseract requiera de algún tipo de procesado sobre las imágenes antes de detectar el texto.**

- Detección de texto de matrículas en video, guardando las detecciones en un csv, junto al número de apariciones del texto detectado.
  ![image](https://github.com/user-attachments/assets/736c90ca-f4b7-49b5-add8-545a0e6f614a)
  
Le apliqué algunas condiciones para filtrar algunas de las strings detectadas erróneamente, eliminando las detecciones de caracteres no alfanúmericos que no seane espacios, y indicando un mínimo de números y letras detectados.

- Seguimiento de matrículas de coches, y guardado en csv.
  
  ![image](https://github.com/user-attachments/assets/5b833570-bbf3-4950-a5fd-037a5aea7e52)

- Anonimización de matrículas y personas mediante desenfoque gaussiano.

Se trata de la utilización del código previamente creado, y añadirle desenfoque gaussiano al recuadro en el que se detecta una matrícula. El problema que se acontece es que no siempre se detecta la matrícula debido al movimiento, con lo que de aplicar simplemente el desenfoque, se estaría viendo de forma intermitente la matrícula real.

```
        for obj_id, obj_data in list(tracked_objects.items()):  # Convertimos a una lista de items
            if obj_id not in current_objects:
                x1, y1, x2, y2, lost_frames = obj_data
                if lost_frames < MAX_LOST_FRAMES:
                    # Desenfocar usando la última ubicación conocida
                    roi = frame[y1:y2, x1:x2]
                    blurred_roi = cv2.GaussianBlur(roi, (99, 99), 0)
                    frame[y1:y2, x1:x2] = blurred_roi
                    # Incrementar los frames perdidos
                    tracked_objects[obj_id] = (x1, y1, x2, y2, lost_frames + 1)
                else:
                    del tracked_objects[obj_id]  # Eliminar si se pierde el objeto
```

1. Seguimiento y Conteo de Frames Perdidos
- Cada vez que una matrícula es detectada en un frame, se almacena su posición (coordenadas x1, y1, x2, y2) y se le asigna un object_id único. Esto permite hacer seguimiento del objeto en frames sucesivos.
Para cada objeto rastreado, se inicializa un contador lost_frames que cuenta cuántos frames seguidos el objeto ha dejado de ser detectado.

2. Desenfoque en Matrículas No Detectadas
- Al final de cada iteración de frames, se comprueba si alguno de los objetos rastreados (tracked_objects) no ha sido detectado en el frame actual. Si un objeto no se detecta, su ID no estará en current_objects.
- Si un objeto se encuentra entre los rastreados pero no en los detectados en el frame actual, se incrementa su contador lost_frames.
  
3. Aplicar Desenfoque en la Última Ubicación Conocida
- Para los objetos cuyo contador lost_frames es menor que MAX_LOST_FRAMES (tolerancia de frames en los que se puede “perder” el objeto sin eliminarlo), se aplica desenfoque sobre la última ubicación conocida de la matrícula.
- El desenfoque se realiza en la región que ocupaba la matrícula la última vez que fue vista, usando el desenfoque gaussiano cv2.GaussianBlur() con un kernel más grande ((99, 99)).
Este desenfoque asegura que, aunque el objeto ya no esté visible o detectado en un frame, su región previa aún se desdibuja para proteger la privacidad.

4. Eliminación de Objetos No Detectados
- Si un objeto supera MAX_LOST_FRAMES sin ser detectado nuevamente, se elimina del diccionario tracked_objects. Esto optimiza el código al no conservar datos de objetos que ya no están en el video o cuya matrícula ya no es relevante.

El problema surge en el caso de que se deje de detectar el objeto al que se está siguiendo, y se cambie de identificador. En el momento en el que se deja de detectar, y vuelve a ser tomado con otro id, se ve la matrícula, con lo que no se puede considerar un acierto completo.
  
- Tarea final, incluye anonimización, mejor seguimiento de los objetos, y generación de archivo csv con los siguientes campos: fotograma,tipo_objeto,confianza,identificador_tracking,x1,y1,x2,y2,confianza_matrícula,mx1,my1,mx2,my2,texto_matricula. 
# Tarea final

## Inicialización de Librerías y Modelos:

- Se importan las librerías cv2, math, y easyocr y los módulos de csv y YOLO de Ultralyitcs.
- Se inicializan dos modelos YOLO: uno para detectar matrículas y otro para detectar coches y personas. Además, se configura un lector OCR (EasyOCR) para interpretar el texto de las matrículas.
  
### Configuración del Video de Entrada y Salida:
  
- Se define la ruta del video a analizar y se abre el archivo de video. También se configura un archivo de salida en formato MP4 para guardar el resultado procesado.

### Estructuras y Parámetros de Rastreo:

- Se crean variables y diccionarios para realizar un seguimiento de objetos detectados en cada cuadro, asignando un identificador único a cada objeto y almacenando sus coordenadas y otra información relevante.
- Se establecen umbrales de distancia y de pérdida de cuadros para mantener la consistencia en el rastreo de los objetos.
  
### Detección de Coches y Personas:

- Para cada cuadro del video, se aplican los modelos YOLO para detectar coches y personas.
- Si se detecta un coche o una persona, se registra su posición y confianza y se dibuja un rectángulo en torno a ellos en el cuadro.
- Las caras de las personas detectadas se desenfocan como medida de privacidad.
  
### Detección y Lectura de Matrículas:

- Usando el modelo de detección específico, el código busca matrículas en los cuadros.
- El texto de las matrículas detectadas se extrae con OCR y se filtran textos que no cumplen con el patrón típico de matrículas (letras y números).
- Las matrículas detectadas se registran en un archivo CSV, y se aplican desenfoques para proteger la información de las matrículas.

### Actualización de Rastreo y Salida de Datos:

- Los datos se escriben continuamente en un archivo CSV, incluyendo detalles como tipo de objeto, confianza, y texto de matrícula.
- Finalmente, el video procesado se guarda en el archivo de salida con todos los elementos resaltados (coches, personas, y matrículas).
  
## Resultados

El seguimiento se realizó de forma bastante aceptable con una distancia máxima para dejar de detectar como el mismo objeto de 50.

![image](https://github.com/user-attachments/assets/7830543f-8e2d-4648-9309-d93166af1815)

Aunque por alguna razón, la matrícula deja de ser detectada durante 25 frames, y supera la distancia superior máxima que puse para que deje de detectar como mismo objeto, con lo que pasa a ser detectada como otro objeto diferente, y obtiene otro identificador a pesar de ser la misma matrícula.

![image](https://github.com/user-attachments/assets/7b2c7826-000c-4d21-a058-4d3c5d24c73e)

Esto se puede solucionar simplemente aumentando la distancia máxima que puse, en el caso anterior estaba a 50, y al ponerlo a 100 se solucionaron varias de las detecciones. Y tanto la matrícula como el coche que fueron identificados con el id 1 al inicio, se mantuvieron como tal. Con esto quiero decir, que dependiendo del video puede ser necesario modificar este parámetro.

![image](https://github.com/user-attachments/assets/91336b47-efe6-4e18-9761-c41284415561)

El video llamado video_output.mp4 que se encuentra en el github, es una demostración de lo que hace el código con un video que saqué. En este video en particular no salen personas, pero de serlo se les desenfoca la cara (para ser exactos la parte superior de lo detectado como persona).
Para las personas se les desenfoca la cara, mientras que para las matrícualas se desenfoca todo el recuadro. 

![image](https://github.com/user-attachments/assets/7bbe2425-2bf1-48a6-b99a-87224bbd9128)

# Referencias

[Otsedom github](https://github.com/otsedom/otsedom.github.io/blob/main/VC/P4/VC_P4.ipynb)

[Video instalación Tesseract](https://www.youtube.com/watch?v=2kWvk4C1pMo)

[Video introducción roboflow](https://www.youtube.com/watch?v=w0DCoo-LvuU)

[Video instalación CUDA, cuDNN y pytorch](https://www.youtube.com/watch?v=DrEuKFnv8K0&t=1039s)




