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


# TO MOD
# Coordenadas de inicio del sudoku en el
# dsipositivo
x, y = 18, 230

# TO MOD
# Dimensiones de cada casilla:
dx, dy = 108, 108


# Variable que nos permite determinar si se
# realizará alguna acción en el dispositivo
impr = 0


#       mat: contine el sudoku incompleto escaneado, una matriz 9x9
# touch mat: matriz que contiene una tupla de coordenadas, es donde
#            se almacena las coordenadas de cada casilla
mat, touch_mat = [], []


# TO MOD
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
        ##
        x += 11 if i % 3 == 0 else 6
        # Extraer el número de cada casilla
        temp = pytesseract.image_to_string(imcrop, config='--psm 10')
        temp = int(temp[0]) if temp[0].isnumeric() else 0
        grid_row.append(temp)
        x += dx
    x = xcopy
    # En nuestra aplicación cada 3 filas se presenta una línea más
    # gruesa, entonces:
    ##
    y += dy + (11 if j % 3 == 0 else 6)
    mat.append(grid_row)
    touch_mat.append(t_row)

# Resolver e imprimir en pantalla el sudoku si es que este se puede resolver,
# caso contrario se imprime en pantalla el mensaje que indica que el sudoku
# no es solucionable y cambia el valor de "impr" a 1 para que ninguna acción
# sea ralizada en pantalla:
print_board(mat)
print("_________________________")
orig_grid = copy.deepcopy(mat)
if sudoku_solver(mat):
    print("Sudoku Resuelto: ")
    print_board(mat)
else:
    print("No existe solución")
    impr = 1


# TO MOD
# Función que permite al programa detectar las coordenadas de cada casilla y
# y realizar un "click" sobre las mismas:
def click(i, j):
    device.shell(f'input touchscreen tap {touch_mat[i][j][0]} {touch_mat[i][j][1]}')


# TO MOD
# Función que permite al programa realizar un "click" encima de cada valor asignable
# al Sudoku utilizando sus coordenas, en caso de esta la app utilizada en este
# proyecto los valores del 1 al 5 se encuentran en la misma fila, por tanto:
def select1to5(n):
    arr = [125, 314, 566, 756, 970]
    device.shell(f'input touchscreen tap {arr[n - 1]} 1342')


# TO MOD
# Función que permite al programa realizar un "click" encima de cada valor asignable
# al Sudoku utilizando sus coordenas, en caso de esta la app utilizada en este
# proyecto los valores del 6 al 9 se encuentran en la misma fila, por tanto:
def select6to9(n):
    arr = [125, 314, 566, 756]
    device.shell(f'input touchscreen tap {arr[n - 6]} 1545')


# TO MOD
# Actualizar los valores en pantalla,realizando una serie de "clicks" en la misma,
# comenzando con la casilla y luego con el valor que debe ir en la misma, solamente
# se seleccionan las casillas que originalmente estaban vacías:
if impr == 0:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # Se define si la casilla estaba originalmente vacía
            if orig_grid[i][j] == 0:
                # Se selecciona la casilla
                click(i, j)
                # Se selecciona el valor de la casilla
                if mat[i][j] < 6:
                    select1to5(mat[i][j])
                else:
                    select6to9(mat[i][j])

