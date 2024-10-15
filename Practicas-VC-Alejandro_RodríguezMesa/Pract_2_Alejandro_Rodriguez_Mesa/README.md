***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

# Enviroment en Anaconda
  La versión de python utilizada es la 3.11.5, se debe instalar opencv-python y matplotlib.
  
# Paquetes necesarios
Para realizar estas tareas, se utilizan las siguientes librerías:
  OpenCV: Para la manipulación de imágenes y visualización en ventanas independientes.
  NumPy: Para manejar y operar matrices de píxeles.
  Matplotlib: Para la visualización de imágenes dentro del entorno de Python.


# Tarea 1: Detección de Contornos y Conteo de Píxeles Blancos con Canny
  El objetivo de esta tarea fue aplicar el operador de **Canny** para detectar los contornos de una imagen, y luego contar los píxeles blancos obtenidos por fila y columna. Además, se determinó el máximo número de píxeles blancos en las filas y se identificaron las filas con al menos el 95% de ese valor máximo.

  ## Procedimiento
  - **Carga de la imagen**: La imagen `mandril.jpg` fue cargada utilizando OpenCV, convertida de BGR a RGB para visualización correcta, y posteriormente convertida a escala de grises para el procesamiento posterior.
  
  - **Aplicación del filtro Canny**: Utilizando el método `cv.Canny`, se detectaron los bordes en la imagen en escala de grises. Se establecieron dos umbrales (100 y 200) para detectar los contornos más significativos.

  - **Conteo de píxeles blancos**: Se utilizó la función `cv.reduce` para contar el número de píxeles blancos (valor 255) por fila y por columna. Posteriormente, estos valores fueron normalizados para obtener proporciones en relación al tamaño de la imagen.

  - **Cálculo del máximo y umbral**: Se determinó el número máximo de píxeles blancos en las filas y se calculó un umbral del 95% de este valor. Luego, se contó cuántas filas superaban este umbral, lo que permite analizar la concentración de bordes en ciertas áreas de la imagen.

  - **Visualización de resultados**: Los resultados fueron presentados gráficamente, mostrando los contornos detectados y la distribución de píxeles blancos por filas y columnas.
    
  ## Resultados
  
  ![image](https://github.com/user-attachments/assets/88f4691d-cd7d-4a31-b8dc-74f399b9126c)
  
  Porcentaje de píxeles blancos por columna: 0.365234375
  Porcentaje de píxeles blancos por fila: 0.4296875
  Número de filas con píxeles blancos >= 0.95 * máximo de filas: 2

# Tarea 2: Umbralización y Conteo de Píxeles con Sobel
  En esta tarea se aplicó el filtro **Sobel** para detectar los cambios de intensidad en la imagen, seguido de una operación de umbralización. El objetivo era contar los píxeles blancos resultantes por fila y columna y compararlos con los obtenidos mediante el operador Canny.

  ## Procedimiento
  - **Aplicación del filtro Sobel**: Se utilizó el filtro Sobel para calcular las derivadas de la imagen en las direcciones horizontal y vertical. Luego, se combinó el resultado de ambos ejes para obtener una imagen que resalta los bordes detectados.

  - **Umbralización**: La imagen resultante del filtro Sobel fue convertida a 8 bits, y luego se aplicó un umbral para binarizar la imagen, es decir, marcar los píxeles como blanco (255) o negro (0) según su valor.

  - **Conteo de píxeles no nulos**: Al igual que en la tarea anterior, se contó el número de píxeles blancos por fila y por columna, normalizando los resultados. Se calculó el valor máximo de píxeles blancos tanto por filas como por columnas y se identificaron las filas y columnas con al menos el 95% del valor máximo.

  - **Comparación con Canny**: Se comparó la distribución de píxeles blancos en los bordes detectados por Sobel con los detectados por Canny. Se generaron gráficos de la distribución de píxeles blancos por filas y columnas para facilitar esta comparación.

  - **Visualización de resultados**: Se generaron gráficos para visualizar la distribución de píxeles blancos y los resultados de la umbralización aplicada a la imagen filtrada con Sobel.
    
  ## Resultados

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

  # Comparación de Resultados entre Canny y Sobel:
  ## Teoría
  ### Similitudes:
  - Ambos detectan bordes resaltando cambios abruptos de intensidad en la imagen.
    
  - Se basan en el cálculo de gradientes de intensidad en direcciones x e y.
  
  - Pueden beneficiarse de un suavizado previo (como un filtro gaussiano) para reducir el ruido.

### Diferencias:
  - **Sobel**: Más simple y rápido, calcula derivadas discretas en x e y, adecuado para bordes básicos pero más sensible al ruido.
  
  - **Canny**: Más avanzado, incluye suavizado, doble umbralización y supresión de no máximos, lo que resulta en bordes más refinados y menos sensibles al ruido.
  ## Caso de uso de la práctica
  - En el caso del *Canny*, apliqué umbrales de 100 y 200, obteniendo una detección de bordes muy fina, con pocos píxeles blancos por fila y columna, especialmente concentrados en ciertas áreas. Solo 2 filas superaron el 95% del máximo de píxeles blancos, indicando que los bordes detectados estaban más distribuidos.
  
  - En la tarea con *Sobel*, al utilizar umbrales más bajos (como 1), los bordes detectados fueron mucho más numerosos, resultando en prácticamente todas las filas y columnas con más del 95% de píxeles blancos. Con un umbral de 200, los resultados fueron más parecidos a los obtenidos con Canny, aunque con bordes más gruesos y menos definidos.

# Tarea 3:
El objetivo de esta tarea es crear un demostrador que capture imágenes en tiempo real desde la cámara web y permita mostrar diversas técnicas de procesamiento de imágenes utilizando las funciones de OpenCV aplicadas previamente.

He implementado un total de 6 modos, que se activan presionando diferentes teclas:

- **O: Modo original, muestra la imagen tal cual es capturada desde la cámara.**

- **L: Detección de bordes utilizando el operador Canny.**

- **G: Conversión de la imagen a escala de grises.**

- **U: Umbralización de la imagen, donde el valor del umbral se ajusta con el trackbar.**

- **S: Suavizado Gaussiano para aplicar desenfoque a la imagen.**

- **H: Modo de ayuda que muestra instrucciones sobre cómo utilizar el demostrador.**

El teclado detectará las pulsaciones de teclado para saber qué modo de visualización debe de mostrar.

  ## Procedimiento

- Configuración de la cámara: Se inició la captura de video en tiempo real desde la cámara web utilizando cv2.VideoCapture. Esto permite obtener cuadros de imagen continuamente, que son procesados de acuerdo con el modo seleccionado por el usuario.
  
- Controles interactivos (trackbars): Se crearon dos barras deslizantes (trackbars) para ajustar dinámicamente:
  
  - El valor del umbral (r) para las operaciones que manejen un umbral.
    
  - El valor del brillo de la imagen.
    
- Modo Inicial:
  
  ![image](https://github.com/user-attachments/assets/d9fb23d8-0184-4a88-b727-d209373531fc)

- En este modo el umbral no hace nada, ya que no tiene nada que hacer con el umbral. Solo le afecta el brillo. Abajo a la izquierda sale un mensaje para activar el modo ayuda, este mensaje no está en ningún otro modo. 
    
- Procesamiento de la imagen: Dependiendo del modo seleccionado, se realizaron las siguientes operaciones:
  
  - Ajuste de brillo: Se ajustó el brillo de la imagen con cv2.convertScaleAbs, permitiendo al usuario aclarar u oscurecer la imagen.
    
  - Brillo Alto:
    
    ![image](https://github.com/user-attachments/assets/7b91f55d-dea6-4726-86e2-cd4db8073ca2)
 
  - Brillo Bajo:
 
    ![image](https://github.com/user-attachments/assets/18bfc057-fdc1-4f4d-a9cd-d296ca9d6b3e)

  - Aunque puse imágenes con brillo solo del modo original, **el brillo se aplica a todos los modos**.
  
  - Detección de bordes: Se aplicó suavizado Gaussiano y luego el operador de Canny para detectar los bordes en la imagen. Los bordes detectados fueron sumados en ambas direcciones (x e y) para obtener el contorno total.
 
  - Umbral Alto, no se detectan todos los contornos, pero tampoco hay ruido:
 
    ![image](https://github.com/user-attachments/assets/70d6ef4e-522c-43f4-8ff1-01250a4032e3)
 
  - Umbral Bajo, a costa de más ruido se ven más lineas:
 
    ![image](https://github.com/user-attachments/assets/5b8820b7-8a6b-4954-b7bc-bdab579fd46a)

  - Umbral cercano al medio:
 
    ![image](https://github.com/user-attachments/assets/ce6f2e2b-63dd-434c-95af-50483de8b417)

  - Escala de grises: Se transformó la imagen a escala de grises usando cv2.cvtColor.
 
    ![image](https://github.com/user-attachments/assets/6913207a-423c-40c3-8e5a-7923312ce03d)
 
  - El umbralizador **no** se usa en este modo.

  - Umbralización: La imagen en escala de grises se umbralizó utilizando un valor ajustable en el trackbar.
 
    ![image](https://github.com/user-attachments/assets/df6e6d7d-e090-42e6-8f07-9d22d0d90fab)

  - Suavizado Gaussiano: Se aplicó un desenfoque Gaussiano a la imagen ajustando el tamaño del kernel según el valor del trackbar.
 
  - Umbral alto:
  
    ![image](https://github.com/user-attachments/assets/c4f477d7-5a0b-4fb5-8684-44f45b4a9858)
 
  - Umbral bajo:
 
    ![image](https://github.com/user-attachments/assets/a819363e-0a2d-4538-a364-1213ff015137)

- Menú de instrucciones: Al presionar la tecla H, se visualiza un menú de ayuda para el manejo del programa. Este modo de visualización tiene una imagen de fondo que fue previamente escalada y se procesó para detectar border, de tal manera que se vea con lineas los contornos. Y añadí a la imagen el texto explicativo.

  ![image](https://github.com/user-attachments/assets/8fe291bf-df71-4706-bd72-ed9150939ce4)

# Tarea 4: Videojuego de Colisión de Pelotas inspirado en "Messa di Voce"
Este videojuego se inspiró en la parte final de la interpretación del video "Messa di Voce", donde las pelotas que caen colisionan con el actor. Esta imagen generó la idea de hacer algo similar, pero en lugar de ser una actuación, se diseñó como un videojuego. El objetivo es evitar que una pelota caiga al suelo usando el cuerpo como un obstáculo, capturado por la cámara. Se recomienda tener una pared plana de fondo y ropa de un color distinto al de la pared para una mejor detección de los contornos.
El juego tiene como reglas que, una vez el jugador recibe 20 goles, pierde la partida. El desafío es tratar de superar el récord mundial previamente establecido por mi, que soy el único que ha jugado.

## Procedimiento
 Captura de Video:
Se utiliza la cámara web para capturar el fondo y el jugador. Se recomienda que el entorno tenga un fondo plano y colores contrastantes para facilitar la detección de los contornos.

- Clase Ball:
  
- Se definió una clase que representa las pelotas, con características como el radio, la posición (x, y) y la velocidad en los ejes X e Y. Las pelotas se mueven de manera aleatoria, y el jugador debe evitar que lleguen al borde inferior de la pantalla.

- Detección de Contornos:
  
- Se aplicó un efecto de línea utilizando la función cv.Canny() para detectar los bordes del jugador y de los objetos que se encuentren en la escena. Esto permite que las pelotas reboten al colisionar con los contornos detectados.
  
- Colisión de Pelotas:

- Las pelotas se mueven de forma aleatoria y rebotan al colisionar con el jugador (detectado mediante contornos) o con los bordes de la pantalla. Cada vez que una pelota toca el borde inferior de la pantalla, se considera un "gol", y cuando el jugador recibe 20 goles, el juego termina. Cabe destacar que las pelotas despues de haber colisionado con el borde inferior, ignorarán cualquier colisión hasta que vuelvan a rebotar con el borde superior, durante este transcurso, la velocidad de la pelota aumenta.

- Aumento de la Dificultad:

- La velocidad de las pelotas se incrementa cada vez que una toca el borde inferior, lo que aumenta la dificultad progresivamente.

- Game Over:

- Al alcanzar 20 goles, se muestra una pantalla de "Game Over" con un fondo rojo, indicando el tiempo transcurrido y el número total de goles.

## Libreria y funciones principales:
Se utilizó OpenCV para la captura de video, el procesamiento de imágenes y la detección de colisiones.

La implementación del efecto de línea y los contornos se hizo con las funciones cv.GaussianBlur() y cv.Canny() para resaltar las áreas de interés.

## Instrucciones de Uso:
- Objetivo: Mover el cuerpo para evitar que las pelotas toquen el borde inferior de la pantalla.
  
- Recomendaciones: Utilizar una pared plana como fondo y ropa de color contrastante con el entorno para optimizar la detección de contornos.

- Aviso: Obstáculos que no sean el jugador podrían interferir negativamente con la experiencia de juego.

- Fin del Juego: El juego termina cuando recibes 20 goles, y se te mostrará el tiempo que lograste resistir. ¡Buena suerte!

## Imágenes del juego

- Sale un marcador de goles recibidos y tiempo a la izquierda, mientras que al recibir un gol el borde se pone rojo.

  ![image](https://github.com/user-attachments/assets/0c3f6f7b-e6a5-4612-8273-380f5b191b05)

- Una vez te han sobrepasado 20 pelotas:
  
  ![image](https://github.com/user-attachments/assets/a25ad844-fe43-47c4-9fc7-1e14a47e58c2)


# Referencias
- **Repositorio de Github de "otsedom":** https://github.com/otsedom/otsedom.github.io/tree/main/VC

- **Página web de openCV:** https://docs.opencv.org/4.x/

- **Jaap Blonk performance - installation Messa di Voce:** https://www.youtube.com/watch?v=GfoqiyB1ndE
