import os
import cv2
import numpy 

path = r"C:\Users\armando\Documents\GitHub\dataset\img_dataset\train"
for n,path_image in enumerate(os.listdir(path)):

    if ".jpg" in path_image:

        path_image_tmp = os.path.join(path,str(n)+".jpg")
        path_image  = os.path.join(path,path_image)

        imagen_blanco_negro = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
        color_naranja = numpy.array([0, 165, 255], dtype=numpy.uint8)  # Naranja en formato BGR
        color_celeste = numpy.array([255, 255, 0], dtype=numpy.uint8)  # Celeste en formato BGR
        
        mask = imagen_blanco_negro<140

        imagen_coloreada = cv2.cvtColor(imagen_blanco_negro, cv2.COLOR_GRAY2BGR)
        imagen_coloreada[mask] = color_naranja  
        imagen_coloreada[~mask] = color_celeste 

        cv2.imwrite(path_image,imagen_coloreada)

 