***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

El archivo "Tareas_VC_P1_Alejandro_Rodriguez_Mesa.ipynb" contiene todas las tareas solicitadas en un único cuaderno. 
Mientras que la carpeta "Tareas_por_separado" tiene varios cuadernos. Cada cuaderno contiene una o en algunos casos, dos de las tareas. 

- # Paquetes necesarios
Para realizar estas tareas, se utilizan las siguientes librerías:
  OpenCV (cv2): Para la manipulación de imágenes y visualización en ventanas independientes.
  NumPy: Para manejar y operar matrices de píxeles.
  Matplotlib: Para la visualización de imágenes dentro del entorno de Python.

- # Tarea 1: Creación de un Tablero de Ajedrez de 600x600 píxeles
El objetivo de esta tarea fue generar una imagen de un tablero de ajedrez de 600x600 píxeles, alternando celdas blancas y negras. El tablero se compone de una cuadrícula de 8x8 celdas.

- ## Procedimiento
  Inicialización de la imagen: Se creó una imagen en escala de grises donde cada píxel tiene inicialmente el valor correspondiente a negro.

  Generación del patrón del tablero: Utilizando un bucle, se recorrieron las posiciones de las celdas para identificar cuáles debían ser blancas y cuáles negras. Este patrón alternado se aplicó a cada fila y columna de la imagen.

  Visualización: Una vez generado el tablero, se visualizó tanto con Matplotlib (dentro de un entorno de desarrollo) como con OpenCV (en una ventana independiente).

- # Tarea 2: Creación de una Imagen Estilo Mondrian (Método 1)
Esta tarea consistió en crear una imagen de estilo Mondrian de 800x800 píxeles utilizando rectángulos de colores primarios (rojo, azul, amarillo), blanco y negro. Mondrian es conocido por sus composiciones geométricas abstractas con bloques de colores separados por líneas negras.

- ## Procedimiento
  Definición de los rectángulos: Se crearon varios rectángulos de diferentes tamaños, cada uno con un color específico (rojo, azul, amarillo, blanco, negro).

  Posicionamiento de los rectángulos: Los rectángulos fueron distribuidos de manera ordenada en distintas posiciones de la imagen.

  Creación del fondo y aplicación de rectángulos: Primero se aplicó un fondo negro sobre toda la imagen. Luego, los rectángulos se colocaron en sus posiciones respectivas, simulando una composición al estilo de Mondrian.

  Visualización: La imagen final se mostró usando Matplotlib, permitiendo apreciar el resultado.

- # Tarea 3: Creación de una Imagen Estilo Mondrian (Método 2 - con OpenCV)
En esta tarea, se utilizó OpenCV para recrear la imagen de estilo Mondrian. En lugar de trabajar con clases y posiciones predefinidas como en el método anterior, aquí se emplearon funciones de dibujo de OpenCV para generar líneas y rellenar áreas con colores.

- ## Procedimiento
  Dibujo de líneas: Se trazaron líneas negras horizontales y verticales en la imagen, formando una cuadrícula similar a las composiciones de Mondrian.

  Coloreado de las áreas: Después de crear las líneas, se utilizó una técnica llamada "flood fill" para rellenar las áreas delimitadas por las líneas con colores primarios como rojo, azul y amarillo, además de blanco.

  Visualización: La imagen resultante se mostró utilizando tanto Matplotlib como OpenCV, permitiendo ver la imagen con las líneas y los bloques de color en detalle.
  
- # Tarea 4: Modificar de forma libre los valores de un plano de la imagen
En esta tarea, separamos los tres planos (canales de color: rojo, verde y azul) de la imagen capturada por la webcam, y aplicamos modificaciones al verde y al azul, manteniendo el rojo sin modificar. 

- ## Procedimiento
  Captura de imagen: Se capturó una imagen utilizando la webcam.
  
  Separación de canales: La imagen capturada se dividió en sus tres canales de color: rojo (R), verde (G) y azul (B).
  
  Modificaciones:

    - Se invirtió el canal azul (B).
  
    - Se aplicó un desenfoque al canal verde (G).
  
  Anotación: Se añadió texto descriptivo a cada plano para indicar las modificaciones realizadas.
  
  Unión de canales: Los tres canales (R, G, B) se combinaron nuevamente para formar una sola imagen.
  
  Visualización: La imagen resultante fue mostrada. Si se presionó la tecla "ESC", se terminó la ejecución.

- # Tarea 5: Pintar círculos en las posiciones del píxel más claro y oscuro de la imagen
En esta tarea, se encuentra el píxel más claro y el más oscuro en cada cuadro de video capturado, y se dibujan círculos sobre ellos.
- ## Procedimiento
  Captura de video: Se capturó un cuadro de video.
  
  Conversión a escala de grises: El cuadro capturado se convirtió a una imagen en escala de grises para facilitar la detección de brillo.
  
  Detección de píxeles extremos: Usando la función cv.minMaxLoc, se localizaron los píxeles con los valores más claros y más oscuros.
  
  Dibujo de círculos: Se dibujó un círculo verde sobre el píxel más claro y un círculo azul sobre el píxel más oscuro.
  
  Anotación: Se mostraron las coordenadas de ambos píxeles en la imagen.
  
  Visualización: La imagen con los círculos y coordenadas fue mostrada. Si se presionó la tecla "ESC", se finalizó la ejecución.
  
