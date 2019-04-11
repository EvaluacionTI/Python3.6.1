#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	28Mar2019
# Objetivo			        :   Biblioteca Urllib
#                                  :
# Procedimiento       :   Descargar archivos
#  La idea general sería usar varios hilos o procesos y que cada uno se encargue de descargar una parte del archivo en si.
# Para ello el servidor tiene que soportar el header Range, esto nos permite obtener del servidor un rango de bytes del archivo en vez del archivo completo. Por lo tanto, la primera tarea es ver si el servidor acepta o no rangos.
# Si los acepta necesitamos que nos diga el total de bytes del archivo para poder partirlo en x intervalos adecuadamente y luego poder reconstruirlo. Una vez calculados el rango de bytes (recordar que el header Range incluye ambos limites al contrario que range en Python) llamamos a un proceso por cada parte y le pedimos que la descarge. Si todos termina haciendo su trabajo solo queda unir cada fragmento de bytes en un archivo, por supuesto hay que hacerlo en orden si no queremos obtener un bonito fichero lleno de datos corruptos.
# Un ejemplo simple usando multiprocesamiento en Python 3.x sería:

# Debe ir como tarea
# Podemos implementar reintentos si un fragmento falla (ahora si un proceso falla podemos decir adiós a nuestra descarga XD), intentar obtener el nombre del archivo del servidor si está disponible, implementar bonitas barras de progreso, implementar pausas y reanudaciones, en definitiva complicarnos la vida todo lo que queramos.
#==============================================================================
import urllib.request
from multiprocessing import Process, Manager

def descargar(url,orden,rango,frag):
    try:
        print('Obteniendo fragmento {}. Descargando desde byte {} hasta byte {}.'.format(orden,*rango))
        req = urllib.request.Request(url)
        req.add_header('Range', 'bytes={}-{}'.format(*rango))
        data = urllib.request.urlopen(req).read()
        if data:
            frag[orden]=data
            print('Fragmento {} descargado correctamente. Obtenidos {} bytes.'.format(orden,len(data)))
        else:
            frag[orden]=None
    except:
        frag[orden]='#Error'
        raise

def descarga_paralela(url, fragmentos, nombre):
    ranges=None
    with urllib.request.urlopen(url) as f:
        #Comprobamos que el servidor acepte la descarga parcial.
        if f.getheader("Accept-Ranges", "none").lower() != "bytes":
            print('Descarga parcial no soportada, iniciando descarga...')
        else:
            print('Descarga parcial soportada')

            #Obtenemos el tamaño total del archivo
            size = int(f.getheader("Content-Length", "none"))
            print('Tamaño del archivo: {} bytes.'.format(size))

            #Dividimos ese tamaño en intervalos de acuerdo al número de procesos que lanzaremos
            tamF = size//fragmentos
            print('Fragmentos: {}.\nTamaño aproximado por fragmento: {} bytes.'.format(fragmentos, tamF))
            ranges = [[i, i+tamF-1] for i in range (0, size, tamF)]
            ranges[-1][-1]=size

            #Vamos a usar un diccionario compartido por los procesos, la clave será el orden que cada fragmento de bytes tiene en el archivo final.
            manager = Manager()
            d = manager.dict()
            #Lanzamos los procesos
            workers = [Process(target=descargar, args=(url,i,r,d)) for i, r in enumerate(ranges)]
            for w in workers:
                w.start()
            for w in workers:
                w.join()

            #reconstruimos el archivo usando cada fragmento en su orden correcto:
            with open(nombre, 'wb') as f:
                for i in range(fragmentos):
                    data = d[i]
                    if data == None or data == '#Error':
                        print('El fragmento {} no se puedo descargar. No se puede reconstruir el archivo'.format(i))
                        break
                    else:
                        f.write(data)
                else:
                    print('Archivo descargado y reconstruido con éxito.')



if __name__ == '__main__':
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Bow_Lake_beim_Icefields_Parkway.jpg/1280px-Bow_Lake_beim_Icefields_Parkway.jpg'
    descarga_paralela(url, 10, 'imagen.jpg')