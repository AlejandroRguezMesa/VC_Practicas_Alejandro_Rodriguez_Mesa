***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

## Instalación y enviroment en Anaconda
```
conda create --name VC_P5 python=3.11.5
conda activate VC_P5
pip install opencv-python
pip install matplotlib
pip install imutils
pip install dlib
pip install pygame
pip install xgboost
pip install mediapipe
pip install scikit-learn
```
## Librerías más utilizadas
1. OpenCV (cv2)
   
  **Uso:** Captura y procesamiento de imágenes en tiempo real desde la cámara, incluyendo la detección y lectura de imágenes faciales.
  
  **Funciones:**
  - Captura de video e imágenes en tiempo real.
  - Dibujo de formas y manipulación de imágenes (e.g., superposición de efectos visuales).
  - Procesamiento de datos de entrada y salida de video.

3. MediaPipe (mediapipe)
   
**Uso:** Detección de puntos de referencia faciales a través del módulo Face Mesh, esencial para la manipulación y detección facial.
  
  **Funciones:**
  - Extracción de puntos de referencia faciales, que facilita las manipulaciones y análisis de expresiones.
  - Cálculo de la malla facial, lo que ayuda en la detección de características específicas.

5. Pygame
   
  **Uso:** Manejo de efectos de sonido y música de fondo en la aplicación.
   
  **Funciones:**
  - Reproducción de efectos de sonido (e.g., efectos de relámpagos).
  - Gestión de música de fondo (e.g., música triste).
  - Integración de sonidos en eventos específicos dentro del flujo de la aplicación.

7. Scikit-learn (sklearn)
   
  **Uso:** Procesamiento de datos y aplicación de modelos de clasificación para emociones y género.

   **Funciones:**
  - Carga y aplicación de modelos entrenados de clasificación de emociones y género.
  - Preprocesamiento de datos de entrada (e.g., reducción de dimensionalidad con PCA y escalado).
  - Evaluación de modelos (matriz de confusión y generación de informes de clasificación).
  - Búsqueda de hiperparámetros con GridSearchCV para optimización del modelo.

9. Pillow (PIL)
    
  **Uso:** Manejo y carga de archivos GIF para superponer animaciones con transparencia en el fondo del video.
  
  **Funciones:**
  - Carga y gestión de archivos GIF (e.g., animaciones de lluvia).
  - Manejo de imágenes con transparencia para efectos visuales en el fondo.

11. Pickle
    
  **Uso:** Serialización y deserialización de datos, facilitando la carga y almacenamiento de modelos y datos faciales.
  
  **Funciones:**
  - Guardado y carga de datos de puntos faciales.
  - Almacenamiento de modelos entrenados, permitiendo su reutilización sin entrenar nuevamente.

13. XGBoost
    
  **Uso:** Entrenamiento de un modelo de clasificación para detectar emociones usando el algoritmo XGBoost.

  **Funciones:**
  - Implementación de un modelo de clasificación avanzado para mejorar la precisión en la detección de emociones.
  - Entrenamiento y ajuste del modelo en base a datos faciales preprocesados.
    
# VC_P5
## Introducción
Me propuse crear un filtro de pikachu mostrando sus orejas, nariz y mofletes(círculos rojos) en el que al inflar los mofletes, salgan rayos desde dichos círculos.
 

## Proceso
Tras crear el enviroment y descargar los landmarks shape_predictor_5_face_landmarks.dat y shape_predictor_68_face_landmarks ejecuté el código y la detección de caras funcionó el código que utiliza dlib. Aun así, decidí buscar otros detectores faciales con la idea de encontrar mejores resultados, y tras una búsqueda y algunas pruebas, encontré que MediaPipe ofrece detección facial mediante una malla de puntos con la que se puede trabajar.

## Rayos
En primer lugar traté de hacer la animación de rayos, ya que parecía tener cierta complejidad al querer hacerlo con opencv. Otra opción habria sido utilizar un gif sin fondo, pero probablemente quedaría peor, asi que inicialmente traté de hacerlos manualmente. 
En el código, los rayos se crean a partir de un proceso que descompone una línea inicial en múltiples segmentos y genera una apariencia ramificada y segmentada:

Para su realización, en primer lugar se define un rayo principal que va desde un punto de origen, hacia un punto de destino situado más abajo. Este segmento de línea principal representa el "tronco" del rayo.

