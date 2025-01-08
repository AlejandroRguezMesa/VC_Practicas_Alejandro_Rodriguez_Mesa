***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

# Trabajo Final de la asignatura
En el readme no entraré demasiado en detalles debido a la memoria que realicé, será para facilitar capturas de la aplicación por si alguien que encuentra el repositorio está interesado en replicarlo. Además de mencionar cómo montar el enviroment de Anaconda.
## Memoria

## Instalación y enviroment en Anaconda
### Para los entrenamientos con YOLO lo mejor es utilizar la GPU mediante CUDA

### CUDA
Para instalarlo es necesario saber qué versión es compatible con tu gráfica, para ello haz lo siguiente en el cmd:
![image](https://github.com/user-attachments/assets/9e9c030e-a947-4567-865b-70c5270693d3)

Una vez sabes la versión de Cuda que necesitas, basta con instalarla en la web oficial, [CUDA Version 12.6](https://developer.nvidia.com/cuda-downloads).

Tras esto instalé el [cuDNN](https://developer.nvidia.com/cudnn-downloads).

Para el pytorch instalé la última versión disponible, que funciona correctamente para las versiones más recientes de CUDA. 
![image](https://github.com/user-attachments/assets/1390642d-39a8-4431-9f3b-ed84b6a969d1)


```
conda create --name VC_Pract_Final python=3.11.5
conda activate VC_Pract_Final
pip install opencv-python
pip install matplotlib
pip install imutils
pip install pygame
pip install mediapipe
pip install tk
pip install ultralytics
pip install lapx
pip install dlib
pip install deepface
```
La instalación de delib probablemente fallará, para instalarlo lo mejor es seguir los pasos de este [video](https://www.youtube.com/watch?v=9zeb902f98s&ab_channel=BoomBoomMushroom), en el que se explica que hay que instalar un archivo de este [github](https://github.com/Murtaza-Saeed/dlib) y hacer un pip install del archivo. **Esta librería es opcional, ya que no es usada para el código final** 

Se usan otras librerías como json o shutil que son parte de las librerías estandar de python, tal como se puede ver en la siguiente [lista](https://docs.python.org/3.10/library/).

# Resultados del entrenamiento
Tras hacer los entrenamientos, tal y como se ve en el [cuaderno](https://github.com/AlejandroRguezMesa/VC_Practicas_Alejandro_Rodriguez_Mesa/blob/main/Practicas-VC-Alejandro_Rodr%C3%ADguezMesa/Pract_6_Alejandro_Rodriguez_Mesa/biometric.ipynb) 

## Spoofing
![image](https://github.com/user-attachments/assets/60ee4562-4ff2-4ae2-8632-a93bbc25ec48)
Según la matriz de confusión, se detectan bastante bien los casos de spòofing. Aunque he detectado que tiende a detectar Device, ya que en ocasiones detecta esta clase cuando corresponde a otro tipo de spoofing. Esto puede deberse al desbalanceo de clases que hay. Podría haber eliminado imágenes para equilibrar, pero como me interesaba simplemente detectar spoofing, y no el tipo, me sirvió para este caso de uso. 

![image](https://github.com/user-attachments/assets/700aa441-ee27-4f1c-bb51-5098b601cab6)

En base en los gráficos mostrados:

**Pérdidas de entrenamiento (train/box_loss, train/cls_loss, train/dfl_loss):**

- Todas las curvas de pérdidas disminuyen progresivamente con el tiempo, lo que indica que el modelo está aprendiendo durante el entrenamiento.

**Pérdidas de validación (val/box_loss, val/cls_loss, val/dfl_loss):**

- Las pérdidas de validación también disminuyen de manera consistente, lo que sugiere que no hay un sobreajuste significativo.

**Métricas de precisión y recall (metrics/precision(B), metrics/recall(B)):**

- Ambas métricas aumentan progresivamente y se estabilizan cerca de valores altos (>0.9), lo que es una señal positiva de un modelo bien entrenado.

**Métricas de mAP (metrics/mAP50(B), metrics/mAP50-95(B)):**

- Estas métricas también mejoran consistentemente y alcanzan valores altos (>0.8), lo que indica que el modelo tiene un buen desempeño en las tareas de detección de objetos.
En general, este entrenamiento parece haber sido exitoso, ya que las pérdidas disminuyen de forma consistente y las métricas de desempeño son altas. Esto sugiere que el modelo está bien ajustado y logra un equilibrio entre entrenamiento y validación sin señales de sobreajuste o bajoajuste.

## Gafas y Máscaras o Mascarillas
![image](https://github.com/user-attachments/assets/a8d0d57b-5daa-4af7-88c6-6f82600d89d4)
Vuelve a haber desbalanceo respecto a mask y no mask, aunque no es demasiado grande. Al final los modelos no eran los más acertados en este campo, y a esto se le añade que tuve que eliminar imágenes por malas anotaciones, el desbalanceo en las gafas no afecta en este caso. 

![image](https://github.com/user-attachments/assets/40654bde-5615-445d-8930-82454fbd3061)

**Pérdidas de entrenamiento (train/box_loss, train/cls_loss, train/dfl_loss):**

- Las pérdidas de entrenamiento disminuyen de manera consistente, lo que indica que el modelo está aprendiendo correctamente.

**Pérdidas de validación (val/box_loss, val/cls_loss, val/dfl_loss):**

- Las pérdidas de validación también muestran una tendencia decreciente, aunque parecen estabilizarse en valores ligeramente más altos que las pérdidas de entrenamiento. Esto podría ser un indicio de una ligera diferencia entre el rendimiento en entrenamiento y validación, pero sigue siendo aceptable.

**Métricas de precisión y recall (metrics/precision(B), metrics/recall(B)):**

- Tanto la precisión como el recall muestran una mejora progresiva y se estabilizan en valores altos (~0.9), lo que es una buena señal del desempeño del modelo.

**Métricas de mAP (metrics/mAP50(B), metrics/mAP50-95(B)):**

- Las métricas mAP50 y mAP50-95 muestran un aumento continuo y alcanzan valores buenos (~0.95 para mAP50 y ~0.7 para mAP50-95). Esto sugiere que el modelo tiene un desempeño sólido en tareas de detección de objetos.

# APP
Al igual que en la memoria, iré por el orden en el que el usuario ve la aplicación al ejecutarla. En primer lugar, se ve el video inicial, que se reproduce con openCV a la par que la música-inicial con pygame. En la carpeta [assets](https://github.com/AlejandroRguezMesa/VC_Practicas_Alejandro_Rodriguez_Mesa/tree/main/Practicas-VC-Alejandro_Rodr%C3%ADguezMesa/Pract_6_Alejandro_Rodriguez_Mesa/assets) se pueden ver las imagenes, gifs, videos y sonidos usados. 

## Previo
Antes de empezar, decir que en el cuaderno no solo se encuentra el código para la ejecución del código final. También está el codigo de los entrenamientos, y un codigo para probar dichos entrenamientos. Además de que se probaron por separado algunas de las funcionalidades antes de añadirlas a la app. 
Un ejemplo de ello son las predicciones del DeepFace.analyze() o la estimación de la posición de la cabeza.

![image](https://github.com/user-attachments/assets/fa3ab42a-c347-437b-a77f-211172314d65)

Este código es necesario ejecutarlo para que funcionen las predicciones en la APP posteriormente

![image](https://github.com/user-attachments/assets/3bb4ca5d-9cf4-4da6-a151-89d9b189750d)

No entraré en muchos detalles, aunque daré una breve explicación de cada parte. La explicación técnica se encuentra en la memoria.
## Inicio
[Es un video de 10 segundos hecho con three.js en glitch para la asignatura de Informática Gráfica](https://glitch.com/edit/#!/animation-maker). Decidí hacer esto en esa asignatura ya que necesitaba un video inicial para este trabajo, y mejor crear uno propio que usar uno ajeno de internet.
![image](https://github.com/user-attachments/assets/066412a6-d1ea-4570-abcc-e81aed2ba107)

## Pantalla Inicial
Al principio creé imagenes png con los botones con el fondo transparente para insertarlas en tkinter como botones, pero por desgracia parece que en tkinter no se puede aplicar transparencia, se genera una zona como fondo a la que le puedes cambiar el color, pero no aplicarle transparencia. Con lo que no quedó tan estético como me gustaría. 
![image](https://github.com/user-attachments/assets/2f098fcf-692e-4774-ae8a-698e1347cfe6)

## Register
Al darle al botón de registrarse te lleva a esta ventana, donde puedes poner tu nombre de usuario y luego aceptar para empezar con el registro. 
![image](https://github.com/user-attachments/assets/60a25daa-64c5-45c7-89ba-59c6405f37cb)

Por supuesto, el nombre de usuario es único, no se puede elegir uno ya existente

![image](https://github.com/user-attachments/assets/9233a56f-156a-46a2-b064-5d0261dd9684)

Hay un modelo de detección de gafas y máscaras/mascarillas, es necesario no tener nada de eso para continuar. (Tenga en cuenta que hay audio durante toda la ejecución.)

![image](https://github.com/user-attachments/assets/c020bcfc-a6a7-4b33-a4fd-cb0adef4be14)

![image](https://github.com/user-attachments/assets/1bdd7d26-b805-4a21-89a4-abaa49365354)

El siguiente paso es poner la cara en la zona indicada por el óvalo

![image](https://github.com/user-attachments/assets/ff4fe4ab-1684-4902-86e1-02a065109531)

Además, se deben seguir varias condiciones, boca cerrada, ojos abiertos, y cara mirando al frente. 

![image](https://github.com/user-attachments/assets/27f365b3-d3e2-4e37-b48e-6339ea6cb5a5)

Una vez hecho eso, ya se puede sacar la foto (a los 2 segundos hay un efecto flash+sonido)

![image](https://github.com/user-attachments/assets/cc3b6564-f311-4b2a-a884-e988e80383f7)

Tras tomar 5 imágenes, se termina el registro. Este usuario fue llamado Prueba. Tenga en cuenta que no hay comparaciones en el register, con lo que un usuario puede tener varias cuentas asociadas a su cara. El sistema compará embeddings, y el que más similitud tenga será el elegido. Se necesita un minimo de un 75% de similitud para que sea considerado la misma persona.

![image](https://github.com/user-attachments/assets/760ab025-08e9-476c-8ef8-a156926c8c1f)


## Login

El proceso de login es mucho más rápido, solo es necesario mirar al frente sin tener gafas ni mascarilla, y pestañear 3 veces. Si es detectado algun objeto de los mencionados, o no se está mirando al frente, se reinicia el contador de pestañeos.
![image](https://github.com/user-attachments/assets/f58a411d-be34-4eee-9b95-abf5936fef85)

![image](https://github.com/user-attachments/assets/d312c92c-9bf7-4284-aa3c-c674d8c63a6b)

Además, en el login también se cuenta con un modelo de detección de ataques de presentación o spoofing. 

![image](https://github.com/user-attachments/assets/cf344430-114d-40aa-851b-26c397e495bc)

![image](https://github.com/user-attachments/assets/6e1917ad-7a7d-4e4c-b862-7292335b66c2)

Aparte de Fotos y Dispositivos, el modelo tambien puede detectar máscaras. Tenga en cuenta que en el dataset de entrenamiento, habian imagenes consideradas spoofing por dispositivo que eran dificiles de detectar incluso para un humano, teniendo en cuenta que obviamente hay una cámara de por medio que sacó la foto. Con lo que en ocasiones puede detectar que hay spoofing por algún reflejo anómalo por ejemplo.

![image](https://github.com/user-attachments/assets/11b5e9fd-5b7c-44a7-bda9-ea34bf1504d4)

Al iniciar sesión, fui detectado como el usuario Prueba 

![image](https://github.com/user-attachments/assets/7e10e021-78ed-4454-82f2-ac20d3ef921d)

En otra instancia, con otro usuario y habiendo eliminado el usuario prueba, eliminé al usuario Prueba y añadí a otras personas. En el botón de estadísticas, podemos ver la similitud detectada respecto a otros usuarios. En este caso, inicié sesión como ale.
![image](https://github.com/user-attachments/assets/5154cc65-5dc3-407d-9bbd-6acd2d681605)



La simetría se realiza dibujando la mesh de la cara para la imagen, recortando la cara, para posteriormente trazar una linea en la mitad del eje x, e invertir una de las mitades y calcular el error cuadrático medio (mse). Se puede ver las imágenes de la parte izquierda y derecha de la cara en el github para ver el resultado del flip.

![image](https://github.com/user-attachments/assets/21fe59ea-ca5f-48f5-b2cb-19a6a0d46b7c)


En el botón de predicciones puede llegar a suceder este error si no se leyó con atención el cuaderno. 

![image](https://github.com/user-attachments/assets/ceb07be3-6e72-4faa-bf5b-6d7004f02128)

Esto se debe a que no se han cargado las dependencias del modelo pre entrenado que predice emociones, edad, raza y género. 

Es necesario ejecutar previamente este código con una imagen existente para asegurarse de que cargue, si falla es cuestión de volver a intentarlo, y reiniciar el enviroment antes de volver a hacerlo. 


```
from deepface import DeepFace

# Analyze the image
demography = DeepFace.analyze("./usuarios/ale/foto_1.png")

# Access the first face's result
if isinstance(demography, list):  # If multiple faces are detected
    demography = demography[0]

print("Age: ", demography["age"])
print("Gender: ", demography["gender"])
print("Emotion: ", demography["dominant_emotion"])
print("Race: ", demography["dominant_race"])
```

La salida será algo así:
Age:  21
Gender:  {'Woman': 0.06050013471394777, 'Man': 99.93950128555298}
Emotion:  neutral
Race:  latino hispanic

Una vez hecho, la predicción se puede realizar sin problema. Las predicciones se hacen con la imagen sin procesar. 

![image](https://github.com/user-attachments/assets/662480b2-3fab-418a-b9c1-073548984df0)

Por último, en el botón de cuenta se puede ver el numero de veces que se ha iniciado sesión y la fecha y hora de la última conexión.
![image](https://github.com/user-attachments/assets/6c4c0d0f-585e-4d2d-b6c1-c05a50191ee8)

# Video Explicativo

# Recursos
Se encuentran en la Memoria



