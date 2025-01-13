import os 
import time
import numpy as np
from deepface import DeepFace

def calcular_distancia_intra_clase(embeddings, metric='cosine'):
    """
    Calcula la distancia promedio de todos los pares de embeddings
    para un solo usuario. Mientras menor sea, mayor consistencia 
    (mejor 'precisión' intra-clase).
    
    metric: 'cosine' o 'euclidean' (o 'euclidean_l2')
    """
    if len(embeddings) < 2:
        # Con solo un embedding no podemos calcular distancias de pares
        return 0.0
    
    distancias = []
    for i in range(len(embeddings)):
        for j in range(i+1, len(embeddings)):
            emb1 = embeddings[i]
            emb2 = embeddings[j]
            
            # Cálculo de la distancia
            if metric == 'cosine':
                # Distancia coseno = 1 - cos(ángulo)
                emb1_norm = emb1 / np.linalg.norm(emb1)
                emb2_norm = emb2 / np.linalg.norm(emb2)
                cos_sim = np.dot(emb1_norm, emb2_norm)
                dist = 1 - cos_sim
            elif metric == 'euclidean':
                dist = np.linalg.norm(emb1 - emb2)
            elif metric == 'euclidean_l2':
                # Euclidean L2 normalization
                emb1_l2 = emb1 / np.linalg.norm(emb1)
                emb2_l2 = emb2 / np.linalg.norm(emb2)
                dist = np.linalg.norm(emb1_l2 - emb2_l2)
            else:
                raise ValueError("Métrica desconocida. Usa 'cosine', 'euclidean' o 'euclidean_l2'.")
            
            distancias.append(dist)
    
    return np.mean(distancias)

def calcular_distancia_inter_usuarios(embeddings_usuario_1, embeddings_usuario_2, metric='cosine'):
    """
    Calcula la distancia promedio entre todos los pares (emb_u1, emb_u2),
    donde emb_u1 pertenece a embeddings_usuario_1 y emb_u2 a embeddings_usuario_2.
    
    metric: 'cosine', 'euclidean' o 'euclidean_l2'.
    """
    if len(embeddings_usuario_1) == 0 or len(embeddings_usuario_2) == 0:
        return 0.0
    
    distancias = []
    for emb1 in embeddings_usuario_1:
        for emb2 in embeddings_usuario_2:
            if metric == 'cosine':
                emb1_norm = emb1 / np.linalg.norm(emb1)
                emb2_norm = emb2 / np.linalg.norm(emb2)
                cos_sim = np.dot(emb1_norm, emb2_norm)
                dist = 1 - cos_sim
            elif metric == 'euclidean':
                dist = np.linalg.norm(emb1 - emb2)
            elif metric == 'euclidean_l2':
                emb1_l2 = emb1 / np.linalg.norm(emb1)
                emb2_l2 = emb2 / np.linalg.norm(emb2)
                dist = np.linalg.norm(emb1_l2 - emb2_l2)
            else:
                raise ValueError("Métrica desconocida. Usa 'cosine', 'euclidean' o 'euclidean_l2'.")
            
            distancias.append(dist)
    
    return np.mean(distancias)
def generar_embeddings_usuario(ruta_carpeta, modelo):
    """
    Genera una lista de embeddings para todas las imágenes en ruta_carpeta,
    usando el modelo indicado.
    """
    imagenes = sorted(
        [f for f in os.listdir(ruta_carpeta) if f.startswith("foto_") and f.endswith(".png")]
    )
    
    embeddings_modelo = []
    for img_name in imagenes:
        img_path = os.path.join(ruta_carpeta, img_name)
        
        emb_data = DeepFace.represent(
            img_path=img_path,
            model_name=modelo,
            enforce_detection=False
        )
        
        if len(emb_data) > 0 and "embedding" in emb_data[0]:
            arr = np.array(emb_data[0]["embedding"])
            embeddings_modelo.append(arr)
    
    return embeddings_modelo

