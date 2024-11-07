import cv2

# Leer la imagen
imagen = cv2.imread("C:\\Users\\andrei.sandu\\PythonPractica\\contornos\\imagenTres.png")
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(0,255,0),1)


# Mostrar la imagen en una ventana
cv2.imshow("Imagen", imagen)
cv2.imshow("Imagen Gris", grises)
cv2.imshow("Imagen umbral", umbral)

# Esperar a que se presione una tecla para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()