# Módulos requeridos a importar para el funcionamiento
from ppadb.client import Client
from PIL import Image

# Conectar con el dispositivo vía adb:
adb = Client()
devices = adb.devices()
if len(devices) == 0:
    print("No se detecto ningún dispositivo")
    quit()
device = devices[0]

# Guardar una captura de pantalla y
# cargarla usando PIL:
result = device.screencap()
with open("screen.png", "wb") as fp:
    fp.write(result)
im = Image.open("screen.png")

# implmentar las coordenadas del sudoku
