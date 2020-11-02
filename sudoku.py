board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# Método que resuelve el sudoku:
def sudoku_solver(matrix):
    find = find_empty_place(matrix)
    if not find:
        # Caso base cuando no hay casillas vacías.
        return True
    else:
        # Caso en que si se encontró una casilla vacía.
        row, col = find

    for num in range(1, 10):
        # Verificar si es valido colocar el número si
        # es asi lo coloca, asumimos que es el correcto.
        if valid(matrix, row, col, num):
            matrix[row][col] = num

            # Llamada recursiva para la siguiente
            # casilla vacía.
            if sudoku_solver(matrix):
                return True

            # Colocamos como vacía la casilla pues no
            # se llegó a la respuesta buscada.
            matrix[row][col] = 0

    return False


# Encuentra una casilla "vacia" y actualiza row
# y column:
def find_empty_place(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i, j  # row, col

    return None


# Verificar si "num" ya esta presente en una columna:
def verify_column(matrix, column, num):
    for row in range(0, 8):
        if matrix[row][column] == num:
            return True

    return False


# Verificar si "num" ya esta presente en una fila:
def verify_row(matrix, row, num):
    for column in range(0, 8):
        if matrix[row][column] == num:
            return True

    return False


# Verificar si "num" ya esta presente en una de
# las cuadrículas 3x3
def verify_3_x_3_box(matrix, start_row, start_col, num):
    for row in range(0, 3):
        for column in range(0, 3):
            if matrix[row + start_row][column + start_col] == num:
                return True

    return False


# Llamamos a los métodos que verifican si colocar
# un número es valido o no
def valid(matrix, row, col, num):
    valid_pro = not verify_column(matrix, col, num) and not verify_row(matrix, row, num) and \
                not verify_3_x_3_box(matrix, row - row % 3, col - col % 3, num)
    return valid_pro

# Imprimimos el sudoku en pantallla
def print_board(matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - -")

        for j in range(len(matrix[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print("[" + str(matrix[i][j]) + "]")
            else:
                print("[" + str(matrix[i][j]) + "]", end="")


print_board(board)
sudoku_solver(board)
print("_________________________")
print_board(board)
