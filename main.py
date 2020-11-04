# Módulos requeridos a importar para el funcionamiento
from ppadb.client import Client
from PIL import Image
import pytesseract
import copy
from sudoku import sudoku_solver, print_board

# Conectar con ell dispositivo vía adb:
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

# Coordenadas de inicio del sudoku en el
# dsipositivo (MOD):
x, y = 18, 230

# Dimensiones de cada casilla:
dx, dy = 108, 108

# Variable que nos permite determinar si se
# realizará alguna acción en el dispositivo
impr = 0

#       mat: contine el sudoku incompleto escaneado, una matriz 9x9
# touch mat: matriz que contiene una tupla de coordenadas, es donde
#            se almacena las coordenadas de cada casilla
mat, touch_mat = [], []

# Analizar cada casilla, extraer su valor y asignarle una coordenada
for j in range(1, 10):
    grid_row, t_row = [], []
    xcopy = x

    for i in range(1, 10):
        # Recorta y realiza un acercamiento en cada casilla individual
        # (se debe procurar que los números sean claros)
        imcrop = im.crop((x, y, x + dx, y + dy)).crop((16, 13, 98, 104))
        t_row.append(((2 * x + dx) // 2, (2 * y + dy) // 2))
        # En nuestra aplicación cada 3 casilla se presenta una línea más
        # gruesa, entonces:
        x += 11 if i % 3 == 0 else 6
        # Extraer el número de cada casilla
        temp = pytesseract.image_to_string(imcrop, config='--psm 10')
        temp = int(temp[0]) if temp[0].isnumeric() else 0
        grid_row.append(temp)
        x += dx
    x = xcopy
    # En nuestra aplicación cada 3 filas se presenta una línea más
    # gruesa, entonces:
    y += dy + (11 if j % 3 == 0 else 6)
    mat.append(grid_row)
    touch_mat.append(t_row)

#Verificar y avisar en la pantalla si se puede resolver
