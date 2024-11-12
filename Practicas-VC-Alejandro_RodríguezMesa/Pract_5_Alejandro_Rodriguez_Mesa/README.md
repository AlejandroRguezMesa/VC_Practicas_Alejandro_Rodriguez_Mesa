***Nombre:*** *Alejandro Rodríguez Mesa*

***Asignatura:*** *Visión por Computador*

## Instalación y enviroment en Anaconda
conda create --name VC_P5 python=3.11.5
conda activate VC_P5
pip install opencv-python
pip install matplotlib
pip install imutils
pip install mtcnn
pip install tensorflow   
pip install deepface
pip install tf-keras
pip install cmake
pip install dlib
pip install pygame
pip install xgboost
pip install mediapipe

## Probando el entorno, detección facial con FaceDetectors
Tras crear el enviroment y descargar los landmarks shape_predictor_5_face_landmarks.dat y shape_predictor_68_face_landmarks ejecuté el código y la detección de caras funcionó. Aun así, decidí buscar otros detectores faciales con la idea de encontrar mejores resultados, y tras una búsqueda y algunas pruebas, encontré que MediaPipe ofrece 
