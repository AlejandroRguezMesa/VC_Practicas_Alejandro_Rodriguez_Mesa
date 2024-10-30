***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

## Enviroment en Anaconda
1. **NumPy**:
    ```
    pip install numpy
    ```

2. **OpenCV**:
    ```
    pip install opencv-python
    ```

3. **Scikit-learn**:
    ```
    pip install scikit-learn
    ```

4. **Matplotlib**:
    ```
    pip install matplotlib
    ```
## Paquetes utilizados
- **NumPy (`numpy`)**: Proporciona soporte para trabajar con arreglos multidimensionales y funciones matemáticas de alto rendimiento. Es fundamental para operaciones numéricas y cálculos algebraicos en Python.
  
- **OpenCV (`cv2`)**: Biblioteca de código abierto orientada a la visión por computadora. Se utiliza para procesar y manipular imágenes y videos, permitiendo tareas como detección de objetos, reconocimiento de patrones, etc.

- **Scikit-learn (`sklearn`)**:
  - **`KNeighborsClassifier`**: Implementación del algoritmo K-Nearest Neighbors (KNN) utilizado para clasificación.
  - **Métricas (`confusion_matrix`, `accuracy_score`, `precision_score`, `recall_score`, `f1_score`)**: Estas funciones permiten evaluar el rendimiento de modelos de clasificación utilizando métricas como la matriz de confusión, la precisión, el recall y el puntaje F1.

- **Matplotlib (`matplotlib.pyplot`)**: Biblioteca para la generación de gráficos en 2D, utilizada para visualizar datos en forma de gráficos como líneas, barras, histogramas, etc.

- **Seaborn (`seaborn`)**: Extensión de Matplotlib para la visualización de datos estadísticos. Proporciona gráficos más estéticos y es más fácil de usar para trazar gráficos complejos.

# Tarea 1 - Detección y reconocimiento de monedas
## 1.1 - Detección con una imágen idónea en cuanto a iluminación, distancia, nitidez, etc

En primer lugar traté de identificar los contornos de las monedas y su valor para la imagen "Monedas.jpg" cuya detección de contornos es muy buena despues del umbralizado.

