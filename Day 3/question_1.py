def read_file(filename: str) -> list:
    file_input = []
    with open(filename) as file:
        for line in file:
            input_list = list(map(int,line.rstrip()))
            file_input.append(input_list)
    return file_input


if __name__ == '__main__':
    values = read_file('input.txt')

    # Transpose the matrix
    transposed_list = list(map(list, zip(*values)))

    # Get gamma
    gamma = []
    for column in transposed_list:
        gamma.append(max(column, key=column.count))

    gamma_str = "".join(map(str, gamma))
    gamma_decimal = int(gamma_str, 2)


    # Get epsilon
    epsilon = []
    for column in transposed_list:
        epsilon.append(min(column, key=column.count))

    epsilon_str = "".join(map(str, epsilon))
    epsilon_decimal = int(epsilon_str, 2)

    # Get power
    power = epsilon_decimal * gamma_decimal

    print(power)