Este segmento principal se divide en partes más pequeñas, generando puntos medios en cada uno. Cada punto medio se desplaza ligeramente de forma aleatoria en una dirección perpendicular, creando una línea con una forma irregular que emula el trazado zigzagueante de un rayo.

Para añadir más realismo, algunos de estos puntos medios generan ramas. Estas ramas son segmentos de línea adicionales que salen de puntos aleatorios en el rayo principal, simulando las bifurcaciones naturales de un rayo.

A medida que se realizan más divisiones y subdivisiones, el desplazamiento de cada punto se reduce para hacer que los detalles sean más finos conforme el rayo se extiende hacia sus extremos. Esto ayuda a crear una apariencia progresivamente más detallada en las partes finales del rayo.

Finalmente, todos los segmentos, tanto los del rayo principal como los de las ramas, se dibujan en el cuadro de video en tiempo real con el color y grosor especificados. Al generarse nuevos rayos en cada cuadro donde se detectan ojos, el efecto aparece animado y da la impresión de rayos que surgen de los ojos en movimiento.

Para probar cómo se veía en video, me basé en el código propuesto como base en el repositorio de otsedom en VC_P5_detectores.ipynb, y puse de origen los ojos. 

## Pruebas con la malla de puntos de MediaPipe
Una vez hecho el rayo, creé un código para convertir los frames detectados a la malla de puntos de puntos que detecta MediaPipe, esto con el fin de comprobar cómo se deforma mi cara al inflar los mofletes, ya que es en este caso que deben dibujarse los rayos. Tras hacer el gesto fue fácil notar que el alto de la cara se reduce, y el ancho de la cara aumenta. Además de que se compacta la parte inferior de la cara. 

Por lo tanto, si se cumplen estas condiciones, se podría suponer que los mofletes se están inflandos. Esto no es absoluto, y podría dar falsos positivos, pero debería de funcionar en la mayoría de situaciones. 

## Código del Filtro de pikachu 

### Detección Facial y Configuración Inicial
El código comienza configurando MediaPipe Face Mesh para detectar puntos clave en el rostro. Estos puntos permiten medir y monitorear características específicas de la cara, como la altura, el ancho y la distancia de la boca. La detección de estos puntos permite activar efectos visuales y auditivos basados en la expresión facial del usuario. 

