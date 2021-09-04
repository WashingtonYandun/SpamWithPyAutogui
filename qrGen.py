import qrcode
from PIL import Image

link = 'https://washingtonyandun.githu'
imagen = qrcode.make(link)

nombreImagen = 'gol.png'
archivoImagen = open(nombreImagen, 'wb')
imagen.save(archivoImagen)
archivoImagen.close()

ruta = './'+nombreImagen
Image.open(ruta).show()