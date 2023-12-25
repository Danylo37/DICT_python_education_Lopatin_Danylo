"""MatrixProcessing project"""
import matrixprocessing as mp
import util


while True:
    print("\n"
          "1. Add matrices\n"
          "2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrix\n"
          "5. Calculate a determinant\n"
          "6. Inverse matrix\n"
          "0. Exit")

    possible_values = [0, 1, 2, 3, 4, 5, 6]
    user_choice = util.get_user_choice(possible_values)

    # Exit
    if user_choice == 0:
        break

    # Add matrices
    elif user_choice == 1:
        matrix_a = mp.create_matrix()
        matrix_b = mp.create_matrix()

        result_matrix = mp.add(matrix_a, matrix_b)
        if result_matrix is not None:
            mp.print_matrix(result_matrix)
        else:
            print("Adding is impossible")

    # Multiply matrix by a constant
    elif user_choice == 2:
        matrix = mp.create_matrix()

        while True:
            constant = input("Enter the constant: > ")
            if util.is_digit(constant):
                constant = int(constant)
                break

        result_matrix = mp.multiply_by_constant(matrix, constant)
        mp.print_matrix(result_matrix)

    # Multiply matrices
    elif user_choice == 3:
        matrix_a = mp.create_matrix()
        matrix_b = mp.create_matrix()

        result_matrix = mp.multiply_by_matrix(matrix_a, matrix_b)
        if result_matrix is not None:
            mp.print_matrix(result_matrix)
        else:
            print("Multiplying is impossible")

    # Transpose matrix
    elif user_choice == 4:
        transpose_matrix = mp.transpose_matrix()

        if transpose_matrix is not None:
            mp.print_matrix(transpose_matrix)

    # Calculate a determinant
    elif user_choice == 5:
        matrix = mp.create_matrix()

        det = mp.calc_determinant(matrix)
        print(f"The result is:\n"
              f"{det}")

    # Inverse matrix
    elif user_choice == 6:
        matrix = mp.create_matrix()
        inverse_matrix = mp.inverse_matrix(matrix)

        if inverse_matrix is not None:
            mp.print_matrix(inverse_matrix)
        else:
            print("This matrix doesn't have an inverse.")
