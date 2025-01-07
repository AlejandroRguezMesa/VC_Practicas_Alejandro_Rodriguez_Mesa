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

# APP
Al igual que en la memoria, iré por el orden en el que el usuario ve la aplicación al ejecutarla. En primer lugar, se ve el video inicial, que se reproduce con openCV a la par que la música-inicial con pygame. En la carpeta [assets](https://github.com/AlejandroRguezMesa/VC_Practicas_Alejandro_Rodriguez_Mesa/tree/main/Practicas-VC-Alejandro_Rodr%C3%ADguezMesa/Pract_6_Alejandro_Rodriguez_Mesa/assets) se pueden ver las imagenes, gifs, videos y sonidos usados. 

## Previo
Antes de empezar, decir que en el cuaderno no solo se encuentra el código para la ejecución del código final. También está el codigo de los entrenamientos, y un codigo para probar dichos entrenamientos. Además de que se probaron por separado algunas de las funcionalidades antes de añadirlas a la app. 
Un ejemplo de ello son las predicciones del DeepFace.analyze() o la estimación de la posición de la cabeza.

![image](https://github.com/user-attachments/assets/fa3ab42a-c347-437b-a77f-211172314d65)

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

Si miramos en el botón de estadísticas, podemos ver la similitud detectada respecto a otros usuarios. En este caso ambos soy yo, me registré como ale en días diferentes, con lo que la imagen de "prueba" que me saqué hace unos minutos es de esperar que tenga más parecido. Al fin y al cabo, la luminosidad es diferente, mi cara puede estar más o menos hinchada, la toma por distancia puede ser distinta, la expresión tomada en ese frame, etc.

![image](https://github.com/user-attachments/assets/9f71ebee-8251-47f0-8881-b46ac594eec2)

La simetría simplemente traza una linea en la mitad del eje x, invierte una de las mitades y calcula el error cuadrático medio (mse)

![image](https://github.com/user-attachments/assets/a71d3a93-6057-4d9b-826b-870bd2368238)


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

![image](https://github.com/user-attachments/assets/6c4c0d0f-585e-4d2d-b6c1-c05a50191ee8)

Una vez hecho, la predicción se puede realizar sin problema. Las predicciones se hacen con la imagen sin procesar. 

![image](https://github.com/user-attachments/assets/662480b2-3fab-418a-b9c1-073548984df0)

# Video Explicativo

# Recursos
Se encuentran en la Memoria



