"""MatrixProcessing module"""
import util


def _get_matrix_row(columns):
    """Gets the right row from the user's input

    Args:
        columns (int): number of columns in the matrix

    Returns:
        list: matrix's row
    """
    while True:
        try:
            row_input = input("> ").split()
            if len(row_input) != columns:
                print(f"Each row of the matrix should have {columns} elements")
            else:
                row = [int(value) if util.is_digit(value) else float(value) for value in row_input]
                return row
        except ValueError:
            print("The input must contain numeric values")


def get_rows_and_columns():
    """Gets the number of rows and columns for the matrix

    Returns:
        tuple: number of rows and columns
    """
    while True:
        try:
            rows, cols = (list(map(int, input("Enter the size of the matrix: > ").split())))
            if rows <= 0 or cols <= 0:
                print("The input must contain two positive numeric values")
            else:
                return rows, cols
        except ValueError:
            print("The input must contain two numeric values")


def create_matrix():
    """Reads matrix row by row

    Returns:
        list: user's matrix
    """
    rows, columns = get_rows_and_columns()
    matrix = []

    print("Enter the matrix:")
    for i in range(rows):
        row = _get_matrix_row(columns)
        matrix.append(row)

    return matrix


def add(matrix_a, matrix_b):
    """Adds two matrices

    Args:
        matrix_a (list): first matrix
        matrix_b (list): second matrix

    Returns:
        list: result of the sum of matrix_a and matrix_b
        None: if the adding is impossible
    """
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    columns_b = len(matrix_b[0])

    result = create_empty_matrix(rows_a, columns_a)

    if rows_a != rows_b or columns_a != columns_b:
        return None

    for i in range(rows_a):
        for j in range(columns_a):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


def multiply_by_constant(matrix, constant):
    """Multiplies a matrix by a constant

    Args:
        matrix (list): matrix to be multiplied
        constant (int/float): constant value

    Returns:
        list: result of matrix multiplied by the constant
    """
    rows = len(matrix)
    cols = len(matrix[0])
    result = create_empty_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] * constant
    return result


def multiply_by_matrix(matrix_a, matrix_b):
    """Multiplies two matrices

    Args:
        matrix_a (list): first matrix
        matrix_b (list): second matrix

    Returns:
        list: tesult of matrix_a multiplied by matrix_b
        None: if multiplication is impossible
    """
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    columns_b = len(matrix_b[0])

    result = create_empty_matrix(rows_a, columns_b)

    if columns_a != rows_b:
        return None

    for i in range(rows_a):
        for j in range(columns_b):
            for k in range(rows_b):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def main_diagonal_transpose(matrix):
    """Transposes a matrix along its main diagonal

    Args:
        matrix (list): matrix to be transposed

    Returns:
        list: transposed matrix along the main diagonal
    """
    rows = len(matrix)
    cols = len(matrix[0])
    result = create_empty_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            result[j][i] = matrix[i][j]
    return result


def side_diagonal_transpose(matrix):
    """Transposes a matrix along its side diagonal

    Args:
        matrix (list): matrix to be transposed

    Returns:
        list: transposed matrix along the side diagonal
    """
    rows = len(matrix)
    columns = len(matrix[0])
    result = create_empty_matrix(rows, columns)

    for i in range(rows):
        for j in range(columns):
            result[columns - 1 - j][rows - 1 - i] = matrix[i][j]
    return result


def vertical_line_transpose(matrix):
    """Transposes a matrix along the vertical line

    Args:
        matrix (list): matrix to be transposed

    Returns:
        list: transposed matrix along the vertical line
    """
    rows = len(matrix)
    columns = len(matrix[0])
    result = create_empty_matrix(rows, columns)

    for i in range(rows):
        for j in range(columns):
            result[i][columns - 1 - j] = matrix[i][j]
    return result


def horizontal_line_transpose(matrix):
    """Transposes a matrix along the horizontal line

    Args:
        matrix (list): matrix to be transposed

    Returns:
        list: transposed matrix along the horizontal line
    """
    rows = len(matrix)
    columns = len(matrix[0])
    result = create_empty_matrix(rows, columns)

    for i in range(rows):
        for j in range(columns):
            result[rows - 1 - i][j] = matrix[i][j]
    return result


def transpose_matrix():
    """Provides options to transpose a matrix based on user choice

    Returns:
        list: transposed matrix based on user selection
        None: if user chooses to go back
    """
    while True:
        print("\n"
              "1. Main diagonal\n"
              "2. Side diagonal\n"
              "3. Vertical line\n"
              "4. Horizontal line\n"
              "0. Back")
        possible_values = [0, 1, 2, 3, 4]
        user_choice = util.get_user_choice(possible_values)

        # Back
        if user_choice == 0:
            return None

        matrix = create_matrix()
        # Main diagonal
        if user_choice == 1:
            return main_diagonal_transpose(matrix)

        # Side diagonal
        elif user_choice == 2:
            return side_diagonal_transpose(matrix)

        # Vertical line
        elif user_choice == 3:
            return vertical_line_transpose(matrix)

        # Horizontal line
        elif user_choice == 4:
            return horizontal_line_transpose(matrix)

        else:
            print("Enter the correct value")


def get_sub_matrix(matrix, row, column):
    """Retrieves a sub-matrix by excluding specified row and column

    Args:
        matrix (list): matrix to extract the sub-matrix from
        row (int): index of the row to exclude
        column (int): index of the column to exclude

    Returns:
        list: Sub-matrix excluding specified row and column
    """
    sub_matrix = []
    for i in range(len(matrix)):
        if i != row:
            sub_row = []
            for j in range(len(matrix)):
                if j != column:
                    sub_row.append(matrix[i][j])
            sub_matrix.append(sub_row)

    return sub_matrix


def calc_determinant(matrix):
    """Calculates the determinant of a square matrix

    Args:
        matrix (list): square matrix to calculate determinant from

    Returns:
        float: determinant of the matrix
    """
    matrix_size = len(matrix)

    if matrix_size == 1:
        return matrix[0][0]

    elif matrix_size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    else:
        det = 0
        for i in range(matrix_size):
            sign = (-1) ** i
            sub_matrix = get_sub_matrix(matrix, 0, i)
            det += matrix[0][i] * sign * calc_determinant(sub_matrix)

        return det


def inverse_matrix(matrix):
    """Computes the inverse of a square matrix

    Args:
        matrix (list): square matrix to find the inverse

    Returns:
        list: inverse of the matrix
        None: if the matrix is non-invertible
    """
    determinant = calc_determinant(matrix)

    if determinant == 0:
        return None

    size = len(matrix)
    if size == 1:
        return [[1 / determinant]]

    new_matrix = create_empty_matrix(size, size)
    for i in range(size):
        for j in range(size):
            sign = (-1) ** (i + j)
            sub_matrix = get_sub_matrix(matrix, i, j)
            new_matrix[j][i] = sign * calc_determinant(sub_matrix)

    return multiply_by_constant(new_matrix, 1 / determinant)


def create_empty_matrix(rows, cols):
    """Creates an empty matrix of specified dimensions

    Args:
        rows (int): number of rows in the matrix
        cols (int): number of columns in the matrix

    Returns:
        list: empty matrix with specified dimensions
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    """Prints the matrix content to the console

    Args:
        matrix (list): matrix to be printed
    """
    print("The result is:")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            num = matrix[i][j]
            if int(num) == num:
                print(int(num), end=" ")
            elif int(num*10) == num*10:
                print(f"{num:.1f}", end=" ")
            else:
                print(f"{num:.2f}", end=" ")
        print()
