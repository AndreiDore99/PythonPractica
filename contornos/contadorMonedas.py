import cv2
import numpy as np
vargaus=3
valorkernel=3
imagen = cv2.imread("C:\\Users\\andrei.sandu\\PythonPractica\\contornos\\monedas.jpg")
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(grises,(vargaus,valorkernel),0)
canny=cv2.Canny(gauss,0,100)



cv2.imshow("Grises",grises)
cv2.imshow("Gauus",gauss)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()