import os       #importar libreria os
import cv2      #importar libreria cv2

class colorimage:

    #Las variables para iniciar el class serán: path: ruta de la imagen, image_name: nombre de la imagen
    def __init__(self, path, image_name):
        self.path = path                    #se crean las variables self
        self.image_name = image_name
        self.path_file = os.path.join(self.path, self.image_name)  #se extrae toda la ruta del path incluyendo la imagen
        self.image = cv2.imread(self.path_file)                    #con la libreria opencv se lee la imagen

    #función para ver el ancho y alto de la imágen
    def displayProperties(self):
        print('Ancho:', self.image.shape[1])     #la función shape devuelve tres variables (alto, ancho, espacio)
        print('Alto:',self.image.shape[0])       #se imprimen los valores correspondientes

    #función para ver la imágen en escala de grises
    def makeGray(self):
        self.gris = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)    #la función cv2.cvtColor permite cambiar el espacio de color, en este caso de BGR a grises
        cv2.imshow('image', self.gris)                              #muestra la imagen de escala de grises
        cv2.waitKey(0)                                              #mantiene abierta la imagen

    #función para ver la imagen de un color específico que depende de la variable 'color'
    def colorizeRGB(self,color):
        if(color == 'red'):                          #si se quiere ver la imagen rojiza
            self.red = self.image.copy()             #se realiza una copia de la imagen original
            self.red[:,:,0] = 0                      #se pone en cero los valores de azul
            self.red[:,:,1] = 0                      #se pone en cero los valores de verde
            cv2.imshow('red_image', self.red)        #muestra la imagen rojiza
            cv2.waitKey(0)                           #mantiene la imagen abierta

        if (color == 'blue'):                        #si se quiere ver la imagen azuloza
            self.blue = self.image.copy()            #se realiza una copia de la imagen original
            self.blue[:, :, 1] = 0                   #se pone en cero los valores de verde
            self.blue[:, :, 2] = 0                   #se pone en cero los valores de rojo
            cv2.imshow('blue_image', self.blue)      #muestra la imagen azuloza
            cv2.waitKey(0)                           #mantiene la imagen abierta

        if (color == 'green'):                       #si se quiere ver la imagen verdoza
            self.green = self.image.copy()           #se realiza una copia de la imagen original
            self.green[:, :, 0] = 0                  #se pone en cero los valores de azul
            self.green[:, :, 2] = 0                  #se pone en cero los valores de rojo
            cv2.imshow('green_image', self.green)    #muestra la imagen verdoza
            cv2.waitKey(0)                           #mantiene la imagen abierta

    #función para ver la imágen resaltando los tonos
    def makeHue(self):
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  #la función cv2.cvtColor permite cambiar el espacio de color, en este caso de BGR a HSV
        self.hsv[:, :, 1] = 255                                 #se pone el valor de Saturation en 255
        self.hsv[:, :, 2] = 255                                 #se pone el valor de Value en 255
        self.hue = cv2.cvtColor(self.hsv, cv2.COLOR_HSV2BGR)  #la función cv2.cvtColor permite cambiar el espacio de color, en este caso de HSV a BGR
        cv2.imshow('hue_image', self.hue)                       #muestra la imagen resaltando tonos
        cv2.waitKey(0)                                          #mantiene la imagen abierta