![image](https://github.com/user-attachments/assets/7dcb6e31-5517-47b8-a439-818d94ad3888)

### Procedimiento

Todas las tareas de la práctica relacionadas a la detección de monedas tienen en común la forma de reconocimiento de las monedas.

En primer lugar, se realizó la detección de todos los contornos, y se filtraron en función de qué tan redondos son, si su circularidad es mayor que la circularidad mínima, 
entonces se considerarán monedas. Esto tiene su contraparte de que objetos circulares que no sean monedas serán detectados como tal, generando falsos positivos. 

Tras esto utilicé la función cv2.minEnclosingCircle() para obtener el radio, lo cual me permitió saber el diámetro de todas las monedas. Estas medidas las añadí a una lista, y una vez se han obtenido todas las medidas, se comprueba el máximo diámetro de la lista.

El diámetro máximo corresponde a la moneda más grande, que es la de dos euros. Sabiendo qué moneda es la de dos euros, se obtiene su tamaño, y ya se estaría teniendo en cuenta la escala,
con lo que solo falta haría una regla de tres con los siguientes conjuntos de datos:

```python
coin_diameters = {
    "one_cent":  16.25,
    "two_cents": 18.75,
    "five_cents": 21.25,
    "ten_cents": 19.75,
    "twenty_cents": 22.25,
    "fifty_cents": 24.25,
    "one_eur": 23.25,
    "two_eur": 25.75
}

# Asignar valores a cada tipo de moneda (en euros)
coin_values = {
    "one_cent": 0.01,
    "two_cents": 0.02,
    "five_cents": 0.05,
    "ten_cents": 0.10,
    "twenty_cents": 0.20,
    "fifty_cents": 0.50,
    "one_eur": 1.00,
    "two_eur": 2.00
}
```
Sabiendo que la medida de la moneda de dos euros es de 25.75, se puede saber los mm correspondientes para todas los demás contornos mediante una regla de tres. Y tras esto se aproxima el valor al diámetro más cercano del conjunto. 

Una vez se tienen todos los diámetros, solo queda obtener su valor a partir de coin_values.

### Resultados

![image](https://github.com/user-attachments/assets/f57a44ce-0fc2-42c2-8888-e650d785254c)

```
Número de monedas detectadas: 8
Moneda encontrada: one_cent, Valor: 0.01 euros
Moneda encontrada: twenty_cents, Valor: 0.2 euros
Moneda encontrada: two_cents, Valor: 0.02 euros
Moneda encontrada: fifty_cents, Valor: 0.5 euros
Moneda encontrada: ten_cents, Valor: 0.1 euros
Moneda encontrada: one_eur, Valor: 1.0 euros
Moneda encontrada: five_cents, Valor: 0.05 euros
Moneda encontrada: two_eur, Valor: 2.0 euros
Suma total de dinero detectado: 3.88 euros
```
![image](https://github.com/user-attachments/assets/90c7367c-d502-41af-bc29-9188ed717627)

En este caso se detectan correctamente todas las monedas gracias a la calidad de la foto. El problema es que no siempre se tendrá esa calidad. 

## 1.2 - Detección con imágenes cuyas condiciones no son las ideales.

En esta ocasión usé el mismo código que en la tarea anterior, con la diferencia que además traté de tener en cuenta la posibilidad de que hayan dos monedas juntas. 

### Procedimiento

La diferencia con el código anterior es que para detectar el valor de monedas que están juntas tuve que tener en cuenta que el choque de las monedas deja un lugar en el que
no se dibujan contornos, esto lo utilicé como un punto central que define la intersección entre las dos monedas.

Para calcular el diámetro de ambas monedas tracé líneas que pasen por el punto central en múltiples ángulos, obteniendo las intersecciones de las líneas, y obteniendo la de mayor tamaño, que será la que dictará el diámetro de ambas monedas. 

Debido a las diferencias en el cálculo del diámetro, es necesario hacer un procedimiento similar en la moneda de dos euros para tener los diámetros en la misma medida, y así poder hacer la regla de 3. Tras esto, solo quedaría relacionar el diámetro con la del conjunto, y añadir su valor a la lista que contiene las demás monedas. 

### Resultados
El código mencionado anteriormente fue encapsulado en una función para facilitar la ejecución del código con distintas imágenes. Como parámetros es necesario pasar la imagen en cuestión y el umbralizado. En caso de que el parámetro de umbralizado sea 0, se aplicará un umbralizado adaptativo
```
tarea1('img3.jpeg', 170)
```
```
Número de monedas incompletas estimadas (truncadas): 2
Número de monedas detectadas: 21
Moneda encontrada: one_eur, Valor: 1.0 euros
Moneda encontrada: fifty_cents, Valor: 0.5 euros
Moneda encontrada: one_eur, Valor: 1.0 euros
Moneda encontrada: two_cents, Valor: 0.02 euros
Moneda encontrada: two_eur, Valor: 2.0 euros
Moneda encontrada: fifty_cents, Valor: 0.5 euros
Moneda encontrada: one_cent, Valor: 0.01 euros
Moneda encontrada: two_cents, Valor: 0.02 euros
Moneda encontrada: five_cents, Valor: 0.05 euros
Moneda encontrada: two_cents, Valor: 0.02 euros
Moneda encontrada: two_cents, Valor: 0.02 euros
Moneda encontrada: twenty_cents, Valor: 0.2 euros
Moneda encontrada: ten_cents, Valor: 0.1 euros
Moneda encontrada: ten_cents, Valor: 0.1 euros
Moneda encontrada: one_eur, Valor: 1.0 euros
Moneda encontrada: twenty_cents, Valor: 0.2 euros
Moneda encontrada: two_eur, Valor: 2.0 euros
Moneda encontrada: five_cents, Valor: 0.05 euros
Moneda encontrada: two_cents, Valor: 0.02 euros
Moneda con contorno incompleto encontrada: two_cents, Valor: 0.02 euros
Moneda con contorno incompleto encontrada: two_cents, Valor: 0.02 euros
Suma total de dinero detectado: 8.85 euros


Resultados
	[+]Precisión de monedas: 0.9130434782608696
	[+]Precisión de dinero: 0.615023474178404

```
![image](https://github.com/user-attachments/assets/f53038fa-cdcf-47b8-bf05-4b6f8ee0ba8a)

```

tarea1('img4.jpeg', 0)
tarea1('img5.jpeg', 0)
tarea1('img6.jpeg', 0)
```
Los resultados dependen de la iluminación y el umbralizado aplicado, además, solo tiene en cuenta un único par de monedas. Cabe recalcar que el escalado se hace en función de la moneda de dos euros, si la moneda de dos euros no es detectada correctamente, el valor se alejará mucho del real, ya que el diámetro de las demás monedas se obtiene a partir de ello.


## Tarea 1.5 Detección de monedas mediante video.

Este ejercicio es una adaptación a formato video de lo realizado anteriormente. Simplemente realiza el cálculo para cada frame proporcionado. Se añadió respecto a lo anterior detección de dónde está el mouse y mediante putText se muestra la moneda seleccionada. 

![image](https://github.com/user-attachments/assets/25801b15-0191-4022-bc71-c35f089c83d4)

Al poner el cursor sobre una moneda, sale lo detectado:

![image](https://github.com/user-attachments/assets/ebec9b12-2fe1-47e5-9e91-65b47eb33d91)

El valor de las monedas puede cambiar continuamente debido a que si en algún frame no se detectan todas las monedas, el precio cambiará. Además de que en ciertos casos la detección del tamaño es complicada debido a la cercanía de diámetros. Por lo general, entre más cerca estén las monedas de la de dos euros, más fácil es su detección, por una cuestión de la distancia a la cámara.

## Tarea 2. Detección de microplásticos.

### Procedimiento
En primer lugar creé una función para procesar la imagen y obtener varias métricas con las que obtener arrays de datos con los contornos detectados. Para ello se detectan los contornos
y se le aplican ciertas operaciones de openCV como contourArea(), arcLength() o fitEllipse()  para obtener las métricas. 

Las métricas que calculé son:

            'area': area,
            'perimeter': perimeter,
            'compactness': compactness,
            'area_ratio': area_ratio,
            'width_ratio': width_ratio,
            'eccentricity': eccentricity,
            'centroid': (centroid_x, centroid_y)

Esta función me devuelve la imagen procesada, sus contornos y las métricas obtenidas para cada contorno, esto último es un array de datos que será necesario para entrenar el modelo de aprendizaje.

        FRA_image, FRA_contours, FRA_metrics = procesar_imagen('FRA.png', 200)
        PEL_image, PEL_contours, PEL_metrics = procesar_imagen('PEL.png', 200)
        TAR_image, TAR_contours, TAR_metrics = procesar_imagen('TAR.png', 200)

De las imagenes FRA, PEL y TAR se obtienen lo siguiente:

![image](https://github.com/user-attachments/assets/e4614077-4ab2-48b7-818b-2e2ccf982747)

    Métricas para FRA:
    {'area': 1850.0, 'perimeter': 208.0243855714798, 'compactness': 23.391429725617133, 'area_ratio': 0.0016785526339666468, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.794531277200762, 'centroid': (1123, 902)}
    {'area': 7144.5, 'perimeter': 348.55129647254944, 'compactness': 17.00440986390861, 'area_ratio': 0.006482388807229572, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.0646336832744023, 'centroid': (747, 844)}
    {'area': 6256.5, 'perimeter': 332.8355667591095, 'compactness': 17.706307759906917, 'area_ratio': 0.005676683542925581, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.6183277091618737, 'centroid': (855, 847)}
    {'area': 12723.5, 'perimeter': 460.3746712207794, 'compactness': 16.657746524277183, 'area_ratio': 0.011544359155824123, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.2847890042907857, 'centroid': (991, 843)}
    {'area': 10528.0, 'perimeter': 462.67618680000305, 'compactness': 20.33332578189507, 'area_ratio': 0.009552325475892355, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.844327656394918, 'centroid': (294, 576)}
    {'area': 4957.0, 'perimeter': 367.2792179584503, 'compactness': 27.212835171307415, 'area_ratio': 0.004497613733282523, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.676717335138229, 'centroid': (663, 494)}
    {'area': 2143.5, 'perimeter': 185.78174436092377, 'compactness': 16.102102420241486, 'area_ratio': 0.001944852741031085, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.2115011852312514, 'centroid': (476, 272)}
    {'area': 9890.0, 'perimeter': 398.8771973848343, 'compactness': 16.0872617384813, 'area_ratio': 0.008973451648610884, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.1425586330351787, 'centroid': (72, 281)}
    {'area': 2122.0, 'perimeter': 178.5096663236618, 'compactness': 15.016824208758285, 'area_ratio': 0.0019253452374471483, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.1821774590706395, 'centroid': (609, 215)}
    {'area': 7062.5, 'perimeter': 342.35028624534607, 'compactness': 16.595216777666604, 'area_ratio': 0.006407988095886185, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.0986119845834759, 'centroid': (1044, 134)}

![image](https://github.com/user-attachments/assets/1dfe2672-a4f6-48e9-b8b0-6a357f0beb2a)

    Métricas para PEL:
    {'area': 6084.0, 'perimeter': 323.4213533401489, 'compactness': 17.19286189946967, 'area_ratio': 0.005520169851380042, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.067127333124228, 'centroid': (713, 827)}
    {'area': 6195.0, 'perimeter': 307.2792180776596, 'compactness': 15.241407241713945, 'area_ratio': 0.005620883009418041, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.0813471743351228, 'centroid': (916, 758)}
    {'area': 6189.0, 'perimeter': 311.42135441303253, 'compactness': 15.670263367983134, 'area_ratio': 0.005615439054929501, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.2607643215332955, 'centroid': (402, 717)}
    {'area': 6648.0, 'perimeter': 316.10764503479004, 'compactness': 15.030692426209509, 'area_ratio': 0.006031901573302847, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.0911217236948882, 'centroid': (647, 634)}
    {'area': 4415.0, 'perimeter': 258.79393768310547, 'compactness': 15.169717368409303, 'area_ratio': 0.0040058431778177, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.0863397950775484, 'centroid': (939, 602)}
    {'area': 7544.5, 'perimeter': 342.8355669975281, 'compactness': 15.579061037645511, 'area_ratio': 0.006845319106465604, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.1509561968930064, 'centroid': (218, 476)}
    {'area': 3594.5, 'perimeter': 262.409161567688, 'compactness': 19.15664712050549, 'area_ratio': 0.00326138240150979, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.1371412387467836, 'centroid': (674, 422)}
    {'area': 4598.0, 'perimeter': 261.1370828151703, 'compactness': 14.830921274731862, 'area_ratio': 0.0041718837897181844, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.0338343226395366, 'centroid': (124, 274)}
    {'area': 7806.5, 'perimeter': 349.86500465869904, 'compactness': 15.679948950852687, 'area_ratio': 0.007083038452465204, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.1588277465398982, 'centroid': (939, 278)}
    {'area': 6292.5, 'perimeter': 307.0365775823593, 'compactness': 14.98155899459486, 'area_ratio': 0.005709347269856824, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.134339902500695, 'centroid': (255, 256)}
    {'area': 6453.0, 'perimeter': 341.2792179584503, 'compactness': 18.049202636034625, 'area_ratio': 0.005854973052425281, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.160329561518303, 'centroid': (615, 153)}

![image](https://github.com/user-attachments/assets/7a319290-cb33-4517-9935-9d88bfd6ded0)

    Métricas para TAR:
    {'area': 1588.0, 'perimeter': 167.3969682455063, 'compactness': 17.64593512455103, 'area_ratio': 0.001440833287967046, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.2872469691753854, 'centroid': (494, 896)}
    {'area': 2662.0, 'perimeter': 211.19595801830292, 'compactness': 16.755722270198635, 'area_ratio': 0.0024153011414157913, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.43275626266612, 'centroid': (808, 741)}
    {'area': 3047.5, 'perimeter': 287.3797233104706, 'compactness': 27.099952541428262, 'area_ratio': 0.0027650752173045165, 'width_ratio': 1.2420382165605095, 'eccentricity': 2.7083745412965916, 'centroid': (687, 748)}
    {'area': 1659.5, 'perimeter': 182.46803605556488, 'compactness': 20.063021501642016, 'area_ratio': 0.0015057070789554867, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.189751146037983, 'centroid': (995, 578)}
    {'area': 2270.0, 'perimeter': 215.1959581375122, 'compactness': 20.400572862873087, 'area_ratio': 0.00205962944816448, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.5348864474383306, 'centroid': (873, 387)}
    {'area': 10153.5, 'perimeter': 433.119837641716, 'compactness': 18.475677722833154, 'area_ratio': 0.00921253198323262, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.1696732736961952, 'centroid': (489, 394)}
    {'area': 1859.0, 'perimeter': 189.0538226366043, 'compactness': 19.22611503685457, 'area_ratio': 0.0016867185656994574, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.424372809812584, 'centroid': (223, 333)}
    {'area': 2674.5, 'perimeter': 220.2670258283615, 'compactness': 18.140797407841493, 'area_ratio': 0.002426642713266917, 'width_ratio': 1.2420382165605095, 'eccentricity': 1.296427008578699, 'centroid': (870, 258)}

Estos arrays los junté y creé otra array que contenga para cada métrica una etiqueta indicativa del grupo al que pertenece.

    all_metrics = FRA_metrics + PEL_metrics + TAR_metrics
    labels = [0] * len(FRA_metrics) + [1] * len(PEL_metrics) + [2] * len(TAR_metrics)

Esto fue realizado con el objetivo de proporcionarle al clasificador KNN las métricas y los grupos a los que corresponden para que encuentre un patrón y lo utilice para futuras métricas.

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(metrics_array, labels)  # Entrenar el modelo

    # Imprimir los resultados de clasificación
    predictions = knn.predict(metrics_array)

Tras esto hice una función parecida a la proporcionada como ejemplo en la práctica para aplicar métricas de rendimiento y una matriz de confusión. Esta matriz de confusión se sacó del mismo conjunto de datos de entrenamiento. Es decir, se entrenó con ciertas métricas el modelo, y luego se le dieron esas mismas métricas para que decidiese a qué grupo pertenecian. 

### Resultados 

    [i] Número de Detecciones:
    	Hay 10 detecciones de FRA.
    	Hay 11 detecciones de PEL.
    	Hay 8 detecciones de TAR.
    
    Resultados de clasificación:
    	Objeto 0 es del grupo 2, Grupo real: 0
    	Objeto 1 es del grupo 0, Grupo real: 0
    	Objeto 2 es del grupo 1, Grupo real: 0
    	Objeto 3 es del grupo 0, Grupo real: 0
    	Objeto 4 es del grupo 0, Grupo real: 0
    	Objeto 5 es del grupo 1, Grupo real: 0
    	Objeto 6 es del grupo 0, Grupo real: 0
    	Objeto 7 es del grupo 0, Grupo real: 0
    	Objeto 8 es del grupo 0, Grupo real: 0
    	Objeto 9 es del grupo 0, Grupo real: 0
    	Objeto 10 es del grupo 1, Grupo real: 1
    	Objeto 11 es del grupo 1, Grupo real: 1
    	Objeto 12 es del grupo 1, Grupo real: 1
    	Objeto 13 es del grupo 1, Grupo real: 1
    	Objeto 14 es del grupo 1, Grupo real: 1
    	Objeto 15 es del grupo 1, Grupo real: 1
    	Objeto 16 es del grupo 1, Grupo real: 1
    	Objeto 17 es del grupo 1, Grupo real: 1
    	Objeto 18 es del grupo 1, Grupo real: 1
    	Objeto 19 es del grupo 1, Grupo real: 1
    	Objeto 20 es del grupo 1, Grupo real: 1
    	Objeto 21 es del grupo 2, Grupo real: 2
    	Objeto 22 es del grupo 2, Grupo real: 2
    	Objeto 23 es del grupo 2, Grupo real: 2
    	Objeto 24 es del grupo 2, Grupo real: 2
    	Objeto 25 es del grupo 0, Grupo real: 2
    	Objeto 26 es del grupo 0, Grupo real: 2
    	Objeto 27 es del grupo 2, Grupo real: 2
    	Objeto 28 es del grupo 2, Grupo real: 2
    
    Métricas de rendimiento:
    Accuracy (TP/(n))= 0.8275862068965517
    Precision (TP/(TP+FP)) = 0.8256073428487222
    Recall (TP/(TP+FN)) = 0.8275862068965517
    F1 Score (2*(precision*recall)/(precision+recall)) = 0.8224742891712038

![image](https://github.com/user-attachments/assets/6f6e918b-afee-4b3d-bcae-4944bf2c0f86)

El PEL debido a su circularidad es mucho más fácil de detectar que el FRA o el TAR, es por esa razón que los resultados son tan favorables en la detección de PEL. 

### Entrenamiento con imágenes con más cantidad de muestras y prueba final con una imagen que contenga todos los tipos de datos. 
    
    # Procesar las imágenes
    FRA_image, FRA_contours, FRA_metrics = procesar_imagen('fragment-03-olympus-10-01-2020.JPG', 800)
    PEL_image, PEL_contours, PEL_metrics = procesar_imagen('pellet-03-olympus-10-01-2020.JPG', 400)
    TAR_image, TAR_contours, TAR_metrics = procesar_imagen('tar-03-olympus-10-01-2020.JPG', 400)

Tras obtener todas las métricas, realicé la parte del entrenamiento del modelo y mostré los resultados. Previamente compacté en funciones lo realizado anteriormente para facilitar las pruebas con nuevos conjuntos de datos.
    
    labels, predictions, knn = entrenamiento_y_resultados()
    rendimiento()
### Resultados del entrenamiento
    
    [i] Número de Detecciones:
    	Hay 74 detecciones de FRA.
    	Hay 70 detecciones de PEL.
    	Hay 60 detecciones de TAR.
    
    Resultados de clasificación:
    	Objeto 0 es del grupo 1, Grupo real: 0
    	Objeto 1 es del grupo 0, Grupo real: 0
    	Objeto 2 es del grupo 0, Grupo real: 0
    	Objeto 3 es del grupo 1, Grupo real: 0
    	Objeto 4 es del grupo 0, Grupo real: 0
    	Objeto 5 es del grupo 2, Grupo real: 0
    	Objeto 6 es del grupo 0, Grupo real: 0
    	Objeto 7 es del grupo 0, Grupo real: 0
    	Objeto 8 es del grupo 1, Grupo real: 0
    	Objeto 9 es del grupo 2, Grupo real: 0
    	Objeto 10 es del grupo 2, Grupo real: 0
    	Objeto 11 es del grupo 2, Grupo real: 0
    	Objeto 12 es del grupo 0, Grupo real: 0
    	Objeto 13 es del grupo 0, Grupo real: 0
    	Objeto 14 es del grupo 0, Grupo real: 0
    	Objeto 15 es del grupo 2, Grupo real: 0
    	Objeto 16 es del grupo 0, Grupo real: 0
    	Objeto 17 es del grupo 0, Grupo real: 0
    	Objeto 18 es del grupo 0, Grupo real: 0
    	Objeto 19 es del grupo 1, Grupo real: 0
    	Objeto 20 es del grupo 0, Grupo real: 0
    	Objeto 21 es del grupo 0, Grupo real: 0
    	Objeto 22 es del grupo 0, Grupo real: 0
    	Objeto 23 es del grupo 0, Grupo real: 0
    	Objeto 24 es del grupo 0, Grupo real: 0
    	Objeto 25 es del grupo 1, Grupo real: 0
    	Objeto 26 es del grupo 2, Grupo real: 0
    	Objeto 27 es del grupo 0, Grupo real: 0
    	Objeto 28 es del grupo 0, Grupo real: 0
    	Objeto 29 es del grupo 1, Grupo real: 0
    	Objeto 30 es del grupo 0, Grupo real: 0
    	Objeto 31 es del grupo 0, Grupo real: 0
    	Objeto 32 es del grupo 0, Grupo real: 0
    	Objeto 33 es del grupo 0, Grupo real: 0
    	Objeto 34 es del grupo 0, Grupo real: 0
    	Objeto 35 es del grupo 0, Grupo real: 0
    	Objeto 36 es del grupo 0, Grupo real: 0
    	Objeto 37 es del grupo 0, Grupo real: 0
    	Objeto 38 es del grupo 0, Grupo real: 0
    	Objeto 39 es del grupo 0, Grupo real: 0
    	Objeto 40 es del grupo 2, Grupo real: 0
    	Objeto 41 es del grupo 2, Grupo real: 0
    	Objeto 42 es del grupo 2, Grupo real: 0
    	Objeto 43 es del grupo 0, Grupo real: 0
    	Objeto 44 es del grupo 0, Grupo real: 0
    	Objeto 45 es del grupo 2, Grupo real: 0
    	Objeto 46 es del grupo 0, Grupo real: 0
    	Objeto 47 es del grupo 2, Grupo real: 0
    	Objeto 48 es del grupo 0, Grupo real: 0
    	Objeto 49 es del grupo 0, Grupo real: 0
    	Objeto 50 es del grupo 0, Grupo real: 0
    	Objeto 51 es del grupo 2, Grupo real: 0
    	Objeto 52 es del grupo 2, Grupo real: 0
    	Objeto 53 es del grupo 0, Grupo real: 0
    	Objeto 54 es del grupo 0, Grupo real: 0
    	Objeto 55 es del grupo 1, Grupo real: 0
    	Objeto 56 es del grupo 0, Grupo real: 0
    	Objeto 57 es del grupo 0, Grupo real: 0
    	Objeto 58 es del grupo 0, Grupo real: 0
    	Objeto 59 es del grupo 0, Grupo real: 0
    	Objeto 60 es del grupo 0, Grupo real: 0
    	Objeto 61 es del grupo 0, Grupo real: 0
    	Objeto 62 es del grupo 0, Grupo real: 0
    	Objeto 63 es del grupo 0, Grupo real: 0
    	Objeto 64 es del grupo 1, Grupo real: 0
    	Objeto 65 es del grupo 2, Grupo real: 0
    	Objeto 66 es del grupo 0, Grupo real: 0
    	Objeto 67 es del grupo 0, Grupo real: 0
    	Objeto 68 es del grupo 0, Grupo real: 0
    	Objeto 69 es del grupo 0, Grupo real: 0
    	Objeto 70 es del grupo 0, Grupo real: 0
    	Objeto 71 es del grupo 0, Grupo real: 0
    	Objeto 72 es del grupo 0, Grupo real: 0
    	Objeto 73 es del grupo 1, Grupo real: 0
    	Objeto 74 es del grupo 0, Grupo real: 1
    	Objeto 75 es del grupo 1, Grupo real: 1
    	Objeto 76 es del grupo 1, Grupo real: 1
    	Objeto 77 es del grupo 1, Grupo real: 1
    	Objeto 78 es del grupo 2, Grupo real: 1
    	Objeto 79 es del grupo 1, Grupo real: 1
    	Objeto 80 es del grupo 1, Grupo real: 1
    	Objeto 81 es del grupo 1, Grupo real: 1
    	Objeto 82 es del grupo 1, Grupo real: 1
    	Objeto 83 es del grupo 1, Grupo real: 1
    	Objeto 84 es del grupo 2, Grupo real: 1
    	Objeto 85 es del grupo 0, Grupo real: 1
    	Objeto 86 es del grupo 2, Grupo real: 1
    	Objeto 87 es del grupo 1, Grupo real: 1
    	Objeto 88 es del grupo 1, Grupo real: 1
    	Objeto 89 es del grupo 1, Grupo real: 1
    	Objeto 90 es del grupo 1, Grupo real: 1
    	Objeto 91 es del grupo 1, Grupo real: 1
    	Objeto 92 es del grupo 1, Grupo real: 1
    	Objeto 93 es del grupo 1, Grupo real: 1
    	Objeto 94 es del grupo 1, Grupo real: 1
    	Objeto 95 es del grupo 1, Grupo real: 1
    	Objeto 96 es del grupo 1, Grupo real: 1
    	Objeto 97 es del grupo 1, Grupo real: 1
    	Objeto 98 es del grupo 0, Grupo real: 1
    	Objeto 99 es del grupo 1, Grupo real: 1
    	Objeto 100 es del grupo 1, Grupo real: 1
    	Objeto 101 es del grupo 1, Grupo real: 1
    	Objeto 102 es del grupo 1, Grupo real: 1
    	Objeto 103 es del grupo 1, Grupo real: 1
    	Objeto 104 es del grupo 1, Grupo real: 1
    	Objeto 105 es del grupo 0, Grupo real: 1
    	Objeto 106 es del grupo 1, Grupo real: 1
    	Objeto 107 es del grupo 1, Grupo real: 1
    	Objeto 108 es del grupo 1, Grupo real: 1
    	Objeto 109 es del grupo 1, Grupo real: 1
    	Objeto 110 es del grupo 0, Grupo real: 1
    	Objeto 111 es del grupo 1, Grupo real: 1
    	Objeto 112 es del grupo 1, Grupo real: 1
    	Objeto 113 es del grupo 1, Grupo real: 1
    	Objeto 114 es del grupo 1, Grupo real: 1
    	Objeto 115 es del grupo 1, Grupo real: 1
    	Objeto 116 es del grupo 1, Grupo real: 1
    	Objeto 117 es del grupo 0, Grupo real: 1
    	Objeto 118 es del grupo 1, Grupo real: 1
    	Objeto 119 es del grupo 1, Grupo real: 1
    	Objeto 120 es del grupo 0, Grupo real: 1
    	Objeto 121 es del grupo 1, Grupo real: 1
    	Objeto 122 es del grupo 1, Grupo real: 1
    	Objeto 123 es del grupo 1, Grupo real: 1
    	Objeto 124 es del grupo 1, Grupo real: 1
    	Objeto 125 es del grupo 0, Grupo real: 1
    	Objeto 126 es del grupo 1, Grupo real: 1
    	Objeto 127 es del grupo 1, Grupo real: 1
    	Objeto 128 es del grupo 0, Grupo real: 1
    	Objeto 129 es del grupo 0, Grupo real: 1
    	Objeto 130 es del grupo 1, Grupo real: 1
    	Objeto 131 es del grupo 1, Grupo real: 1
    	Objeto 132 es del grupo 1, Grupo real: 1
    	Objeto 133 es del grupo 1, Grupo real: 1
    	Objeto 134 es del grupo 0, Grupo real: 1
    	Objeto 135 es del grupo 1, Grupo real: 1
    	Objeto 136 es del grupo 0, Grupo real: 1
    	Objeto 137 es del grupo 1, Grupo real: 1
    	Objeto 138 es del grupo 1, Grupo real: 1
    	Objeto 139 es del grupo 1, Grupo real: 1
    	Objeto 140 es del grupo 1, Grupo real: 1
    	Objeto 141 es del grupo 1, Grupo real: 1
    	Objeto 142 es del grupo 0, Grupo real: 1
    	Objeto 143 es del grupo 1, Grupo real: 1
    	Objeto 144 es del grupo 2, Grupo real: 2
    	Objeto 145 es del grupo 2, Grupo real: 2
    	Objeto 146 es del grupo 1, Grupo real: 2
    	Objeto 147 es del grupo 2, Grupo real: 2
    	Objeto 148 es del grupo 0, Grupo real: 2
    	Objeto 149 es del grupo 0, Grupo real: 2
    	Objeto 150 es del grupo 2, Grupo real: 2
    	Objeto 151 es del grupo 1, Grupo real: 2
    	Objeto 152 es del grupo 2, Grupo real: 2
    	Objeto 153 es del grupo 2, Grupo real: 2
    	Objeto 154 es del grupo 1, Grupo real: 2
    	Objeto 155 es del grupo 1, Grupo real: 2
    	Objeto 156 es del grupo 2, Grupo real: 2
    	Objeto 157 es del grupo 2, Grupo real: 2
    	Objeto 158 es del grupo 2, Grupo real: 2
    	Objeto 159 es del grupo 0, Grupo real: 2
    	Objeto 160 es del grupo 2, Grupo real: 2
    	Objeto 161 es del grupo 2, Grupo real: 2
    	Objeto 162 es del grupo 2, Grupo real: 2
    	Objeto 163 es del grupo 0, Grupo real: 2
    	Objeto 164 es del grupo 0, Grupo real: 2
    	Objeto 165 es del grupo 0, Grupo real: 2
    	Objeto 166 es del grupo 2, Grupo real: 2
    	Objeto 167 es del grupo 0, Grupo real: 2
    	Objeto 168 es del grupo 2, Grupo real: 2
    	Objeto 169 es del grupo 0, Grupo real: 2
    	Objeto 170 es del grupo 2, Grupo real: 2
    	Objeto 171 es del grupo 2, Grupo real: 2
    	Objeto 172 es del grupo 2, Grupo real: 2
    	Objeto 173 es del grupo 2, Grupo real: 2
    	Objeto 174 es del grupo 0, Grupo real: 2
    	Objeto 175 es del grupo 2, Grupo real: 2
    	Objeto 176 es del grupo 2, Grupo real: 2
    	Objeto 177 es del grupo 2, Grupo real: 2
    	Objeto 178 es del grupo 2, Grupo real: 2
    	Objeto 179 es del grupo 0, Grupo real: 2
    	Objeto 180 es del grupo 2, Grupo real: 2
    	Objeto 181 es del grupo 2, Grupo real: 2
    	Objeto 182 es del grupo 0, Grupo real: 2
    	Objeto 183 es del grupo 2, Grupo real: 2
    	Objeto 184 es del grupo 2, Grupo real: 2
    	Objeto 185 es del grupo 2, Grupo real: 2
    	Objeto 186 es del grupo 2, Grupo real: 2
    	Objeto 187 es del grupo 2, Grupo real: 2
    	Objeto 188 es del grupo 0, Grupo real: 2
    	Objeto 189 es del grupo 0, Grupo real: 2
    	Objeto 190 es del grupo 2, Grupo real: 2
    	Objeto 191 es del grupo 0, Grupo real: 2
    	Objeto 192 es del grupo 2, Grupo real: 2
    	Objeto 193 es del grupo 0, Grupo real: 2
    	Objeto 194 es del grupo 2, Grupo real: 2
    	Objeto 195 es del grupo 2, Grupo real: 2
    	Objeto 196 es del grupo 2, Grupo real: 2
    	Objeto 197 es del grupo 2, Grupo real: 2
    	Objeto 198 es del grupo 2, Grupo real: 2
    	Objeto 199 es del grupo 2, Grupo real: 2
    	Objeto 200 es del grupo 2, Grupo real: 2
    	Objeto 201 es del grupo 2, Grupo real: 2
    	Objeto 202 es del grupo 2, Grupo real: 2
    	Objeto 203 es del grupo 2, Grupo real: 2
    
    Métricas de rendimiento:
    Accuracy (TP/(n))= 0.7156862745098039
    Precision (TP/(TP+FP)) = 0.7186463502448217
    Recall (TP/(TP+FN)) = 0.7156862745098039
    F1 Score (2*(precision*recall)/(precision+recall)) = 0.7167192663695855

Esta vez se equilibraron más los resultados. Cabe destacar que apliqué un filtro respecto al área mínima que deben tener los contornos para ser considerados como una detección, es posible que ese valor deba ser ajustado dependiendo de la situación.

### Prueba final con la imagen que contiene todos los elementos. 

Por último, haciendo uso del entrenamiento previo, procesé la imagen MPs.JPG para obtener las métricas de los contornos, y hice que el algoritmo k-nearest neighbor predijese los grupos a los que pertenecen dichos contornos. Los resultados fueron los siguientes:

    Se detectaron 5 del Grupo 0, correspondiente a FRA
    Se detectaron 37 del Grupo 1, correspondiente a PEL
    Se detectaron 31 del Grupo 2, correspondiente a TAR

No pude hacer una matriz de confusión de estos resultados por no saber los resultados reales, pero lo más probable es que estén lejos de la realidad. La razón por la que digo esto es la diferencia entre cómo han sido tomadas las fotos utilizadas en el entrenamiento respecto a la usada como prueba final.

![image](https://github.com/user-attachments/assets/fe1b0c09-6683-439c-afa9-223532acdbbe)
*Foto de entrenamiento*

![image](https://github.com/user-attachments/assets/01eb2d94-7ede-4e4e-8b27-52cb5379d193)
*MPs.JPG*

Se pueden apreciar diferencias notables en el brillo, escala y diferencia en el sombreado. La foto MPs.JPG fue tomada de forma muy diferente.

Para acabar, mostré en una ventana nueva las detecciones realizadas, lo hice de dos formas:

La primera fue mostrar en una ventana nueva la imagen en la que cada contorno tiene su respectiva etiqueta.

![image](https://github.com/user-attachments/assets/38415b88-f8a1-4460-a966-a5297c9cfa72)

La segunda se diferencia en que hay que hacer click en el objeto para que salga su etiqueta.

![image](https://github.com/user-attachments/assets/05b563bd-1480-4baf-846e-05a3942db95a)


# Referencias

https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

https://docs.opencv.org/4.x/d7/dd0/tutorial_js_thresholding.html

