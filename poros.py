import cv2
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del laboratorio
scale_bar_length_nm = 1  # Longitud de la escala en la imagen (en nanómetros)
scale_bar_length_px = 1    # Longitud en píxeles de la barra de escala medida en la imagen
nano_particle_ref = 114.10  # Tamaño promedio de las partículas esperado en nm

# Factor de conversión de píxeles a nanómetros
pixel_to_nm = (scale_bar_length_nm / scale_bar_length_px)

# Cargar la imagen
image_path = "poro.png"  # Cambia el nombre si es necesario
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Verificar que la imagen se cargó correctamente
if image is None:
    raise ValueError("Error al cargar la imagen.")

# Invertir la imagen para que los poros oscuros se vuelvan claros
image_inverted = cv2.bitwise_not(image)

# Recortar la región de interés (ROI) para eliminar las letras
height, width = image_inverted.shape
roi = image_inverted[0:height-100, :]  # Ajustar según las dimensiones de las letras

# Mejorar contraste con ecualización de histograma
roi_enhanced = cv2.equalizeHist(roi)

# Aplicar detector de bordes Canny
edges = cv2.Canny(roi_enhanced, 50, 150)

# Aplicar dilatación y erosión para limpiar los bordes
kernel = np.ones((3, 3), np.uint8)
final_edges = cv2.dilate(edges, kernel, iterations=1)
final_edges = cv2.erode(final_edges, kernel, iterations=1)

# Detectar círculos con la Transformada de Hough
circles = cv2.HoughCircles(image_inverted, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=60, param2=20, minRadius=5, maxRadius=50)

# Crear una copia de la imagen para dibujar los resultados
output_image = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)

# Lista para almacenar las áreas
areas_nm = []

# Procesar y calcular el área promedio
if circles is not None:
    circles = np.round(circles[0, :]).astype(int)
    for (x, y, r) in circles:
        # Calcular el área en píxeles
        area_px = np.pi * (r ** 2)

        # Convertir el área a nanómetros cuadrados
        area_nm = area_px * (pixel_to_nm ** 2)

        # Agregar el área a la lista
        areas_nm.append(area_nm)

        # Dibujar el círculo y mostrar el área en la imagen
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 2)
        cv2.putText(output_image, f"{area_nm:.2f} nm²", (x - r, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    # Calcular y mostrar el promedio de las áreas
    if areas_nm:
        average_area_nm = np.mean(areas_nm)
        print(f"Promedio de las áreas de las partículas detectadas: {average_area_nm:.2f} nm²")
else:
    print("No se detectaron partículas.")

# Mostrar las imágenes procesadas en subgráficas
plt.figure(figsize=(15, 10))

plt.subplot(1, 4, 1)
plt.title("Imagen Original")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title("Imagen Invertida")
plt.imshow(roi, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.title("Bordes Detectados")
plt.imshow(final_edges, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.title("Círculos Detectados")
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Mostrar las imágenes procesadas en ventanas separadas
cv2.imshow("Imagen Original", image)
cv2.imshow("Imagen Invertida", roi)
cv2.imshow("Bordes Detectados", final_edges)
cv2.imshow("Circulos Detectados", output_image)

plt.show()

# Esperar a que el usuario presione una tecla para cerrar todas las ventanas de OpenCV
cv2.waitKey(0)
cv2.destroyAllWindows()
