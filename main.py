#import codigoQr
from codigoQr import *

qr = Qr()

qr.bienvenida()
qr.GenerarQr()
qr.comprobarArchivo()

respuesta = input("¿ Desea ver la imagen QR generada? (S/n)")

if respuesta == 'S' or respuesta == 's':
    qr.abrirImg()
else:
    print("Revisar directorio con imagen")