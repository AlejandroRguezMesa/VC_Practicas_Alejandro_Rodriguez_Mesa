***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

- # Enviroment
  La versión de python utilizada es la 3.11.5, se debe instalar opencv-python y matplotlib.
  
- # Paquetes necesarios
Para realizar estas tareas, se utilizan las siguientes librerías:
  OpenCV (cv2): Para la manipulación de imágenes y visualización en ventanas independientes.
  NumPy: Para manejar y operar matrices de píxeles.
  Matplotlib: Para la visualización de imágenes dentro del entorno de Python.

- # Tarea 1:
- # Tarea 1: Detección de Contornos y Conteo de Píxeles Blancos con Canny
  El objetivo de esta tarea fue aplicar el operador de **Canny** para detectar los contornos de una imagen, y luego contar los píxeles blancos obtenidos por fila y columna. Además, se determinó el máximo número de píxeles blancos en las filas y se identificaron las filas con al menos el 95% de ese valor máximo.

- ## Procedimiento
  - **Carga de la imagen**: La imagen `mandril.jpg` fue cargada utilizando OpenCV, convertida de BGR a RGB para visualización correcta, y posteriormente convertida a escala de grises para el procesamiento posterior.
  
  - **Aplicación del filtro Canny**: Utilizando el método `cv.Canny`, se detectaron los bordes en la imagen en escala de grises. Se establecieron dos umbrales (100 y 200) para detectar los contornos más significativos.

  - **Conteo de píxeles blancos**: Se utilizó la función `cv.reduce` para contar el número de píxeles blancos (valor 255) por fila y por columna. Posteriormente, estos valores fueron normalizados para obtener proporciones en relación al tamaño de la imagen.

  - **Cálculo del máximo y umbral**: Se determinó el número máximo de píxeles blancos en las filas y se calculó un umbral del 95% de este valor. Luego, se contó cuántas filas superaban este umbral, lo que permite analizar la concentración de bordes en ciertas áreas de la imagen.

  - **Visualización de resultados**: Los resultados fueron presentados gráficamente, mostrando los contornos detectados y la distribución de píxeles blancos por filas y columnas.
    
- ## Resultados
  
  ![image](https://github.com/user-attachments/assets/88f4691d-cd7d-4a31-b8dc-74f399b9126c)
  
  Porcentaje de píxeles blancos por columna: 0.365234375
  Porcentaje de píxeles blancos por fila: 0.4296875
  Número de filas con píxeles blancos >= 0.95 * máximo de filas: 2


)


---

- # Tarea 2: Umbralización y Conteo de Píxeles con Sobel
  En esta tarea se aplicó el filtro **Sobel** para detectar los cambios de intensidad en la imagen, seguido de una operación de umbralización. El objetivo era contar los píxeles blancos resultantes por fila y columna y compararlos con los obtenidos mediante el operador Canny.

- ## Procedimiento
  - **Aplicación del filtro Sobel**: Se utilizó el filtro Sobel para calcular las derivadas de la imagen en las direcciones horizontal y vertical. Luego, se combinó el resultado de ambos ejes para obtener una imagen que resalta los bordes detectados.

  - **Umbralización**: La imagen resultante del filtro Sobel fue convertida a 8 bits, y luego se aplicó un umbral para binarizar la imagen, es decir, marcar los píxeles como blanco (255) o negro (0) según su valor.

  - **Conteo de píxeles no nulos**: Al igual que en la tarea anterior, se contó el número de píxeles blancos por fila y por columna, normalizando los resultados. Se calculó el valor máximo de píxeles blancos tanto por filas como por columnas y se identificaron las filas y columnas con al menos el 95% del valor máximo.

  - **Comparación con Canny**: Se comparó la distribución de píxeles blancos en los bordes detectados por Sobel con los detectados por Canny. Se generaron gráficos de la distribución de píxeles blancos por filas y columnas para facilitar esta comparación.

  - **Visualización de resultados**: Se generaron gráficos para visualizar la distribución de píxeles blancos y los resultados de la umbralización aplicada a la imagen filtrada con Sobel.
    
- ## Resultados

- Con un umbralizado muy bajo, en este caso 1. Prácticamente todos los pixeles serán blancos.

  ![image](https://github.com/user-attachments/assets/d67c5f32-a463-4fa3-bddd-68f4ee29766f)

  ![image](https://github.com/user-attachments/assets/ff98c403-4584-401c-83fe-fc98782d9c28)


- Porcentaje de píxeles blancos por columna: 1.0

- Porcentaje de píxeles blancos por fila: 0.998046875

- Número de filas más de un 95% de píxeles blancos: 506

- Número de columnas con más de un 95% de píxeles blancos: 500

- Con un umbralizado de 100:

  ![image](https://github.com/user-attachments/assets/dd57b30b-7c7d-4daf-aeb5-df7123d91b08)

  ![image](https://github.com/user-attachments/assets/1e96af87-2e39-46f3-a989-cc8e36bf4f1a)

  
- Porcentaje de píxeles blancos por columna: 0.921875

- Porcentaje de píxeles blancos por fila: 0.931640625

- Número de filas más de un 95% de píxeles blancos: 63

- Número de columnas con más de un 95% de píxeles blancos: 117

- Con un umbralizado de 200:

  ![image](https://github.com/user-attachments/assets/ba12a0a4-706d-4a86-926e-fd902bc3fe14)

  ![image](https://github.com/user-attachments/assets/2080843a-a8fa-4a22-99b3-fac369160884)


- Porcentaje de píxeles blancos por columna: 0.546875

- Porcentaje de píxeles blancos por fila: 0.5

- Número de filas más de un 95% de píxeles blancos: 2

- Número de columnas con más de un 95% de píxeles blancos: 2

- # Comparación de Resultados entre Canny y Sobel:
- ## Teoría
- ### Similitudes:
  - Ambos detectan bordes resaltando cambios abruptos de intensidad en la imagen.
    
  - Se basan en el cálculo de gradientes de intensidad en direcciones x e y.
  
  - Pueden beneficiarse de un suavizado previo (como un filtro gaussiano) para reducir el ruido.
    
- ### Diferencias:
  - **Sobel**: Más simple y rápido, calcula derivadas discretas en x e y, adecuado para bordes básicos pero más sensible al ruido.
  
  - **Canny**: Más avanzado, incluye suavizado, doble umbralización y supresión de no máximos, lo que resulta en bordes más refinados y menos sensibles al ruido.
- ## Caso de uso de la práctica
  - En el caso del *Canny*, apliqué umbrales de 100 y 200, obteniendo una detección de bordes muy fina, con pocos píxeles blancos por fila y columna, especialmente concentrados en ciertas áreas. Solo 2 filas superaron el 95% del máximo de píxeles blancos, indicando que los bordes detectados estaban más distribuidos.
  
  - En la tarea con *Sobel*, al utilizar umbrales más bajos (como 1), los bordes detectados fueron mucho más numerosos, resultando en prácticamente todas las filas y columnas con más del 95% de píxeles blancos. Con un umbral de 200, los resultados fueron más parecidos a los obtenidos con Canny, aunque con bordes más gruesos y menos definidos.

- # Tarea 3:
- # Tarea 4:
