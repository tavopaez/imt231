import cv2
import numpy as np
##import RPi.GPIO as GPIO
import time

# Inicializar GPIO para controlar el brazo robÃ³tico
##GPIO.setmode(GPIO.BCM)
# Configurar los pines del GPIO para los motores del brazo robÃ³tico
motor1_pin = 17
motor2_pin = 27
##GPIO.setup(motor1_pin, GPIO.OUT)
##GPIO.setup(motor2_pin, GPIO.OUT)

# FunciÃ³n para mover el brazo robÃ³tico
def move_arm(angle1, angle2):
    # Convertir los Ã¡ngulos a seÃ±ales PWM para los motores
    duty1 = int(angle1 / 180 * 100)
    duty2 = int(angle2 / 180 * 100)
    
    # Activar los motores con los Ã¡ngulos correspondientes
    GPIO.output(motor1_pin, GPIO.HIGH)
    GPIO.output(motor2_pin, GPIO.HIGH)
    time.sleep(duty1 / 100.0)
    time.sleep(duty2 / 100.0)
    GPIO.output(motor1_pin, GPIO.LOW)
    GPIO.output(motor2_pin, GPIO.LOW)

# FunciÃ³n para detectar frutas no maduras
def detect_unripe_fruit(frame):
    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir los rangos de color para detectar frutas no maduras
    lower_green = np.array([25, 50, 50])
    upper_green = np.array([75, 255, 255])
    
    # Crear una mÃ¡scara para detectar los pÃ­xeles verdes
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Encontrar los contornos de la fruta no madura
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Si se encuentra al menos una fruta no madura, mover el brazo robÃ³tico
    if len(contours) > 0:
        # Calcular el centro del contorno mÃ¡s grande
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        # Mover el brazo robÃ³tico hacia la fruta no madura
        ##move_arm(cX, cY)
        
    return mask

# Capturar video de la cÃ¡mara
cap = cv2.VideoCapture(0)

while True:
    # Leer un fotograma del video
    ret, frame = cap.read()
    
    # Detectar frutas no maduras y mover el brazo robÃ³tico
    mask = detect_unripe_fruit(frame)
    
    # Mostrar la imagen original y la mÃ¡scara
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    
    # Salir del bucle al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpiar y cerrar
cap.release()