def generar_embeddings_y_metricas(ruta_carpeta_usuario, modelos, usuarios_externos):
    """
    Lee las imágenes de 'ruta_carpeta_usuario', genera embeddings con cada modelo
    y calcula métricas de velocidad, tamaño, distancia intra-clase y distancia
    inter-usuarios (discriminación).
    
    usuarios_externos: lista con los nombres de otros usuarios, ej. ["adriana", "mama", "papa"].
    Se asume que su ruta es algo como ./usuarios/<nombre> con el mismo formato de imagen.
    """
    
    # 1. Obtener lista de imágenes del usuario principal (Ale)
    imagenes = sorted(
        [f for f in os.listdir(ruta_carpeta_usuario) if f.startswith("foto_") and f.endswith(".png")]
    )
    
    # Diccionario para guardar resultados por modelo
    resultados = {}
    
    for modelo in modelos:
        print(f"\n=== Procesando modelo: {modelo} ===")
        
        # === Embeddings para el usuario principal (Ale) ===
        inicio_tiempo = time.time()
        embeddings_ale = generar_embeddings_usuario(ruta_carpeta_usuario, modelo)
        fin_tiempo = time.time()
        
        # Calcular tiempo total y promedio para Ale
        tiempo_total = fin_tiempo - inicio_tiempo
        tiempo_promedio = tiempo_total / len(imagenes) if len(imagenes) > 0 else 0
        
        # Tamaño de embedding
        dim_embedding = embeddings_ale[0].shape[0] if len(embeddings_ale) > 0 else 0
        
        # Distancia intra-clase (solo Ale)
        distancia_intra = calcular_distancia_intra_clase(embeddings_ale, metric='cosine')
        
        # === Calcular distancias inter-usuarios (Ale vs adriana, vs mama, vs papa...) ===
        distancias_inter_usuarios = {}
        for usuario_ext in usuarios_externos:
            ruta_carpeta_ext = os.path.join("./usuarios", usuario_ext)
            embeddings_ext = generar_embeddings_usuario(ruta_carpeta_ext, modelo)
            
            # Calculamos la distancia entre embeddings de Ale y el usuario externo
            dist = calcular_distancia_inter_usuarios(embeddings_ale, embeddings_ext, metric='cosine')
            distancias_inter_usuarios[usuario_ext] = dist
        
        # Guardar resultados en diccionario
        resultados[modelo] = {
            "tiempo_total_s": tiempo_total,
            "tiempo_promedio_s": tiempo_promedio,
            "tamanio_embedding": dim_embedding,
            "distancia_intra_clase": distancia_intra,
            "distancias_inter_usuarios": distancias_inter_usuarios
        }
    
    return resultados


if __name__ == "__main__":
    # Ruta de la carpeta del usuario principal (Ale)
    ruta_carpeta_ale = "./usuarios/ale"
    
    # Modelos soportados por DeepFace
    modelos_disponibles = [
        "Facenet",
        "VGG-Face",
        "OpenFace",
        "DeepID",
        "ArcFace",
        "Dlib",
        "SFace"
    ]
    
    # Lista de otros usuarios para comparar contra Ale
    otros_usuarios = ["adriana", "mama", "papa"]
    
    # Generar embeddings y métricas
    metrics = generar_embeddings_y_metricas(ruta_carpeta_ale, modelos_disponibles, otros_usuarios)
    
    # Guardar resultados en un archivo de texto
    with open("metricas.txt", "w") as file:
        file.write("=== RESULTADOS FINALES ===\n")
        for modelo, info in metrics.items():
            file.write(f"\nModelo: {modelo}\n")
            file.write(f" - Tiempo Total (s)           : {info['tiempo_total_s']:.4f}\n")
            file.write(f" - Tiempo Promedio (s/imagen) : {info['tiempo_promedio_s']:.4f}\n")
            file.write(f" - Tamaño de Embedding        : {info['tamanio_embedding']}\n")
            file.write(f" - Distancia Intra-clase      : {info['distancia_intra_clase']:.6f}\n")
            
            # Distancias inter-usuarios
            file.write(f" - Distancias Inter-usuarios (Ale vs ...):\n")
            for usuario_ext, dist in info['distancias_inter_usuarios'].items():
                file.write(f"     * {usuario_ext}: {dist:.6f}\n")
    
    print("Resultados guardados en 'metricas.txt'")
