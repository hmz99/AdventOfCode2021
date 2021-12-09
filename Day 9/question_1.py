def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            file_input.append(list(map(int, list(line.rstrip()))))
    return file_input

if __name__ == '__main__':
    matrix = read_file('input.txt')

    lowest_elems = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            elem_being_checked = matrix[i][j]
            low_point = True
            if i > 0:
                # above
                if matrix[i-1][j] <= elem_being_checked:
                    low_point = False
            if i < len(matrix)-1:
                # below
                if matrix[i+1][j] <= elem_being_checked:
                    low_point = False
            if j > 0:
                # left
                if matrix[i][j-1] <= elem_being_checked:
                    low_point = False
            if j < len(matrix[i])-1:
                # right
                if matrix[i][j+1] <= elem_being_checked:
                    low_point = False

            if low_point:
                lowest_elems.append(matrix[i][j])

    risk_level = sum(lowest_elems) + len(lowest_elems)
    print(risk_level)
