import math


def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            file_input.append(list(map(int, list(line.rstrip()))))
    return file_input


def get_basin_from_low_point(matrix, i, j, basin_elems, visited):

    if i < 0 or i == len(matrix):
        return

    if j < 0 or j == len(matrix[i]):
        return

    if matrix[i][j] == 9:
        return

    if (i, j) in visited:
        return

    basin_elems.append(matrix[i][j])
    visited.append((i, j))

    get_basin_from_low_point(matrix, i+1, j, basin_elems, visited)
    get_basin_from_low_point(matrix, i, j+1, basin_elems, visited)
    get_basin_from_low_point(matrix, i, j-1, basin_elems, visited)
    get_basin_from_low_point(matrix, i-1, j, basin_elems, visited)

    return


if __name__ == '__main__':
    matrix = read_file('input.txt')

    lowest_elems = []
    basin_lengths = []
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
                basin_elems = []
                visited = []
                get_basin_from_low_point(matrix, i, j, basin_elems, visited)
                basin_lengths.append(len(basin_elems))

    three_largest_basin_lengths = sorted(basin_lengths, reverse=True)[0:3]

    product = math.prod(three_largest_basin_lengths)
    print(product)