El número que le corresponde a cada punto de la malla se puede buscar en internet, y saldrán varias imagenes anotadas. [Esta página](https://medium.com/@hotakoma/mediapipe-landmark-face-hand-pose-sequence-number-list-view-778364d6c414) es uno de esos recursos 

### Superposición de Imágenes
Para mejorar el efecto visual, se superponen imágenes de orejas en la cabeza detectada, ajustando el tamaño y rotación de acuerdo con la inclinación y el tamaño de la cara. El código incluye una función para rotar las imágenes de las orejas y una para superponerlas, utilizando transparencia para una integración visual suave.

### Detección de "Mofletes Inflados"
El sistema detecta mofletes inflados al calcular el ancho y la altura del rostro, además de la distancia entre el punto medio del labio superior e inferior como medida para la compactación. Cuando el ancho aumenta y la altura y distancia de los puntos de la boca disminuye en comparación con los valores iniciales, el sistema interpreta esto como "mofletes inflados" y activa el efecto de rayos, previamente detallado en otra sección.

### Efecto de Rayos
Cuando los mofletes están inflados, se dibujan rayos en tiempo real desde los mofletes, creando un efecto visual que simula la salida de rayos.

### Recalibración y Tiempo Real
El código se recalibra automáticamente cada 10 segundos para ajustar los valores base de las características faciales, asegurando que el sistema se adapte a posibles cambios en la posición y expresión del usuario. El proceso principal de captura de video y renderizado continúa en tiempo real hasta que se cierra la ventana de visualización o se detiene el programa.

### Sonido
Tras terminar el filtro se me ocurrió añadir sonido al detectar que se abre la boca, es decir, los puntos de la boca se alejan más allá de un umbral definido. El sonido es un archivo .mp3 del sonido que hace pikachu, que se reproduce con Pygame.

### Visualización
Con OpenCV se muestra la imagen de la webcam procesada, a los frames le apliqué un cv2.flip para que se vea en modo espejo.

### Uso
Para ver el filtro de pikachu, simplemente se debe mostrar la cara en cámara. En cuanto a los rayos, se recomienda no moverse demasiado despues de la recalibración para que se detecte correctamente la acción de inflar los mofletes. Además, al abrir la boca se repoduce el sonido de "pika pika"

## Detección de género
Para la implementación de un clasificador de géneros en dos clases (hombre y mujer), se llevó a cabo el siguiende procedmiento.

- Carga y Preprocesamiento de Imágenes:

  - Se utiliza la biblioteca os para la navegación de archivos y carpetas, y cv2 (OpenCV) para cargar imágenes de la carpeta DatabaseGender59x65.
  - Las imágenes se convierten a escala de grises, y sus píxeles se aplanan para crear un vector unidimensional, facilitando su uso en modelos de aprendizaje automático.
  - Cada imagen se asocia con una etiqueta numérica que identifica la clase a la que pertenece.


- División del Conjunto de Datos:
  - Se utiliza train_test_split de sklearn para dividir los datos en conjuntos de entrenamiento (70%) y prueba (30%), permitiendo evaluar el modelo con datos no vistos durante el entrenamiento.

- Análisis de Componentes Principales (PCA):
  - Se emplea PCA de sklearn.decomposition para reducir la dimensionalidad de los datos, conservando el 85% de la varianza. Esto transforma los vectores de las imágenes en componentes principales (conocidas como "eigenfaces") que representan patrones en los rostros.
  - La reducción de dimensionalidad optimiza el procesamiento y ayuda a evitar el sobreajuste.

- Normalización de los Datos:
  - Se usa MinMaxScaler de sklearn.preprocessing para escalar los datos a un rango [0, 1] antes de entrenar el modelo, asegurando que los datos tengan una escala adecuada para el modelo SVM.

- Entrenamiento del Clasificador SVM:
  - Un clasificador de Máquinas de Vectores de Soporte (SVM) es entrenado usando GridSearchCV de sklearn con un kernel rbf (Radial Basis Function), explorando diferentes combinaciones de hiperparámetros (C y gamma) para optimizar el modelo.
  - GridSearchCV aplica validación cruzada (5 pliegues) para seleccionar la mejor combinación de parámetros en función de los datos de entrenamiento.

- Predicción y Evaluación del Modelo:
  - El modelo entrenado se utiliza para predecir las etiquetas del conjunto de prueba.
  - Se calculan métricas de desempeño, como la precisión y el recall, además de un reporte de clasificación detallado y una matriz de confusión, para evaluar la calidad del clasificador SVM en clasificar correctamente los géneros.

## Implementación del clasificador de género en el filtro

- Captura de la Imagen Facial:
  - Una vez que MediaPipe identifica un rostro, se extrae el área de la cara y se utiliza esta sección para realizar la predicción de género.

- Preprocesamiento:
  - La imagen de la cara detectada se convierte a escala de grises y se redimensiona a una resolución específica (definida por las variables height y width) para igualar las dimensiones esperadas por el modelo.
  - La imagen redimensionada se convierte en un vector unidimensional para que sea compatible con el modelo de aprendizaje automático.
- Reducción de Dimensionalidad y Normalización:
  - Se aplica una reducción de dimensionalidad con PCA (Análisis de Componentes Principales) para reducir el número de características, reteniendo solo aquellas que capturan mejor la varianza de los datos. Esto ayuda a simplificar el modelo y reducir el ruido.
  - El vector resultante es normalizado mediante MinMaxScaler para adaptarse al rango de valores con los que el modelo fue entrenado.
- Predicción usando SVM:
  - El vector de características preprocesado se pasa a un modelo SVM (Support Vector Machine) previamente entrenado que predice el género. Este modelo ha sido ajustado para clasificar entre dos etiquetas: 0 para Mujer y 1 para Hombre.
  - La predicción resultante (género masculino o femenino) se almacena en genero_predicho, que luego se utiliza en otras partes del código.
- Efectos Visuales
  - El color de los rayos cambia en función del género, y a las mujeres se les añade unas largas "pestañas" con opencv.

## Deteción de Emociones
Para el entrenamiento de un modelo de clasificación de expresiones faciales a partir de imágenes, hice uso de MediaPipe y XGBoost. La base de datos que utilicé tiene varias clases, y utilicé únicamente 4 de ellas, enfado, tristeza, neutralidad y felicidad.

1. Extracción de Landmarks: Se usa MediaPipe para detectar landmarks faciales en imágenes de entrenamiento. Cada imagen es procesada y, si se detecta una cara, se almacenan las coordenadas de sus landmarks. Estos datos son organizados en un diccionario y guardados para su uso posterior.

2. Preparación de Datos: Los datos de landmarks almacenados se cargan y se convierten en un formato adecuado para el modelo, con cada imagen representada como un vector de coordenadas y etiquetas de clase.

3. Entrenamiento del Modelo: Utilizando XGBoost, se entrena un modelo de clasificación. Se configura una búsqueda en grid para optimizar ciertos hiperparámetros del modelo, mejorando su precisión en la clasificación de emociones.

4. Evaluación: El modelo entrenado es evaluado en un conjunto de prueba mediante métricas como precisión y matriz de confusión para observar el rendimiento de la clasificación. La matriz de confusión de los test es el siguiente:

![image](https://github.com/user-attachments/assets/020cf980-8586-447e-a956-8bbde0f0f670)

Como se puede ver hay muchas detecciones de la clase happy en comparación con lo demás, esto me hizo revisar el conjunto de entrenamiento.
Antes de nada, una vez ejecutado el código correspondiente a los 3 primeros puntos, se creará el modelo mp_model.pkl, que será el utilizado para futuras predicciones. El dataset que yo usé, contiene unas 4 mil imagénes para todas las clases, excepto felicidad que contiene 7000, viendo los resultados se puede sospechar de que hubo un desbalanceo de clases, aunque no pude asegurar que haya sesgo porque en otras clases tambien hay bastantes falsas detecciones. 
Tras ver las imágenes, me percaté que el dataset no es idóneo por el tipo de imágenes que maneja, en ocasiones expresiones muy exageradas, fotos de bebés o incluso personajes ficticios que no son humanos, lo que obviamente afecta negativamente al rendimiento del modelo. También mencionar que no se detectan caras en todas las imágenes, sobretodo debido a imágenes de personas o personajes de perfil.

A pesar de que probablemente lo mejor era cambiar de dataset, opté por quedarme con el que tengo actualmente, pero eliminando imágenes del conjunto de happy para que se equilibre para comprobar por mi mismo si se mejoran los resultados con un buen balance. 

Para equilibrarlo dejé un aproximado de 4000 imágenes por clase. Y tras un nuevo entrenamiento se obtuvieron los siguientes resultados para el mismo conjunto de test:


5. Predicciones Nuevas: Una vez entrenado, el modelo puede realizar predicciones de expresiones faciales en nuevas imágenes, mostrando la etiqueta de expresión y el nivel de confianza en el resultado.

### Implementación en el filtro
A modo tarea final junté todo lo que he hecho anteriormente con el nuevo detector facial. Muestra en la esquina superior derecha la emoción y género detectado. Y al detectar tristeza empieza a llover (se aplica un gif sin fondo usando el canal alfa), a la par que suena una canción triste. Además, añadí sonido cuando se dibujan los rayos.

- **Clasificador de Emociones**
  - Inicialización: El modelo de emociones se carga desde un archivo mp_model.pkl que contiene el clasificador entrenado y las etiquetas de clase.
  - Predicción de Emociones: Durante el procesamiento de cada fotograma, se detectan landmarks faciales y se generan predicciones de emociones en función de la configuración de estos puntos en el rostro.
  - Acciones Basadas en la Emoción: Si la emoción detectada es "sad", el programa reproduce una canción triste y superpone un efecto de lluvia (GIF animado). Si la emoción cambia de "sad" a otra, la canción se pausa, pero el efecto de lluvia permanece pausado hasta que la emoción vuelva a cambiar a "sad".
  - 
- **GIF de Lluvia**
  - Carga del GIF con Transparencia: El archivo GIF de lluvia es procesado para manejar la transparencia, permitiendo superponerlo en el fotograma sin alterar el fondo del video.
  - Superposición del GIF: Se ajusta el GIF de lluvia al tamaño del fotograma de la cámara y se coloca sobre la imagen de fondo usando su canal alfa para respetar las zonas transparentes.
  - Animación Basada en el Tiempo: Cada cuadro del GIF se selecciona en función del tiempo, creando el efecto de animación de lluvia en cada fotograma.

# Demostración

# Referencias
[Dataset de Emociones](https://www.kaggle.com/datasets/msambare/fer2013?resource=download)
[Inspiración inicial para los rayos](https://github.com/codemonkeycxy/Thor/blob/master/lightning_generatror.py)
[Uso de modelo de deteccion facial con MediaPipe](https://www.kaggle.com/code/pabasar/facial-expression-recognition-mediapipe/notebook)
[Repositorio de Otsedom de la práctica](https://github.com/otsedom/otsedom.github.io/tree/main/VC/P5)