- # Tarea 6: Pintar las zonas 8x8 más claras y más oscuras
En esta tarea, se buscan las regiones de 8x8 píxeles más claras y más oscuras dentro de la imagen y se resaltan dibujando un rectángulo sobre ellas.
- ## Procedimiento
  Captura de video: Se capturó un cuadro de video.
  
  Conversión a escala de grises: El cuadro se convirtió a una imagen en escala de grises.
  
  Búsqueda de regiones: Se utilizaron dos bucles anidados para recorrer todas las posibles regiones de 8x8 píxeles dentro del cuadro.
  
    -En cada región, se calculó el brillo promedio.
  
    -Se guardaron las coordenadas de la región con el brillo promedio más alto (más clara) y más bajo (más oscura).
  
  Dibujo de rectángulos: Se dibujó un rectángulo verde alrededor de la región más clara y un rectángulo azul en la región más oscura.
  
  Anotación: Se añadió texto indicando las regiones más claras y más oscuras.
  
  Visualización: La imagen con los rectángulos y anotaciones fue mostrada. Si se presionó la tecla "ESC", se finalizó la ejecución.
  
- # Tarea 7: Pop Art
 En esta tarea se desarrollaron tres variaciones de efectos de Pop Art aplicados en tiempo real sobre el video capturado por una webcam. Cada variación presenta un estilo diferente: uno basado en una malla de triángulos, otro en una disposición de círculos, y un último usando contornos de líneas.

- ## Procedimiento General
Captura de video: En cada uno de los efectos, se inicializa la captura de video utilizando la webcam.
Procesamiento del fotograma: Dependiendo del efecto seleccionado (triángulos, círculos o líneas), el fotograma capturado es procesado utilizando diferentes técnicas de segmentación y dibujo.

Visualización: Se muestra el resultado en tiempo real, permitiendo ver la transformación en la imagen capturada. Si se presiona la tecla 'ESC', el programa termina.

- ### Efecto 1: Pop Art de Triángulos
Este efecto divide el fotograma en una malla de triángulos, y cada triángulo se rellena con el color promedio de la región que cubre.

  **Procedimiento:**
  
  Se dibuja una malla de triángulos sobre el fotograma, dividiendo la imagen en celdas de tamaño especificado.

  Para cada triángulo, se calcula el color promedio de la región que ocupa en la imagen original.

  Los triángulos son coloreados con los colores promedio calculados.

  La imagen resultante, con el efecto de triángulos, se muestra en una ventana.

Tuve que disminuir el número de triángulos debido a que tenía un coste computacional muy alto el tener demasiados triángulos, lo que hacía que la imagen no se viese a tiempo real.

- ### Efecto 2: Pop Art de Círculos
En este efecto, el fotograma se segmenta en una malla de círculos, y cada círculo se rellena con el color promedio de la región que cubre.

  **Procedimiento:**
  
  Se dibuja una malla de círculos centrados en puntos definidos por una segmentación regular de la imagen.
      
  Para cada círculo, se calcula el color promedio de la región que abarca.
      
  Cada círculo es rellenado con su color promedio correspondiente.
  
  El fotograma con el efecto de círculos se muestra en tiempo real en una ventana.

- ### Efecto 3: Pop Art de Líneas
Este efecto utiliza el detector de bordes de Canny para resaltar los contornos en el fotograma y luego aplica un mapa de colores para generar un estilo artístico tipo Pop Art basado en líneas.

  **Procedimiento:**

Se convierte el fotograma capturado a escala de grises.

Se aplican técnicas de detección de bordes usando el método de Canny.

Los bordes detectados se colorean utilizando un mapa de colores para crear un efecto vibrante de estilo Pop Art.

La imagen con los contornos coloreados se muestra en una ventana en tiempo real. 

- # Extras de Prueba
Estos son ejemplos de efectos adicionales que exploré mientras investigaba diferentes técnicas de procesamiento de imágenes y la creación de estilos visuales únicos. Aunque no eran parte de mi proyecto principal de Pop Art, me parecieron interesantes y útiles para seguir experimentando con nuevas formas de transformar las imágenes en tiempo real.

1. Detección de Movimiento
   
Este efecto utiliza diferencias en la intensidad de los píxeles entre fotogramas consecutivos para detectar cambios en la imagen. Se analiza el cambio promedio dentro de pequeñas celdas (8x8 píxeles) y las áreas con mayor variación se destacan, lo que permite visualizar el movimiento en tiempo real.

2. Detección de Caras
   
Aquí, un clasificador en cascada detecta rostros en el fotograma de video. Cada rostro detectado se enmarca con un rectángulo, lo que permite identificar fácilmente a las personas en la imagen.

3. Efecto Desenfoque de la Cara
   
Similar al efecto de detección de caras, pero en lugar de marcar los rostros, se aplica un desenfoque (filtro Gaussiano) a las áreas detectadas como caras, ocultándolas parcialmente. Este efecto podría ser útil para situaciones en las que se quiere preservar la privacidad de los individuos.

4. Combinación de Detección de Movimiento + Rostros + Mapas de Color
   
Este efecto es una combinación de varios elementos que había utilizado:

  Detección de rostros para modificar su apariencia mediante bordes detectados con el algoritmo de Canny.
  
  Detección de movimiento para destacar áreas en la imagen que cambian entre fotogramas.
  
  Aplicación de mapas de color para dar un estilo visual tipo "pop art" a diferentes secciones de la imagen.
  
  La imagen se divide en celdas, y las diferencias entre fotogramas consecutivos resaltan áreas de movimiento, excepto en las regiones de los rostros, donde se aplica un efecto de contornos de líneas.

Estos efectos adicionales me permitieron explorar cómo interactúan el reconocimiento de patrones y los filtros visuales, todo en tiempo real. Aunque no encajaban demasiado con la estética de lo que imagino como pop art, me ayudaron a entender mejor el procesamiento de imágenes y su potencial para crear efectos artísticos.
