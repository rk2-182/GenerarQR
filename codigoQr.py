"""
Un código QR (del inglés Quick Response code, «código de respuesta rápida») es la evolución del código de barras.
Es un módulo para almacenar información en una matriz de puntos o en un código de barras bidimensional.

apoyo: https://www.youtube.com/watch?v=FD6bXAudZT0&t
https://binary-coffee.dev/post/generando-codigos-qr-con-python

"""
import qrcode
import os
import pathlib
from PIL import Image

class Qr():

    def __init__(self):

        self.ruta = str(pathlib.Path().absolute())+'\\qr\\'
        self.NombreImg = ' '

    
    def bienvenida(self):
        os.system("cls")
        mensaje = "***** BIENVENIDO A GENERADOR DE QR 1.0 *****"
        print(mensaje.center(50))
        print("\n")

    def GenerarQr(self):

        texto = input("Introduzca el texto para generar codigo QR: ")

        #Convertir en qr el texto
        imagen = qrcode.make(texto)

        #Ingresar un nombre a la imagen generada con extensin png
        NombreImg = input("Introduzca el nombre de la imagen QR: ") + '.png'
        self.NombreImg = NombreImg

        #Asignar ruta mas el nombre de la imagen
        self.ruta=self.ruta+self.NombreImg

        #Abrimos un archivo en modo escritura que es donde se guardará nuestro código.
        f = open(self.ruta,'wb')

        imagen.save(f)
        f.close()

        return f

    def comprobarArchivo(self):
        if os.path.exists(self.ruta):
            print("Existe: ",self.ruta)
        else:
            print("No existe")

   
    def abrirImg(self):
        #Abrir imagen
        ruta_imagen = self.ruta
        Image.open(ruta_imagen).show()


