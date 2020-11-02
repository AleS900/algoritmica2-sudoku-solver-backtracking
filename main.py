# Módulos requeridos a importar para el funcionamiento
from ppadb.client import Client

# Conectar con el dispositivo vía adb:
adb = Client()
devices = adb.devices()
if len(devices) == 0:
    print("No se detecto ningún dispositivo")
    quit()
device = devices[0]

#aqui se deberia poner para escanear la pantalla